'''
### Prompt ###

import numpy as np

def count_true_number(arr):
    # How to count the number of true elements in a NumPy bool array?
    # return the count value

### Solution ###

    return arr.sum()

### Test ###

def check(candidate):
    assert candidate(np.array([[0, 0, 1], [1, 0, 1], [1, 0, 1]], dtype=np.bool)) == 5
    assert candidate(np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1]], dtype=np.bool)) == 6
    assert candidate(np.array([[0, 1, 1], [1, 1, 1], [1, 0, 1]], dtype=np.bool)) == 7
    assert candidate(np.array([[0, 0, 0], [1, 1, 1], [1, 0, 1]], dtype=np.bool)) == 5
    assert candidate(np.array([[1, 1, 1], [1, 1, 1], [1, 0, 1]], dtype=np.bool)) == 8
    assert candidate(np.array([[0, 0, 1], [1, 1, 1]], dtype=np.bool)) == 4
    assert candidate(np.array([[0, 1, 1], [1, 1, 1]], dtype=np.bool)) == 5
    assert candidate(np.array([[1, 1, 1], [1, 1, 1]], dtype=np.bool)) == 6
    assert candidate(np.array([[0, 0, 1], [0, 1, 1]], dtype=np.bool)) == 3
    assert candidate(np.array([[0, 0, 1], [0, 0, 1]], dtype=np.bool)) == 2
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def count_true_number(arr):` that takes a NumPy bool array and returns an integer to solve the following problem:
  How to count the number of true elements in a NumPy bool array?

validator:
  table_test:
    function_name: count_true_number
    test_cases:
    - ["`np.array([[0, 0, 1], [1, 0, 1], [1, 0, 1]], dtype=bool)`"]
    - ["`np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1]], dtype=bool)`"]
    - ["`np.array([[0, 1, 1], [1, 1, 1], [1, 0, 1]], dtype=bool)`"]
    - ["`np.array([[0, 0, 0], [1, 1, 1], [1, 0, 1]], dtype=bool)`"]
    - ["`np.array([[1, 1, 1], [1, 1, 1], [1, 0, 1]], dtype=bool)`"]
    - ["`np.array([[0, 0, 1], [1, 1, 1]], dtype=bool)`"]
    - ["`np.array([[0, 1, 1], [1, 1, 1]], dtype=bool)`"]
    - ["`np.array([[1, 1, 1], [1, 1, 1]], dtype=bool)`"]
    - ["`np.array([[0, 0, 1], [0, 1, 1]], dtype=bool)`"]
    - ["`np.array([[0, 0, 1], [0, 0, 1]], dtype=bool)`"]
"""

def count_true_number(arr):
    return arr.sum()
