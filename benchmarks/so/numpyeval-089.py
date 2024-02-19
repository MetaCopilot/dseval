'''
### Prompt ###

import numpy as np

def consecutive(data, stepsize=1):
    # How to find the groups of consecutive elements in a NumPy array
    # I have to cluster the consecutive elements from a NumPy array. Considering the following example
    # a = [ 0, 47, 48, 49, 50, 97, 98, 99]
    # The output should be a list of tuples as follows
    # [(0), (47, 48, 49, 50), (97, 98, 99)]
    # Here the difference is just one between the elements. It will be great if the difference can also be specified as a limit or a hardcoded number.
    # Finally, return the number of consecutive elements in the array.

### Solution ###

    return len(np.split(data, np.where(np.diff(data) != stepsize)[0]+1))

### Test ###

def check(candidate):
    assert candidate(np.array([0, 47, 48, 49, 50, 97, 98, 99])) == 3
    assert candidate(np.array([0, 47, 48, 49, 20, 97, 98, 99])) == 4
    assert candidate(np.array([0, 2, 3, 49, 50, 97, 98, 99])) == 4
    assert candidate(np.array([0, 2, 3, 4, 50, 97, 98, 99])) == 4
    assert candidate(np.array([0, 2, 3, 4, 5, 97, 98, 99])) == 3
    assert candidate(np.array([0, 2, 3, 4, 5, 9, 98, 99])) == 4
    assert candidate(np.array([0, 2, 2, 4, 5, 9, 98, 99])) == 6
    assert candidate(np.array([0, 2, 2, 4, 5, 9, 100, 99])) == 7
    assert candidate(np.array([0, 2, 2, 4, 5, 9, 100, 200])) == 7
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def consecutive(data, stepsize=1):` that takes a NumPy array and an optional stepsize and returns an integer to solve the following problem:
  How to find the groups of consecutive elements in a NumPy array
  I have to cluster the consecutive elements from a NumPy array. Considering the following example
  a = [ 0, 47, 48, 49, 50, 97, 98, 99]
  The output should be a list of tuples as follows
  [(0), (47, 48, 49, 50), (97, 98, 99)]
  Here the difference is just one between the elements. It will be great if the difference can also be specified as a limit or a hardcoded number.
  Finally, return the number of consecutive elements in the array.

validator:
  table_test:
    function_name: consecutive
    test_cases:
    - ["`np.array([0, 47, 48, 49, 50, 97, 98, 99])`"]
    - ["`np.array([0, 47, 48, 49, 20, 97, 98, 99])`"]
    - ["`np.array([0, 2, 3, 49, 50, 97, 98, 99])`"]
    - ["`np.array([0, 2, 3, 4, 50, 97, 98, 99])`"]
    - ["`np.array([0, 2, 3, 4, 5, 97, 98, 99])`"]
    - ["`np.array([0, 2, 3, 4, 5, 9, 98, 99])`"]
    - ["`np.array([0, 2, 2, 4, 5, 9, 98, 99])`"]
    - ["`np.array([0, 2, 2, 4, 5, 9, 100, 99])`"]
    - ["`np.array([0, 2, 2, 4, 5, 9, 100, 200])`"]
"""

def consecutive(data, stepsize=1):
    return len(np.split(data, np.where(np.diff(data) != stepsize)[0]+1))
