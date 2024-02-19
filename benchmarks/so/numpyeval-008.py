'''
### Prompt ###

import numpy as np

def remove_all_rows_contain_non_numeric_values(arr):
    # How to remove all rows in a numpy.ndarray that contain non-numeric values?
    # Return the final result

### Solution ###

    return arr[~np.isnan(arr).any(axis=1)]

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([[1,2,3], [4,5,np.nan], [7,8,9]])), np.array([[1,2,3], [7,8,9]]))
    assert np.array_equal(candidate(np.array([[1,2,3], [np.nan,5,np.nan], [7,8,9]])), np.array([[1,2,3], [7,8,9]]))
    assert np.array_equal(candidate(np.array([[1,2,3], [np.nan, np.nan, np.nan], [7,8,9]])), np.array([[1,2,3], [7,8,9]]))
    assert np.array_equal(candidate(np.array([[1,2,np.nan], [np.nan, np.nan, np.nan], [7,8,9]])), np.array([[7,8,9]]))
    assert np.array_equal(candidate(np.array([[1,np.nan,np.nan], [np.nan, np.nan, np.nan], [7,8,9]])), np.array([[7,8,9]]))
    assert np.array_equal(candidate(np.array([[np.nan,np.nan,np.nan], [np.nan, np.nan, np.nan], [7,8,9]])), np.array([[7,8,9]]))
    assert np.array_equal(candidate(np.array([[np.nan,np.nan,np.nan], [7,8,9], [np.nan, np.nan, np.nan]])), np.array([[7,8,9]]))
    assert np.array_equal(candidate(np.array([[np.nan,np.nan,np.nan], [7,8,2], [np.nan, np.nan, np.nan]])), np.array([[7,8,2]]))
    assert np.array_equal(candidate(np.array([[np.nan,np.nan,np.nan], [7,2,2], [np.nan, np.nan, np.nan]])), np.array([[7,2,2]]))
    assert np.array_equal(candidate(np.array([[np.nan,np.nan,np.nan], [2,2,2], [np.nan, np.nan, np.nan]])), np.array([[2,2,2]]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def remove_all_rows_contain_non_numeric_values(arr):` that takes a numpy array and returns a numpy array to solve the following problem:
  How to remove all rows in a numpy.ndarray that contain non-numeric values?

validator:
  table_test:
    function_name: remove_all_rows_contain_non_numeric_values
    test_cases:
    - ["`np.array([[1,2,3], [4,5,np.nan], [7,8,9]])`"]
    - ["`np.array([[1,2,3], [np.nan,5,np.nan], [7,8,9]])`"]
    - ["`np.array([[1,2,3], [np.nan, np.nan, np.nan], [7,8,9]])`"]
    - ["`np.array([[1,2,np.nan], [np.nan, np.nan, np.nan], [7,8,9]])`"]
    - ["`np.array([[1,np.nan,np.nan], [np.nan, np.nan, np.nan], [7,8,9]])`"]
    - ["`np.array([[np.nan,np.nan,np.nan], [np.nan, np.nan, np.nan], [7,8,9]])`"]
    - ["`np.array([[np.nan,np.nan,np.nan], [7,8,9], [np.nan, np.nan, np.nan]])`"]
    - ["`np.array([[np.nan,np.nan,np.nan], [7,8,2], [np.nan, np.nan, np.nan]])`"]
    - ["`np.array([[np.nan,np.nan,np.nan], [7,2,2], [np.nan, np.nan, np.nan]])`"]
    - ["`np.array([[np.nan,np.nan,np.nan], [2,2,2], [np.nan, np.nan, np.nan]])`"]
"""

def remove_all_rows_contain_non_numeric_values(arr):
    return arr[~np.isnan(arr).any(axis=1)]
