'''
### Prompt ###

import numpy as np

a = np.array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11],
       [12, 13, 14]])

# We want row with the first column value is 0
# and the second colum value is 1
# Maybe using np.where() is better
b =

### Solution ###

 a[np.where((a[:,0] == 0) * (a[:,1] == 1))]

### Test ###

def check():
    assert np.array_equal(b, np.array([[0, 1, 2]]))
'''

# %%
import numpy as np

a = np.array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11],
       [12, 13, 14]])

# %%
"""
question: |
  We want row with the first column value is 0
  and the second colum value is 1
  Maybe using np.where() is better
"""

a[np.where((a[:,0] == 0) * (a[:,1] == 1))]
