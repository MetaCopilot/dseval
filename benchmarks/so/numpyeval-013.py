'''
### Prompt ###

import numpy as np

def inverse_matrix(matrix):
    # Inverse of a matrix using numpy and return it.
    # Input:
    #   matrix: numpy array, shape (n, n)
    # Output:
    #   inverse: numpy array, shape (n, n)

### Solution ###

    return np.linalg.inv(matrix)

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.matrix([[2,3],[4,5]])), np.matrix([[-2.5,1.5],[2,-1]]))
    assert np.array_equal(candidate(np.matrix([[2,2],[4,5]])), np.matrix([[2.5,-1],[-2,1]]))
    assert np.array_equal(candidate(np.matrix([[0,1],[4,5]])), np.matrix([[-1.25,0.25],[1,0]]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def inverse_matrix(matrix):` that takes a numpy array and returns a numpy array to solve the following problem:
  Inverse of a matrix using numpy and return it.
  Input:
    matrix: numpy array, shape (n, n)
  Output:
    inverse: numpy array, shape (n, n)

validator:
  table_test:
    function_name: inverse_matrix
    test_cases:
    - ["`np.matrix([[2,3],[4,5]])`"]
    - ["`np.matrix([[2,2],[4,5]])`"]
    - ["`np.matrix([[0,1],[4,5]])`"]
"""

def inverse_matrix(matrix):
    return np.linalg.inv(matrix)
