import re

import numpy as np
import pytest

from .match import Match
from .simulation import Error
from .validator import (
    And,
    ModelValidator,
    NamespaceChecker,
    NamespaceIntactGuard,
    CrashValidator,
    Or,
    ResultValidator,
    StreamOutputValidator,
    TableTestValidator,
    ValidateResult,
    Validator,
    _DictWithError,
    _DictWithExecuteResult,
    _DictWithNamespaceDiff,
    _DictWithNamespaceSnapshot,
    _DictWithStreamOutput,
    _code_to_compare_fn,
    _guess_print_output,
)


def test_crash_validator():
    validator = CrashValidator()
    reference = _DictWithError(error=None)
    submission = _DictWithError(error=None)
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "yes",
        "category": "crash",
        "reason": "Execution finishes successfully.",
    }

    reference = _DictWithError(error=None)
    submission = _DictWithError(error=Error(ename="ValueError", evalue="Some error message", traceback=[]))
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "no",
        "category": "crash",
        "reason": "Submission crashes.",
    }


def test_addition_allowed():
    guard = NamespaceIntactGuard()
    reference = _DictWithNamespaceDiff(namespace_diff={})
    submission = _DictWithNamespaceDiff(namespace_diff={"foo": "added"})
    result = guard.validate(reference, submission)
    assert result == ValidateResult(correct="yes", category="namespace_intact", reason="Namespace is intact.")


def test_update_not_allowed():
    guard = NamespaceIntactGuard()
    reference = _DictWithNamespaceDiff(namespace_diff={})
    submission = _DictWithNamespaceDiff(namespace_diff={"foo": "updated"})
    result = guard.validate(reference, submission)
    assert result == ValidateResult(
        correct="no",
        category="namespace_intact",
        reason="Unexpected variable updated: foo",
    )


def test_update_allowed():
    guard = NamespaceIntactGuard()
    reference = _DictWithNamespaceDiff(namespace_diff={"foo": "updated"})
    submission = _DictWithNamespaceDiff(namespace_diff={"foo": "updated"})
    result = guard.validate(reference, submission)
    assert result == ValidateResult(correct="yes", category="namespace_intact", reason="Namespace is intact.")


def test_replacement_not_allowed():
    guard = NamespaceIntactGuard(replacement=False)
    reference = _DictWithNamespaceDiff(namespace_diff={"foo": "updated"})
    submission = _DictWithNamespaceDiff(namespace_diff={"foo": "replaced"})
    result = guard.validate(reference, submission)
    assert result == ValidateResult(
        correct="no",
        category="namespace_intact",
        reason="Unexpected variable replaced: foo",
    )


def test_replacement_allowed():
    guard = NamespaceIntactGuard(replacement=True)
    reference = _DictWithNamespaceDiff(namespace_diff={})
    submission = _DictWithNamespaceDiff(namespace_diff={"foo": "replaced"})
    result = guard.validate(reference, submission)
    assert result == ValidateResult(correct="yes", category="namespace_intact", reason="Namespace is intact.")


def test_deletion_not_allowed():
    guard = NamespaceIntactGuard(deletion=["bar"])
    reference = _DictWithNamespaceDiff(namespace_diff={})
    submission = _DictWithNamespaceDiff(namespace_diff={"foo": "deleted"})
    result = guard.validate(reference, submission)
    assert result == ValidateResult(
        correct="no",
        category="namespace_intact",
        reason="Unexpected variable deleted: foo",
    )


def test_deletion_allowed():
    guard = NamespaceIntactGuard(deletion=["foo"])
    reference = _DictWithNamespaceDiff(namespace_diff={"foo": "added"})
    submission = _DictWithNamespaceDiff(namespace_diff={"foo": "deleted"})
    result = guard.validate(reference, submission)
    assert result == ValidateResult(correct="yes", category="namespace_intact", reason="Namespace is intact.")


def test_specific_variables_allowed():
    guard = NamespaceIntactGuard(update=["foo"], deletion=["bar"])
    reference = _DictWithNamespaceDiff(namespace_diff={})
    submission = _DictWithNamespaceDiff(namespace_diff={"foo": "updated", "bar": "deleted"})
    result = guard.validate(reference, submission)
    assert result == ValidateResult(correct="yes", category="namespace_intact", reason="Namespace is intact.")


def test_validate_with_exact_match():
    validator = ResultValidator()
    reference = _DictWithExecuteResult(execute_result="Hello, world!")
    submission = _DictWithExecuteResult(execute_result="Hello, world!")
    result = validator.validate(reference, submission)
    assert result["correct"] == "yes"


def test_validate_fuzzy_match():
    import pandas as pd

    one = pd.Series([1, 2, 3], index=pd.Index([4, 5, 6], name="a"), name="b")
    other = pd.Series([7, 8, 9], index=pd.Index([1, 2, 3], name="c"), name="d")
    reference = _DictWithExecuteResult(execute_result=one)
    submission = _DictWithExecuteResult(execute_result=other)
    validator = ResultValidator(ignore_index=True, match_partial=True)
    result = validator.validate(reference, submission)
    assert result["correct"] == "partial"
    assert isinstance(result["reason"], str) and result["reason"].startswith(
        "Result matches the expected with looser constraints:\nPartial match on index:"
    )

    validator = ResultValidator(ignore_index=True, ignore_names=True, match_partial=True)
    result = validator.validate(reference, submission)
    assert result["correct"] == "yes"
    assert isinstance(result["reason"], str) and result["reason"].startswith(
        "Result matches the expected:\nPartial match on index:"
    )


def test_guess_print_output():
    # Test with a single print statement
    source_code = "print('Hello, world!')"
    namespace = {}
    expected = "Hello, world!"
    result = _guess_print_output(source_code, namespace, expected)
    assert result is None

    # Test with multiple print statements
    source_code = "a = 1\nb = 2\nc = 4\nprint(a, b)\nprint(c)"
    namespace = {"a": 1, "b": 2, "c": 4}
    result = _guess_print_output(source_code, namespace, (2, 3, 5))
    assert result == (1, 2, 4)

    # Test with a print statement that prints a complex expression
    source_code = "y = 10\nprint(f'abc:{x * y}', x - y)"
    namespace = {"x": 5, "y": 10}
    expected = {"result": 30, "t": 5}
    result = _guess_print_output(source_code, namespace, expected)
    assert result == {"result": 50, "t": -5}

    # Test with assign statement
    source_code = "x = 1\ny = 2\nz = 3"
    namespace = {"x": 1, "y": 2, "z": 3}
    expected = 4
    result = _guess_print_output(source_code, namespace, expected)
    assert result == 3

    # Test with attribute assign statement
    import pandas as pd

    source_code = "import pd\nx = pd.DataFrame({'a': [1]})\nx.columns = ['b']"
    namespace = {"x": pd.DataFrame({"b": [1]})}
    expected = pd.DataFrame({"a": [1]})
    result = _guess_print_output(source_code, namespace, expected)
    assert result.equals(namespace["x"])

    source_code = "import pd\nx = pd.DataFrame({'a': [1]})\nx.reset_index(inplace=True, drop=True)"
    result = _guess_print_output(source_code, namespace, expected)
    assert result.equals(namespace["x"])


def test_remediate_output():
    validator = ResultValidator()
    reference = _DictWithExecuteResult(execute_result="Hello, world!")
    submission = dict(
        execute_result=None,
        namespace_snapshot={"x": "Hello, world!"},
        source_code="print(x)",
    )
    result = validator.validate(reference, submission)  # type: ignore
    assert result == {
        "correct": "partial",
        "category": "result",
        "reason": "Correct with inferred output:\nResult matches the expected.",
    }

    submission["namespace_snapshot"]["x"] = "Goodbye, world!"  # type: ignore
    result = validator.validate(reference, submission)  # type: ignore
    assert result == {
        "correct": "no",
        "category": "result",
        "reason": "Expect Hello, world!, got Goodbye, world!",
    }

    submission = _DictWithExecuteResult(execute_result="Hello, world!")
    result = validator.validate(reference, submission)
    assert result["correct"] == "yes"


def test_validate_with_exact_mismatch():
    validator = ResultValidator()
    reference = _DictWithExecuteResult(execute_result="Hello, world!")
    submission = _DictWithExecuteResult(execute_result="Goodbye, world!")
    result = validator.validate(reference, submission)
    assert result["correct"] == "no"
    assert "reason" in result
    assert result["category"] == "result"
    assert result["reason"] == "Expect Hello, world!, got Goodbye, world!"


def test_validate_with_assertion_error():
    def foo(a, b):
        assert 1 == 2
        return Match(match=True, reason="")

    validator = ResultValidator(foo)
    reference = _DictWithExecuteResult(execute_result="Hello, world!")
    submission = _DictWithExecuteResult(execute_result="Hello, world!")
    result = validator.validate(reference, submission)
    assert result["correct"] == "no"
    assert "reason" in result
    assert isinstance(result["reason"], str) and result["reason"].startswith("Comparison raises AssertionError:")


def test_validate_with_none_reference():
    validator = ResultValidator()
    reference = _DictWithExecuteResult(execute_result=None)
    submission = _DictWithExecuteResult(execute_result="Hello, world!")
    result = validator.validate(reference, submission)
    assert result["correct"] == "yes"
    assert "reason" in result
    assert result["reason"] == "Result is ignored since ground-truth is none."


def test_validate_with_none_submission():
    validator = ResultValidator()
    reference = _DictWithExecuteResult(execute_result="Hello, world!")
    submission = _DictWithExecuteResult(execute_result=None)
    result = validator.validate(reference, submission)
    assert result["correct"] == "no"
    assert "reason" in result
    assert result["category"] == "result"
    assert result["reason"] == "Output is missing."


def test_validate_with_compare_fn():
    def compare_fn(ref, sub):
        return Match(match=True, reason="")

    validator = ResultValidator(compare_fn)
    reference = _DictWithExecuteResult(execute_result="Hello, world!")
    submission = _DictWithExecuteResult(execute_result="Goodbye, world!")
    result = validator.validate(reference, submission)
    assert result["correct"] == "yes"
    assert compare_fn("Hello, world!", "Goodbye, world!")


def test_code_to_compare_fn():
    code = "def compare_fn(ref, sub):\n    return {'match': ref == sub, 'reason': ''}\n"
    compare_fn = _code_to_compare_fn(code)
    assert callable(compare_fn)
    result = compare_fn("Hello, world!", "Hello, world!")
    assert result == {"match": True, "reason": ""}

    validator = ResultValidator(compare_fn)
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([1, 2, 3])
    result = validator.validate(
        _DictWithExecuteResult(execute_result=arr1),
        _DictWithExecuteResult(execute_result=arr2),
    )
    assert result["correct"] == "no"
    assert isinstance(result["reason"], str) and result["reason"].startswith("Comparison failure:")


def test_or_with_one_validator_passing():
    validator1 = ResultValidator(lambda a, b: Match(match=False, reason=""))
    validator2 = ResultValidator()
    validator = Or(validator1, validator2)
    assert re.match(r"Or\(\n  ResultValidator\(.*\),\n  ResultValidator\(.*\)\n\)", repr(validator))
    reference = _DictWithExecuteResult(execute_result="Hello, world!")
    submission = _DictWithExecuteResult(execute_result="Hello, world!")
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "yes",
        "category": "or",
        "reason": [
            {"correct": "no", "category": "result", "reason": ""},
            {
                "correct": "yes",
                "category": "result",
                "reason": "Result matches the expected.",
            },
        ],
    }


def test_or_with_multiple_validators():
    validator1 = ResultValidator(lambda ref, sub: {"match": (ref == sub).all(), "reason": ""})
    validator2 = ResultValidator(lambda ref, sub: {"match": (ref != sub).all(), "reason": ""})
    validator3 = ResultValidator(lambda ref, sub: {"match": (ref + sub).sum() == 0, "reason": ""})
    validator = Or(validator1, validator2, validator3)
    reference = _DictWithExecuteResult(execute_result=np.array([1, 2, 3]))
    submission = _DictWithExecuteResult(execute_result=np.array([-1, -2, -3]))
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "yes",
        "category": "or",
        "reason": [
            {"correct": "no", "category": "result", "reason": ""},
            {
                "correct": "yes",
                "category": "result",
                "reason": "Result matches the expected.",
            },
            {
                "correct": "yes",
                "category": "result",
                "reason": "Result matches the expected.",
            },
        ],
    }


def test_and_with_all_validators_passing():
    validator1 = ResultValidator()
    validator2 = ResultValidator(lambda a, b: Match(match=True, reason=""))
    validator = And(validator1, validator2)
    reference = _DictWithExecuteResult(execute_result="Hello, moon!")
    submission = _DictWithExecuteResult(execute_result="Hello, moon!")
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "yes",
        "category": "and",
        "reason": [
            {
                "correct": "yes",
                "category": "result",
                "reason": "Result matches the expected.",
            },
            {
                "correct": "yes",
                "category": "result",
                "reason": "Result matches the expected.",
            },
        ],
    }


def test_and_with_fuzzy_match():
    import pandas as pd

    one = [4, 5, 6]
    other = pd.DataFrame(
        {
            "a": [1, 2, 3],
            "b": [4, 5, 6],
        }
    )
    validator = And(ResultValidator(ignore_index=True, ignore_names=True, match_partial=True))
    reference = _DictWithExecuteResult(execute_result=one)
    submission = _DictWithExecuteResult(execute_result=other)
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "yes",
        "category": "and",
        "reason": [
            {
                "correct": "yes",
                "category": "result",
                "reason": "Result matches the expected:\nPartial match on column: b",
            }
        ],
    }

    validator = And(ResultValidator())
    result = validator.validate(reference, submission)
    print(result)
    assert result == {
        "correct": "partial",
        "category": "and",
        "reason": [
            {
                "correct": "partial",
                "category": "result",
                "reason": "Result matches the expected with looser constraints:\nPartial match on column: b",
            }
        ],
    }


def test_and_with_one_validator_failing():
    validator1 = ResultValidator(lambda a, b: Match(match=True, reason=""))
    validator2 = ResultValidator()
    validator = And(validator1, validator2)
    reference = _DictWithExecuteResult(execute_result="Hello, moon!")
    submission = _DictWithExecuteResult(execute_result="Goodbye, moon!")
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "no",
        "category": "and",
        "reason": [
            {
                "correct": "yes",
                "category": "result",
                "reason": "Result matches the expected.",
            },
            {
                "correct": "no",
                "category": "result",
                "reason": "Expect Hello, moon!, got Goodbye, moon!",
            },
        ],
    }


def test_answer_in_source():
    validator = ResultValidator()
    reference = _DictWithExecuteResult(source_code="", execute_result=123)
    submission = _DictWithExecuteResult(execute_result=None, source_code="Has 123 observations in total.")
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "partial",
        "category": "result",
        "reason": "Output is directly shown in the code: 123",
    }


def test_namespace_checker_with_exact_match():
    checker = NamespaceChecker(foo=None)
    reference = _DictWithNamespaceSnapshot(namespace_snapshot={"foo": "bar", "baz": 42})
    submission = _DictWithNamespaceSnapshot(namespace_snapshot={"foo": "bar", "baz": 43})
    result = checker.validate(reference, submission)
    assert result == {
        "correct": "yes",
        "category": "namespace_check",
        "reason": [
            {
                "correct": "yes",
                "variable": "foo",
                "reason": "Result matches the expected.",
            }
        ],
    }


def test_namespace_checker_with_mismatch():
    checker = NamespaceChecker(foo=None, baz=None)
    reference = _DictWithNamespaceSnapshot(namespace_snapshot={"foo": "bar", "baz": 42})
    submission = _DictWithNamespaceSnapshot(namespace_snapshot={"foo": "bar", "baz": 43})
    result = checker.validate(reference, submission)
    assert result == {
        "correct": "no",
        "category": "namespace_check",
        "reason": [
            {
                "correct": "yes",
                "variable": "foo",
                "reason": "Result matches the expected.",
            },
            {
                "correct": "no",
                "variable": "baz",
                "reason": "Variable baz: Wrong value: 42 vs. 43",
            },
        ],
    }


def test_namespace_checker_with_missing_variable():
    checker = NamespaceChecker(foo=None, baz=None)
    reference = _DictWithNamespaceSnapshot(namespace_snapshot={"foo": "bar", "baz": 42})
    submission = _DictWithNamespaceSnapshot(namespace_snapshot={"foo": "bar"})
    result = checker.validate(reference, submission)
    assert result == {
        "correct": "no",
        "category": "namespace_check",
        "reason": [
            {
                "correct": "yes",
                "variable": "foo",
                "reason": "Result matches the expected.",
            },
            {
                "correct": "no",
                "variable": "baz",
                "reason": "Variable baz not found in submission.",
            },
        ],
    }

    reference = _DictWithNamespaceSnapshot(namespace_snapshot={"foo": "bar"})
    with pytest.raises(ValueError, match="Variable baz not found in reference."):
        checker.validate(reference, submission)


def test_namespace_checker_with_custom_compare_fn():
    code = "def compare_fn(ref, sub):\n    return {'match': ref + 1 == sub, 'reason': ''}\n"
    compare_fn = _code_to_compare_fn(code)
    checker = NamespaceChecker(foo=compare_fn)
    reference = _DictWithNamespaceSnapshot(namespace_snapshot={"foo": 1})
    submission = _DictWithNamespaceSnapshot(namespace_snapshot={"foo": 2})
    result = checker.validate(reference, submission)
    assert result["correct"] == "yes"


def test_model_validator():
    from sklearn.datasets import make_classification
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LogisticRegression

    X, y = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, random_state=1)
    X_train, X_test, y_train, y_test = X[:80], X[80:], y[:80], y[80:]
    reference = _DictWithNamespaceSnapshot(
        namespace_snapshot={
            "model": LogisticRegression().fit(X_train, y_train),
            "inputs": X_test,
            "labels": y_test,
        }
    )
    submission = _DictWithNamespaceSnapshot(
        namespace_snapshot={
            "model": RandomForestClassifier().fit(X_train, y_train),
            "inputs": X_test,
            "labels": y_test,
        }
    )

    validator = ModelValidator("model", "inputs", "labels", "accuracy")
    result = validator.validate(reference, submission)
    assert result["correct"] in ["yes", "no"]
    if result["correct"] == "no":
        assert isinstance(result["reason"], str) and result["reason"].startswith("Metric accuracy is incorrect:")

    validator = ModelValidator("model", "inputs", "labels", "accuracy", -0.1)
    result = validator.validate(reference, submission)
    assert result["correct"] == "yes"

    validator = ModelValidator("model", "inputs", "labels", ["accuracy", "roc_auc"], -0.1)
    result = validator.validate(reference, submission)
    assert result["correct"] == "yes"


def test_table_test_validator():
    validator = TableTestValidator("my_function", [(0, 0), (3, 4)])
    reference = _DictWithNamespaceSnapshot(
        namespace_snapshot={
            "my_function": lambda x, y: x + y,
        }
    )
    submission = _DictWithNamespaceSnapshot(
        namespace_snapshot={
            "my_function": lambda x, y: x + y,
        }
    )
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "yes",
        "category": "table_test",
        "reason": "All test cases pass.",
    }

    submission = _DictWithNamespaceSnapshot(
        namespace_snapshot={
            "my_function": lambda x, y: x * y,
        }
    )
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "no",
        "category": "table_test",
        "reason": "Output of function my_function is problematic on test case (3, 4): Wrong value: 7 vs. 12",
    }

    submission = _DictWithNamespaceSnapshot(
        namespace_snapshot={
            "my_function": lambda x, y: x // y,
        }
    )
    result = validator.validate(reference, submission)
    assert result["correct"] == "no"
    assert result["category"] == "crash"
    assert isinstance(result["reason"], str) and result["reason"].startswith(
        "Function my_function raised an exception on test case (0, 0)"
    )

    submission = _DictWithNamespaceSnapshot(
        namespace_snapshot={
            "my_function": lambda x, y: x * y,
        }
    )
    validator = TableTestValidator(
        "my_function",
        [(0, 0), (3, 4)],
        output_checker=lambda *args: Match(match=True, reason=""),
    )
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "yes",
        "category": "table_test",
        "reason": "All test cases pass.",
    }

    validator = TableTestValidator("my_function", [{"x": 3, "y": 4}])
    reference = _DictWithNamespaceSnapshot(
        namespace_snapshot={
            "my_function": lambda x, y: x + y,
        }
    )
    submission = _DictWithNamespaceSnapshot(
        namespace_snapshot={
            "my_function": lambda x, y: x + y,
        }
    )
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "yes",
        "category": "table_test",
        "reason": "All test cases pass.",
    }


def test_stream_output_validator():
    validator = StreamOutputValidator()
    reference = _DictWithStreamOutput(stream_output="Hello, world!")
    submission = _DictWithStreamOutput(stream_output="Hello, world!")
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "yes",
        "category": "stream",
        "reason": "Stream output is correct.",
    }

    submission = _DictWithStreamOutput(stream_output="Goodbye, world!")
    result = validator.validate(reference, submission)
    assert result["correct"] == "no"


def test_input_output_checker():
    validator = TableTestValidator(
        "my_function",
        [({0, 2},), ({3, 4},)],
        input_checker=lambda x, y: Match(match=len(y[0]) == 3, reason=""),
        output_checker=lambda x, y: Match(match=y is None, reason=""),
    )

    def foo(x):
        x.add(1)

    submission = _DictWithNamespaceSnapshot(namespace_snapshot={"my_function": foo})
    result = validator.validate(submission, submission)
    assert result == {
        "correct": "yes",
        "category": "table_test",
        "reason": "All test cases pass.",
    }

    validator.test_cases.append(({1, 3},))
    result = validator.validate(submission, submission)
    assert result["correct"] == "no"


def test_code_to_test_case():
    parameter = "```\n_test_case = [1, 2, 3]\n```"
    result = TableTestValidator.code_to_test_case(parameter)
    assert result == [1, 2, 3]

    parameter = "`pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})`"
    result = TableTestValidator.code_to_test_case(parameter)
    import pandas as pd

    assert isinstance(result, pd.DataFrame)
    assert result.equals(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}))

    parameter = "`'hello'`"
    result = TableTestValidator.code_to_test_case(parameter)
    assert result == "hello"

    parameter = "[1, 2, 3]"
    result = TableTestValidator.code_to_test_case(parameter)
    assert result == "[1, 2, 3]"

    parameter = "```\ndef my_function(x):\n    return x + 1\n```"
    with pytest.raises(ValueError):
        TableTestValidator.code_to_test_case(parameter)

    parameter = "```\ndef _generate():\n    return [1, 2, 3]\n```"
    result = TableTestValidator.code_to_test_case(parameter)
    assert result == [1, 2, 3]

    result = TableTestValidator.code_to_test_case(
        [
            "```\ndef _generate():\n    return [1, 2, 3]\n```",
            "`pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})`",
            "`'hello'`",
        ],
        assume_list_as_tuple=True,
    )
    assert isinstance(result, tuple)
    assert result[0] == [1, 2, 3]
    assert isinstance(result[1], pd.DataFrame)

    validator = TableTestValidator(
        "my_function",
        [
            "```\ndef _generate():\n    return np.random.randint(0, 10, size=100), \n```",
            "//",
            "//",
        ],
        lambda a: ((a >= 0) & (a < 10)).all(),
    )
    v1_0 = validator.test_cases[0][0]
    v1_1 = validator.test_cases[1][0]
    assert not (v1_0 == v1_1).all()
    validator = TableTestValidator(
        "my_function",
        [
            "```\ndef _generate():\n    return np.random.randint(0, 10, size=100), \n```",
        ],
    )
    v2_0 = validator.test_cases[0][0]
    assert (v1_0 == v2_0).all()

    with pytest.raises(ValueError, match=r"^Invalid test case"):
        TableTestValidator("my_function", [(0, 0), (3, 4)], input_validator=lambda x, _: x > 0)

    def foo(x, y):
        assert x + 1 >= y

    TableTestValidator("my_function", [(0, 0), (3, 4)], input_validator=foo)


def test_validator_loose():
    config = Validator.augment_config({}, "comparison")
    validator = Validator.load("and", config)

    reference = {
        "error": None,
        "execute_result": 123,
        "namespace_diff": {},
        "namespace_snapshot": {},
        "source_code": "",
        "stream_output": "",
    }
    submission = {
        "error": {"ename": "SyntaxError", "evalue": "", "traceback": ""},
        "execute_result": None,
        "namespace_diff": {"foo": "added"},
        "namespace_snapshot": {"foo": 123},
        "source_code": "123 observations in total.",
        "stream_output": "Hello, world!",
    }
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "no",
        "category": "and",
        "reason": [
            {"correct": "no", "category": "crash", "reason": "Submission crashes."},
            {
                "correct": "yes",
                "category": "namespace_intact",
                "reason": "Namespace is intact.",
            },
            {
                "correct": "partial",
                "category": "result",
                "reason": "Output is directly shown in the code: 123",
            },
        ],
    }

    submission["namespace_diff"] = {"foo": "updated"}

    result = validator.validate(reference, submission)
    assert result == {
        "correct": "no",
        "category": "and",
        "reason": [
            {"correct": "no", "category": "crash", "reason": "Submission crashes."},
            {
                "correct": "no",
                "category": "namespace_intact",
                "reason": "Unexpected variable updated: foo",
            },
            {
                "correct": "partial",
                "category": "result",
                "reason": "Output is directly shown in the code: 123",
            },
        ],
    }

    submission["namespace_diff"] = {}
    validator = Validator.load("result", {})
    result = validator.validate(reference, submission)
    assert result == {
        "correct": "partial",
        "category": "result",
        "reason": "Output is directly shown in the code: 123",
    }
