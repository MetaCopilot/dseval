'''
### Prompt ###

import numpy as np

a = np.array([1,3,4])
b = np.array([5,2,1])

# I have two simple one-dimensional arrays in NumPy. 
# I should be able to concatenate them using numpy.concatenate.
c =

### Solution ###

 np.concatenate([a, b])

### Test ###

def check():
    assert np.array_equal(c, np.concatenate((a, b)))
'''

# %%
import numpy as np

a = np.array([1,3,4])
b = np.array([5,2,1])

# %%
"""
question: |
  I have two simple one-dimensional arrays in NumPy. 
  I should be able to concatenate them using numpy.concatenate.
"""

np.concatenate([a, b])
