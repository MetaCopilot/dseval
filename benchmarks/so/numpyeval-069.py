'''
### Prompt ###

import numpy as np

A = np.array([[1, 2], [3, 0]])

# How can I know the (row, column) index of the minimum of a numpy array/matrix?
# Use unravel_index()
out =

### Solution ###

 np.unravel_index(A.argmin(), A.shape)

### Test ###

def check():
    assert out == (1, 1)
'''

# %%
import numpy as np

A = np.array([[1, 2], [3, 0]])

# %%
"""
question: |
  How can I know the (row, column) index of the minimum of a numpy array/matrix?
  Use unravel_index().
"""

np.unravel_index(A.argmin(), A.shape)
