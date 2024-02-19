'''
### Prompt ###

import numpy as np

dists = np.array([[5,1,2], [2,8,1], [1,6,3], [5,2,2], [5,1,2], [3,1,2]])
r, dr = 2, 3
# I have an array of distances called dists. I want to select dists which are within a range [r, r+dr].
# You don't actually need where if you're just trying to filter out the elements of dists that don't fit your criteria:
out =

### Solution ###

 dists[np.where(np.logical_and(dists >= r, dists <= r+dr))]

### Test ###

def check():
    assert np.array_equal(out, np.array([5, 2, 2, 3, 5, 2, 2, 5, 2, 3, 2]))
'''

# %%
import numpy as np

dists = np.array([[5,1,2], [2,8,1], [1,6,3], [5,2,2], [5,1,2], [3,1,2]])
r, dr = 2, 3

# %%
"""
question: |
  I have an array of distances called dists. I want to select dists which are within a range [r, r+dr].
  You don't actually need where if you're just trying to filter out the elements of dists that don't fit your criteria.
"""

dists[np.where(np.logical_and(dists >= r, dists <= r+dr))]
