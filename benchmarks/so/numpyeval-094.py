'''
### Prompt ###

import numpy as np

arr = np.array([[ 1.41421356, 0.70710678, 0.70710678], [0., 1.22474487,1.22474487], [0., 0., 0.]])
# remove zero rows 2-D numpy array
# Use np.all with an axis argument:
new_arr =

### Solution ###

 arr[~np.all(arr == 0, axis=1)]

### Test ###

def check():
    assert np.array_equal(new_arr, np.array([[ 1.41421356, 0.70710678, 0.70710678], [0., 1.22474487,1.22474487]]))
'''

# %%
import numpy as np

arr = np.array([[ 1.41421356, 0.70710678, 0.70710678], [0., 1.22474487,1.22474487], [0., 0., 0.]])

# %%
"""
question: |
  Remove zero rows from a 2-D numpy array.
  Use np.all with an axis argument.
"""

arr[~np.all(arr == 0, axis=1)]
