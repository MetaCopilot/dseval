'''
### Prompt ###

import numpy as np
from numpy import newaxis

a = np.array([
     [1,2],
     [3,4],
     [5,6],
     [7,8]])

b = np.array([1,2,3,4])

# multiply arrays rowwise
# Basically out[i] = a[i] * b[i], where a[i].shape is (2,) and b[i] then is a scalar.
# What's the trick?
out =

### Solution ###

 a * b[:, newaxis]

### Test ###

def check():
    assert np.array_equal(out, a * b[:, newaxis])
'''

# %%
import numpy as np
from numpy import newaxis

a = np.array([
     [1,2],
     [3,4],
     [5,6],
     [7,8]])

b = np.array([1,2,3,4])

# %%
"""
question: |
  Multiply arrays rowwise.
  Basically out[i] = a[i] * b[i], where a[i].shape is (2,) and b[i] then is a scalar.
  What's the trick?

"""

a * b[:, newaxis]
