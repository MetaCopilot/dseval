'''
### Prompt ###

import numpy as np

def arr2tuple(arr):
    # Convert numpy array to tuple
    # Return the transformed tuple

### Solution ###

    return tuple(map(tuple, arr))

### Test ###

def check(candidate):
    assert candidate(np.array(((2,2),(2,-2)))) == ((2,2),(2,-2))
    assert candidate(np.array(((2,2),(2,2)))) == ((2,2),(2,2))
    assert candidate(np.array(((2,3),(2,-2)))) == ((2,3),(2,-2))
    assert candidate(np.array(((4,2),(2,-2)))) == ((4,2),(2,-2))
    assert candidate(np.array(((2,2),(5,-2)))) == ((2,2),(5,-2))
    assert candidate(np.array(((2,32),(2,-2)))) == ((2,32),(2,-2))
    assert candidate(np.array(((21,2),(2,-2)))) == ((21,2),(2,-2))
    assert candidate(np.array(((2,2),(32,-2)))) == ((2,2),(32,-2))
    assert candidate(np.array(((2,2),(2,-12)))) == ((2,2),(2,-12))
    assert candidate(np.array(((222,2),(2,-2)))) == ((222,2),(2,-2))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def arr2tuple(arr):` that takes a numpy array and returns a tuple to solve the following problem:
  Convert numpy array to tuple

validator:
  table_test:
    function_name: arr2tuple
    test_cases:
    - ["`np.array(((2,2),(2,-2)))`"]
    - ["`np.array(((2,2),(2,2)))`"]
    - ["`np.array(((2,3),(2,-2)))`"]
    - ["`np.array(((4,2),(2,-2)))`"]
    - ["`np.array(((2,2),(5,-2)))`"]
    - ["`np.array(((2,32),(2,-2)))`"]
    - ["`np.array(((21,2),(2,-2)))`"]
    - ["`np.array(((2,2),(32,-2)))`"]
    - ["`np.array(((2,2),(2,-12)))`"]
    - ["`np.array(((222,2),(2,-2)))`"]
"""

def arr2tuple(arr):
    return tuple(map(tuple, arr))
