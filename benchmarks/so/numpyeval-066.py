'''
### Prompt ###

import numpy as np

a = np.array([ 0,  3,  6,  9, 12])
b = np.array([ 1,  4,  7, 10, 13])
c = np.array([ 2,  5,  8, 11, 14])

# How can I join them using numpy methods
# You can transpose and flatten the arrays:
d =

### Solution ###

 np.array([a, b, c]).T.flatten()

### Test ###

def check():
    assert np.array_equal(d, np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]))
'''

# %%
import numpy as np

a = np.array([ 0,  3,  6,  9, 12])
b = np.array([ 1,  4,  7, 10, 13])
c = np.array([ 2,  5,  8, 11, 14])

# %%
"""
question: |
  How can I join them using numpy methods
  You can transpose and flatten the arrays:
"""

np.array([a, b, c]).T.flatten()
