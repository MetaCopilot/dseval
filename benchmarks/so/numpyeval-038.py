'''
### Prompt ###

import numpy as np

# I have a list containing numpy arrays something like L=[a,b,c] where a, b and c are numpy arrays with sizes N_a in T, N_b in T and N_c in T.
# I want to row-wise concatenate a, b and c and get a numpy array with shape (N_a+N_b+N_c, T). 
# Clearly one solution is run a for loop and use numpy.concatenate, but is there any pythonic way to do this?
a = np.ones((3,2))
b = np.zeros((2,2))
c = np.ones((4,2))
L = [a,b,c]
concated_arr =

### Solution ###

 np.concatenate(L, axis=0)

### Test ###

def check():
    assert np.array_equal(concated_arr, np.concatenate(L, axis=0))
'''

# %%
import numpy as np

a = np.ones((3,2))
b = np.zeros((2,2))
c = np.ones((4,2))
L = [a,b,c]

# %%
"""
question: |
  I have a list containing numpy arrays something like L=[a,b,c] where a, b and c are numpy arrays with sizes N_a in T, N_b in T and N_c in T.
  I want to row-wise concatenate a, b and c and get a numpy array with shape (N_a+N_b+N_c, T). 
  Clearly one solution is run a for loop and use numpy.concatenate, but is there any pythonic way to do this?
"""

np.concatenate(L, axis=0)
