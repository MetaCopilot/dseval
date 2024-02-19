'''
### Prompt ###

import numpy as np

def crop(arr, top, bottom, left, right):
    # How do I extract a sub-array from a numpy 2d array? 
    # I'd like to extract a numpy array with a specified size from a numpy 2d array--essentially I want to crop the array.
    # Return a sub-array from a numpy 2d array.

### Solution ###

    return arr[top:bottom, left:right]

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([[1, 3, 3], [4, 6, 6], [7, 8, 9]]), 0, 2, 0, 2), np.array([[1, 3], [4, 6]]))
    assert np.array_equal(candidate(np.array([[2, 3, 3], [2, 6, 6], [7, 8, 9]]), 0, 2, 0, 2), np.array([[2, 3], [2, 6]]))
    assert np.array_equal(candidate(np.array([[2, 3, 4], [2, 6, 6], [7, 8, 9]]), 0, 2, 0, 2), np.array([[2, 3], [2, 6]]))
    assert np.array_equal(candidate(np.array([[2, 3, 42], [2, 6, 6], [7, 8, 9]]), 0, 2, 0, 2), np.array([[2, 3], [2, 6]]))
    assert np.array_equal(candidate(np.array([[1, 9, 3], [2, 6, 6], [7, 8, 9]]), 0, 2, 0, 2), np.array([[1, 9], [2, 6]]))
    assert np.array_equal(candidate(np.array([[0, 3, 3], [2, 6, 6], [7, 8, 9]]), 0, 2, 0, 2), np.array([[0, 3], [2, 6]]))
    assert np.array_equal(candidate(np.array([[6, 3, 3], [2, 1, 6], [7, 8, 9]]), 0, 2, 0, 2), np.array([[6, 3], [2, 1]]))
    assert np.array_equal(candidate(np.array([[2, 3, 3], [2, 6, 3], [7, 8, 3]]), 0, 2, 0, 2), np.array([[2, 3], [2, 6]]))
    assert np.array_equal(candidate(np.array([[12, 3, 3], [2, 6, 6], [7, 8, 9]]), 0, 2, 0, 2), np.array([[12, 3], [2, 6]]))
    assert np.array_equal(candidate(np.array([[23, 34, 3], [2, 6, 6], [7, 8, 9]]), 0, 2, 0, 2), np.array([[23, 34], [2, 6]]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def crop(arr, top, bottom, left, right):` that takes a numpy 2d array and four integers and returns a numpy 2d array to solve the following problem:
  How do I extract a sub-array from a numpy 2d array? 
  I'd like to extract a numpy array with a specified size from a numpy 2d array--essentially I want to crop the array.
  Return a sub-array from a numpy 2d array.

validator:
  table_test:
    function_name: crop
    test_cases:
    - ["`np.array([[1, 3, 3], [4, 6, 6], [7, 8, 9]])`", 0, 2, 0, 2]
    - ["`np.array([[2, 3, 3], [2, 6, 6], [7, 8, 9]])`", 0, 2, 0, 2]
    - ["`np.array([[2, 3, 4], [2, 6, 6], [7, 8, 9]])`", 0, 2, 0, 2]
    - ["`np.array([[2, 3, 42], [2, 6, 6], [7, 8, 9]])`", 0, 2, 0, 2]
    - ["`np.array([[1, 9, 3], [2, 6, 6], [7, 8, 9]])`", 0, 2, 0, 2]
    - ["`np.array([[0, 3, 3], [2, 6, 6], [7, 8, 9]])`", 0, 2, 0, 2]
    - ["`np.array([[6, 3, 3], [2, 1, 6], [7, 8, 9]])`", 0, 2, 0, 2]
    - ["`np.array([[2, 3, 3], [2, 6, 3], [7, 8, 3]])`", 0, 2, 0, 2]
    - ["`np.array([[12, 3, 3], [2, 6, 6], [7, 8, 9]])`", 0, 2, 0, 2]
    - ["`np.array([[23, 34, 3], [2, 6, 6], [7, 8, 9]])`", 0, 2, 0, 2]
"""

def crop(arr, top, bottom, left, right):
    return arr[top:bottom, left:right]
