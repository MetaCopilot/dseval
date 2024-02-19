'''
### Prompt ###

import numpy as np

def matrix_to_array(matrix):
    # I am using numpy. I have a matrix with 1 column and N rows and I want to get an array from with N elements.
    # For example, if i have M = matrix([[1], [2], [3], [4]]), I want to get A = array([1,2,3,4]).
    # Return the array

### Solution ###

    return np.squeeze(np.asarray(matrix))

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([[1], [2], [3], [4]])), np.array([1,2,3,4]))
    assert np.array_equal(candidate(np.array([[2], [3], [7], [3]])), np.array([2,3,7,3]))
    assert np.array_equal(candidate(np.array([[2], [3], [7], [3]])), np.array([2,3,7,3]))
    assert np.array_equal(candidate(np.array([[3], [3], [7], [3]])), np.array([3,3,7,3]))
    assert np.array_equal(candidate(np.array([[2], [4], [7], [3]])), np.array([2,4,7,3]))
    assert np.array_equal(candidate(np.array([[2], [3], [5], [3]])), np.array([2,3,5,3]))
    assert np.array_equal(candidate(np.array([[9], [3], [7], [3]])), np.array([9,3,7,3]))
    assert np.array_equal(candidate(np.array([[1], [3], [7], [3]])), np.array([1,3,7,3]))
    assert np.array_equal(candidate(np.array([[2], [3], [7], [4]])), np.array([2,3,7,4]))
    assert np.array_equal(candidate(np.array([[3], [3], [3], [3]])), np.array([3,3,3,3]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def matrix_to_array(matrix):` that takes a matrix and returns an array to solve the following problem:
  I am using numpy. I have a matrix with 1 column and N rows and I want to get an array from with N elements.
  For example, if i have M = matrix([[1], [2], [3], [4]]), I want to get A = array([1,2,3,4]).

validator:
  table_test:
    function_name: matrix_to_array
    test_cases:
    - ["`np.array([[1], [2], [3], [4]])`"]
    - ["`np.array([[2], [3], [7], [3]])`"]
    - ["`np.array([[2], [3], [7], [3]])`"]
    - ["`np.array([[3], [3], [7], [3]])`"]
    - ["`np.array([[2], [4], [7], [3]])`"]
    - ["`np.array([[2], [3], [5], [3]])`"]
    - ["`np.array([[9], [3], [7], [3]])`"]
    - ["`np.array([[1], [3], [7], [3]])`"]
    - ["`np.array([[2], [3], [7], [4]])`"]
    - ["`np.array([[3], [3], [3], [3]])`"]
"""

def matrix_to_array(matrix):
    return np.squeeze(np.asarray(matrix))
