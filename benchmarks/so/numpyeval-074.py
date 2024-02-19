'''
### Prompt ###

import numpy as np

def find_index_within_range(arr, low, high):
    # find index of the elements within range [low, high]
    # Return the final array of indices.

### Solution ###

    return np.where(np.logical_and(arr >= low, arr <= high))[0]

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3, 6), np.array([2, 3, 4, 5]))
    assert np.array_equal(candidate(np.array([1, 2, 3, 4, 5, 1, 7, 8, 9, 10]), 3, 6), np.array([2, 3, 4]))
    assert np.array_equal(candidate(np.array([1, 2, 3, 4, 5, 1, 7, 11, 9, 10]), 3, 6), np.array([2, 3, 4]))
    assert np.array_equal(candidate(np.array([1, 2, 3, 4, 5, 1, 1, 11, 9, 10]), 3, 6), np.array([2, 3, 4]))
    assert np.array_equal(candidate(np.array([1, 2, 3, 4, 5, 1, 121, 11, 9, 10]), 3, 6), np.array([2, 3, 4]))
    assert np.array_equal(candidate(np.array([1, 2, 3, 4, 5, 1, 121, 11, 19, 10]), 3, 6), np.array([2, 3, 4]))
    assert np.array_equal(candidate(np.array([1, 2, 13, 4, 5, 1, 121, 11, 19, 10]), 3, 6), np.array([3, 4]))
    assert np.array_equal(candidate(np.array([1, 2, 13, 4, 5, 1, 121, 11, 19, 10]), 3, 10), np.array([3, 4, 9]))
    assert np.array_equal(candidate(np.array([1, 2, 13, 4, 5, 1, 121, 11, 100, 10]), 3, 10), np.array([3, 4, 9]))
    assert np.array_equal(candidate(np.array([1, 2, 13, 4, 5, 11, 121, 11, 100, 10]), 3, 10), np.array([3, 4, 9]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def find_index_within_range(arr, low, high):` that takes a numpy array and two numbers (low and high) and returns a numpy array to solve the following problem:
  find index of the elements within range [low, high]

validator:
  table_test:
    function_name: find_index_within_range
    test_cases:
    - ["`np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])`", 3, 6]
    - ["`np.array([1, 2, 3, 4, 5, 1, 7, 8, 9, 10])`", 3, 6]
    - ["`np.array([1, 2, 3, 4, 5, 1, 7, 11, 9, 10])`", 3, 6]
    - ["`np.array([1, 2, 3, 4, 5, 1, 1, 11, 9, 10])`", 3, 6]
    - ["`np.array([1, 2, 3, 4, 5, 1, 121, 11, 9, 10])`", 3, 6]
    - ["`np.array([1, 2, 3, 4, 5, 1, 121, 11, 19, 10])`", 3, 6]
    - ["`np.array([1, 2, 13, 4, 5, 1, 121, 11, 19, 10])`", 3, 6]
    - ["`np.array([1, 2, 13, 4, 5, 1, 121, 11, 19, 10])`", 3, 10]
    - ["`np.array([1, 2, 13, 4, 5, 1, 121, 11, 100, 10])`", 3, 10]
    - ["`np.array([1, 2, 13, 4, 5, 11, 121, 11, 100, 10])`", 3, 10]
"""

def find_index_within_range(arr, low, high):
    return np.where(np.logical_and(arr >= low, arr <= high))[0]
