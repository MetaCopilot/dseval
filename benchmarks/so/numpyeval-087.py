'''
### Prompt ###

import numpy as np

a = np.array([[1,1,0],[1,0,0],[1,0,0],[1,1,0]])
# I want to check if all values in the columns of a numpy array/matrix are the same.
# A column shares a common value if all the values in that column are True:
# The below code checks if all values in the columns are the same using a == a[0,:] and axis=0
result =

### Solution ###

 np.all(a == a[0,:], axis = 0)

### Test ###

def check():
    assert np.array_equal(result, np.array([True, False, True]))
'''

# %%
import numpy as np

a = np.array([[1,1,0],[1,0,0],[1,0,0],[1,1,0]])

# %%
"""
question: |
  I want to check if all values in the columns of a numpy array/matrix are the same.
  A column shares a common value if all the values in that column are True:
  The below code checks if all values in the columns are the same using a == a[0,:] and axis=0
"""

np.all(a == a[0,:], axis = 0)
