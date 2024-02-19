import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from .match import ExactMatcher


def test_exact_matcher_equal():
    one = "hello"
    other = "hello"
    result = ExactMatcher()(one, other)
    assert result == {"match": True, "reason": ""}


def test_exact_matcher_not_equal():
    one = "hello"
    other = "world"
    result = ExactMatcher()(one, other)
    assert result == {"match": False, "reason": "Expect hello, got world"}


def test_type_match():
    one = "hello"
    other = "world"
    result = ExactMatcher(type_only=True)(one, other)
    assert result == {"match": True, "reason": ""}

    class Foo(str):
        pass

    other = Foo("hello")
    result = ExactMatcher(type_only=True)(one, other)
    assert result["match"] == False
    assert result["reason"].startswith("Type mismatch:")

    result = ExactMatcher()(one, other)
    assert result == {"match": True, "reason": ""}


def test_boolean_matcher():
    one = True
    other = False
    result = ExactMatcher()(one, other)
    assert result["match"] == False

    other = np.bool_(True)
    result = ExactMatcher()(one, other)
    assert result == {"match": True, "reason": ""}


def test_number_matcher_equal():
    one = 1.0
    other = 1.0
    result = ExactMatcher()(one, other)
    assert result == {"match": True, "reason": ""}


def test_number_matcher_not_equal():
    one = 1.0
    other = 2.0
    result = ExactMatcher()(one, other)
    assert result == {"match": False, "reason": "Wrong value: 1.0 vs. 2.0"}


def test_number_matcher_tolerance():
    one = 1e-32
    other = 1e-33
    result = ExactMatcher()(one, other)
    assert result == {"match": True, "reason": ""}
    result = ExactMatcher(atol=0)(one, other)
    assert result == {"match": False, "reason": "Wrong value: 1e-32 vs. 1e-33"}
    other = 1.000001e-32
    result = ExactMatcher(atol=0)(one, other)
    assert result == {"match": True, "reason": ""}


def test_number_matcher_wrong_type():
    one = 1.0
    other = "1.0"
    result = ExactMatcher()(one, other)
    assert result == {"match": False, "reason": "Wrong type: <class 'float'>, <class 'str'>"}


def test_numpy_array_matcher_equal():
    one = np.array([1, 2, 3])
    other = np.array([1, 2, 3])
    result = ExactMatcher()(one, other)
    assert result == {"match": True, "reason": ""}

    result = ExactMatcher()(one, other.astype(np.float32))
    assert result == {"match": True, "reason": ""}

    result = ExactMatcher(strict_type=True)(one, other.astype(np.float32))
    assert result["match"] == False

    one = np.array([-np.inf, np.inf, np.nan, 0.])
    other = np.array([-np.inf, np.inf, np.nan, 0.])
    result = ExactMatcher()(one, other)
    assert result == {"match": True, "reason": ""}


def test_numpy_array_matcher_not_equal():
    one = np.array([1, 2, 3])
    other = np.array([1, 2, 4])
    result = ExactMatcher()(one, other)
    assert result == {"match": False, "reason": "Numpy arrays are not a perfect match: 67%"}


def test_numpy_array_matcher_wrong_type():
    one = np.array([1, 2, 3])
    other = [1, 2, 3]
    result = ExactMatcher()(one, other)
    assert result == {"match": False, "reason": "Wrong type: <class 'numpy.ndarray'>, <class 'list'>"}


def test_csr_matrix_matcher():
    # Create two identical CSR matrices
    data = np.array([1, 2, 3, 4, 5])
    indices = np.array([0, 2, 2, 0, 1])
    indptr = np.array([0, 2, 3, 5])
    ref = csr_matrix((data, indices, indptr))
    sub = csr_matrix((data, indices, indptr), copy=True)

    matcher = ExactMatcher(rtol=1e-05, atol=1e-08)
    result = matcher.match(ref, sub)
    assert result["match"] == True
    assert result["reason"] == ""

    # Change one element in the 'sub' matrix
    sub[0, 0] = 10
    result = matcher.match(ref, sub)
    assert result["match"] == False
    assert "wrong data" in result["reason"]

    # Change the shape of the 'sub' matrix
    sub = csr_matrix((data, indices, indptr), shape=(3, 6))
    result = matcher.match(ref, sub)
    assert result["match"] == False
    assert "wrong shape" in result["reason"]

    # Test with non-CSR matrix
    sub = np.array([1, 2, 3])
    result = matcher.match(ref, sub)
    assert result["match"] == False
    assert "Wrong type" in result["reason"]


def test_pandas_object_matcher_dataframe_equal():
    one = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    other = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    result = ExactMatcher()(one, other)
    assert result == {"match": True, "reason": ""}

    one = pd.DataFrame({"Name": ["Juda", "Pri"], "Email": [{"a@a.com", "b@b.com"}, ""]})
    other = pd.DataFrame({"Name": ["Juda", "Pri"], "Email": [{"b@b.com", "a@a.com"}, ""]})
    result = ExactMatcher()(one, other)
    assert result == {"match": True, "reason": ""}


def test_pandas_object_matcher_dataframe_not_equal():
    one = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    other = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 7]})
    result = ExactMatcher()(one, other)
    assert result["match"] == False
    assert "DataFrame not equal" in result["reason"]


def test_pandas_object_matcher_series_equal():
    one = pd.Series([1, 2, 3])
    other = pd.Series([1, 2, 3])
    result = ExactMatcher()(one, other)
    assert result == {"match": True, "reason": ""}


def test_pandas_object_matcher_series_not_equal():
    one = pd.Series([1, 2, 3])
    other = pd.Series([1, 2, 4])
    result = ExactMatcher()(one, other)
    assert result["match"] == False
    assert "Series not equal" in result["reason"]


def test_pandas_object_matcher_index_equal():
    one = pd.Index([1, 2, 3])
    other = pd.Index([1, 2, 3])
    result = ExactMatcher()(one, other)
    assert result == {"match": True, "reason": ""}


def test_pandas_object_matcher_index_not_equal():
    one = pd.Index([1, 2, 3])
    other = pd.Index([1, 2, 4])
    result = ExactMatcher()(one, other)
    assert result["match"] == False
    assert "Index not equal" in result["reason"]


def test_pandas_object_matcher_wrong_type():
    one = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    other = pd.Series([1, 2, 3])
    result = ExactMatcher()(one, other)
    assert result == {
        "match": False,
        "reason": "Mismatched type: <class 'pandas.core.frame.DataFrame'>, <class 'pandas.core.series.Series'>",
    }


def test_pandas_object_ignore():
    one = pd.Series([1, 2, 3], index=pd.Index([1, 2, 3], name="a"), name="b")
    other = pd.Series([1, 2, 3], index=pd.Index([1, 2, 3], name="c"), name="b")
    result = ExactMatcher()(one, other)
    assert not result["match"]
    result = ExactMatcher(ignore_index=True)(one, other)
    assert result == {"match": True, "reason": ""}
    result = ExactMatcher(ignore_names=True)(one, other)
    assert result == {"match": True, "reason": ""}

    other.iloc[1:3] = [3, 2]
    result = ExactMatcher(ignore_index=True)(one, other)
    assert not result["match"]

    result = ExactMatcher(ignore_order=True)(one, other)
    assert result == {"match": True, "reason": ""}

    one = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, index=pd.Index([1, 2, 3], name="c"))
    other = pd.DataFrame({"a": [1, 2, 3], "c": [4, 5, 6]}, index=pd.Index([1, 2, 3], name="d"))
    result = ExactMatcher()(one, other)
    assert not result["match"]
    result = ExactMatcher(ignore_names=True)(one, other)
    assert result == {"match": True, "reason": ""}

    one = pd.DataFrame({"a": [1., 2., 3.], "b": [4, 5, 6]})
    other = pd.DataFrame({"a": [1, 2, 3], "b": ["4", "5", "6"]})
    result = ExactMatcher()(one, other)
    assert not result["match"]
    result = ExactMatcher(ignore_dtypes=True)(one, other)
    assert result == {"match": True, "reason": ""}


def test_partial_match():
    one = pd.Series([1, 2, 3], index=pd.Index([4, 5, 6], name="a"), name="b")
    other = pd.Series([7, 8, 9], index=pd.Index([1, 2, 3], name="c"), name="d")
    result = ExactMatcher(ignore_index=True, match_partial=True)(one, other)
    assert not result["match"]
    result = ExactMatcher(ignore_index=True, ignore_names=True, match_partial=True)(one, other)
    assert result == {"match": True, "reason": "Partial match on index: Index([1, 2, 3], dtype='int64', name='a')"}

    other = pd.DataFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6],
    })
    result = ExactMatcher(ignore_index=True, ignore_names=True, match_partial=True)(one, other)
    assert result == {"match": True, "reason": "Partial match on column: a"}

    one = [4, 5, 6]
    result = ExactMatcher(ignore_index=True, ignore_names=True, match_partial=True)(one, other)
    assert result == {"match": True, "reason": "Partial match on column: b"}

    one = pd.DataFrame({"a": [2, 1, 3]})
    result = ExactMatcher(ignore_index=True, ignore_names=True, ignore_order=True, match_partial=True)(one, other)
    assert result == {"match": True, "reason": "Partial match on subset of columns: ['a']"}


def test_metric_tolerance():
    one = 0.8
    other = 0.7
    result = ExactMatcher(metrictol=0.9)(one, other)
    assert result == {"match": False, "reason": "Metric too low (less than 90.0%): 0.7 vs. 0.8"}

    result = ExactMatcher(metrictol=0.85)(one, other)
    assert result == {"match": True, "reason": "Metric satisfies the condition: 0.7 vs. 0.8"}

    one = {
        "accuracy": 0.8,
        "precision": 0.9,
    }
    other = {
        "a": 0.73,
        "p": 0.82
    }
    result = ExactMatcher(metrictol=0.9, ignore_index=True)(one, other)
    assert result == {"match": True, "reason": ""}


def test_value_only():
    one = pd.DataFrame({"a": [1]})
    other = [1]
    assert not ExactMatcher()(one, other)["match"]
    assert ExactMatcher(value_only=True)(one, other)["match"]

    other = np.array([1.])
    assert not ExactMatcher()(one, other)["match"]
    assert ExactMatcher(value_only=True)(one, other)["match"]


def test_container_matcher():
    matcher = ExactMatcher(ignore_order=True)

    # Test list matching
    one = [1, 2, 3]
    other = [3, 2, 1]
    result = matcher(one, other)
    assert result["match"] is True

    one = [1, 2, 3]
    other = [1, 2]
    result = matcher(one, other)
    assert result["match"] is False
    assert "Length mismatch" in result["reason"]

    one = [1, 2, 3]
    other = [1, 2, "3"]
    result = matcher(one, other)
    assert result["match"] is False
    assert "Element 2 not equal" in result["reason"]

    # Test tuple matching
    one = (1, 2, 3)
    other = (3, 2, 1)
    result = matcher(one, other)
    assert result["match"] is True

    one = (1, 2, 3)
    other = (1, 2)
    result = matcher(one, other)
    assert result["match"] is False
    assert "Length mismatch" in result["reason"]

    one = (1, 2, 3)
    other = (1, 2, "3")
    result = matcher(one, other)
    assert result["match"] is False
    assert "Element 2 not equal" in result["reason"]

    # Test dict matching
    one = {"a": 1, "b": 2, "c": 3}
    other = {"c": 3, "b": 2, "a": 1}
    result = matcher(one, other)
    assert result["match"] is True

    one = {"a": 1, "b": 2, "c": 3}
    other = {"a": 1, "b": 2}
    result = matcher(one, other)
    assert result["match"] is False
    assert "Keys mismatch" in result["reason"]

    one = {"a": 1, "b": 2, "c": 3}
    other = {"a": 1, "b": 2, "c": "3"}
    result = matcher(one, other)
    assert result["match"] is False
    assert "Element c not equal" in result["reason"]

    # Test set matching
    one = {1, 2, 3}
    other = {3, 2, 1}
    result = matcher(one, other)
    assert result["match"] is True

    one = {1, 2, 3}
    other = {1, 2}
    result = matcher(one, other)
    assert result["match"] is False
    assert "Set not equal" in result["reason"]
