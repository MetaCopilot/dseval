'''
### Prompt ###

import numpy as np

def add_row_to_arr(arr, row):
    # How does one add rows to a numpy array?
    # Is there a numpythonic way to do this?

### Solution ###

    return np.vstack((arr, row))

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([[1, 2, 3]]), np.array([[4, 5, 6]])), np.array([[1, 2, 3], [4, 5, 6]]))
    assert np.array_equal(candidate(np.array([[1, 2, 4]]), np.array([[4, 5, 6]])), np.array([[1, 2, 4], [4, 5, 6]]))
    assert np.array_equal(candidate(np.array([[1, 3, 4]]), np.array([[4, 5, 6]])), np.array([[1, 3, 4], [4, 5, 6]]))
    assert np.array_equal(candidate(np.array([[1, 3, 4]]), np.array([[4, 8, 6]])), np.array([[1, 3, 4], [4, 8, 6]]))
    assert np.array_equal(candidate(np.array([[2, 3, 4]]), np.array([[4, 8, 6]])), np.array([[2, 3, 4], [4, 8, 6]]))
    assert np.array_equal(candidate(np.array([[3, 3, 4]]), np.array([[4, 8, 6]])), np.array([[3, 3, 4], [4, 8, 6]]))
    assert np.array_equal(candidate(np.array([[4, 3, 4]]), np.array([[4, 8, 6]])), np.array([[4, 3, 4], [4, 8, 6]]))
    assert np.array_equal(candidate(np.array([[4, 4, 4]]), np.array([[4, 8, 6]])), np.array([[4, 4, 4], [4, 8, 6]]))
    assert np.array_equal(candidate(np.array([[4, 4]]), np.array([[4, 8]])), np.array([[4, 4], [4, 8]]))
    assert np.array_equal(candidate(np.array([[4, 6]]), np.array([[4, 8]])), np.array([[4, 6], [4, 8]]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def add_row_to_arr(arr, row):` that takes a numpy array and a row to add and returns a numpy array to solve the following problem:
  How does one add rows to a numpy array?
  Is there a numpythonic way to do this?

validator:
  table_test:
    function_name: add_row_to_arr
    test_cases:
    - ["`np.array([[1, 2, 3]])`", "`np.array([[4, 5, 6]])`"]
    - ["`np.array([[1, 2, 4]])`", "`np.array([[4, 5, 6]])`"]
    - ["`np.array([[1, 3, 4]])`", "`np.array([[4, 5, 6]])`"]
    - ["`np.array([[1, 3, 4]])`", "`np.array([[4, 8, 6]])`"]
    - ["`np.array([[2, 3, 4]])`", "`np.array([[4, 8, 6]])`"]
    - ["`np.array([[3, 3, 4]])`", "`np.array([[4, 8, 6]])`"]
    - ["`np.array([[4, 3, 4]])`", "`np.array([[4, 8, 6]])`"]
    - ["`np.array([[4, 4, 4]])`", "`np.array([[4, 8, 6]])`"]
    - ["`np.array([[4, 4]])`", "`np.array([[4, 8]])`"]
    - ["`np.array([[4, 6]])`", "`np.array([[4, 8]])`"]
"""

def add_row_to_arr(arr, row):
    return np.vstack((arr, row))
