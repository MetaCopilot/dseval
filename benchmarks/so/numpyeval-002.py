'''
### Prompt ###

import numpy as np

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
# How to get the cumulative distribution function with NumPy?
# set bins to 10
# and then generate a cumulative sum of the histogram contents to variable hist self
hist, bin_edges =

### Solution ###

 np.histogram(arr, bins=10)
hist = hist.cumsum()

### Test ###

def check():
    assert np.array_equal(hist, np.array([1, 2, 3, 4, 4, 5, 6, 7, 8, 9]))
'''

# %%
import numpy as np

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])

# %%
"""
question: |
  How to get the cumulative distribution function with NumPy?
  set bins to 10
  and then generate a cumulative sum of the histogram contents to a variable `hist`

validator:
  namespace_check:
    hist:
"""

hist, bin_edges = np.histogram(arr, bins=10)
hist = hist.cumsum()
