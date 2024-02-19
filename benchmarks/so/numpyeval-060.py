'''
### Prompt ###

import numpy as np
x = np.array([[0, 1], [3, 2]])
# Return the indices of the minimum values along (axis is zero).
out =

### Solution ###

 np.argmin(x, axis=0)

### Test ###

def check():
    assert np.array_equal(out, np.array([0, 0]))
'''

# %%
import numpy as np
x = np.array([[0, 1], [3, 2]])

# %%

"""
question: |
  Return the indices of the minimum values along (axis is zero).
"""

np.argmin(x, axis=0)
