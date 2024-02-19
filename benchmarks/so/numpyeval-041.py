'''
### Prompt ###

import numpy as np

a = np.arange(9)
a = a.reshape((3, 3))
b = np.zeros((5, 5))
# Copy numpy array 'a' into part of another array 'b' in [1:4, 1:4]

### Solution ###

b[1:4, 1:4] = a

### Test ###

def check():
    tmp_b = np.zeros((5, 5))
    tmp_b[1:4, 1:4] = a
    assert np.array_equal(b, tmp_b)
'''

# %%
import numpy as np

a = np.arange(9)
a = a.reshape((3, 3))
b = np.zeros((5, 5))

# %%
"""
question: |
  Copy numpy array 'a' into part of another array 'b' in [1:4, 1:4]
  Modify the array `b` in-place.

validator:
  namespace_check:
    b:
"""

b[1:4, 1:4] = a
