'''
### Prompt ###

import numpy as np

a = np.array([[2,3,2],[5,6,1]])
b = np.array([3,5])
# How to multiply a nD array with 1D array, where len(1D-array) == len(nD array)?
# You need to convert array b to a (2, 1) shape array, use None or numpy.newaxis in the index tuple:
c =

### Solution ###

 a * b[:, np.newaxis]

### Test ###

def check():
    assert np.array_equal(c, np.array([[6, 9, 6], [25, 30, 5]]))
'''

# %%
import numpy as np

a = np.array([[2,3,2],[5,6,1]])
b = np.array([3,5])

# %%
"""
question: |
  How to multiply a nD array with 1D array, where len(1D-array) == len(nD array)?
  You need to convert array b to a (2, 1) shape array, use None or numpy.newaxis in the index tuple:
"""

a * b[:, np.newaxis]
