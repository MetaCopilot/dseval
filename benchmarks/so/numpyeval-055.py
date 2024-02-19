'''
### Prompt ###

import numpy as np

a = np.array([1, 2, 3, -4, 5])
# Is there a simple way of replacing all negative values in an array with `0`?
# using a NumPy function `where` to solve it.
result =

### Solution ###

np.where(a < 0, 0, a)

### Test ###

def check():
    assert np.array_equal(result, np.where(a < 0, 0, a))
'''

# %%
import numpy as np

a = np.array([1, 2, 3, -4, 5])

# %%
"""
question: |
  Is there a simple way of replacing all negative values in an array with `0`?
  using a NumPy function `where` to solve it.
"""

np.where(a < 0, 0, a)
