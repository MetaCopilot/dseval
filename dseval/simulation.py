from __future__ import annotations

import ast
import copy
import io
import logging
import traceback
import types
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from typing import Any, Literal, TypedDict

from .limit import limit_memory, limit_time, measure_time
from .match import ExactMatcher
from .utils import exec_code

_logger = logging.getLogger(__name__)

DiffType = Literal["added", "updated", "replaced", "deleted"]


class Error(TypedDict):
    ename: str
    evalue: str
    traceback: list[str]


class CellOutput(TypedDict):
    source_code: str
    stream_output: str
    execute_time: float
    execute_result: Any
    error: Error | None
    namespace_snapshot: dict[str, Any]
    namespace_diff: dict[str, DiffType]


class _Forbidden:
    def __eq__(self, _: Any) -> bool:
        return False


class Cell:
    @property
    def source(self) -> str:
        return self._source

    @property
    def output(self) -> Any:
        return self._output

    def __init__(self, source: str, output: CellOutput | None):
        self._source = source
        self._output = output

    def update_source(self, source: str) -> None:
        self._source = source


class Environment:
    namespace: dict[str, Any]
    cells: list[Cell]

    class _Missing:
        def __eq__(self, value: Any) -> bool:
            return False

    def __init__(self):
        self.namespace = {}
        self.cells = []

        self._missing = self._Missing()

    @staticmethod
    def exec_with_output(script: str, globals: dict | None = None, locals: dict | None = None) -> Any:
        # https://stackoverflow.com/q/33908794/6837658
        a = ast.parse(script)
        last_expression = None
        if a.body:
            if isinstance(a_last := a.body[-1], ast.Expr):
                last_expression = ast.unparse(a.body.pop())
            # Assignment is ignored.
            # elif isinstance(a_last, ast.Assign):
            #     last_expression = ast.unparse(a_last.targets[0])
            # elif isinstance(a_last, (ast.AnnAssign, ast.AugAssign)):
            #     last_expression = ast.unparse(a_last.target)
        exec_code(ast.unparse(a), "submission", globals, locals, mode="exec")
        if last_expression:
            return exec_code(last_expression, "submission-last-line", globals, locals, mode="eval")

    def execute(
        self,
        code: str,
        raise_error: bool = False,
        forbid_names: list[str] | None = None,
        max_time: int = 1,
        max_memory: int = -1,
    ) -> Any:
        # For variable diff
        namespace_copy = self.namespace_copy()
        namespace_ids = {name: id(value) for name, value in self.namespace.items()}

        # Forbid some names from being used.
        forbid_namespace = {}
        if forbid_names is not None:
            for name in forbid_names:
                if name in self.namespace:
                    forbid_namespace[name] = self.namespace[name]
                    self.namespace[name] = _Forbidden()

        output = error = None
        time_measurer = None
        io = StringIO()
        with redirect_stdout(io), redirect_stderr(io):
            try:
                ex = limit_time(max_time)(self.exec_with_output)
                ex = limit_memory(max_memory)(ex)
                try:
                    with measure_time() as time_measurer:
                        output = ex(code, self.namespace)
                    if time_measurer.interval > max_time:
                        raise TimeoutError(
                            "Actual time consumption is: %.2f seconds. Exceeds time limit: %.1f seconds."
                            % (time_measurer.interval, float(max_time))
                        )
                except KeyboardInterrupt:
                    if time_measurer is not None and time_measurer.interval > max_time:
                        raise TimeoutError(
                            "Actual time consumption is: %.2f seconds. Exceeds time limit: %.1f seconds."
                            % (time_measurer.interval, float(max_time))
                        )
                    raise
            except KeyboardInterrupt:
                raise
            except Exception as e:
                if raise_error:
                    # This should not be caught anywhere.
                    # The namespace is already not intact.
                    raise
                try:
                    traceback_str = traceback.format_exc().splitlines()
                except Exception:
                    traceback_str = ["Failed to get traceback."]
                error = Error(
                    ename=type(e).__name__,
                    evalue=str(e),
                    traceback=traceback_str,
                )

        # Restore the namespace.
        for name in forbid_namespace:
            self.namespace[name] = forbid_namespace[name]

        diff = self.namespace_diff(self.namespace, namespace_copy, namespace_ids)
        self.cells.append(
            Cell(
                code,
                CellOutput(
                    source_code=code,
                    stream_output=io.getvalue(),
                    execute_time=time_measurer.interval if time_measurer is not None else 0.0,
                    execute_result=output,
                    error=error,
                    namespace_snapshot=self.namespace,
                    namespace_diff=diff,
                ),
            )
        )

        return output

    @property
    def last_cell(self) -> Cell | None:
        if self.cells:
            return self.cells[-1]
        return None

    @property
    def last_exception(self) -> str | None:
        if self.cells and self.cells[-1].output["error"]:
            return "\n".join(self.cells[-1].output["error"]["traceback"])
        return None

    def fork(self) -> "Environment":
        new_env = Environment()
        new_env.namespace.update(self.namespace_copy())
        new_env.cells = list(self.cells)
        return new_env

    def namespace_copy(self) -> dict[str, Any]:
        new_namespace = {}
        for name, value in self.namespace.items():
            if isinstance(value, (types.ModuleType, types.FunctionType, types.BuiltinFunctionType, io.IOBase)):
                new_namespace[name] = value
            elif name == "__builtins__":
                new_namespace[name] = value
            else:
                try:
                    new_namespace[name] = copy.deepcopy(value)
                except (TypeError, IndexError):
                    # Index error is raised rarely for pandas dataframes.
                    _logger.exception(
                        "Deep copy failed for object of type: %s (name = %s). The object might be manipulated unintentionally.",
                        type(value),
                        name,
                    )
                    try:
                        new_namespace[name] = copy.copy(value)
                    except:
                        _logger.error("Unable to copy an object of type: %s", type(value))
                        new_namespace[name] = value
        return new_namespace

    def namespace_diff(
        self,
        namespace: dict[str, Any],
        prev_namespace: dict[str, Any],
        prev_ids: dict[str, int],
    ) -> dict[str, DiffType]:
        diff = {}
        for name, value in namespace.items():
            if name in ["__builtins__", "__warningregistry__"]:
                continue
            if name not in prev_namespace:
                diff[name] = "added"
            elif id(value) != prev_ids[name]:
                diff[name] = "replaced"
            else:
                try:
                    if not ExactMatcher()(value, prev_namespace[name])["match"]:
                        diff[name] = "updated"
                except KeyboardInterrupt:
                    raise
                except:
                    _logger.warning(f"Failed to compare {name}. Assuming it's updated.")
                    diff[name] = "updated"
        for name in prev_namespace:
            if name not in namespace:
                diff[name] = "deleted"
        return diff

    def get_variable(self, name: str) -> Any:
        return self.namespace.get(name, self._missing)
