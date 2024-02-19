'''
### Prompt ###

import numpy as np

def average_every_3_elements(arr):
    # Averaging over every 3 elements of a numpy array
    # I have a numpy array. I want to create a new array which is the average over every consecutive triplet of elements. So the new array will be a third of the size as the original.
    # Return it

### Solution ###

    return np.mean(arr.reshape(-1, 3), axis=1)

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([1,2,3,1,2,3,1,2,3])), np.array([2, 2, 2]))
    assert np.array_equal(candidate(np.array([1,2,3,1,2,3,2,3,4])), np.array([2, 2, 3]))
    assert np.array_equal(candidate(np.array([1,2,3,3,4,5,2,3,4])), np.array([2, 4, 3]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def average_every_3_elements(arr):` that takes a numpy array and returns a numpy array to solve the following problem:
  Averaging over every 3 elements of a numpy array
  I have a numpy array. I want to create a new array which is the average over every consecutive triplet of elements. So the new array will be a third of the size as the original.

validator:
  table_test:
    function_name: average_every_3_elements
    test_cases:
    - ["`np.array([1,2,3,1,2,3,1,2,3])`"]
    - ["`np.array([1,2,3,1,2,3,2,3,4])`"]
    - ["`np.array([1,2,3,3,4,5,2,3,4])`"]
"""

def average_every_3_elements(arr):
    return np.mean(arr.reshape(-1, 3), axis=1)
