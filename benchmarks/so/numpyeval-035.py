'''
### Prompt ###

import numpy as np

# create a numpy array composed of a list [[8, 7, 2], [5, 6, 1], [8, 2, 6]]
array =

### Solution ###

np.array([[8, 7, 2], [5, 6, 1], [8, 2, 6]])

### Test ###

def check():
    assert np.array_equal(array, np.array([[8, 7, 2], [5, 6, 1], [8, 2, 6]]))
    assert type(array) == np.ndarray
'''

# %%

import numpy as np

# %%

"""
question: |
  Create a numpy array composed of a list [[8, 7, 2], [5, 6, 1], [8, 2, 6]]. Save it to array.

validator:
  namespace_check:
    array:
"""

array = np.array([[8, 7, 2], [5, 6, 1], [8, 2, 6]])
