'''
### Prompt ###

import numpy as np

m = np.arange(2*3*5).reshape((2,3,5))
axis, start, end = 2, 1, 3
target = m[:, :, 1:3]
slc = [slice(None)] * len(m.shape)
# I would like to dynamically slice a numpy array along a specific axis.
# I think one way would be to use slice(start, end):

### Solution ###

slc[axis] = slice(start, end)

### Test ###

def check():
    assert slc == [slice(None, None, None), slice(None, None, None), slice(1, 3, None)]
'''

# %%
import numpy as np

m = np.arange(2*3*5).reshape((2,3,5))
axis, start, end = 2, 1, 3
target = m[:, :, 1:3]
slc = [slice(None)] * len(m.shape)

# %%
"""
question: |
  I would like to dynamically slice a numpy array along a specific axis.
  I think one way would be to use slice(start, end). Save the slice in the list `slc`.

validator:
  namespace_check:
    slc:
"""

slc[axis] = slice(start, end)
