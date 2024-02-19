'''
### Prompt ###

import numpy as np

def get_i_th_index_in_last_dim(arr, i):
    """
    I would like to slice a numpy array to obtain the i-th index in the last dimension.
    Is there a way I can obtain this slice for any array without explicitly having to write the array dimensions?
    There is ... or Ellipsis, which does exactly this
    Returns: numpy array
    """

### Solution ###

    return arr[...,i]

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]]), 1), np.array([2,6,10]))
    assert np.array_equal(candidate(np.array([[10,2,3,4], [5,6,7,8], [9,10,11,12]]), 1), np.array([2,6,10]))
    assert np.array_equal(candidate(np.array([[10,2,3,4], [15,6,7,8], [9,10,11,12]]), 1), np.array([2,6,10]))
    assert np.array_equal(candidate(np.array([[10,2,3,4], [15,16,7,8], [9,10,11,12]]), 1), np.array([2,16,10]))
    assert np.array_equal(candidate(np.array([[10,2,3,4], [15,16,7,8], [9,110,11,12]]), 1), np.array([2,16,110]))
    assert np.array_equal(candidate(np.array([[10,2,3,4], [15,16,7,8], [9,110,111,12]]), 1), np.array([2,16,110]))
    assert np.array_equal(candidate(np.array([[10,2,3,4], [15,16,7,8], [9,110,111,112]]), 1), np.array([2,16,110]))
    assert np.array_equal(candidate(np.array([[10,2,3,4], [15,16,7,8], [19,110,111,112]]), 1), np.array([2,16,110]))
    assert np.array_equal(candidate(np.array([[10,2,3,4], [15,16,17,8], [19,110,111,112]]), 1), np.array([2,16,110]))
    assert np.array_equal(candidate(np.array([[10,2,23,4], [15,16,17,8], [19,110,111,112]]), 1), np.array([2,16,110]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def get_i_th_index_in_last_dim(arr, i):` that takes a numpy array and an index and returns a numpy array to solve the following problem:
  I would like to slice a numpy array to obtain the i-th index in the last dimension.
  Is there a way I can obtain this slice for any array without explicitly having to write the array dimensions?
  There is ... or Ellipsis, which does exactly this

validator:
  table_test:
    function_name: get_i_th_index_in_last_dim
    test_cases:
    - ["`np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])`", 1]
    - ["`np.array([[10,2,3,4], [5,6,7,8], [9,10,11,12]])`", 1]
    - ["`np.array([[10,2,3,4], [15,6,7,8], [9,10,11,12]])`", 1]
    - ["`np.array([[10,2,3,4], [15,16,7,8], [9,10,11,12]])`", 1]
    - ["`np.array([[10,2,3,4], [15,16,7,8], [9,110,11,12]])`", 1]
    - ["`np.array([[10,2,3,4], [15,16,7,8], [9,110,111,12]])`", 1]
    - ["`np.array([[10,2,3,4], [15,16,7,8], [9,110,111,112]])`", 1]
    - ["`np.array([[10,2,3,4], [15,16,7,8], [19,110,111,112]])`", 1]
    - ["`np.array([[10,2,3,4], [15,16,17,8], [19,110,111,112]])`", 1]
    - ["`np.array([[10,2,23,4], [15,16,17,8], [19,110,111,112]])`", 1]
"""

def get_i_th_index_in_last_dim(arr, i):
    return arr[...,i]
