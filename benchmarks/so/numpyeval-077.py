'''
### Prompt ###

import numpy as np

z = np.array([ 0, 1, 3, 9, 18 ])
# What is the inverse of the numpy cumsum function?
z[1:] =

### Solution ###

 z[:-1]

### Test ###

def check():
    assert np.array_equal(z, [ 0, 0, 1, 3, 9 ])
'''

# %%
import numpy as np

z = np.array([ 0, 1, 3, 9, 18 ])

# %%
"""
question: |
  What is the inverse of the numpy cumsum function?
  Do the inverse of the cumsum function on `z` and assign it to `z[1:]`.

validator:
  namespace_check:
    z:
"""

z[1:] = np.diff(z)
