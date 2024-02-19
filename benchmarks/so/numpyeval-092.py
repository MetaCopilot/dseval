'''
### Prompt ###

import numpy as np

a = np.matrix([[ 0.16666667, 0.66666667, 0.16666667]])
# how can I make a python list obj from this matrix?
# # the list should be one dimensional and contain all values of the matrix
a_list =

### Solution ###

 list(np.array(a).reshape(-1,))

### Test ###

def check():
    assert a_list == [0.16666667, 0.66666667, 0.16666667]
'''

# %%
import numpy as np

a = np.matrix([[ 0.16666667, 0.66666667, 0.16666667]])

# %%
"""
question: |
  How can I make a python list obj from this matrix?
  The list should be one dimensional and contain all values of the matrix.
"""

list(np.array(a).reshape(-1,))
