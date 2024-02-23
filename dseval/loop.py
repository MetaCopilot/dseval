from __future__ import annotations

import json
import logging
import os
import shutil
import traceback
from contextlib import contextmanager
from enum import Enum
from pathlib import Path
from typing import Any, TypedDict

import colorama
from typing_extensions import NotRequired

from .agent import Agent, AgentException, TentativeSolution, TentativeSolutions
from .problem import Benchmark, ProblemSet
from .simulation import Environment
from .validator import Verdict, Subverdict

_logger = logging.getLogger(__name__)


class EvaluationDetail(TypedDict):
    # To locate the current problem
    benchmark: str
    version: str
    problemset: str
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
    validator: dict
    # Generated code by agents
    code: str
    # Computation costs from agents
    agent_stats: NotRequired[dict[str, Any]]


class EvaluationResult:
    num_problems: int
    num_passed: int
    details: list[EvaluationDetail]

    def __init__(self, num_problems: int, num_passed: int, details: list[EvaluationDetail]):
        self.num_problems = num_problems
        self.num_passed = num_passed
        self.details = details

    def write(self, path: Path | str) -> None:
        if not isinstance(path, Path):
            path = Path(path)
        with path.open("w") as f:
            for detail in self.details:
                f.write(json.dumps(detail) + "\n")

    @property
    def score(self) -> float:
        return self.num_passed / self.num_problems


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

            if not problem.question:
                if problem.reference_code:
                    environment.execute(problem.reference_code, raise_error=True)
                continue

            total += 1
            _logger.info("[Question %d] %s", total, problem.question.strip())
            playground_env = environment.fork()
            environment.execute(problem.reference_code, **(problem.execution or {}), raise_error=True)
            playground_env.execute(problem.reference_code, **(problem.execution or {}))

            if problem.validator is not None:
                validate_result = problem.validator.validate(
                    environment.last_cell.output, playground_env.last_cell.output
                )
                _logger.info(
                    "[Question %d] %s%s%s! (time elapsed: %s%.2f%s seconds)",
                    total,
                    (colorama.Fore.GREEN if validate_result["correct"] else colorama.Fore.RED),
                    "Correct" if validate_result["correct"] else "Incorrect",
                    colorama.Fore.RESET,
                    (
                        colorama.Fore.GREEN
                        if environment.last_cell.output["execute_time"]
                        < (problem.execution or {}).get("max_time", 1) / 3
                        else colorama.Fore.YELLOW
                    ),
                    environment.last_cell.output["execute_time"],
                    colorama.Fore.RESET,
                )
                correct += int(validate_result["correct"])
                if not validate_result["correct"]:
                    _logger.warning("[Question %d] %s", total, validate_result["reason"])
            else:
                correct += 1

        print("Correct: %d / %d" % (correct, total))

        return correct / total

    def solve_only(self, problems: ProblemSet, solver: Solver) -> TentativeSolutions:
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

            if not problem.question:
                if problem.reference_code:
                    environment.execute(problem.reference_code, raise_error=True)
                    code_with_errors.append(problem.reference_code)
                continue

            total += 1

            _logger.info("[Question %d] %s", total, problem.question.strip())
            with solver.track_stats(), self.propagate_errors(environment, code_with_errors):
                code = solver.solve(problem.question, environment)
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
                    "solver_stats": solver.stats,
                }
            )

        return TentativeSolutions(codes)

    def solve_evaluate(self, problems: ProblemSet, solver: Solver) -> EvaluationResult:
        environment = Environment()
        correct = total = 0
        evaluation_results: list[EvaluationDetail] = []

        # For error propagation
        code_with_errors: list[str] = []

        for problem in problems:
            problem.prepare_data()
            if not problem.question:
                # Problem without a prompt
                if problem.reference_code:
                    environment.execute(problem.reference_code, raise_error=True)
                    code_with_errors.append(problem.reference_code)
                continue

            total += 1
            _logger.info("[Question %d] %s", total, problem.question)
            playground_env = environment.fork()
            environment.execute(problem.reference_code, **(problem.execution or {}), raise_error=True)
            assert environment.last_cell is not None
            answer = environment.last_cell.output

            crashed = code = solver_crashed = ""
            hint = ""
            produced_output = validate_result = validate_result_loose = None
            playground_env_backup = None
            if self.retry_reset and self.max_attempts >= 1:
                playground_env_backup = playground_env.fork()
            current_correct = current_correct_loose = False
            retry_count = 0
            solver_stats_accumulator = {}
            while retry_count <= self.max_attempts and not current_correct:
                current_correct = current_correct_loose = True  # reset to true
                if retry_count >= 1 and playground_env_backup is not None:
                    # Reset the playground_env in case there is a backup
                    playground_env = playground_env_backup.fork()

                with solver.track_stats(), self.propagate_errors(playground_env, code_with_errors):
                    try:
                        if retry_count == 0:
                            code = solver.solve(problem.question, playground_env)
                        else:
                            _logger.info(
                                "[Question %d] Retry %d:\nError:\n%s\nOutput:\n%s",
                                total,
                                retry_count,
                                crashed,
                                produced_output,
                            )
                            if self.retry_hint and not crashed:
                                _logger.info("[Question %d] Retry with hint: %s", total, hint)
                                code = solver.retry(crashed or "", produced_output, hint)
                            code = solver.retry(crashed or "", produced_output)
                    except SolverException:
                        if not self.ignore_agent_exception:
                            raise
                        _logger.exception(
                            "[Question %d] Solver failed to produce a solution.",
                            total,
                        )
                        solver_crashed = traceback.format_exc()
                        code = ""

                # Accumulate token counts, ...
                for stat_key, stat_value in solver.stats.items():
                    if stat_key in solver_stats_accumulator:
                        solver_stats_accumulator[stat_key] += stat_value
                    else:
                        solver_stats_accumulator[stat_key] = stat_value

                _logger.info(
                    "[Question %d] Code:\n%s%s%s",
                    total,
                    colorama.Fore.GREEN,
                    code,
                    colorama.Fore.RESET,
                )

                # Using the same playground_env throughout all retries
                # Won't rollback even for failed attempts.
                produced_output = playground_env.execute(code, **(problem.execution or {}))
                code_with_errors.append(code)
                assert playground_env.last_cell is not None

                crashed = playground_env.last_exception
                if crashed is not None:
                    _logger.warning(
                        "%sError occurred while executing the code:\n%s%s",
                        colorama.Fore.YELLOW,
                        crashed,
                        colorama.Fore.RESET,
                    )

                if problem.validator is not None:
                    validate_result = problem.validator.validate(answer, playground_env.last_cell.output)
                    hint = validate_result.get("reason", "")
                    current_correct = validate_result["correct"]

                if problem.validator_loose is not None:
                    validate_result_loose = problem.validator_loose.validate(answer, playground_env.last_cell.output)
                    current_correct_loose = validate_result_loose["correct"]

                retry_count += 1

            _logger.info(
                "[Question %d] %s!",
                total,
                "Correct" if current_correct else "Incorrect",
            )
            if current_correct:
                correct += 1

            summary: EvaluationDetail = {
                "correct": current_correct,
                "correct_loose": current_correct_loose,
                "tries": retry_count,
                "question": problem.question,
                "code": code,
                "crashed": bool(crashed),
                "solver_stats": solver_stats_accumulator,
                "solver_crashed": solver_crashed,
            }
            if validate_result:
                if "category" in validate_result:
                    summary["val_category"] = validate_result["category"]
                if "reason" in validate_result:
                    summary["val_reason"] = validate_result["reason"]
            if validate_result_loose:
                if "category" in validate_result_loose:
                    summary["val_loose_category"] = validate_result_loose["category"]
                if "reason" in validate_result_loose:
                    summary["val_loose_reason"] = validate_result_loose["reason"]
            evaluation_results.append(summary)

        return EvaluationResult(total, correct, evaluation_results)


@contextmanager
def running_environment(run_directory: Path, data_source: Path | None = None):
    current_working_directory = Path.cwd().resolve()
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
        # Clean up
        for file in run_directory.iterdir():
            if file.is_file() or file.is_symlink():
                file.unlink()
            else:
                shutil.rmtree(file)

        os.chdir(current_working_directory)
