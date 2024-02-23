from __future__ import annotations

import ast
import copy
import json
import logging
import random
import re
import traceback
import types
from enum import Enum
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Generic,
    Literal,
    TypedDict,
    TypeVar,
    cast,
)

import numpy as np
from typing_extensions import NotRequired

from .match import ExactMatcher, Match
from .utils import add_indent, exec_code

if TYPE_CHECKING:
    from .simulation import DiffType, Error

_logger = logging.getLogger(__name__)


class _DictWithStreamOutput(TypedDict):
    stream_output: str


class _DictWithExecuteResult(TypedDict):
    execute_result: Any
    source_code: NotRequired[str]
    namespace_snapshot: NotRequired[dict[str, Any]]


class _DictWithError(TypedDict):
    error: Error | None
    execute_result: NotRequired[Any]
    source_code: NotRequired[str]
    namespace_snapshot: NotRequired[dict[str, Any]]


class _DictWithNamespaceDiff(TypedDict):
    namespace_diff: dict[str, DiffType]


class _DictWithNamespaceSnapshot(TypedDict):
    namespace_snapshot: dict[str, Any]


class ValidateResult(TypedDict):
    correct: Literal["yes", "partial", "no"]
    category: str
    reason: str | list["ValidateResult"]


T = TypeVar("T")


class Validator(Generic[T]):
    alias: ClassVar[str]

    def validate(self, reference: T, submission: T) -> ValidateResult:
        raise NotImplementedError()

    @classmethod
    def load(cls, type_, config):
        if hasattr(cls, "alias") and type_ == cls.alias:
            if config is None:
                return cls()
            elif isinstance(config, list):
                return cls(*config)
            elif isinstance(config, dict):
                return cls(**config)
            else:
                return cls(config)  # type: ignore
        for subcls in cls.__subclasses__():
            if subcls.alias == type_:
                return subcls.load(type_, config)
        raise ValueError(f"Unknown validator type: {type_}")

    @staticmethod
    def augment_config(
        config: dict[str, Any],
        template: Literal["basic", "empty", "intact", "comparison"],
    ):
        if template == "empty":
            base_config = {}
        elif template == "basic":
            base_config = {"crash": None}
        elif template == "intact":
            base_config = {"crash": None, "namespace_intact": None}
        elif template == "comparison":
            base_config = {"crash": None, "namespace_intact": None, "result": None}

        # Deep merge the base config and the user config.
        def merge(base, user):
            if isinstance(base, dict) and isinstance(user, dict):
                for key, value in user.items():
                    if key in base:
                        base[key] = merge(base[key], value)
                    else:
                        base[key] = value
                return base
            else:
                return user

        config = merge(base_config, config)

        return config


class CrashValidator(Validator[_DictWithError]):
    """Ensure that the code didn't crash.

    It also returns "partial" when the code raises an exception, but the answer is contained in the code.
    """

    alias: ClassVar[str] = "crash"

    def __repr__(self) -> str:
        return "CrashValidator()"

    def validate(self, reference, submission) -> ValidateResult:
        if submission["error"] is not None:
            # Try to find answer in source code, in which case we can forgive the crash.
            if "source_code" in submission and "execute_result" in reference:
                execute_result_ref = reference["execute_result"]
                try:
                    answer_in_source = _find_answer_in_source_code(submission["source_code"], execute_result_ref)
                    if answer_in_source:
                        return {
                            "correct": "partial",
                            "category": self.alias,
                            "reason": answer_in_source,
                        }
                except:
                    pass
            return {
                "correct": "no",
                "category": self.alias,
                "reason": "Submission crashes"
                + (":\n" + "\n".join(submission["error"]["traceback"]) if submission["error"]["traceback"] else "."),
            }
        return {
            "correct": "yes",
            "category": self.alias,
            "reason": "Execution finishes successfully.",
        }


class NamespaceIntactGuard(Validator[_DictWithNamespaceDiff]):
    """After execution, we examine the namespace diff. By default:

    - Addition: allowed.
    - Update: not allowed unless it's also updated in the reference.
    - Replacement: not allowed unless it's also replaced in the reference.
    - Deletion: not allowed unless it's also deleted in the reference.

    The settings can be overridden by setting initialization parameters,
    which could be either a boolean or a list of variable names, indicating the allowed variable names.
    """

    alias: ClassVar[str] = "namespace_intact"

    def __init__(
        self,
        addition: list[str] | bool = True,
        update: list[str] | bool | None = None,
        replacement: list[str] | bool | None = None,
        deletion: list[str] | bool | None = None,
        treat_replacement_as_update: bool | None = None,
    ):
        self.addition = addition
        self.update = update
        self.replacement = replacement
        self.deletion = deletion

        if treat_replacement_as_update is None:
            treat_replacement_as_update = replacement is None

        self.treat_replacement_as_update = treat_replacement_as_update

        if self.treat_replacement_as_update:
            if self.replacement is not None:
                raise ValueError("Cannot specify replacement when treat_replacement_as_update is True.")

    def __repr__(self) -> str:
        return (
            f"NamespaceIntactGuard(addition={self.addition}, update={self.update}, "
            f"replacement={self.replacement}, deletion={self.deletion}, "
            f"treat_replacement_as_update={self.treat_replacement_as_update})"
        )

    def validate(self, reference, submission) -> ValidateResult:
        if self.treat_replacement_as_update:
            reference_diff = {
                name: "updated" if diff == "replaced" else diff for name, diff in reference["namespace_diff"].items()
            }
            submission_diff = {
                name: "updated" if diff == "replaced" else diff for name, diff in submission["namespace_diff"].items()
            }
        else:
            reference_diff = reference["namespace_diff"]
            submission_diff = submission["namespace_diff"]

        allowed = {
            "added": self.addition,
            "updated": self.update,
            "replaced": self.replacement,
            "deleted": self.deletion,
        }
        for key in ["updated", "replaced", "deleted"]:
            if allowed[key] is None:
                allowed[key] = [name for name, diff in reference_diff.items() if diff == key]

        for name, diff in submission_diff.items():
            if allowed[diff] is False or (isinstance(allowed[diff], list) and name not in allowed[diff]):
                return {
                    "correct": "no",
                    "category": self.alias,
                    "reason": f"Unexpected variable {diff}: {name}",
                }
        return {
            "correct": "yes",
            "category": self.alias,
            "reason": "Namespace is intact.",
        }


def _guess_print_output(source_code: str, namespace: dict, expected: Any) -> Any:
    parsed_code = ast.parse(source_code)
    eval_objects = []

    # 1. Handle prints
    def walk_print(node):
        if (
            isinstance(node, ast.expr)
            and not isinstance(node, ast.Constant)
            and not isinstance(node, ast.FormattedValue)
            and not isinstance(node, ast.JoinedStr)
        ):
            yield node
        else:
            for child in ast.iter_child_nodes(node):
                yield from walk_print(child)

    for line in parsed_code.body:
        if (
            isinstance(line, ast.Expr)
            and isinstance(line.value, ast.Call)
            and isinstance(line.value.func, ast.Name)
            and line.value.func.id == "print"
        ):
            for arg in line.value.args:
                for value in walk_print(arg):
                    code = ast.unparse(value)
                    obj = exec_code(code, "print", globals=namespace, mode="eval")
                    eval_objects.append(obj)

    # 2. Handle assignments
    if len(eval_objects) == 0 and len(parsed_code.body) >= 1:
        target = None
        for line in parsed_code.body[::-1]:
            if isinstance(line, ast.Assign):
                target = line.targets[0]
            elif isinstance(line, ast.AnnAssign) or isinstance(line, ast.AugAssign):
                target = line.target
            if target is not None:
                break

        if target is not None:
            # Handle assignments like `.columns`
            if isinstance(target, (ast.Attribute, ast.Subscript)):
                target = target.value
            stmt = ast.unparse(target)
            obj = exec_code(stmt, "assignment", globals=namespace, mode="eval")
            eval_objects.append(obj)

    if len(eval_objects) == 0:
        return None
    if len(eval_objects) == 1:
        return eval_objects[0]
    if isinstance(expected, tuple):
        return tuple(eval_objects)
    if isinstance(expected, list):
        return list(eval_objects)
    if isinstance(expected, dict):
        if len(eval_objects) > len(expected):
            return dict(zip(expected.keys(), eval_objects[-len(expected) :]))
        elif len(eval_objects) < len(expected):
            return dict(
                zip(
                    expected.keys(),
                    [None] * (len(expected) - len(eval_objects)) + eval_objects,
                )
            )
        else:
            return dict(zip(expected.keys(), eval_objects))
    _logger.warning("Couldn't guess the print output, assuming the last.")
    return eval_objects[-1]


def _find_answer_in_source_code(source_code: str, expected_result: Any) -> str:
    # When returns something, the answer is found in source code.
    if expected_result is not None:
        res_string = str(expected_result)
        if re.search(r"\b" + re.escape(res_string) + r"\b", source_code):
            return f"Output is directly shown in the code: " + res_string
    return ""


CompareFunction = Callable[[Any, Any], Match]


def _compare_fn_from_config(
    code_or_config_or_fn: str | dict | CompareFunction | None,
    loose: bool = False,
) -> CompareFunction:
    if loose:
        if code_or_config_or_fn is None:
            code_or_config_or_fn = {}
        if isinstance(code_or_config_or_fn, dict):
            code_or_config_or_fn.update(
                {
                    "ignore_order": True,
                    "ignore_names": True,
                    "ignore_dtypes": True,
                    "match_partial": True,
                }
            )
        return _compare_fn_from_config(code_or_config_or_fn)

    if isinstance(code_or_config_or_fn, str):
        return _code_to_compare_fn(code_or_config_or_fn)
    elif isinstance(code_or_config_or_fn, dict):
        return ExactMatcher(**code_or_config_or_fn)
    elif callable(code_or_config_or_fn):
        return code_or_config_or_fn
    elif code_or_config_or_fn is None:
        return ExactMatcher()
    else:
        raise ValueError(f"Unsupported type: {code_or_config_or_fn}")


def _code_to_compare_fn(code: str) -> CompareFunction:
    ns = exec_code(code, "compare-fn")
    return ns["compare_fn"]


def _run_compare_fn(
    compare_fn: CompareFunction,
    compare_fn_loose: CompareFunction | None,
    expected: Any,
    found: Any,
    validator_alias: str,
    mismatch_prefix: str = "",
    failure_prefix: str = "Comparison failure:\n{}",
) -> ValidateResult:
    """Run the comparison function and return the result.

    Args:
        compare_fn: The comparison function.
        compare_fn_loose: The comparison function for loose comparison.
        expected: The expected value.
        found: The found value.
        validator_alias: The alias of the validator.
        mismatch_prefix: The prefix for the mismatch reason.
        failure_prefix: The prefix for the failure reason.
    """
    try:
        match = compare_fn(expected, found)
        if match["match"]:
            return {
                "correct": "yes",
                "category": validator_alias,
                "reason": "Result matches the expected" + (":\n" + match["reason"] if match["reason"] else "."),
            }
        if compare_fn_loose is not None:
            match = compare_fn_loose(expected, found)
            if match["match"]:
                return {
                    "correct": "partial",
                    "category": validator_alias,
                    "reason": "Result matches the expected with looser constraints"
                    + (":\n" + match["reason"] if match["reason"] else "."),
                }

        return {
            "correct": "yes" if match["match"] else "no",
            "category": validator_alias,
            "reason": mismatch_prefix + match["reason"] if match["reason"] else "",
        }
    except AssertionError:
        return {
            "correct": "no",
            "category": validator_alias,
            "reason": mismatch_prefix + "Comparison raises AssertionError:\n" + traceback.format_exc(),
        }
    except KeyboardInterrupt:
        raise
    except:
        return {
            "correct": "no",
            "category": validator_alias,
            "reason": failure_prefix + traceback.format_exc(),
        }


class ResultValidator(Validator[_DictWithExecuteResult]):
    """Compare the result (aka cell's execute output).

    Returns "yes" if the result is a perfect match.
    Returns "partial" in the following cases:
    1. Submission is wrong in the index / columns.
    2. Data in submission is part of the reference data (e.g., a sub-dataframe or one column).
    3. The output is printed to the console rather than returned.
    4. The output is directly shown within the source code.
    Returns "no" otherwise.
    """

    alias: ClassVar[str] = "result"

    def __init__(
        self,
        compare_fn: CompareFunction | str | dict | None = None,
        **kwargs: Any,
    ):
        self.source_code = None
        self.source_config = None
        if compare_fn is None and kwargs:
            compare_fn = kwargs
        if isinstance(compare_fn, str):
            self.source_code = compare_fn
        elif isinstance(compare_fn, dict):
            self.source_config = compare_fn

        self.compare_fn = _compare_fn_from_config(compare_fn)
        self.loose_compare_fn = _compare_fn_from_config(compare_fn, loose=True)

    def validate(self, reference, submission) -> ValidateResult:
        execute_result_ref = reference["execute_result"]
        execute_result = submission["execute_result"]
        if execute_result_ref is not None:
            output_inferred = False
            if execute_result is None:
                # 1. Try to find answer in source code.
                if "source_code" in submission:
                    try:
                        answer_in_source = _find_answer_in_source_code(submission["source_code"], execute_result_ref)
                        if answer_in_source:
                            return {
                                "correct": "partial",
                                "category": self.alias,
                                "reason": answer_in_source,
                            }
                    except:
                        pass

                # 2. Trying to guess the missing output.
                try:
                    if "source_code" in submission and "namespace_snapshot" in submission:
                        execute_result = _guess_print_output(
                            cast(Any, submission)["source_code"],
                            cast(Any, submission)["namespace_snapshot"],
                            execute_result_ref,
                        )
                        output_inferred = True
                except Exception:
                    return {
                        "correct": "no",
                        "category": self.alias,
                        "reason": "Output is missing and cannot be inferred:\n" + traceback.format_exc(),
                    }

                # 3. still empty
                if execute_result is None:
                    return {
                        "correct": "no",
                        "category": self.alias,
                        "reason": "Output is missing.",
                    }

            result = _run_compare_fn(
                self.compare_fn,
                self.loose_compare_fn,
                execute_result_ref,
                execute_result,
                self.alias,
            )
            if output_inferred and result["correct"] != "no":
                return {
                    "correct": "partial",
                    "category": self.alias,
                    "reason": "Correct with inferred output:"
                    + ("\n" + str(result["reason"]) if result["reason"] else "."),
                }
            return result
        else:
            # Ignore any result as ground-truth does not have one.
            return {
                "correct": "yes",
                "category": self.alias,
                "reason": (
                    "Correct. Both none." if execute_result is None else "Result is ignored since ground-truth is none."
                ),
            }

    def __repr__(self):
        if self.source_code is not None:
            return f"ResultValidator(\n{add_indent(self.source_code.rstrip(), 2)}\n)"
        elif self.source_config is not None:
            return "ResultValidator(" + ", ".join([f"{key}={value}" for key, value in self.source_config.items()]) + ")"
        elif isinstance(self.compare_fn, ExactMatcher):
            return "ResultValidator()"
        return f"ResultValidator({self.compare_fn})"


class Or(Validator[T]):
    alias: ClassVar[str] = "or"

    def __init__(self, *validators: Validator[T]):
        self.validators = validators

    def validate(self, reference, submission):
        results = []
        for validator in self.validators:
            results.append(validator.validate(reference, submission))
        if any(r["correct"] == "yes" for r in results):
            correct = "yes"
        elif any(r["correct"] == "partial" for r in results):
            correct = "partial"
        else:
            correct = "no"
        return {"correct": correct, "category": self.alias, "reason": results}

    def __repr__(self):
        return "Or(\n" + ",\n".join([add_indent(repr(validator), 2) for validator in self.validators]) + "\n)"

    @classmethod
    def load(cls, type_, config):
        return Or(*[Validator.load(subtype, subconfig) for subtype, subconfig in config.items()])


class And(Validator[T]):
    alias: ClassVar[str] = "and"

    def __init__(self, *validators: Validator[T]):
        self.validators = validators

    def validate(self, reference, submission):
        results = []
        for validator in self.validators:
            results.append(validator.validate(reference, submission))

        if any(r["correct"] == "no" for r in results):
            correct = "no"
        elif any(r["correct"] == "partial" for r in results):
            correct = "partial"
        else:
            correct = "yes"
        return {"correct": correct, "category": self.alias, "reason": results}

    def __repr__(self):
        return "And(\n" + ",\n".join([add_indent(repr(validator), 2) for validator in self.validators]) + "\n)"

    @classmethod
    def load(cls, type_, config):
        return And(*[Validator.load(subtype, subconfig) for subtype, subconfig in config.items()])


class NamespaceChecker(Validator[_DictWithNamespaceSnapshot]):
    """Checking whether the specified variables have the correct value."""

    alias: ClassVar[str] = "namespace_check"

    def __init__(self, **names: CompareFunction | str | dict | None):
        self.names: dict[str, tuple[CompareFunction, CompareFunction]] = {}
        for name, compare_fn in names.items():
            self.names[name] = (
                _compare_fn_from_config(compare_fn),
                _compare_fn_from_config(compare_fn, loose=True),
            )

    def validate(self, reference, submission):
        namespace_ref = reference["namespace_snapshot"]
        namespace = submission["namespace_snapshot"]
        results = []
        for name, (compare_fn, compare_loose) in self.names.items():
            if name not in namespace_ref:
                raise ValueError(f"Variable {name} not found in reference.")
            if name not in namespace:
                results.append(
                    {"correct": "no", "category": self.alias, "variable": name, "reason": f"Variable {name} not found in submission."}
                )
            else:
                result = _run_compare_fn(
                    compare_fn,
                    compare_loose,
                    namespace_ref[name],
                    namespace[name],
                    self.alias,
                    mismatch_prefix=f"Variable {name}: ",
                    failure_prefix=f"Cannot compare variable {name}:\n",
                )
                results.append(
                    {"correct": result["correct"], "category": self.alias, "variable": name, "reason": result["reason"]}
                )

        if any(r["correct"] == "no" for r in results):
            correct = "no"
        elif any(r["correct"] == "partial" for r in results):
            correct = "partial"
        else:
            correct = "yes"
        return {"correct": correct, "category": self.alias, "reason": results}

    def __repr__(self) -> str:
        return (
            "NamespaceChecker(\n"
            + ",\n".join([add_indent(f"{name}: {compare_fn}", 2) for name, compare_fn in self.names.items()])
            + "\n)"
        )


class StreamOutputValidator(Validator[_DictWithStreamOutput]):
    """Check the output of the cell."""

    alias: ClassVar[str] = "stream"

    def validate(self, reference, submission):
        stream_output_ref = reference["stream_output"]
        stream_output = submission["stream_output"]
        if stream_output_ref != stream_output:
            return {
                "correct": "no",
                "category": self.alias,
                "reason": f"Stream output is incorrect:\nExpected:\n{stream_output_ref}\nFound:\n{stream_output}",
            }
        return {"correct": "yes", "category": self.alias, "reason": "Stream output is correct."}

    def __repr__(self) -> str:
        return "StreamOutputValidator()"


class ModelValidator(Validator[_DictWithNamespaceSnapshot]):
    """The moel will be tested against inputs, and the outputs will be compared with the labels,
    with the ``metric_type`` metric. The metric will be compared against the reference metric with the ``tolerance``.

    If ``tolerance`` is 0, the metric will be compared with the reference metric exactly.
    If ``tolerance`` is positive, the metric should be no greater than (1 + tolerance) * reference_metric.
    If ``tolerance`` is negative, the metric should be no less than (1 + tolerance) * reference_metric.
    """

    alias: ClassVar[str] = "model"

    def __init__(
        self,
        model_name: str,
        inputs_name: str,
        labels_name: str,
        metric_type: str | list[str],
        tolerance: float | list[float] = 0.0,
    ):
        self.model_name = model_name
        self.inputs_name = inputs_name
        self.labels_name = labels_name

        if not isinstance(metric_type, list):
            metric_type = [metric_type]
        if not isinstance(tolerance, list):
            tolerance = [tolerance for _ in range(len(metric_type))]
        assert len(metric_type) == len(tolerance), "metric_type and tolerance should have the same length."

        self.metric_type = metric_type

        supported_metric_types = [
            "accuracy",
            "precision",
            "recall",
            "f1",
            "roc_auc",
            "r2",
            "mse",
            "rmse",
        ]
        for metric_type in self.metric_type:
            assert (
                metric_type in supported_metric_types
            ), f"metric_type should be one of {supported_metric_types}, not {metric_type}"

        self.tolerance = tolerance

    def __repr__(self) -> str:
        return (
            f"ModelValidator(model_name={self.model_name}, inputs_name={self.inputs_name}, "
            f"labels_name={self.labels_name}, metric_type={self.metric_type}, tolerance={self.tolerance})"
        )

    def evaluate_metric(self, metric_type, y_true, y_pred):
        if metric_type == "accuracy":
            from sklearn.metrics import accuracy_score

            reference_metric = accuracy_score(y_true, y_pred)
        elif metric_type == "precision":
            from sklearn.metrics import precision_score

            reference_metric = precision_score(y_true, y_pred)
        elif metric_type == "recall":
            from sklearn.metrics import recall_score

            reference_metric = recall_score(y_true, y_pred)
        elif metric_type == "f1":
            from sklearn.metrics import f1_score

            reference_metric = f1_score(y_true, y_pred)
        elif metric_type == "roc_auc":
            from sklearn.metrics import roc_auc_score

            reference_metric = roc_auc_score(y_true, y_pred)
        elif metric_type == "r2":
            from sklearn.metrics import r2_score

            reference_metric = r2_score(y_true, y_pred)
        elif metric_type == "mse":
            from sklearn.metrics import mean_squared_error

            reference_metric = mean_squared_error(y_true, y_pred)
        elif metric_type == "rmse":
            from sklearn.metrics import mean_squared_error

            reference_metric = np.sqrt(mean_squared_error(y_true, y_pred))
        else:
            raise ValueError(f"Unsupported metric_type: {metric_type}")
        return reference_metric

    def validate(self, reference, submission) -> ValidateResult:
        reference_model = reference["namespace_snapshot"][self.model_name]
        inputs = reference["namespace_snapshot"][self.inputs_name]
        labels = reference["namespace_snapshot"][self.labels_name]
        reference_pred = reference_model.predict(inputs)

        if self.model_name not in submission["namespace_snapshot"]:
            return {
                "correct": "no",
                "category": self.alias,
                "reason": f"Model {self.model_name} not found in submission.",
            }
        submission_model = submission["namespace_snapshot"][self.model_name]
        try:
            submission_pred = submission_model.predict(inputs)
        except Exception:
            return {
                "correct": "no",
                "category": self.alias,
                "reason": f"Model {self.model_name} raised an exception when predicting:\n{traceback.format_exc()}",
            }

        for metric_type, tolerance in zip(self.metric_type, self.tolerance):
            reference_metric = self.evaluate_metric(metric_type, labels, reference_pred)
            try:
                submission_metric = self.evaluate_metric(metric_type, labels, submission_pred)
            except Exception:
                return {
                    "correct": "no",
                    "category": self.alias,
                    "reason": f"Model {self.model_name} raised an exception when calculating metric {metric_type}:\n{traceback.format_exc()}",
                }

            if tolerance == 0:
                if not np.isclose(submission_metric, reference_metric):
                    return {
                        "correct": "no",
                        "category": self.alias,
                        "reason": f"Metric {metric_type} is incorrect: {submission_metric} vs {reference_metric}",
                    }
            elif tolerance > 0:
                if submission_metric > (1 + tolerance) * reference_metric:
                    return {
                        "correct": "no",
                        "category": self.alias,
                        "reason": f"Metric {metric_type} is incorrect: {submission_metric} vs {reference_metric} (tolerance = {tolerance})",
                    }
            elif tolerance < 0:
                if submission_metric < (1 + tolerance) * reference_metric:
                    return {
                        "correct": "no",
                        "category": self.alias,
                        "reason": f"Metric {metric_type} is incorrect: {submission_metric} vs {reference_metric} (tolerance = {tolerance})",
                    }
        return {"correct": "yes", "category": self.alias, "reason": "Model satisfies the specified criterion."}


class TableTestValidator(Validator[_DictWithNamespaceSnapshot]):
    """The defined function will be tested against multiple inputs.

    Parameters:
        function_name: The name of the function to be tested.
        test_cases:
            A list of test cases.
            Each test case is a tuple of parameters or a dict of parameters, or a code that generates a test case.
        input_validator: A function that takes the parameters and returns whether the test case is valid.
        input_checker: To check whether the input is correctly modified after execution.
        output_checker: To check whether the output is correct.
    """

    alias: ClassVar[str] = "table_test"

    def __init__(
        self,
        function_name: str,
        test_cases: list[tuple[Any, ...] | dict[str, Any] | str],
        input_validator: str | Callable[..., bool | None] | None = None,
        input_checker: str | CompareFunction | dict | bool | None = None,
        output_checker: str | CompareFunction | dict | None = None,
    ):
        self.function_name = function_name
        self.test_cases: list[tuple[Any, ...] | dict[str, Any]] = []
        if isinstance(input_validator, str):
            self.input_validator = self.code_to_input_validator(input_validator)
        elif input_validator is None:
            self.input_validator = self.always_true
        else:
            self.input_validator = input_validator

        if input_checker is False:
            self.input_checker = None
        else:
            if input_checker in (True, None):
                input_checker = None  # default
            self.input_checker = (
                _compare_fn_from_config(input_checker),
                _compare_fn_from_config(input_checker, loose=True),
            )

        self.output_checker = (
            _compare_fn_from_config(output_checker),
            _compare_fn_from_config(output_checker, loose=True),
        )

        last_case = None
        for case_id, test_case in enumerate(test_cases):
            random.seed(case_id)
            np.random.seed(case_id)
            if test_case == "//":
                # Repeat last test case
                if last_case is None:
                    raise ValueError("No test case to repeat.")
                else:
                    # Generate the case with a different random seed
                    new_case = self.code_to_test_case(last_case, case_id, assume_list_as_tuple=True)
            else:
                new_case = self.code_to_test_case(test_case, case_id, assume_list_as_tuple=True)
                last_case = test_case
            if not isinstance(new_case, tuple) and not isinstance(new_case, dict):
                raise ValueError(f"Invalid test case (#{case_id}), not a tuple and not a dict: {new_case}")
            try:
                if (isinstance(new_case, dict) and self.input_validator(**new_case) is False) or (
                    isinstance(new_case, tuple) and self.input_validator(*new_case) is False
                ):
                    raise ValueError(f"Invalid test case (#{case_id}): {new_case}")
            except AssertionError:
                raise ValueError(f"Invalid test case (#{case_id}): {new_case}\n{traceback.format_exc()}")
            self.test_cases.append(new_case)

    @staticmethod
    def always_true(*args, **kwargs) -> bool:
        return True

    @staticmethod
    def code_to_input_validator(code: str) -> Callable[..., bool]:
        ns = exec_code(code, "input-validator")
        return ns["_validate"]

    @staticmethod
    def code_to_test_case(parameter: Any, case_id: int | None = None, assume_list_as_tuple: bool = False) -> Any:
        if isinstance(parameter, tuple):
            return tuple(TableTestValidator.code_to_test_case(item, case_id) for item in parameter)
        if assume_list_as_tuple and isinstance(parameter, list):
            # YAML has trouble expressing a tuple. So list should be treated as tuple on the top-level.
            return tuple(TableTestValidator.code_to_test_case(item, case_id) for item in parameter)

        if isinstance(parameter, str):
            param_stripped = parameter.strip()
            if param_stripped.startswith("```\n") and param_stripped.endswith("```"):
                param_stripped = param_stripped[4:-3]
                ns = exec_code(param_stripped, "test-generate")
                if "_test_case" in ns:
                    parameter = ns["_test_case"]
                elif "_generate" in ns and isinstance(ns["_generate"], types.FunctionType):
                    parameter = ns["_generate"]()
                else:
                    raise ValueError(f"Couldn't find _test_case or function _generate in {ns.keys()}")
        if isinstance(parameter, str) and parameter.startswith("`") and parameter.endswith("`"):
            parameter = parameter[1:-1]
            parameter = exec_code(parameter, "test-expression", mode="eval")
        return parameter

    def __repr__(self) -> str:
        return (
            "TableTestValidator(\n"
            + ",\n".join([self.function_name] + [add_indent(repr(test_case), 2) for test_case in self.test_cases])
            + "\n)"
        )

    def validate(self, reference, submission) -> ValidateResult:
        namespace_ref = reference["namespace_snapshot"]
        namespace = submission["namespace_snapshot"]
        if self.function_name not in namespace_ref:
            raise ValueError(f"Function {self.function_name} not found in reference.")
        if self.function_name not in namespace:
            return {
                "correct": "no",
                "category": self.alias,
                "reason": f"Function {self.function_name} not found in submission.",
            }
        function_ref = namespace_ref[self.function_name]
        function = namespace[self.function_name]
        for args in self.test_cases:
            input_expected = copy.deepcopy(args)
            if isinstance(input_expected, dict):
                output_expected = function_ref(**input_expected)
            else:
                output_expected = function_ref(*input_expected)
            try:
                input_found = copy.deepcopy(args)
                if isinstance(input_found, dict):
                    output_found = function(**input_found)
                else:
                    output_found = function(*input_found)
            except KeyboardInterrupt:
                raise
            except:
                return {
                    "correct": "no",
                    "category": "crash",
                    "reason": f"Function {self.function_name} raised an exception on test case {args}:\n{traceback.format_exc()}",
                }

            if self.input_checker is not None:
                check, check_loose = self.input_checker
                result = _run_compare_fn(
                    check,
                    check_loose,
                    input_expected,
                    input_found,
                    self.alias,
                    mismatch_prefix=f"Input of function {self.function_name} is problematic after execution on test case #{args}: ",
                    failure_prefix=f"Failed to compare input of function {self.function_name} after execution on test case #{args}:\n",
                )
                if result["correct"] != "yes":
                    return result

            check, check_loose = self.output_checker
            result = _run_compare_fn(
                check,
                check_loose,
                output_expected,
                output_found,
                self.alias,
                mismatch_prefix=f"Output of function {self.function_name} is problematic on test case {args}: ",
                failure_prefix=f"Failed to compare output of function {self.function_name} on test case {args}:\n",
            )
            if result["correct"] != "yes":
                return result

        return {"correct": "yes", "category": self.alias, "reason": "All test cases pass."}


class VisualizationValidator(Validator):
    alias: ClassVar[str] = "vis"

    # TODO: implement this


class Verdict(str, Enum):
    Correct = "CORRECT"
    IntactViolation = "INTACT_VIOLATION"
    PresentationError = "PRESENTATION_ERROR"
    WrongOutput = "WRONG_OUTPUT"
    WrongVariables = "WRONG_VARIABLES"
    UnitTestFailure = "UNIT_TEST_FAILURE"
    Timeout = "TIMEOUT"
    Crash = "CRASH"
    BadModel = "BAD_MODEL"
    SyntaxError = "SYNTAX_ERROR"
    Unknown = "UNKNOWN"


class Subverdict(str, Enum):
    Uncategorized = "UNCATEGORIZED"
    # For presentation error
    IndexMismatch = "INDEX_MISMATCH"
    MissingReturn = "MISSING_RETURN"
    PartialMatch = "PARTIAL_MATCH"
    NonCode = "NON_CODE"
    # For wrong output / variables / unit-test failure
    ShapeMismatch = "SHAPE_MISMATCH"
    DtypeMismatch = "DTYPE_MISMATCH"
    ColumnsMismatch = "COLUMNS_MISMATCH"
    ValueMismatch = "VALUE_MISMATCH"
    UnexpectedType = "UNEXPECTED_TYPE"
    # Crash
    ModuleNotFound = "MODULE_NOT_FOUND"
    AttributeError = "ATTRIBUTE_ERROR"
    KeyError = "KEY_ERROR"
    NameError = "NAME_ERROR"
    TypeError = "TYPE_ERROR"
    ValueError = "VALUE_ERROR"


def categorize_comparison_failure(failure: str) -> Subverdict:
    if "shape mismatch" in failure:
        return Subverdict.ShapeMismatch
    if '"dtype" are different' in failure:
        return Subverdict.DtypeMismatch
    if "columns are different" in failure or "Columns mismatch:" in failure:
        return Subverdict.ColumnsMismatch
    if (
        "Wrong value:" in failure
        or "values are different" in failure
        or "Series are different" in failure
        or "not equal:" in failure
        or "Length mismatch:" in failure
        or "Keys mismatch:" in failure
    ):
        return Subverdict.ValueMismatch
    if "Wrong type:" in failure or "Mismatched type:" in failure:
        return Subverdict.UnexpectedType
    return Subverdict.Uncategorized


def validator_comments_to_verdict(
    comments: ValidateResult,
) -> tuple[Verdict, Subverdict, str]:
    def _traverse_comments(comments: ValidateResult):
        if comments["correct"] != "yes":
            if comments["correct"] == "no":
                completely_problematic_categories.add(comments["category"])
            if comments["category"] not in problematic_verdicts and comments["category"] not in ("and", "or"):
                problematic_verdicts[comments["category"]] = comments["reason"]
            if comments["correct"] == "partial" and isinstance(comments["reason"], str):
                partially_problematic_verdicts.append(comments["reason"])
        if isinstance(comments["reason"], list):
            for sub_comments in comments["reason"]:
                _traverse_comments(sub_comments)

    # All validate results that are problematic (with correct being partial or no)
    problematic_verdicts: dict[str, list[ValidateResult] | str] = {}
    # Verdict categories that return no.
    completely_problematic_categories: set[str] = set()
    # with correct being partial
    partially_problematic_verdicts: list[str] = []
    _traverse_comments(comments)

    if comments["correct"] == "yes":
        return Verdict.Correct, Subverdict.Uncategorized, ""

    if comments["correct"] == "no" and "crash" in completely_problematic_categories:
        crash_reason = str(problematic_verdicts["crash"])
        if "SyntaxError:" in problematic_verdicts["crash"]:
            return Verdict.SyntaxError, Subverdict.Uncategorized, crash_reason
        if "dseval.limit.TimeLimitError" in problematic_verdicts["crash"]:
            return Verdict.Timeout, Subverdict.Uncategorized, crash_reason

        verdict = Verdict.Crash
        subverdict = Subverdict.Uncategorized
        if "\n" in crash_reason:
            lines = crash_reason.splitlines()
            if any(line.startswith("ModuleNotFoundError:") for line in lines):
                subverdict = Subverdict.ModuleNotFound
            elif any(line.startswith("KeyError:") for line in lines):
                subverdict = Subverdict.KeyError
            elif any(line.startswith("TypeError:") for line in lines):
                subverdict = Subverdict.TypeError
            elif any(line.startswith("ValueError:") for line in lines):
                subverdict = Subverdict.ValueError
            elif any(line.startswith("NameError:") for line in lines):
                subverdict = Subverdict.NameError
            elif any(line.startswith("AttributeError:") for line in lines):
                subverdict = Subverdict.AttributeError
        return verdict, subverdict, crash_reason

    print(completely_problematic_categories)
    if completely_problematic_categories == {"namespace_intact"}:
        return (
            Verdict.IntactViolation,
            Subverdict.Uncategorized,
            str(problematic_verdicts["namespace_intact"]),
        )

    if comments["correct"] == "partial":
        comment_fallback = ""
        for comment in partially_problematic_verdicts:
            # This will include "partial" from result, namespace_check and etc.
            if "Partial match on" in comment:
                return Verdict.PresentationError, Subverdict.PartialMatch, comment
            if "Correct with inferred output:" in comment:
                return Verdict.PresentationError, Subverdict.MissingReturn, comment
            if "Output is directly shown in the code" in comment:
                return Verdict.PresentationError, Subverdict.NonCode, comment
            comment_fallback = comment
        return Verdict.PresentationError, Subverdict.IndexMismatch, comment_fallback

    if "namespace_check" in problematic_verdicts:
        check_reason = problematic_verdicts["namespace_check"]
        assert isinstance(check_reason, list)
        return (
            Verdict.WrongVariables,
            categorize_comparison_failure(str(check_reason)),
            "\n".join(["- " + str(line["reason"]) for line in check_reason]),
        )

    if "result" in problematic_verdicts:
        result_reason = problematic_verdicts["result"]
        assert isinstance(result_reason, str)
        return (
            Verdict.WrongOutput,
            categorize_comparison_failure(result_reason),
            result_reason,
        )

    if "model" in problematic_verdicts:
        model_reason = problematic_verdicts["model"]
        assert isinstance(model_reason, str)
        return Verdict.BadModel, Subverdict.Uncategorized, model_reason

    if "table_test" in problematic_verdicts:
        table_reason = problematic_verdicts["table_test"]
        assert isinstance(table_reason, str)
        return (
            Verdict.UnitTestFailure,
            categorize_comparison_failure(table_reason),
            table_reason,
        )

    return Verdict.Unknown, Subverdict.Uncategorized, json.dumps(problematic_verdicts)
