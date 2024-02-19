'''
### Prompt ###

import numpy as np

def get_index_max_element(arr, axis_value):
    # How to get the index of a maximum element in a NumPy array along axis_value?
    # Return the result

### Solution ###

    return np.argmax(arr, axis=axis_value)

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([[1, 2, 3], [2, 3, 4]]), 1), np.array([2, 2]))
    assert np.array_equal(candidate(np.array([[1, 2, 3], [2, 3, 4]]), 0), np.array([1, 1, 1]))
    assert np.array_equal(candidate(np.array([[1, 2, 3], [2, 2, 4]]), 0), np.array([1, 0, 1]))
    assert np.array_equal(candidate(np.array([[1, 2, 4], [2, 2, 4]]), 0), np.array([1, 0, 0]))
    assert np.array_equal(candidate(np.array([[1, 2, 14], [2, 2, 4]]), 0), np.array([1, 0, 0]))
    assert np.array_equal(candidate(np.array([[1, 12, 14], [2, 2, 4]]), 0), np.array([1, 0, 0]))
    assert np.array_equal(candidate(np.array([[1, 12, 14], [2, 2, 1]]), 0), np.array([1, 0, 0]))
    assert np.array_equal(candidate(np.array([[1, 12, 14], [2, 1, 1]]), 0), np.array([1, 0, 0]))
    assert np.array_equal(candidate(np.array([[1, 12, 14], [2, 1, 11]]), 0), np.array([1, 0, 0]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def get_index_max_element(arr, axis_value):` that takes a NumPy array and an axis value and returns a NumPy array to solve the following problem:
  How to get the index of a maximum element in a NumPy array along axis_value?

validator:
  table_test:
    function_name: get_index_max_element
    test_cases:
    - ["`np.array([[1, 2, 3], [2, 3, 4]])`", 1]
    - ["`np.array([[1, 2, 3], [2, 3, 4]])`", 0]
    - ["`np.array([[1, 2, 3], [2, 2, 4]])`", 0]
    - ["`np.array([[1, 2, 4], [2, 2, 4]])`", 0]
    - ["`np.array([[1, 2, 14], [2, 2, 4]])`", 0]
    - ["`np.array([[1, 12, 14], [2, 2, 4]])`", 0]
    - ["`np.array([[1, 12, 14], [2, 2, 1]])`", 0]
    - ["`np.array([[1, 12, 14], [2, 1, 1]])`", 0]
    - ["`np.array([[1, 12, 14], [2, 1, 11]])`", 0]
"""

def get_index_max_element(arr, axis_value):
    return np.argmax(arr, axis=axis_value)
