'''
### Prompt ###

import numpy as np

# I have a 2D numpy array of shape (N,2) which is holding N points.
a = np.array([(3, 2), (6, 2), (3, 6), (3, 4), (5, 3)])
# Sorting it such that my points are ordered by x-coordinate, and then by y in cases where the x coordinate is the same, and get the values by inplace
ind =

### Solution ###

 np.lexsort((a[:, 0], a[:, 1]))
a = a[ind]

### Test ###

def check():
    assert np.array_equal(a, np.array([(3, 2), (6, 2), (5, 3), (3, 4), (3, 6)]))
'''

# %%
import numpy as np

a = np.array([(3, 2), (6, 2), (3, 6), (3, 4), (5, 3)])

# %%
"""
question: |
  I have a 2D numpy array of shape (N,2) which is holding N points.
  Sorting it such that my points are ordered by x-coordinate, and then by y in cases where the x coordinate is the same, and get the values by inplace
  Modify the numpy array `a` in-place.

validator:
  namespace_check:
    a:
"""

ind = np.lexsort((a[:, 0], a[:, 1]))
a = a[ind]
