'''
### Prompt ###

import numpy as np
def get_minimum_value(arr):
    # I wish to find and return the minimum value in this 2D array
    # The following code is aim to implement it

### Solution ###

    return np.min(arr)

### Test ###

def check(candidate):
    assert candidate(np.array([[8,2,3,4,5,6], [3,8,5,1,-2,9]])) == -2
    assert candidate(np.array([[8,2,3,4,4,6], [3,8,3,1,-2,9]])) == -2
    assert candidate(np.array([[81,2,3,41,5,6], [3,8,5,1,-2,9]])) == -2
    assert candidate(np.array([[8,2,3,4,15,6], [3,8,5,1,-3,19]])) == -3
    assert candidate(np.array([[8,12,3,4,35,6], [3,8,5,1,-2,9]])) == -2
    assert candidate(np.array([[8,2,3,44,5,6], [3,8,5,1,-2,9]])) == -2
    assert candidate(np.array([[8,2,33,4,5,6], [3,84,5,1,-2,9]])) == -2
    assert candidate(np.array([[83,2,3,44,5,6], [3,8,5,11,-2,9]])) == -2
    assert candidate(np.array([[8,12,3,42,5,6], [3,8,5,1,-2,19]])) == -2
    assert candidate(np.array([[8,12,3,4,5,26], [3,-8,5,1,-2,9]])) == -8
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def get_minimum_value(arr):` that takes a 2D numpy array and returns a number to solve the following problem:
  I wish to find and return the minimum value in this 2D array

validator:
  table_test:
    function_name: get_minimum_value
    test_cases:
    - ["`np.array([[8,2,3,4,5,6], [3,8,5,1,-2,9]])`"]
    - ["`np.array([[8,2,3,4,4,6], [3,8,3,1,-2,9]])`"]
    - ["`np.array([[81,2,3,41,5,6], [3,8,5,1,-2,9]])`"]
    - ["`np.array([[8,2,3,4,15,6], [3,8,5,1,-3,19]])`"]
    - ["`np.array([[8,12,3,4,35,6], [3,8,5,1,-2,9]])`"]
    - ["`np.array([[8,2,3,44,5,6], [3,8,5,1,-2,9]])`"]
    - ["`np.array([[8,2,33,4,5,6], [3,84,5,1,-2,9]])`"]
    - ["`np.array([[83,2,3,44,5,6], [3,8,5,11,-2,9]])`"]
    - ["`np.array([[8,12,3,42,5,6], [3,8,5,1,-2,19]])`"]
    - ["`np.array([[8,12,3,4,5,26], [3,-8,5,1,-2,9]])`"]
"""

def get_minimum_value(arr):
    return np.min(arr)
