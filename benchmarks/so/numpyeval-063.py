'''
### Prompt ###

import numpy as np

A = np.array([1,2,3,4,5,6,7])
B = np.array([2,4,6])
C = np.searchsorted(A, B)
# Check if each element in a numpy array is in another array
# This problem seems easy but I cannot quite get a nice-looking solution. 
# I have two numpy arrays (A and B), and I want to get the indices of A where the elements of A are in B and also get the indices of A where the elements are not in B.
D =

### Solution ###

 np.delete(np.arange(np.alen(A)), C)

### Test ###

def check():
    assert np.array_equal(D, np.array([0, 2, 4, 6]))
'''

# %%
import numpy as np

A = np.array([1,2,3,4,5,6,7])
B = np.array([2,4,6])

# %%
"""
question: |
  Check if each element in a numpy array is in another array
  This problem seems easy but I cannot quite get a nice-looking solution. 
  I have two numpy arrays (A and B), and I want to get the indices of A where the elements are not in B.
"""

C = np.searchsorted(A, B)
np.delete(np.arange(len(A)), C)
