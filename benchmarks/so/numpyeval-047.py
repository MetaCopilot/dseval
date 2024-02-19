'''
### Prompt ###

import numpy as np

a = np.array([1,2,3,4,5,6])
b = np.array([2,3,5])

# Perform a symmetric difference between two numpy arrays.
# Don't convert the numpy array to a set to perform exclusive-or. Use setxor1d directly.
diff_arr =

### Solution ###

 np.setxor1d(a, b)

### Test ###

def check():
    assert np.array_equal(diff_arr, np.array([1, 4, 6]))
'''

# %%
import numpy as np

a = np.array([1,2,3,4,5,6])
b = np.array([2,3,5])

# %%
"""
question: Perform a symmetric difference between two numpy arrays. Don't convert the numpy array to a set to perform exclusive-or. Use setxor1d directly.
"""

np.setxor1d(a, b)
