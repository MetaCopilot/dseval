'''
### Prompt ###

import numpy as np

a = np.array([[1, 1, 1, 0, 0, 0],
       [0, 1, 1, 1, 0, 0],
       [0, 1, 1, 1, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1, 0]])
# I need to find unique rows in a numpy.array.
out =

### Solution ###

 np.unique(a, axis=0)

### Test ###

def check():
    assert np.array_equal(out, np.unique(a, axis=0))
'''

# %%
import numpy as np

a = np.array([[1, 1, 1, 0, 0, 0],
       [0, 1, 1, 1, 0, 0],
       [0, 1, 1, 1, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1, 0]])

# %%
"""
question: I need to find unique rows in a numpy.array.
"""

np.unique(a, axis=0)
