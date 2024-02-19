'''
### Prompt ###

import numpy as np
from numpy import newaxis

a = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
# I have a 2d array with shape (x, y) which I want to convert to a 3d array with shape (x, y, 1).
# Is there a nice Pythonic way to do this?
b =

### Solution ###

 a[:, :, newaxis]

### Test ###

def check():
    assert np.array_equal(b, np.array([[[1], [2], [3]], [[3], [4], [5]], [[5], [6], [7]]]))
'''

# %%
import numpy as np
from numpy import newaxis

a = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])

# %%
"""
question: |
  I have a 2d array with shape (x, y) which I want to convert to a 3d array with shape (x, y, 1).
  Is there a nice Pythonic way to do this?
"""

a[:, :, newaxis]
