'''
### Prompt ###

import numpy as np

master = np.array([1,2,3,4,5])
search = np.array([4,2,2,3])

# Find indices of a list of values in a numpy array
out =

### Solution ###

 np.searchsorted(master, search)

### Test ###

def check():
    assert np.array_equal(out, np.array([3, 1, 1, 2]))
'''

# %%
import numpy as np

master = np.array([1,2,3,4,5])
search = np.array([4,2,2,3])

# %%
"""
question: Find indices of a list of values in a numpy array
"""

np.searchsorted(master, search)
