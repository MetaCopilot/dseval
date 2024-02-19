'''
### Prompt ###

import numpy as np

def find_most_frequent_number(arr):
    # Find the most frequent number in a NumPy array
    # Return the number

### Solution ###

    return np.bincount(arr).argmax()

### Test ###

def check(candidate):
    assert candidate(np.array([1,2,3,1,2,1,1,1,3,2,2,1])) == 1
    assert candidate(np.array([1,1,3,1,2,1,1,1,3,2,2,1])) == 1
    assert candidate(np.array([1,2,1,1,2,1,1,1,3,2,2,1])) == 1
    assert candidate(np.array([1,2,3,1,2,1,1,1,1,2,2,1])) == 1
    assert candidate(np.array([1,2,3,1,2,1,1,1,3,2,1,0])) == 1
    assert candidate(np.array([1,2,3,1,2,1,1,1,3,1,1,1])) == 1
    assert candidate(np.array([1,2,3,1,2,1,1,1,1,2,2,1])) == 1
    assert candidate(np.array([1,2,3,1,2,1,1,1,0,1,1,1])) == 1
    assert candidate(np.array([1,1,3,1,2,1,1,1,1,2,2,1])) == 1
    assert candidate(np.array([2,2,3,2,2,2,2,2,3,2,2,2])) == 2
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def find_most_frequent_number(arr):` that takes a NumPy array and returns a number to solve the following problem:
  Find the most frequent number in a NumPy array.

validator:
  table_test:
    function_name: find_most_frequent_number
    test_cases:
    - ["`np.array([1,2,3,1,2,1,1,1,3,2,2,1])`"]
    - ["`np.array([1,1,3,1,2,1,1,1,3,2,2,1])`"]
    - ["`np.array([1,2,1,1,2,1,1,1,3,2,2,1])`"]
    - ["`np.array([1,2,3,1,2,1,1,1,1,2,2,1])`"]
    - ["`np.array([1,2,3,1,2,1,1,1,3,2,1,0])`"]
    - ["`np.array([1,2,3,1,2,1,1,1,3,1,1,1])`"]
    - ["`np.array([1,2,3,1,2,1,1,1,1,2,2,1])`"]
    - ["`np.array([1,2,3,1,2,1,1,1,0,1,1,1])`"]
    - ["`np.array([1,1,3,1,2,1,1,1,1,2,2,1])`"]
    - ["`np.array([2,2,3,2,2,2,2,2,3,2,2,2])`"]
"""

def find_most_frequent_number(arr):
    return np.bincount(arr).argmax()
