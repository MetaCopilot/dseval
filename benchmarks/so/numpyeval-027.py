'''
### Prompt ###

import numpy as np

arr = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
# How to invoke the standard deviation function on a 2d array?
# with axis=0, it will return a 1d array with the standard deviation of each column
arr_sd =

### Solution ###

 np.std(arr, axis=0)

### Test ###

def check():
    assert np.array_equal(arr_sd, np.std(arr, axis=0))
'''

# %%
import numpy as np

arr = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])

# %%
"""
question: |
  How to invoke the standard deviation function on a 2d array?
  with axis=0, it will return a 1d array with the standard deviation of each column

"""

np.std(arr, axis=0)
