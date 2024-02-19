'''
### Prompt ###

import numpy as np

def broadcasting_app(a, L, S):  # Window len = L, Stride len/stepsize = S
    """
    I want to create a matrix of sub sequences from this array of length L with stride S.
    Return the numpy array of sub sequences.
    """
    nrows = ((a.size-L)//S)+1

### Solution ###

    return a[S*np.arange(nrows)[:,None] + np.arange(L)]

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([1,2,3,4,5,6,7,8,9,10]), 3, 2), np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]))
    assert np.array_equal(candidate(np.array([11,2,3,4,5,6,7,8,9,10]), 3, 2), np.array([[11, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]))
    assert np.array_equal(candidate(np.array([11,2,13,4,5,6,7,8,9,10]), 3, 2), np.array([[11, 2, 13], [13, 4, 5], [5, 6, 7], [7, 8, 9]]))
    assert np.array_equal(candidate(np.array([11,2,13,14,5,6,7,8,9,10]), 3, 2), np.array([[11, 2, 13], [13, 14, 5], [5, 6, 7], [7, 8, 9]]))
    assert np.array_equal(candidate(np.array([11,2,13,14,15,6,7,8,9,10]), 3, 2), np.array([[11, 2, 13], [13, 14, 15], [15, 6, 7], [7, 8, 9]]))
    assert np.array_equal(candidate(np.array([11,2,13,14,15,16,7,8,9,10]), 3, 2), np.array([[11, 2, 13], [13, 14, 15], [15, 16, 7], [7, 8, 9]]))
    assert np.array_equal(candidate(np.array([11,2,13,14,15,16,17,8,9,10]), 3, 2), np.array([[11, 2, 13], [13, 14, 15], [15, 16, 17], [17, 8, 9]]))
    assert np.array_equal(candidate(np.array([11,2,13,14,15,16,17,18,9,10]), 3, 2), np.array([[11, 2, 13], [13, 14, 15], [15, 16, 17], [17, 18, 9]]))
    assert np.array_equal(candidate(np.array([11,2,13,14,15,16,17,18,19,10]), 3, 2), np.array([[11, 2, 13], [13, 14, 15], [15, 16, 17], [17, 18, 19]]))
    assert np.array_equal(candidate(np.array([11,12,13,14,15,16,17,18,19,10]), 3, 2), np.array([[11, 12, 13], [13, 14, 15], [15, 16, 17], [17, 18, 19]]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def broadcasting_app(a, L, S):` that takes a numpy array, a window length, and a stride length and returns a numpy array to solve the following problem:
  I want to create a matrix of sub sequences from this array of length L with stride S.

validator:
  table_test:
    function_name: broadcasting_app
    test_cases:
    - ["`np.array([1,2,3,4,5,6,7,8,9,10])`", 3, 2]
    - ["`np.array([11,2,3,4,5,6,7,8,9,10])`", 3, 2]
    - ["`np.array([11,2,13,4,5,6,7,8,9,10])`", 3, 2]
    - ["`np.array([11,2,13,14,5,6,7,8,9,10])`", 3, 2]
    - ["`np.array([11,2,13,14,15,6,7,8,9,10])`", 3, 2]
    - ["`np.array([11,2,13,14,15,16,7,8,9,10])`", 3, 2]
    - ["`np.array([11,2,13,14,15,16,17,8,9,10])`", 3, 2]
    - ["`np.array([11,2,13,14,15,16,17,18,9,10])`", 3, 2]
    - ["`np.array([11,2,13,14,15,16,17,18,19,10])`", 3, 2]
    - ["`np.array([11,12,13,14,15,16,17,18,19,10])`", 3, 2]
"""

def broadcasting_app(a, L, S):
    nrows = ((a.size-L)//S)+1
    return a[S*np.arange(nrows)[:,None] + np.arange(L)]
