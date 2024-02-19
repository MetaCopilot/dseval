'''
### Prompt ###

import numpy as np

def append_arr_to_new_empty_arr(arr1, arr2):
    new_arr = np.array([])
    # How to add a new row to an empty numpy array
    # example: 
    # input: np.array([1,2,3]) and np.array([4,5,6])
    # output: np.array([[1,2,3],[4,5,6]])
    # Return the new array

### Solution ###

    return np.vstack((np.hstack((new_arr, arr1)), arr2))

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([1,2,3]), np.array([4,5,6])), np.array([[1,2,3],[4,5,6]]))
    assert np.array_equal(candidate(np.array([5,2,1]), np.array([8,5,0])), np.array([[5,2,1],[8,5,0]]))
    assert np.array_equal(candidate(np.array([5,5,5]), np.array([8,5,0])), np.array([[5,5,5],[8,5,0]]))
    assert np.array_equal(candidate(np.array([2,2,2]), np.array([8,5,0])), np.array([[2,2,2],[8,5,0]]))
    assert np.array_equal(candidate(np.array([5,4,1]), np.array([8,5,0])), np.array([[5,4,1],[8,5,0]]))
    assert np.array_equal(candidate(np.array([5,2,1]), np.array([8,4,4])), np.array([[5,2,1],[8,4,4]]))
    assert np.array_equal(candidate(np.array([5,2,1]), np.array([8,8,8])), np.array([[5,2,1],[8,8,8]]))
    assert np.array_equal(candidate(np.array([5,2,1]), np.array([5,5,5])), np.array([[5,2,1],[5,5,5]]))
    assert np.array_equal(candidate(np.array([5,2,1]), np.array([0,5,0])), np.array([[5,2,1],[0,5,0]]))
    assert np.array_equal(candidate(np.array([5,2,1]), np.array([4,5,0])), np.array([[5,2,1],[4,5,0]]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def append_arr_to_new_empty_arr(arr1, arr2):` that takes two numpy arrays and returns a numpy array to solve the following problem:
  How to add a new row to an empty numpy array
  example: 
  input: np.array([1,2,3]) and np.array([4,5,6])
  output: np.array([[1,2,3],[4,5,6]])

validator:
  table_test:
    function_name: append_arr_to_new_empty_arr
    test_cases:
    - ["`np.array([1,2,3])`", "`np.array([4,5,6])`"]
    - ["`np.array([5,2,1])`", "`np.array([8,5,0])`"]
    - ["`np.array([5,5,5])`", "`np.array([8,5,0])`"]
    - ["`np.array([2,2,2])`", "`np.array([8,5,0])`"]
    - ["`np.array([5,4,1])`", "`np.array([8,5,0])`"]
    - ["`np.array([5,2,1])`", "`np.array([8,4,4])`"]
    - ["`np.array([5,2,1])`", "`np.array([8,8,8])`"]
    - ["`np.array([5,2,1])`", "`np.array([5,5,5])`"]
    - ["`np.array([5,2,1])`", "`np.array([0,5,0])`"]
    - ["`np.array([5,2,1])`", "`np.array([4,5,0])`"]
"""

def append_arr_to_new_empty_arr(arr1, arr2):
    new_arr = np.array([])
    return np.vstack((np.hstack((new_arr, arr1)), arr2))
