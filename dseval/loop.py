from __future__ import annotations

import json
import logging
import os
import shutil
import traceback
from contextlib import contextmanager
from enum import Enum
from pathlib import Path
from typing import Any, List, TypedDict, cast

import colorama
from typing_extensions import NotRequired

from .agent import Agent, AgentException, TentativeSolution, TentativeSolutions
from .problem import Benchmark, ProblemSet
from .simulation import Environment
from .validator import Verdict, Subverdict, ValidateResult, validator_comments_to_verdict
from .utils import read_jsonl, write_jsonl

_logger = logging.getLogger(__name__)


class EvaluationDetail(TypedDict):
    # To locate the current problem
    benchmark: str | None
    version: str | None
    problemset: str | None
    index: int
    # Attempt ID
    attempt: int
    # Safe to drop duplicates from above if needed
    # ========================
    # Evaluation results
    # Correct put upfront for ease of inspection
    verdict: Verdict
    subverdict: Subverdict
    extended_verdict: str
    # Question content
    question: str
    # If agent crashes
    agent_exception: str
    # Validator comments
    validation: ValidateResult
    # Generated code by agents
    code: str
    # Computation costs from agents
    agent_stats: dict[str, Any]


class EvaluationResult:
    details: list[EvaluationDetail]

    def __init__(self, details: list[EvaluationDetail]):
        self.details: list[EvaluationDetail] = []

        # Later records will overwrite the previous ones
        self.existing_records: set[tuple[str | None, int, int]] = set()
        for detail in details:
            key = (detail["problemset"], detail["index"], detail["attempt"])
            if key in self.existing_records:
                continue
            self.details.append(detail)
            self.existing_records.add(key)

    def has(self, problemset: str | None, index: int, attempt: int) -> bool:
        return (problemset, index, attempt) in self.existing_records

    def extend(self, other: EvaluationResult) -> None:
        added_problemsets = set([other["problemset"] for other in other.details])
        self.details = [detail for detail in self.details if detail["problemset"] not in added_problemsets]
        self.existing_records = set(
            (detail["problemset"], detail["index"], detail["attempt"]) for detail in self.details
        )
        for detail in other.details:
            self.details.append(detail)
            self.existing_records.add((detail["problemset"], detail["index"], detail["attempt"]))

    def write(self, path: Path | str) -> None:
        if not isinstance(path, Path):
            path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        write_jsonl(path, cast(List[dict], self.details))

    @classmethod
    def read(cls, path: Path | str) -> EvaluationResult:
        if not isinstance(path, Path):
            path = Path(path)
        return cls(cast(List[EvaluationDetail], read_jsonl(path)))

    @property
    def score(self) -> float:
        return len([detail for detail in self.details if detail["verdict"] == Verdict.Correct]) / len(self.details)


class Evaluator:
    def __init__(
        self,
        max_attempts: int = 1,
        retry_hint: bool = False,
        retry_reset: bool = False,
        ignore_agent_exception: bool = False,
        error_propagation: bool = False,
    ):
        self.max_attempts = max_attempts
        self.retry_hint = retry_hint
        self.retry_reset = retry_reset
        self.ignore_agent_exception = ignore_agent_exception
        self.error_propagation = error_propagation

    @contextmanager
    def propagate_errors(self, environment: Environment, code_with_errors: list[str]):
        if self.error_propagation:
            previous_sources = [cell.source for cell in environment.cells]
            if self.max_attempts == 1:
                assert len(code_with_errors) == len(previous_sources)
            for cell, code in zip(environment.cells, code_with_errors):
                cell.update_source(code)
            yield
            for cell, source in zip(environment.cells, previous_sources):
                cell.update_source(source)
        else:
            yield

    def dry_run(self, problems: ProblemSet) -> float:
        environment = Environment()
        correct = total = 0

        for problem in problems:
            problem.prepare_data()

            if not problem.is_complete:
                environment.execute(problem.reference_code, raise_error=True)
                continue

            assert problem.question is not None
            total += 1
            _logger.info("[Question %d] %s", total, problem.question.strip())
            playground_env = environment.fork()
            environment.execute(problem.reference_code, **(problem.execution or {}), raise_error=True)
            playground_env.execute(problem.reference_code, **(problem.execution or {}))

            if problem.validator is not None:
                last_cell, last_cell_playground = environment.last_cell, playground_env.last_cell
                assert last_cell is not None and last_cell_playground is not None
                validate_result = problem.validator.validate(last_cell.output, last_cell_playground.output)
                _logger.info(
                    "[Question %d] %s%s%s! (time elapsed: %s%.2f%s seconds)",
                    total,
                    (colorama.Fore.GREEN if validate_result["correct"] else colorama.Fore.RED),
                    "Correct" if validate_result["correct"] else "Incorrect",
                    colorama.Fore.RESET,
                    (
                        colorama.Fore.GREEN
                        if last_cell.output["execute_time"] < (problem.execution or {}).get("max_time", 1) / 3
                        else colorama.Fore.YELLOW
                    ),
                    last_cell.output["execute_time"],
                    colorama.Fore.RESET,
                )
                correct += int(validate_result["correct"])
                if not validate_result["correct"]:
                    _logger.warning("[Question %d] %s", total, validate_result["reason"])
            else:
                correct += 1

        print("Correct: %d / %d" % (correct, total))

        return correct / total

    def solve_only(self, problems: ProblemSet, agent: Agent) -> TentativeSolutions:
        """Solve the problems and return the codes.

        Solve with retry is not supported in this mode.
        """
        environment = Environment()
        codes: list[TentativeSolution] = []

        # For error propagation
        code_with_errors: list[str] = []

        total = 0

        for problem in problems:
            problem.prepare_data()

            if not problem.is_complete:
                environment.execute(problem.reference_code, raise_error=True)
                code_with_errors.append(problem.reference_code)
            assert problem.question is not None

            total += 1

            _logger.info("[Question %d] %s", total, problem.question.strip())
            with agent.track_stats(), self.propagate_errors(environment, code_with_errors):
                code = agent.solve(problem.question, environment)
            _logger.info(
                "[Question %d] Code:\n%s%s%s",
                total,
                colorama.Fore.GREEN,
                code,
                colorama.Fore.RESET,
            )

            code_with_errors.append(code)
            environment.execute(problem.reference_code, **(problem.execution or {}), raise_error=True)

            codes.append(
                {
                    "question": problem.question,
                    "code": code,
                    "agent_stats": agent.stats,
                }
            )

        return TentativeSolutions(codes)

    def evaluate(
        self, problems: ProblemSet, agent: Agent, benchmark_name: str | None = None, version: str | None = None
    ) -> EvaluationResult:
        environment = Environment()
        total = 0
        evaluation_results: list[EvaluationDetail] = []

        # For error propagation
        code_with_errors: list[str] = []

        for problem in problems:
            problem.prepare_data()
            if not problem.is_complete:
                environment.execute(problem.reference_code, raise_error=True)
                code_with_errors.append(problem.reference_code)
                continue
            assert problem.question is not None and problem.validator is not None

            total += 1
            _logger.info("[Question %d] %s", total, problem.question)
            playground_env = environment.fork()

            # Execute ground truth code
            environment.execute(problem.reference_code, **(problem.execution or {}), raise_error=True)
            assert environment.last_cell is not None
            answer = environment.last_cell.output

            code = agent_exception = ""
            retry_kwargs = {}

            # Rollback the playground for another retry
            playground_env_backup = None
            if self.retry_reset and self.max_attempts >= 1:
                playground_env_backup = playground_env.fork()

            for attempt_id in range(1, self.max_attempts + 1):
                if attempt_id > 1 and playground_env_backup is not None:
                    # Reset the playground_env in case there is a backup
                    playground_env = playground_env_backup.fork()

                # Invoke agent for code generation.
                with agent.track_stats(), self.propagate_errors(playground_env, code_with_errors):
                    try:
                        if attempt_id == 1:
                            code = agent.solve(problem.question, playground_env)
                        else:
                            _logger.info("[Question %d] Attempt #%d: %s", total, attempt_id, retry_kwargs)
                            code = agent.retry(**retry_kwargs)
                    except AgentException:
                        if not self.ignore_agent_exception:
                            raise
                        _logger.exception(
                            "[Question %d] Agent failed to produce a solution.",
                            total,
                        )
                        agent_exception = traceback.format_exc()
                        code = ""

                _logger.info(
                    "[Question %d] Code:\n%s%s%s",
                    total,
                    colorama.Fore.GREEN,
                    code,
                    colorama.Fore.RESET,
                )

                # Execute the generated code.
                playground_env.execute(code, **(problem.execution or {}))
                code_with_errors.append(code)
                assert playground_env.last_cell is not None

                # Validate the generation result.
                validate_result = problem.validator.validate(answer, playground_env.last_cell.output)
                verdict, subverdict, extended_verdict = validator_comments_to_verdict(validate_result)

                # Set information needed for retries
                if playground_env.last_exception is not None:
                    _logger.warning(
                        "%sError occurred while executing the code:\n%s%s",
                        colorama.Fore.YELLOW,
                        playground_env.last_exception,
                        colorama.Fore.RESET,
                    )
                    retry_kwargs["error"] = playground_env.last_exception
                else:
                    retry_kwargs["error"] = "No exception."
                retry_kwargs["output"] = playground_env.last_cell.output
                if self.retry_hint:
                    retry_kwargs["hint"] = json.dumps(validate_result)

                _logger.info(
                    "[Question %d]%s %s!",
                    total,
                    " (attempt #%d)" % attempt_id if attempt_id > 1 else "",
                    "Correct" if validate_result["correct"] else "Incorrect",
                )

                summary: EvaluationDetail = {
                    "benchmark": benchmark_name,
                    "version": version,
                    "problemset": problems.name,
                    "index": total,
                    "attempt": attempt_id,
                    "verdict": verdict,
                    "subverdict": subverdict,
                    "extended_verdict": extended_verdict,
                    "question": problem.question,
                    "agent_exception": agent_exception,
                    "validation": validate_result,
                    "code": code,
                    "agent_stats": agent.stats,
                }

                evaluation_results.append(summary)

                if verdict == Verdict.Correct:
                    break

        return EvaluationResult(evaluation_results)


@contextmanager
def running_environment(run_directory: Path, data_source: Path | None = None):
    current_working_directory = Path.cwd().resolve()
    run_directory = run_directory.resolve()
    try:
        run_directory.mkdir(exist_ok=True, parents=True)

        # Delete old files
        for file in run_directory.iterdir():
            if file.is_file() or file.is_symlink():
                file.unlink()
            else:
                shutil.rmtree(file)

        # Link input directory
        if data_source is not None:
            shutil.copytree(data_source.resolve(), run_directory / "inputs")

        os.chdir(run_directory)

        yield

    finally:
        os.chdir(current_working_directory)

        # Clean up
        for file in run_directory.iterdir():
            if file.is_file() or file.is_symlink():
                file.unlink()
            else:
                shutil.rmtree(file)


def resumable_benchmark_evaluation_loop(
    benchmark: Benchmark, agent: Agent, evaluator: Evaluator, run_directory: Path, result_path: Path
) -> None:
    overall_result = EvaluationResult.read(result_path)

    for idx, problemset in enumerate(benchmark, start=1):
        agent.reset()

        # Check whether the problemset is already tested
        if overall_result.has(benchmark.name, idx, 1):
            _logger.info("[Problem set %d] %s (skipped)", idx, problemset.name)
            continue

        _logger.info("[Problem set %d] %s", idx, problemset.name)

        with running_environment(run_directory, benchmark.data_directory):
            result = evaluator.evaluate(problemset, agent, benchmark.name, benchmark.version)
            overall_result.extend(result)
            _logger.info("[Problem set %d] Score: %.2f", idx, result.score)

        overall_result.write(result_path)
        _logger.info("[Problem set %d] Overall score so far: %.3f", idx, overall_result.score)
