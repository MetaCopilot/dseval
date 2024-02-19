'''
### Prompt ###

import numpy as np

A = np.array([1, 7, 9, 2, 0.1, 17, 17, 1.5])
k = 3

# Find the index of the k smallest values of a numpy array
idx =

### Solution ###

np.argpartition(A, k)[:k]

### Test ###

def check():
    assert np.array_equal(idx, np.array([4, 0, 7]))
'''

# %%
import numpy as np

A = np.array([1, 7, 9, 2, 0.1, 17, 17, 1.5])
k = 3

# %%
"""
question: |
  Find the index of the k smallest values of a numpy array
"""

np.argpartition(A, k)[:k]
