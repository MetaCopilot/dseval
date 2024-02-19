'''
### Prompt ###

import numpy as np

def get_multiply_diff(t):
    # Is there a function that returns an array with the results of dividing the next element by the previous one? Like a "diff()", but with dividing
    # Not-numpy-example:
    # source = [1,3,6,24,36]
    # target = [j / i for i, j in zip(source[:-1], source[1:])]
    # Return: target implemented in numpy.

### Solution ###

    return t[1:] / t[:-1]

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([1,3,6,24,36])), np.array([3, 2, 4, 1.5]))
    assert np.array_equal(candidate(np.array([1,3,6,48,36])), np.array([3, 2, 8, 0.75]))
    assert np.array_equal(candidate(np.array([1,3,6,48,96])), np.array([3, 2, 8, 2]))
    assert np.array_equal(candidate(np.array([1,3,6,48,144])), np.array([3, 2, 8, 3]))
    assert np.array_equal(candidate(np.array([1,3,6,48,192])), np.array([3, 2, 8, 4]))
    assert np.array_equal(candidate(np.array([1,3,6,48,240])), np.array([3, 2, 8, 5]))
    assert np.array_equal(candidate(np.array([1,3,6,48,288])), np.array([3, 2, 8, 6]))
    assert np.array_equal(candidate(np.array([1,3,6,48,336])), np.array([3, 2, 8, 7]))
    assert np.array_equal(candidate(np.array([1,3,6,48,384])), np.array([3, 2, 8, 8]))
    assert np.array_equal(candidate(np.array([1,3,6,48,432])), np.array([3, 2, 8, 9]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def get_multiply_diff(t):` that takes a numpy array and returns a numpy array to solve the following problem:
  Is there a function that returns an array with the results of dividing the next element by the previous one? Like a "diff()", but with dividing

validator:
  table_test:
    function_name: get_multiply_diff
    test_cases:
    - ["`np.array([1,3,6,24,36])`"]
    - ["`np.array([1,3,6,48,36])`"]
    - ["`np.array([1,3,6,48,96])`"]
    - ["`np.array([1,3,6,48,144])`"]
    - ["`np.array([1,3,6,48,192])`"]
    - ["`np.array([1,3,6,48,240])`"]
    - ["`np.array([1,3,6,48,288])`"]
    - ["`np.array([1,3,6,48,336])`"]
    - ["`np.array([1,3,6,48,384])`"]
    - ["`np.array([1,3,6,48,432])`"]
"""

def get_multiply_diff(t):
    return t[1:] / t[:-1]
