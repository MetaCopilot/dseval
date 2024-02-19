'''
### Prompt ###

import numpy as np

a = np.array([1,2,3,4,5])
# I have a numpy array and I like to check if it is sorted.
# Using numpy.all to do this.
is_sorted =

### Solution ###

 np.all(a[:-1] <= a[1:])

### Test ###

def check():
    assert is_sorted == True
'''

# %%
import numpy as np

a = np.array([1,2,3,4,5])

# %%

"""
question: |
  I have a numpy array and I like to check if it is sorted.
  Using numpy.all to do this.
"""

np.all(a[:-1] <= a[1:])
