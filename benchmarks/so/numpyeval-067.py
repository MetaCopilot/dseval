'''
### Prompt ###

import numpy as np

def find_indices_zero(arr):
    # Find indices of elements equal to zero in a NumPy array
    # Return the indices

### Solution ###

    return np.where(arr == 0)[0]

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([1, 0, 2, 3, 9, 0])), np.array([1, 5]))
    assert np.array_equal(candidate(np.array([1, 0, 2, 3, 10, 0])), np.array([1, 5]))
    assert np.array_equal(candidate(np.array([1, 0, 3, 3, 10, 0])), np.array([1, 5]))
    assert np.array_equal(candidate(np.array([1, 0, 4, 3, 10, 0])), np.array([1, 5]))
    assert np.array_equal(candidate(np.array([1, 0, 4, 3, 10, 2])), np.array([1]))
    assert np.array_equal(candidate(np.array([1, 0, 0, 3, 10, 2])), np.array([1, 2]))
    assert np.array_equal(candidate(np.array([1, 0, 0, 4, 10, 2])), np.array([1, 2]))
    assert np.array_equal(candidate(np.array([1, 0, 0, 4, 0, 2])), np.array([1, 2, 4]))
    assert np.array_equal(candidate(np.array([1, 0, 0, 4, 0, 4])), np.array([1, 2, 4]))
    assert np.array_equal(candidate(np.array([1, 0, 0, 4, 0, 31])), np.array([1, 2, 4]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def find_indices_zero(arr):` that takes a NumPy array and returns the indices of elements equal to zero.

validator:
  table_test:
    function_name: find_indices_zero
    test_cases:
    - ["`np.array([1, 0, 2, 3, 9, 0])`"]
    - ["`np.array([1, 0, 2, 3, 10, 0])`"]
    - ["`np.array([1, 0, 3, 3, 10, 0])`"]
    - ["`np.array([1, 0, 4, 3, 10, 0])`"]
    - ["`np.array([1, 0, 4, 3, 10, 2])`"]
    - ["`np.array([1, 0, 0, 3, 10, 2])`"]
    - ["`np.array([1, 0, 0, 4, 10, 2])`"]
    - ["`np.array([1, 0, 0, 4, 0, 2])`"]
    - ["`np.array([1, 0, 0, 4, 0, 4])`"]
    - ["`np.array([1, 0, 0, 4, 0, 31])`"]
"""

def find_indices_zero(arr):
    return np.where(arr == 0)[0]
