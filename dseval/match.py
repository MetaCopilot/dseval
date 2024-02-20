import logging
from typing import Any, TypedDict

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix

_logger = logging.getLogger(__name__)


class Match(TypedDict):
    match: bool
    reason: str


class MatchConfig(TypedDict):
    ignore_order: bool  # Ignore order of elements in container / dataframe
    ignore_index: bool  # Drop index when making comparisons (or drop keys in case of a container)
    ignore_names: bool  # Ignore the difference in column names, index names, etc.
    ignore_dtypes: bool  # Ignore the difference in dtypes
    match_partial: bool  # Check if the information is presented in the submission, but ignore the rest
    type_only: bool  # Only check the type of the object
    value_only: (
        bool  # Ignore container type (e.g., list vs. tuple vs. numpy array vs. series; single element array vs. scalar)
    )
    strict_type: bool  # Type must be strictly the same (for numpy arrays)
    atol: float  # Absolute tolerance for numerical comparisons
    rtol: float  # Relative tolerance for numerical comparisons
    metrictol: (
        float | None
    )  # Tolerance for metrics. If set to a number, the submission must be no less than the reference value multiplied by the tolerance.


class ExactMatcher:
    def __init__(
        self,
        ignore_order: bool = False,
        ignore_index: bool = False,
        ignore_names: bool = False,
        ignore_dtypes: bool = False,
        match_partial: bool = False,
        value_only: bool = False,
        type_only: bool = False,
        strict_type: bool = False,
        atol: float = 1e-8,
        rtol: float = 1e-5,
        metrictol: float | None = None,
    ) -> None:
        self.config: MatchConfig = {
            "ignore_order": ignore_order,
            "ignore_index": ignore_index,
            "ignore_names": ignore_names,
            "ignore_dtypes": ignore_dtypes,
            "match_partial": match_partial,
            "value_only": value_only,
            "type_only": type_only,
            "strict_type": strict_type,
            "atol": atol,
            "rtol": rtol,
            "metrictol": metrictol,
        }

    @classmethod
    def supports(cls, ref, sub) -> bool:
        return True

    @staticmethod
    def _strip_container(obj):
        if isinstance(obj, (list, tuple, set)):
            obj = [ExactMatcher._strip_container(x) for x in obj]
        elif isinstance(obj, np.ndarray):
            obj = ExactMatcher._strip_container(obj.tolist())
        elif isinstance(obj, pd.Series):
            obj = ExactMatcher._strip_container(obj.tolist())
        elif isinstance(obj, pd.DataFrame):
            obj = ExactMatcher._strip_container(obj.to_numpy().tolist())
        elif isinstance(obj, pd.Index):
            obj = ExactMatcher._strip_container(obj.tolist())
        if isinstance(obj, list) and len(obj) == 1:
            obj = obj[0]
        return obj

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(" + ", ".join([f"{k}={v}" for k, v in self.config.items()]) + ")"

    def __call__(self, ref: Any, sub: Any) -> Match:
        if self.config["type_only"]:
            return self.match(ref, sub)
        if self.config["value_only"]:
            ref, sub = ExactMatcher._strip_container(ref), ExactMatcher._strip_container(sub)
        match = self.match(ref, sub)
        if not match["match"] and self.config["match_partial"]:
            match_partial = self.match_partial(ref, sub)
            if match_partial["match"]:
                return match_partial
        return match

    def match_partial(self, ref, sub) -> Match:
        # We assume that the useful content in the answer are in values (not index).
        if isinstance(sub, pd.DataFrame):
            if isinstance(ref, pd.DataFrame):
                # Both dataframes. Columns must be a subset of the reference dataframe.
                # First reset index to make sure index is also treated as a column.
                try:
                    sub = sub.reset_index()
                except Exception:
                    _logger.exception("Failed to reset index.")
                if sub.columns.tolist() != ref.columns.tolist() and all(
                    column in sub.columns.tolist() for column in ref.columns.tolist()
                ):
                    sub = sub[ref.columns]
                    match = self.match(ref, sub)
                    if match["match"]:
                        return {
                            "match": True,
                            "reason": f"Partial match on subset of columns: {ref.columns.tolist()}",
                        }
            if isinstance(ref, (pd.Series, list)):
                # Dataframe and series. Answer must be one of the columns or index.
                if isinstance(ref, list):
                    ref = pd.Series(ref)
                for column in sub.columns:
                    match = self.match(ref, sub[column])
                    if match["match"]:
                        return {
                            "match": True,
                            "reason": f"Partial match on column: {column}",
                        }
                match = self.match(ref, pd.Series(sub.index))
                if match["match"]:
                    return {
                        "match": True,
                        "reason": f"Partial match on index: {sub.index}",
                    }

        if isinstance(sub, pd.Series):
            # Both series.
            if isinstance(ref, (pd.Series, list)):
                if isinstance(ref, list):
                    ref = pd.Series(ref)
                # Answer must be index.
                match = self.match(ref, pd.Series(sub.index))
                if match["match"]:
                    return {
                        "match": True,
                        "reason": f"Partial match on index: {sub.index}",
                    }
                # Or value.
                match = self.match(ref, pd.Series(sub.values))
                if match["match"]:
                    return {
                        "match": True,
                        "reason": f"Partial match on values: {sub.values}",
                    }
            # Series and dataframe. Answer must be to frame.
            if isinstance(ref, pd.DataFrame):
                match = self.match(ref, sub.to_frame())
                if match["match"]:
                    return {
                        "match": True,
                        "reason": f"Partial match on `to_frame`: {sub.to_frame()}",
                    }

        return {"match": False, "reason": "Partial match failed"}

    def match(self, ref, sub) -> Match:
        if self.config["type_only"]:
            if type(ref) is type(sub):
                return {"match": True, "reason": ""}
            return {
                "match": False,
                "reason": f"Type mismatch: {type(ref)} vs. {type(sub)}",
            }
        for subcls in self.__class__.__subclasses__():
            if subcls.supports(ref, sub):
                return subcls(**self.config).match(ref, sub)
        try:
            success = bool(ref == sub)
            return {
                "match": success,
                "reason": "" if success else f"Expect {ref}, got {sub}",
            }
        except:
            return {
                "match": False,
                "reason": "Couldn't match reference and submission.",
            }


class BooleanMatcher(ExactMatcher):
    @classmethod
    def supports(cls, ref, sub):
        return isinstance(ref, (bool, np.bool_)) or isinstance(sub, (bool, np.bool_))

    def match(self, ref, sub) -> Match:
        if not isinstance(sub, (bool, np.bool_)) or not isinstance(ref, (bool, np.bool_)):
            return {"match": False, "reason": f"Wrong type: {type(ref)}, {type(sub)}"}
        if ref == sub:
            return {"match": True, "reason": ""}
        return {"match": False, "reason": f"Wrong value: {ref} vs. {sub}"}


class NumberMatcher(ExactMatcher):
    @classmethod
    def supports(cls, ref, sub):
        return isinstance(ref, (float, int, np.number)) or isinstance(sub, (float, int, np.number))

    def match(self, ref, sub) -> Match:
        if not isinstance(sub, (float, int, np.number)) or not isinstance(ref, (float, int, np.number)):
            return {"match": False, "reason": f"Wrong type: {type(ref)}, {type(sub)}"}
        if self.config["metrictol"] is not None:
            if sub < ref * self.config["metrictol"]:
                return {
                    "match": False,
                    "reason": f"Metric too low (less than {self.config['metrictol'] * 100:.1f}%): {sub} vs. {ref}",
                }
            else:
                return {
                    "match": True,
                    "reason": f"Metric satisfies the condition: {sub} vs. {ref}",
                }
        if np.isclose(sub, ref, rtol=self.config["rtol"], atol=self.config["atol"]).item():
            return {"match": True, "reason": ""}
        return {"match": False, "reason": f"Wrong value: {ref} vs. {sub}"}


class NumpyArrayMatcher(ExactMatcher):
    @classmethod
    def supports(cls, ref, sub):
        return isinstance(ref, np.ndarray) or isinstance(sub, np.ndarray)

    def match(self, ref, sub) -> Match:
        if not isinstance(sub, np.ndarray) or not isinstance(ref, np.ndarray):
            return {"match": False, "reason": f"Wrong type: {type(ref)}, {type(sub)}"}
        if self.config["strict_type"] and ref.dtype != sub.dtype:
            return {
                "match": False,
                "reason": f"Wrong dtype: {ref.dtype}, {sub.dtype}",
            }
        if ref.shape != sub.shape:
            return {"match": False, "reason": f"Wrong shape: {ref.shape}, {sub.shape}"}
        if np.issubdtype(ref.dtype, np.floating) and np.issubdtype(sub.dtype, np.floating):
            if not np.allclose(np.isnan(ref), np.isnan(sub)):
                return {
                    "match": False,
                    "reason": f"Wrong NaN: {np.isnan(ref)}, {np.isnan(sub)}",
                }
            if not np.allclose(np.isinf(ref), np.isinf(sub)):
                return {
                    "match": False,
                    "reason": f"Wrong Inf: {np.isinf(ref)}, {np.isinf(sub)}",
                }
            try:
                if np.allclose(
                    sub[~np.isnan(sub)],
                    ref[~np.isnan(ref)],
                    rtol=self.config["rtol"],
                    atol=self.config["atol"],
                ):
                    return {"match": True, "reason": ""}
                return {
                    "match": False,
                    "reason": f"Numpy arrays are not a perfect match: {np.isclose(sub, ref).sum() / ref.size * 100:.0f}%",
                }
            except:
                return {
                    "match": False,
                    "reason": f"Numpy arrays are not equal:\nExpected: {ref}\nActual: {sub}",
                }
        else:
            try:
                if np.array_equal(ref, sub):
                    return {"match": True, "reason": ""}
                return {
                    "match": False,
                    "reason": f"Numpy arrays are not a perfect match: {(ref == sub).sum() / ref.size * 100:.0f}%",
                }
            except:
                return {
                    "match": False,
                    "reason": f"Numpy arrays are not equal:\nExpected: {ref}\nActual: {sub}",
                }


class CsrMatrixMatcher(ExactMatcher):
    @classmethod
    def supports(cls, ref, sub):
        return isinstance(ref, csr_matrix) or isinstance(sub, csr_matrix)

    def match(self, ref, sub) -> Match:
        if not isinstance(sub, csr_matrix) or not isinstance(ref, csr_matrix):
            return {"match": False, "reason": f"Wrong type: {type(ref)}, {type(sub)}"}
        if len(ref.indices) != len(sub.indices):
            return {
                "match": False,
                "reason": f"CSR matrix unequal: wrong number of nonzero elements: {len(ref.indices)}, {len(sub.indices)}",
            }
        if ref.shape != sub.shape:
            return {
                "match": False,
                "reason": f"CSR matrix unequal: wrong shape: {ref.shape}, {sub.shape}",
            }
        if not np.allclose(ref.data, sub.data, rtol=self.config["rtol"], atol=self.config["atol"]):
            return {
                "match": False,
                "reason": f"CSR matrix unequal: wrong data: {ref.data}, {sub.data}",
            }
        if not np.array_equal(ref.indices, sub.indices):
            return {
                "match": False,
                "reason": f"CSR matrix unequal: wrong indices: {ref.indices}, {sub.indices}",
            }
        if not np.array_equal(ref.indptr, sub.indptr):
            return {
                "match": False,
                "reason": f"CSR matrix unequal: wrong indptr: {ref.indptr}, {sub.indptr}",
            }
        return {"match": True, "reason": ""}


class PandasObjectMatcher(ExactMatcher):
    @classmethod
    def supports(cls, ref, sub):
        return isinstance(ref, (pd.DataFrame, pd.Series, pd.Index)) or isinstance(
            sub, (pd.DataFrame, pd.Series, pd.Index)
        )

    def match(self, ref, sub) -> Match:
        if isinstance(ref, pd.DataFrame) and isinstance(sub, pd.DataFrame):
            type_name, testing_func = "DataFrame", pd.testing.assert_frame_equal
        elif isinstance(ref, pd.Series) and isinstance(sub, pd.Series):
            type_name, testing_func = "Series", pd.testing.assert_series_equal
        elif isinstance(ref, pd.Index) and isinstance(sub, pd.Index):
            type_name, testing_func = "Index", pd.testing.assert_index_equal
        else:
            return {
                "match": False,
                "reason": f"Mismatched type: {type(ref)}, {type(sub)}",
            }
        if self.config["ignore_names"]:
            if isinstance(ref, pd.DataFrame) and isinstance(sub, pd.DataFrame):
                columns = ref.columns.tolist()  # Keep columns only from expected DataFrame
                if set(columns) == set(sub.columns.tolist()):
                    sub = sub[columns]
                try:
                    if sub.index.shape == ref.index.shape:
                        sub.rename_axis(ref.index.names, inplace=True)
                except Exception:
                    _logger.exception("Failed to rename index.")
                try:
                    if len(sub.columns) == len(ref.columns):
                        sub.rename(
                            columns=dict(zip(sub.columns.tolist(), ref.columns.tolist())),
                            inplace=True,
                        )
                except Exception:
                    _logger.exception("Failed to rename columns.")
            if isinstance(ref, pd.Series) and isinstance(sub, pd.Series):
                try:
                    if sub.index.shape == ref.index.shape:
                        sub.rename_axis(ref.index.names, inplace=True)
                except Exception:
                    _logger.exception("Failed to rename index.")
                try:
                    sub.rename(ref.name, inplace=True)
                except Exception:
                    _logger.exception("Failed to rename name of series.")
        if self.config["ignore_order"] or self.config["ignore_index"]:
            if isinstance(ref, pd.DataFrame) and isinstance(sub, pd.DataFrame):
                columns = ref.columns.tolist()  # Keep columns only from expected DataFrame
                if not set(columns) == set(sub.columns.tolist()):
                    return {
                        "match": False,
                        "reason": f"Columns mismatch: {columns} vs. {sub.columns}",
                    }
                ref = ref.reset_index(drop=True)
                sub = sub[columns].reset_index(drop=True)
                if self.config["ignore_order"]:
                    ref = ref.sort_values(by=columns).reset_index(drop=True)
                    sub = sub.sort_values(by=columns).reset_index(drop=True)
            if isinstance(ref, pd.Series) and isinstance(sub, pd.Series):
                ref = ref.reset_index(drop=True)
                sub = sub.reset_index(drop=True)
                if self.config["ignore_order"]:
                    try:
                        ref = ref.sort_values().reset_index(drop=True)
                        sub = sub.sort_values().reset_index(drop=True)
                    except Exception:
                        _logger.exception("Failed to sort series.")
        if self.config["ignore_dtypes"]:
            try:
                if isinstance(ref, pd.DataFrame) and isinstance(sub, pd.DataFrame):
                    sub = sub.astype(ref.dtypes.to_dict())
                if isinstance(ref, pd.Series) and isinstance(sub, pd.Series):
                    sub = sub.astype(ref.dtype)
            except:
                _logger.exception("Failed to cast dtypes.")
        try:
            testing_func(ref, sub)  # type: ignore
            return {"match": True, "reason": ""}
        except AssertionError as e:
            return self._diff(e.args[0], ref, sub, type_name)
        except:
            if not ref.equals(sub):  # type: ignore
                return self._diff("", ref, sub, type_name)
            return {"match": True, "reason": ""}

    def _diff(self, msg, ref, sub, type_name) -> Match:
        to_string_kwargs = dict(max_cols=10, max_colwidth=15, max_rows=10)
        try:
            match_summary = ref.compare(sub).to_string(**to_string_kwargs)  # type: ignore
            return {
                "match": False,
                "reason": f"{type_name} not equal. Assertion error: {msg}\nDiff:\n{match_summary}",
            }
        except:
            try:
                expected = ref.to_string(**to_string_kwargs)  # type: ignore
                actual = sub.to_string(**to_string_kwargs)  # type: ignore
                return {
                    "match": False,
                    "reason": f"{type_name} not equal:\nAssertion error: {msg}\nExpected:\n{expected}\n\nActual:\n{actual}",
                }
            except:
                try:
                    expected = str(ref)
                    actual = str(sub)
                    return {
                        "match": False,
                        "reason": f"{type_name} not equal:\nAssertion error: {msg}\nExpected:\n{expected}\n\nActual:\n{actual}",
                    }
                except:
                    return {
                        "match": False,
                        "reason": f"{type_name} not equal and diff failed. Assertion error: {msg}",
                    }


class ContainerMatcher(ExactMatcher):
    @classmethod
    def supports(cls, ref, sub):
        return isinstance(ref, (list, tuple, dict, set)) or isinstance(sub, (list, tuple, dict, set))

    @staticmethod
    def _general_type_sorted(sequence):
        return sorted(sequence, key=lambda x: (str(type(x)), x))

    def match(self, ref, sub) -> Match:
        if isinstance(ref, (list, tuple)) and isinstance(sub, (list, tuple)):
            if len(ref) != len(sub):
                return {
                    "match": False,
                    "reason": f"Length mismatch: {len(ref)} vs. {len(sub)}",
                }
            if self.config["ignore_order"]:
                ref = ContainerMatcher._general_type_sorted(ref)
                sub = ContainerMatcher._general_type_sorted(sub)
            for i, (a, b) in enumerate(zip(list(ref), list(sub))):
                match = ExactMatcher(**self.config).match(a, b)
                if not match["match"]:
                    return {
                        "match": False,
                        "reason": f"Element {i} not equal: {match['reason']}",
                    }
        elif isinstance(ref, dict) and isinstance(sub, dict):
            if self.config["ignore_index"]:
                if len(ref) != len(sub):
                    return {
                        "match": False,
                        "reason": f"Length mismatch: {len(ref)} vs. {len(sub)}",
                    }
                for (ref_key, ref_val), (sub_key, sub_val) in zip(ref.items(), sub.items()):
                    match = ExactMatcher(**self.config).match(ref_val, sub_val)
                    if not match["match"]:
                        return {
                            "match": False,
                            "reason": f"Element {ref_key} -- {sub_key} not equal: {match['reason']}",
                        }
            else:
                if sorted(ref.keys()) != sorted(sub.keys()):
                    return {
                        "match": False,
                        "reason": f"Keys mismatch: {ref.keys()} vs. {sub.keys()}",
                    }
                for key in ref:
                    match = ExactMatcher(**self.config).match(ref[key], sub[key])
                    if not match["match"]:
                        return {
                            "match": False,
                            "reason": f"Element {key} not equal: {match['reason']}",
                        }
        elif isinstance(ref, set) and isinstance(sub, set):
            if ref != sub:
                return {"match": False, "reason": f"Set not equal: {ref} vs. {sub}"}
        else:
            return {
                "match": False,
                "reason": f"Mismatched type: {type(ref)}, {type(sub)}",
            }
        return {"match": True, "reason": ""}
