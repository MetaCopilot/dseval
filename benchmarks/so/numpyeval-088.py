'''
### Prompt ###

import numpy as np

def convert_nan_to_zero(arr):
    # convert nan value to zero
    # Return the changed array

### Solution ###

    arr[np.isnan(arr)] = 0
    return arr

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([1, 2, np.nan, 4, np.nan])), np.array([1, 2, 0, 4, 0]))
    assert np.array_equal(candidate(np.array([1, 2, 3, 4, np.nan])), np.array([1, 2, 3, 4, 0]))
    assert np.array_equal(candidate(np.array([1, 2, 5, 4, np.nan])), np.array([1, 2, 5, 4, 0]))
    assert np.array_equal(candidate(np.array([1, 2, np.nan, np.nan, np.nan])), np.array([1, 2, 0, 0, 0]))
    assert np.array_equal(candidate(np.array([1, 2, 5, 4, np.nan])), np.array([1, 2, 5, 4, 0]))
    assert np.array_equal(candidate(np.array([1, 2, 1, 4, 5])), np.array([1, 2, 1, 4, 5]))
    assert np.array_equal(candidate(np.array([1, 2, 1, np.nan, 5])), np.array([1, 2, 1, 0, 5]))
    assert np.array_equal(candidate(np.array([np.nan, 2, 1, 2, 5])), np.array([0, 2, 1, 2, 5]))
    assert np.array_equal(candidate(np.array([np.nan, 2, np.nan, 2, 5])), np.array([0, 2, 0, 2, 5]))
    assert np.array_equal(candidate(np.array([np.nan, 2, 1, np.nan, 5])), np.array([0, 2, 1, 0, 5]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def convert_nan_to_zero(arr):` that takes a numpy array and returns a numpy array to solve the following problem:
  convert nan value to zero

validator:
  table_test:
    function_name: convert_nan_to_zero
    test_cases:
    - ["`np.array([1, 2, np.nan, 4, np.nan])`"]
    - ["`np.array([1, 2, 3, 4, np.nan])`"]
    - ["`np.array([1, 2, 5, 4, np.nan])`"]
    - ["`np.array([1, 2, np.nan, np.nan, np.nan])`"]
    - ["`np.array([1, 2, 5, 4, np.nan])`"]
    - ["`np.array([1, 2, 1, 4, 5])`"]
    - ["`np.array([1, 2, 1, np.nan, 5])`"]
    - ["`np.array([np.nan, 2, 1, 2, 5])`"]
    - ["`np.array([np.nan, 2, np.nan, 2, 5])`"]
    - ["`np.array([np.nan, 2, 1, np.nan, 5])`"]
"""

def convert_nan_to_zero(arr):
    arr[np.isnan(arr)] = 0
    return arr
