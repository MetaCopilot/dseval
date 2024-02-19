'''
### Prompt ###

import numpy as np

def add_first_element_to_arr(arr):
    # I want to add the first element on to the end of the array.
    # Return the appended array.

### Solution ###

    return np.append(arr, arr[0])

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([1, 2, 3])), np.array([1, 2, 3, 1]))
    assert np.array_equal(candidate(np.array([1, 3, 3])), np.array([1, 3, 3, 1]))
    assert np.array_equal(candidate(np.array([2, 2, 3])), np.array([2, 2, 3, 2]))
    assert np.array_equal(candidate(np.array([1, 3])), np.array([1, 3, 1]))
    assert np.array_equal(candidate(np.array([1, 2, 3, 4])), np.array([1, 2, 3, 4, 1]))
    assert np.array_equal(candidate(np.array([1, 4, 3])), np.array([1, 4, 3, 1]))
    assert np.array_equal(candidate(np.array([1, 2, 13])), np.array([1, 2, 13, 1]))
    assert np.array_equal(candidate(np.array([1, 12, 13])), np.array([1, 12, 13, 1]))
    assert np.array_equal(candidate(np.array([1, 32, 3])), np.array([1, 32, 3, 1]))
    assert np.array_equal(candidate(np.array([11, 2, 3])), np.array([11, 2, 3, 11]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def add_first_element_to_arr(arr):` that takes a numpy array and returns a numpy array to solve the following problem:
  I want to add the first element on to the end of the array.

validator:
  table_test:
    function_name: add_first_element_to_arr
    test_cases:
    - ["`np.array([1, 2, 3])`"]
    - ["`np.array([1, 3, 3])`"]
    - ["`np.array([2, 2, 3])`"]
    - ["`np.array([1, 3])`"]
    - ["`np.array([1, 2, 3, 4])`"]
    - ["`np.array([1, 4, 3])`"]
    - ["`np.array([1, 2, 13])`"]
    - ["`np.array([1, 12, 13])`"]
    - ["`np.array([1, 32, 3])`"]
    - ["`np.array([11, 2, 3])`"]
"""

def add_first_element_to_arr(arr):
    return np.append(arr, arr[0])
