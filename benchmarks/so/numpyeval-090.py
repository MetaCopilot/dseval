'''
### Prompt ###

import numpy as np

def concatenate_two_arrays(arr1, arr2):
    # Concatenate a NumPy array to another NumPy array

### Solution ###

    return np.concatenate((arr1, arr2))

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([[1,2]]), np.array([[3,4]])), np.array([[1,2],[3,4]]))
    assert np.array_equal(candidate(np.array([[1,2]]), np.array([[3,5]])), np.array([[1,2],[3,5]]))
    assert np.array_equal(candidate(np.array([[2,2]]), np.array([[3,5]])), np.array([[2,2],[3,5]]))
    assert np.array_equal(candidate(np.array([[1,2]]), np.array([[4,5]])), np.array([[1,2],[4,5]]))
    assert np.array_equal(candidate(np.array([[31,2]]), np.array([[3,5]])), np.array([[31,2],[3,5]]))
    assert np.array_equal(candidate(np.array([[3,2]]), np.array([[3,5]])), np.array([[3,2],[3,5]]))
    assert np.array_equal(candidate(np.array([[31,2]]), np.array([[3,52]])), np.array([[31,2],[3,52]]))
    assert np.array_equal(candidate(np.array([[31,2]]), np.array([[31,15]])), np.array([[31,2],[31,15]]))
    assert np.array_equal(candidate(np.array([[31,2]]), np.array([[33,5]])), np.array([[31,2],[33,5]]))
    assert np.array_equal(candidate(np.array([[32,12]]), np.array([[3,5]])), np.array([[32,12],[3,5]]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def concatenate_two_arrays(arr1, arr2):` that takes two NumPy arrays and returns a NumPy array to solve the following problem:
  Concatenate a NumPy array to another NumPy array

validator:
  table_test:
    function_name: concatenate_two_arrays
    test_cases:
    - ["`np.array([[1,2]])`", "`np.array([[3,4]])`"]
    - ["`np.array([[1,2]])`", "`np.array([[3,5]])`"]
    - ["`np.array([[2,2]])`", "`np.array([[3,5]])`"]
    - ["`np.array([[1,2]])`", "`np.array([[4,5]])`"]
    - ["`np.array([[31,2]])`", "`np.array([[3,5]])`"]
    - ["`np.array([[3,2]])`", "`np.array([[3,5]])`"]
    - ["`np.array([[31,2]])`", "`np.array([[3,52]])`"]
    - ["`np.array([[31,2]])`", "`np.array([[31,15]])`"]
    - ["`np.array([[31,2]])`", "`np.array([[33,5]])`"]
    - ["`np.array([[32,12]])`", "`np.array([[3,5]])`"]
"""

def concatenate_two_arrays(arr1, arr2):
    return np.concatenate((arr1, arr2))
