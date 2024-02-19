'''
### Prompt ###

import numpy as np

def replace_elements_that_greater_than_value(arr, value, new_value):
    # Replace all elements of Python NumPy Array that are greater than `value` with `new_value`
    # Return the array

### Solution ###

    arr[arr > value] = new_value
    return arr

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([[1, 2, 3, 4], [5, 6, 7, 8]]), 5, 0), np.array([[1, 2, 3, 4], [5, 0, 0, 0]]))
    assert np.array_equal(candidate(np.array([[1, 2, 3, 4], [5, 6, 7, 8]]), 5, 1), np.array([[1, 2, 3, 4], [5, 1, 1, 1]]))
    assert np.array_equal(candidate(np.array([[1, 2, 3, 4], [5, 6, 7, 8]]), 6, 1), np.array([[1, 2, 3, 4], [5, 6, 1, 1]]))
    assert np.array_equal(candidate(np.array([[1, 2, 3, 4], [5, 6, 7, 8]]), 7, 1), np.array([[1, 2, 3, 4], [5, 6, 7, 1]]))
    assert np.array_equal(candidate(np.array([[1, 2, 3, 4], [5, 6, 7, 9]]), 7, 1), np.array([[1, 2, 3, 4], [5, 6, 7, 1]]))
    assert np.array_equal(candidate(np.array([[1, 2, 3, 4], [5, 6, 7, 10]]), 7, 1), np.array([[1, 2, 3, 4], [5, 6, 7, 1]]))
    assert np.array_equal(candidate(np.array([[1, 2, 3, 4], [5, 6, 7, 11]]), 7, 1), np.array([[1, 2, 3, 4], [5, 6, 7, 1]]))
    assert np.array_equal(candidate(np.array([[1, 2, 3, 4], [5, 6, 7, 12]]), 7, 1), np.array([[1, 2, 3, 4], [5, 6, 7, 1]]))
    assert np.array_equal(candidate(np.array([[1, 2, 3, 4], [5, 6, 7, 15]]), 7, 1), np.array([[1, 2, 3, 4], [5, 6, 7, 1]]))
    assert np.array_equal(candidate(np.array([[1, 2, 3, 4], [5, 6, 7, 15]]), 7, 0), np.array([[1, 2, 3, 4], [5, 6, 7, 0]]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def replace_elements_that_greater_than_value(arr, value, new_value):` that takes a NumPy array, a value, and a new value and returns a NumPy array to solve the following problem:
  Replace all elements of Python NumPy Array that are greater than `value` with `new_value`.

validator:
  table_test:
    function_name: replace_elements_that_greater_than_value
    test_cases:
    - ["`np.array([[1, 2, 3, 4], [5, 6, 7, 8]])`", 5, 0]
    - ["`np.array([[1, 2, 3, 4], [5, 6, 7, 8]])`", 5, 1]
    - ["`np.array([[1, 2, 3, 4], [5, 6, 7, 8]])`", 6, 1]
    - ["`np.array([[1, 2, 3, 4], [5, 6, 7, 8]])`", 7, 1]
    - ["`np.array([[1, 2, 3, 4], [5, 6, 7, 9]])`", 7, 1]
    - ["`np.array([[1, 2, 3, 4], [5, 6, 7, 10]])`", 7, 1]
    - ["`np.array([[1, 2, 3, 4], [5, 6, 7, 11]])`", 7, 1]
    - ["`np.array([[1, 2, 3, 4], [5, 6, 7, 12]])`", 7, 1]
    - ["`np.array([[1, 2, 3, 4], [5, 6, 7, 15]])`", 7, 1]
    - ["`np.array([[1, 2, 3, 4], [5, 6, 7, 15]])`", 7, 0]
"""

def replace_elements_that_greater_than_value(arr, value, new_value):
    arr[arr > value] = new_value
    return arr
