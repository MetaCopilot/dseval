'''
### Prompt ###

import numpy as np

a = np.array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.],
       [ 0.,  0.,  0.],
       [ 0.,  0.,  0.],
       [ 0.,  0.,  0.]])
x = np.ones(5)
# Assigning array x to the 2th column of array a.

### Solution ###

a[:, 1] = x

### Test ###

def check():
    assert np.array_equal(a, np.array([[ 0.,  1.,  0.],[ 0.,  1.,  0.],[ 0.,  1.,  0.],[ 0.,  1.,  0.],[ 0.,  1.,  0.]]))
'''

# %%
import numpy as np

a = np.array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.],
       [ 0.,  0.,  0.],
       [ 0.,  0.,  0.],
       [ 0.,  0.,  0.]])
x = np.ones(5)

# %%
"""
question: |
  Assign array x to the 2th column of array a.
  Modify the array `a` in-place.

validator:
  namespace_check:
    a:
"""

a[:, 1] = x
