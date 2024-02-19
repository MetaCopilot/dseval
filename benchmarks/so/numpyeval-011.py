'''
### Prompt ###

import numpy as np

input_list = [np.array([[ 0.00353654]]), np.array([[ 0.00353654]]), np.array([[ 0.00353654]]), np.array([[ 0.00353654]]), np.array([[ 0.00353654]]), np.array([[ 0.00353654]]), np.array([[ 0.00353654]]), np.array([[ 0.00353654]])]
# Flattening a list of NumPy arrays?
# We can use numpy.concatenate, which as the name suggests, basically concatenates all the elements of such an input list into a single NumPy array
# And then we can use numpy.ravel to flatten the array
output =

### Solution ###

np.concatenate(input_list).ravel()

### Test ###

def check():
    assert np.array_equal(output, np.concatenate(input_list).ravel())
'''

# %%
import numpy as np

input_list = [np.array([[ 0.00353654]]), np.array([[ 0.00353654]]), np.array([[ 0.00353654]]), np.array([[ 0.00353654]]), np.array([[ 0.00353654]]), np.array([[ 0.00353654]]), np.array([[ 0.00353654]]), np.array([[ 0.00353654]])]

# %%
"""
question: |
  Flattening a list of NumPy arrays?
  We can use numpy.concatenate, which as the name suggests, basically concatenates all the elements of such an input list into a single NumPy array
  And then we can use numpy.ravel to flatten the array
"""

np.concatenate(input_list).ravel()
