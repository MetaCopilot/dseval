'''
### Prompt ###

import numpy as np

def prepend_element_to_array(arr, element):
    # Prepend element to numpy array
    # Return the array

### Solution ###

    return np.insert(arr, 0, element)

### Test ###

def check(candidate):
    assert np.array_equal(candidate(np.array([[5.], [4.], [3.], [2.], [1.]]), 0), np.array([0, 5., 4., 3., 2., 1.]))
    assert np.array_equal(candidate(np.array([[5.], [4.], [3.], [2.], [3.]]), 0), np.array([0, 5., 4., 3., 2., 3.]))
    assert np.array_equal(candidate(np.array([[5.], [4.], [3.], [3.], [3.]]), 0), np.array([0, 5., 4., 3., 3., 3.]))
    assert np.array_equal(candidate(np.array([[5.], [5.], [3.], [2.], [3.]]), 0), np.array([0, 5., 5., 3., 2., 3.]))
    assert np.array_equal(candidate(np.array([[1.], [4.], [3.], [2.], [3.]]), 0), np.array([0, 1., 4., 3., 2., 3.]))
    assert np.array_equal(candidate(np.array([[5.], [4.], [33.], [2.], [3.]]), 0), np.array([0, 5., 4., 33., 2., 3.]))
    assert np.array_equal(candidate(np.array([[5.], [4.], [3.], [23.], [3.]]), 0), np.array([0, 5., 4., 3., 23., 3.]))
    assert np.array_equal(candidate(np.array([[5.], [4.], [3.], [21.], [3.]]), 0), np.array([0, 5., 4., 3., 21., 3.]))
    assert np.array_equal(candidate(np.array([[5.], [4.], [3.], [2.], [34.]]), 0), np.array([0, 5., 4., 3., 2., 34.]))
    assert np.array_equal(candidate(np.array([[54.], [4.], [3.], [2.], [3.]]), 0), np.array([0, 54., 4., 3., 2., 3.]))
'''

# %%
import numpy as np

# %%

"""
question: |
  Write a function `def prepend_element_to_array(arr, element):` that takes a numpy array and an element and returns a numpy array to solve the following problem:
  Prepend element to numpy array

validator:
  table_test:
    function_name: prepend_element_to_array
    test_cases:
    - ["`np.array([[5.], [4.], [3.], [2.], [1.]])`", 0]
    - ["`np.array([[5.], [4.], [3.], [2.], [3.]])`", 0]
    - ["`np.array([[5.], [4.], [3.], [3.], [3.]])`", 0]
    - ["`np.array([[5.], [5.], [3.], [2.], [3.]])`", 0]
    - ["`np.array([[1.], [4.], [3.], [2.], [3.]])`", 0]
    - ["`np.array([[5.], [4.], [33.], [2.], [3.]])`", 0]
    - ["`np.array([[5.], [4.], [3.], [23.], [3.]])`", 0]
    - ["`np.array([[5.], [4.], [3.], [21.], [3.]])`", 0]
    - ["`np.array([[5.], [4.], [3.], [2.], [34.]])`", 0]
    - ["`np.array([[54.], [4.], [3.], [2.], [3.]])`", 0]
"""

def prepend_element_to_array(arr, element):
    return np.insert(arr, 0, element)
