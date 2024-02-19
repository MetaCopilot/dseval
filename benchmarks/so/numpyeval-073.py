'''
### Prompt ###

import numpy as np

def find_nearest(array, value):
    array = np.asarray(array)
    # Find nearest value in numpy array
    # return the result

### Solution ###

    idx = (np.abs(array - value)).argmin()
    return array[idx]

### Test ###

def check(candidate):
    assert candidate(np.array([1, 2, 3, 8, 3, 1, 9, 0]), 1) == 1
    assert candidate(np.array([3, 1, 9, 0, 1, 2, 3, 8]), 3) == 3
    assert candidate(np.array([3, 1, 9, 0, 1, 2, 3, 3]), 3) == 3
    assert candidate(np.array([3, 1, 9, 0, 1, 3, 3, 3]), 3) == 3
    assert candidate(np.array([3, 1, 9, 0, 1, 3, 34, 3]), 3) == 3
    assert candidate(np.array([3, 1, 9, 0, 0, 3, 34, 3]), 3) == 3
    assert candidate(np.array([3, 1, 9, 0, 12, 3, 34, 3]), 3) == 3
    assert candidate(np.array([3, 2, 9, 0, 12, 3, 34, 3]), 3) == 3
    assert candidate(np.array([3, 2, 9, 1, 12, 3, 34, 3]), 3) == 3
    assert candidate(np.array([3, 2, 9, 1, 41, 3, 34, 3]), 3) == 3
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def find_nearest(array, value):` that takes a numpy array and a value and returns a number to solve the following problem:
  Find nearest value in numpy array.

validator:
  table_test:
    function_name: find_nearest
    test_cases:
    - ["`np.array([1, 2, 3, 8, 3, 1, 9, 0])`", 1]
    - ["`np.array([3, 1, 9, 0, 1, 2, 3, 8])`", 3]
    - ["`np.array([3, 1, 9, 0, 1, 2, 3, 3])`", 3]
    - ["`np.array([3, 1, 9, 0, 1, 3, 3, 3])`", 3]
    - ["`np.array([3, 1, 9, 0, 1, 3, 34, 3])`", 3]
    - ["`np.array([3, 1, 9, 0, 0, 3, 34, 3])`", 3]
    - ["`np.array([3, 1, 9, 0, 12, 3, 34, 3])`", 3]
    - ["`np.array([3, 2, 9, 0, 12, 3, 34, 3])`", 3]
    - ["`np.array([3, 2, 9, 1, 12, 3, 34, 3])`", 3]
    - ["`np.array([3, 2, 9, 1, 41, 3, 34, 3])`", 3]
"""

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]
