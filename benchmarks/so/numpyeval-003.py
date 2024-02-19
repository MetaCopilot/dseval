'''
### Prompt ###

import numpy as np

def convert_string_in_array_to_float(arr):
    # How to convert an array of strings to an array of floats in numpy?
    # Return the final result

### Solution ###

    return arr.astype(np.float)

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array(['1.0', '2.0', '3.0'])), np.array([1.0, 2.0, 3.0]))
    assert np.array_equal(candidate(np.array(['1.0', '3.0', '3.0'])), np.array([1.0, 3.0, 3.0]))
    assert np.array_equal(candidate(np.array(['1.0', '2.0', '4.0'])), np.array([1.0, 2.0, 4.0]))
    assert np.array_equal(candidate(np.array(['1.0', '2.0', '6.0'])), np.array([1.0, 2.0, 6.0]))
    assert np.array_equal(candidate(np.array(['3.0', '2.0', '3.0'])), np.array([3.0, 2.0, 3.0]))
    assert np.array_equal(candidate(np.array(['1.0', '3.0', '3.0'])), np.array([1.0, 3.0, 3.0]))
    assert np.array_equal(candidate(np.array(['13.0', '2.0', '3.0'])), np.array([13.0, 2.0, 3.0]))
    assert np.array_equal(candidate(np.array(['133.0', '23.0', '3.0'])), np.array([133.0, 23.0, 3.0]))
    assert np.array_equal(candidate(np.array(['1.0', '2.0', '343.0'])), np.array([1.0, 2.0, 343.0]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def convert_string_in_array_to_float(arr):` that takes a numpy array and returns a numpy array to solve the following problem:
  How to convert an array of strings to an array of floats in numpy?

validator:
  table_test:
    function_name: convert_string_in_array_to_float
    test_cases:
    - ["`np.array(['1.0', '2.0', '3.0'])`"]
    - ["`np.array(['1.0', '3.0', '3.0'])`"]
    - ["`np.array(['1.0', '2.0', '4.0'])`"]
    - ["`np.array(['1.0', '2.0', '6.0'])`"]
    - ["`np.array(['3.0', '2.0', '3.0'])`"]
    - ["`np.array(['1.0', '3.0', '3.0'])`"]
    - ["`np.array(['13.0', '2.0', '3.0'])`"]
    - ["`np.array(['133.0', '23.0', '3.0'])`"]
    - ["`np.array(['1.0', '2.0', '343.0'])`"]
"""

def convert_string_in_array_to_float(arr):
    return arr.astype(np.float32)
