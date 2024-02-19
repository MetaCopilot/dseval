'''
### Prompt ###

import numpy as np

def test_arr_contain_only_zeros(arr):
    # Test if numpy array contains only zeros
    # Return the result

### Solution ###

    return not np.any(arr)

### Test ###

def check(candidate):
    assert candidate(np.array(((0,0),(0,0)))) == True
    assert candidate(np.array(((1,0),(0,0)))) == False
    assert candidate(np.array(((1,0),(1,0)))) == False
    assert candidate(np.array(((1,0),(12,0)))) == False
    assert candidate(np.array(((1,0),(10,10)))) == False
    assert candidate(np.array(((12,0),(12,0)))) == False
    assert candidate(np.array(((1,20),(0,0)))) == False
    assert candidate(np.array(((1,0),(0,1230)))) == False
    assert candidate(np.array(((1,10),(10,0)))) == False
    assert candidate(np.array(((1,230),(10,10)))) == False
'''

# %%
import numpy as np

# %%
"""
question: |
  Write a function `def test_arr_contain_only_zeros(arr):` that takes a numpy array and returns a boolean to solve the following problem:
  Test if numpy array contains only zeros.

validator:
  table_test:
    function_name: test_arr_contain_only_zeros
    test_cases:
    - ["`np.array(((0,0),(0,0)))`"]
    - ["`np.array(((1,0),(0,0)))`"]
    - ["`np.array(((1,0),(1,0)))`"]
    - ["`np.array(((1,0),(12,0)))`"]
    - ["`np.array(((1,0),(10,10)))`"]
    - ["`np.array(((12,0),(12,0)))`"]
    - ["`np.array(((1,20),(0,0)))`"]
    - ["`np.array(((1,0),(0,1230)))`"]
    - ["`np.array(((1,10),(10,0)))`"]
    - ["`np.array(((1,230),(10,10)))`"]
"""

def test_arr_contain_only_zeros(arr):
    return not np.any(arr)
