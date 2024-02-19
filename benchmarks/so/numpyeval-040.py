'''
### Prompt ###

import numpy as np

def interweaving_two_arrays(a, b):
    # How would one interweave them efficiently?
    # It can be assumed that length(a)==length(b).
    c = np.empty((a.size + b.size,), dtype=a.dtype)

### Solution ###

    c[0::2] = a
    c[1::2] = b
    return c

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([1,3,5]), np.array([2,4,6])), np.array([1,2,3,4,5,6]))
    assert np.array_equal(candidate(np.array([1,3,5]), np.array([2,4,7])), np.array([1,2,3,4,5,7]))
    assert np.array_equal(candidate(np.array([1,3,5]), np.array([2,3,6])), np.array([1,2,3,3,5,6]))
    assert np.array_equal(candidate(np.array([12,3,5]), np.array([2,4,6])), np.array([12,2,3,4,5,6]))
    assert np.array_equal(candidate(np.array([1,23,5]), np.array([2,4,6])), np.array([1,2,23,4,5,6]))
    assert np.array_equal(candidate(np.array([1,3,53]), np.array([2,4,6])), np.array([1,2,3,4,53,6]))
    assert np.array_equal(candidate(np.array([1,3,5]), np.array([42,4,6])), np.array([1,42,3,4,5,6]))
    assert np.array_equal(candidate(np.array([1,3,5]), np.array([2,43,6])), np.array([1,2,3,43,5,6]))
    assert np.array_equal(candidate(np.array([1,3,5]), np.array([2,4,64])), np.array([1,2,3,4,5,64]))
    assert np.array_equal(candidate(np.array([1,3,5]), np.array([2,4,63])), np.array([1,2,3,4,5,63]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def interweaving_two_arrays(a, b):` that takes two numpy arrays and returns a numpy array to solve the following problem:
  How would one interweave them efficiently?
  It can be assumed that length(a)==length(b).

validator:
  table_test:
    function_name: interweaving_two_arrays
    test_cases:
    - ["`np.array([1,3,5])`", "`np.array([2,4,6])`"]
    - ["`np.array([1,3,5])`", "`np.array([2,4,7])`"]
    - ["`np.array([1,3,5])`", "`np.array([2,3,6])`"]
    - ["`np.array([12,3,5])`", "`np.array([2,4,6])`"]
    - ["`np.array([1,23,5])`", "`np.array([2,4,6])`"]
    - ["`np.array([1,3,53])`", "`np.array([2,4,6])`"]
    - ["`np.array([1,3,5])`", "`np.array([42,4,6])`"]
    - ["`np.array([1,3,5])`", "`np.array([2,43,6])`"]
    - ["`np.array([1,3,5])`", "`np.array([2,4,64])`"]
    - ["`np.array([1,3,5])`", "`np.array([2,4,63])`"]
"""

def interweaving_two_arrays(a, b):
    c = np.empty((a.size + b.size,), dtype=a.dtype)
    c[0::2] = a
    c[1::2] = b
    return c
