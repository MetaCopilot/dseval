'''
### Prompt ###

import numpy as np

a = np.array([1,2,3,4,5,6])
b = np.array([1,4,5])

# Is there a way to compare what elements in a exist in b?
# Return a array of booleans, True if elements in a exist in b, False otherwise
c =

### Solution ###

 np.in1d(a,b)

### Test ###

def check():
    assert np.array_equal(c, np.array([True, False, False, True, True, False]))
'''

# %%
import numpy as np

a = np.array([1,2,3,4,5,6])
b = np.array([1,4,5])

# %%
"""
question: |
  Is there a way to compare what elements in a exist in b?
  Return a array of booleans, True if elements in a exist in b, False otherwise
"""

np.in1d(a,b)
