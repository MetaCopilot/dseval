from __future__ import annotations

import os
import re
from pathlib import Path
from typing import TypedDict

import requests
import yaml
from typing_extensions import NotRequired

from .validator import Validator, add_indent


class ExecutionConfig(TypedDict):
    max_time: NotRequired[int]
    max_memory: NotRequired[int]
    forbid_names: NotRequired[list[str]]


class SubProblem:
    reference_code: str
    question: str | None
    validator: Validator | None
    validator_loose: Validator | None
    data: dict | None
    execution: ExecutionConfig | None

    def __init__(
        self,
        reference_code: str,
        question: str | None = None,
        validator: Validator | dict | None = None,
        data: dict | None = None,
        execution: ExecutionConfig | None = None,
    ):
        self.question = question
        self.reference_code = reference_code
        validator_ = validator_loose = None
        if question is not None and validator is None:
            validator_ = Validator.load("and", Validator.augment_config({}, "comparison"))
            validator_loose = Validator.load("and", Validator.augment_config({}, "comparison", loose=True))
        elif isinstance(validator, dict):
            template = validator.pop("template", "comparison")
            validator_ = Validator.load("and", Validator.augment_config(validator, template))
            validator_loose = Validator.load(
                "and",
                Validator.augment_config(validator, template, loose=True),
            )
        self.validator = validator_
        self.validator_loose = validator_loose
        self.data = data
        self.execution = execution

    def prepare_data(self) -> None:
        if self.data is None:
            return

        for file_name, url in self.data.items():
            file_path = os.path.join("inputs", file_name)
            if not os.path.exists(file_path):
                with open(file_path, "wb") as f:
                    f.write(requests.get(url, allow_redirects=True).content)

    def __repr__(self):
        return (
            f"SubProblem(\n  question: {self.question!r},\n  reference_code: {self.reference_code!r},\n"
            f"  validator: {add_indent(repr(self.validator), 2).lstrip()}\n)"
        )

    def to_plain_text(self, index: int | None = None, answer_prefix: bool = True) -> str:
        index_str = str(index) if index is not None else ""
        if self.question is not None:
            ret = f"Q{index_str}: {self.question.rstrip()}\n\n"
            if answer_prefix:
                ret += f"A{index_str}:\n"
            ret += f"```\n{self.reference_code.rstrip()}\n```"
            return ret
        else:
            return f"Context:\n```\n{self.reference_code}\n```"


class ProblemSet:
    problems: list[SubProblem]

    def __init__(self, problems: list[SubProblem]):
        self.problems = problems

    def __iter__(self):
        return iter(self.problems)

    def __getitem__(self, index: int) -> SubProblem:
        return self.problems[index]

    def __len__(self):
        return len(self.problems)

    def to_plain_text(self) -> str:
        texts = []
        counter = 0
        for problem in self.problems:
            if problem.question is not None:
                counter += 1
                texts.append(f"Problem {counter}:\n\n{problem.to_plain_text()}")
            else:
                texts.append(problem.to_plain_text())
        return "\n\n\n".join(texts)

    @classmethod
    def fromfile(cls, code_path: Path | str) -> "ProblemSet":
        if not isinstance(code_path, Path):
            code_path = Path(code_path)
        problems = []
        for section in code_path.read_text().split("# %%\n")[1:]:
            # Toss away the first one.
            section = section.strip()
            if not section:
                continue
            match = re.match(r'r?"""([\s\S]+?)"""\n([\s\S]+)', section)
            if match is not None:
                setup, code = match.groups()
                setup = yaml.safe_load(setup)
                problems.append(SubProblem(reference_code=code.strip(), **setup))
            else:
                problems.append(SubProblem(reference_code=section))
        return cls(problems)

    def __repr__(self) -> str:
        return (
            "ProblemSet(\n"
            + ",\n".join([add_indent(str(i) + ": " + repr(problem), 2) for i, problem in enumerate(self.problems)])
            + "\n)"
        )


class Benchmark:
    problemsets: list[ProblemSet]

    def __init__(self, problemsets: list[ProblemSet], input_directory: Path | None = None):
        self.problemsets = problemsets

    def __iter__(self):
        return iter(self.problemsets)

    def __getitem__(self, index: int) -> ProblemSet:
        return self.problemsets[index]

    def __len__(self):
        return len(self.problemsets)

    @classmethod
    def frompath(cls, benchmark_path: Path | str) -> "Benchmark":
        if not isinstance(benchmark_path, Path):
            benchmark_path = Path(benchmark_path)
        if benchmark_path.is_dir():
            problemsets = [path for path in benchmark_path.glob("*.py") if not path.name.startswith("_")]
            return cls([ProblemSet.fromfile(problemset) for problemset in problemsets])
        else:
            # for debugging purposes
            return cls([ProblemSet.fromfile(benchmark_path)])

    def __repr__(self) -> str:
        return (
            "Benchmark(\n"
            + ",\n".join([add_indent(str(i) + ": " + repr(problemset), 2) for i, problemset in enumerate(self.problemsets)])
            + "\n)"
        )
