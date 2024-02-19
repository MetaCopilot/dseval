'''
### Prompt ###

import numpy as np

def xor_operation(x, y, z):
    """
    How can I define in numpy a matrix that uses operations modulo 2?
    This operation is called "xor".
    Arguments:
        x: a numpy array
        y: a numpy array
        z: a numpy array
    Returns:
        a numpy array containing the result of the operation
    """

### Solution ###

    return (x ^ y ^ z)

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([1, 2, 3]), np.array([5, 6, 7]), np.array([9, 10, 11])), np.array([13, 14, 15]))
    assert np.array_equal(candidate(np.array([4, 3, 2]), np.array([8, 7, 6]), np.array([9, 10, 11])), np.array([5, 14, 15]))
    assert np.array_equal(candidate(np.array([4, 4, 2]), np.array([8, 7, 6]), np.array([9, 10, 11])), np.array([5, 9, 15]))
    assert np.array_equal(candidate(np.array([44, 4, 2]), np.array([8, 7, 6]), np.array([9, 10, 11])), np.array([45, 9, 15]))
    assert np.array_equal(candidate(np.array([44, 2, 2]), np.array([8, 7, 6]), np.array([9, 10, 11])), np.array([45, 15, 15]))
    assert np.array_equal(candidate(np.array([44, 2, 1]), np.array([8, 7, 6]), np.array([9, 10, 11])), np.array([45, 15, 12]))
    assert np.array_equal(candidate(np.array([44, 2, 1]), np.array([83, 7, 6]), np.array([9, 10, 11])), np.array([118, 15, 12]))
    assert np.array_equal(candidate(np.array([44, 2, 1]), np.array([83, 7, 3]), np.array([9, 10, 11])), np.array([118, 15, 9]))
    assert np.array_equal(candidate(np.array([2, 2, 1]), np.array([83, 7, 3]), np.array([9, 10, 11])), np.array([88, 15, 9]))
    assert np.array_equal(candidate(np.array([2, 31, 1]), np.array([83, 7, 3]), np.array([9, 10, 11])), np.array([88, 18, 9]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def xor_operation(x, y, z):` that takes three numpy arrays and returns a numpy array,
  to compute the xor operation (modulo 2) on each element of the three arrays.

validator:
  table_test:
    function_name: xor_operation
    test_cases:
    - ["`np.array([1, 2, 3])`", "`np.array([5, 6, 7])`", "`np.array([9, 10, 11])`"]
    - ["`np.array([4, 3, 2])`", "`np.array([8, 7, 6])`", "`np.array([9, 10, 11])`"]
    - ["`np.array([4, 4, 2])`", "`np.array([8, 7, 6])`", "`np.array([9, 10, 11])`"]
    - ["`np.array([44, 4, 2])`", "`np.array([8, 7, 6])`", "`np.array([9, 10, 11])`"]
    - ["`np.array([44, 2, 2])`", "`np.array([8, 7, 6])`", "`np.array([9, 10, 11])`"]
    - ["`np.array([44, 2, 1])`", "`np.array([8, 7, 6])`", "`np.array([9, 10, 11])`"]
    - ["`np.array([44, 2, 1])`", "`np.array([83, 7, 6])`", "`np.array([9, 10, 11])`"]
    - ["`np.array([44, 2, 1])`", "`np.array([83, 7, 3])`", "`np.array([9, 10, 11])`"]
    - ["`np.array([2, 2, 1])`", "`np.array([83, 7, 3])`", "`np.array([9, 10, 11])`"]
    - ["`np.array([2, 31, 1])`", "`np.array([83, 7, 3])`", "`np.array([9, 10, 11])`"]
"""

def xor_operation(x, y, z):
    return (x ^ y ^ z)
