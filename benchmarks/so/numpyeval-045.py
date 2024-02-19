'''
### Prompt ###

import numpy as np

a = np.array([[1,3,4],[1,2,3],[1,2,1]])
b = np.array([1,2,3])
# How to add items into a numpy array?
# add one element to each row using column stack operation.
c =

### Solution ###

 np.column_stack((a, b))

### Test ###

def check():
    assert np.array_equal(c, np.column_stack((a, b)))
'''

# %%
import numpy as np

a = np.array([[1,3,4],[1,2,3],[1,2,1]])
b = np.array([1,2,3])

# %%
"""
question: |
  How to add items into a numpy array?
  add one element to each row using column stack operation.
"""

np.column_stack((a, b))
