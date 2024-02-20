from __future__ import annotations

import atexit
import tempfile
import uuid
from pathlib import Path
from typing import Any, Literal

_temp_directory: tempfile.TemporaryDirectory | None = None


def add_indent(text: str, indent: int = 2) -> str:
    return "\n".join(" " * indent + line for line in text.splitlines())


def get_temporary_file_name(prefix: str) -> Path:
    global _temp_directory
    if _temp_directory is None:
        _temp_directory = tempfile.TemporaryDirectory(prefix="dseval-")
        atexit.register(_temp_directory.cleanup)

    return Path(_temp_directory.name) / (prefix + "-" + uuid.uuid4().hex + ".py")


def default_namespace() -> dict[str, Any]:
    import random

    import numpy
    import pandas

    return {**globals(), "pd": pandas, "np": numpy, "random": random}


def exec_code(
    code: str,
    source_prefix: str,
    globals: dict[str, Any] | None = None,
    locals: dict[str, Any] | None = None,
    mode: Literal["exec", "eval"] = "exec",
) -> dict[str, Any]:
    if globals is None:
        globals = default_namespace()
    source_path = get_temporary_file_name(source_prefix)
    source_path.write_text(code)
    compiled = compile(code, source_path, mode)
    if mode == "eval":
        return eval(compiled, globals, locals)
    else:
        exec(compiled, globals, locals)
        return globals


def get_code_complexity(code: str) -> float:
    import ast

    module = ast.parse(code)

    complexity = 0.0
    for node in ast.walk(module):
        # Conditions
        if isinstance(node, (ast.For, ast.While, ast.If, ast.With)):
            complexity += 3
        # Other statements
        elif isinstance(node, ast.stmt):
            complexity += 1
        # Constant, variable
        elif isinstance(node, (ast.Constant, ast.Name)):
            complexity += 0
        # Call other methods
        elif isinstance(node, ast.Call):
            complexity += 3
        # Calling an attribute or a subscript
        elif isinstance(node, (ast.Attribute, ast.Subscript)):
            complexity += 4
        # Other expressions
        elif isinstance(node, ast.expr):
            complexity += 1
        # Function arguments
        elif isinstance(node, ast.arg):
            complexity += 1

    return complexity
