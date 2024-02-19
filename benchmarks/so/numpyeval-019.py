'''
### Prompt ###

import numpy as np

# How do I create an array where every entry is the same value?
# I know numpy.ones() and numpy.zeros() do this for 1's and 0's, but what about -1?
# the shape of the array is (5, 5)
out =

### Solution ###

 np.full((5, 5), -1.)

### Test ###

def check():
    assert np.array_equal(out, np.full((5, 5), -1.))
'''

# %%

import numpy as np

# %%

"""
question: |
  How do I create an array where every entry is the same value?
  I know numpy.ones() and numpy.zeros() do this for 1's and 0's, but what about -1?
  the shape of the array is (5, 5)
"""

np.full((5, 5), -1.)
