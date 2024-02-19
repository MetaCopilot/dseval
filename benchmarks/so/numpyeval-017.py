'''
### Prompt ###

import numpy as np

a = np.array([np.array([13.16]), np.array([1.58 , 1.2]), np.array([13.1]), np.array([1. , 2.6])], dtype=object)
# I need a general way to flatten that array into a single array of N elements, with N=every float in all the sub-arrays.

out =

### Solution ###

 np.hstack(aa)

### Test ###

def check():
    assert np.array_equal(out, np.array([13.16, 1.58, 1.2, 13.1, 1. , 2.6]))
'''

# %%
import numpy as np

a = np.array([np.array([13.16]), np.array([1.58 , 1.2]), np.array([13.1]), np.array([1. , 2.6])], dtype=object)

# %%
"""
question: |
  I need a general way to flatten that array into a single array of N elements, with N=every float in all the sub-arrays.
"""

np.hstack(a)
