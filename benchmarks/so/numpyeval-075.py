'''
### Prompt ###

import numpy as np

x=np.array([range(100,1,-1)])
#This will tell me those values
# generate a mask to find all values that are even numbers
# Is there an efficient Numpy mechanism to retrieve the integer indexes of locations in an array based on a condition is true as opposed to the Boolean mask array?
out =

### Solution ###

 np.where(x % 2 == 0)

### Test ###

def check():
    assert np.array_equal(out[1], np.where(x % 2 == 0)[1])
'''

# %%
import numpy as np

x=np.array([range(100,1,-1)])

# %%
"""
question: |
  generate a mask to find all values that are even numbers
  Is there an efficient Numpy mechanism to retrieve the integer indexes of locations in an array based on a condition is true as opposed to the Boolean mask array?
"""

np.where(x % 2 == 0)
