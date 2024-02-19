'''
### Prompt ###

import numpy as np
def matrix2array(M):
    # I am using numpy. I have a matrix `M` 1*N and I want to get an array from with N elements.
    # To achieve it, Does anyone know a more elegant way to get the result?

### Solution ###

    return np.squeeze(np.asarray(M))

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.matrix([[1], [2], [3], [4]])), np.array([1, 2, 3, 4]))
    assert np.array_equal(candidate(np.matrix([[1], [2], [3], [5]])), np.array([1, 2, 3, 5]))
    assert np.array_equal(candidate(np.matrix([[1], [5], [3], [5]])), np.array([1, 5, 3, 5]))
    assert np.array_equal(candidate(np.matrix([[2], [5], [3], [5]])), np.array([2, 5, 3, 5]))
    assert np.array_equal(candidate(np.matrix([[2], [5], [4], [5]])), np.array([2, 5, 4, 5]))
    assert np.array_equal(candidate(np.matrix([[4], [5], [4], [5]])), np.array([4, 5, 4, 5]))
    assert np.array_equal(candidate(np.matrix([[4], [5], [4]])), np.array([4, 5, 4]))
    assert np.array_equal(candidate(np.matrix([[1], [5], [4]])), np.array([1, 5, 4]))
    assert np.array_equal(candidate(np.matrix([[1], [2], [4]])), np.array([1, 2, 4]))
    assert np.array_equal(candidate(np.matrix([[1], [2], [3]])), np.array([1, 2, 3]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def matrix2array(M):` that takes a numpy matrix and returns a numpy array to solve the following problem:
  I am using numpy. I have a matrix `M` 1*N and I want to get an array from with N elements.
  To achieve it, Does anyone know a more elegant way to get the result?

validator:
  table_test:
    function_name: matrix2array
    test_cases:
    - ["`np.matrix([[1], [2], [3], [4]])`"]
    - ["`np.matrix([[1], [2], [3], [5]])`"]
    - ["`np.matrix([[1], [5], [3], [5]])`"]
    - ["`np.matrix([[2], [5], [3], [5]])`"]
    - ["`np.matrix([[2], [5], [4], [5]])`"]
    - ["`np.matrix([[4], [5], [4], [5]])`"]
    - ["`np.matrix([[4], [5], [4]])`"]
    - ["`np.matrix([[1], [5], [4]])`"]
    - ["`np.matrix([[1], [2], [4]])`"]
    - ["`np.matrix([[1], [2], [3]])`"]
"""

def matrix2array(M):
    return np.squeeze(np.asarray(M))
