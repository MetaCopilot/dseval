'''
### Prompt ###

import numpy as np

def numpy_is_empty(arr):
    # How can I check whether a numpy array is empty or not?
    # Return the reuslt that contains True or False

### Solution ###

    return arr.size == 0

### Test ###

def check(candidate):
    assert candidate(np.array([])) == True
    assert candidate(np.array([1])) == False
    assert candidate(np.array([2])) == False
    assert candidate(np.array([1, 2])) == False
    assert candidate(np.array([1, 3, 4])) == False
    assert candidate(np.array([8])) == False
    assert candidate(np.array([5])) == False
    assert candidate(np.array([3, 5])) == False
    assert candidate(np.array([3, 1])) == False
    assert candidate(np.array([7])) == False
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def numpy_is_empty(arr):` that takes a numpy array and returns a boolean to solve the following problem:
  How can I check whether a numpy array is empty or not?

validator:
  table_test:
    function_name: numpy_is_empty
    test_cases:
    - ["`np.array([])`"]
    - ["`np.array([1])`"]
    - ["`np.array([2])`"]
    - ["`np.array([1, 2])`"]
    - ["`np.array([1, 3, 4])`"]
    - ["`np.array([8])`"]
    - ["`np.array([5])`"]
    - ["`np.array([3, 5])`"]
    - ["`np.array([3, 1])`"]
    - ["`np.array([7])`"]
"""

def numpy_is_empty(arr):
    return arr.size == 0
