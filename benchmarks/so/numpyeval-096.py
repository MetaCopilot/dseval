'''
### Prompt ###

import numpy as np

# How do I create a numpy array of arbitrary shape 3x4 filled with all True?
data =

### Solution ###

 np.ones((3, 4), dtype=bool)

### Test ###

def check():
    assert np.array_equal(data, np.ones((3, 4), dtype=bool))
'''

# %%

import numpy as np

# %%

"""
question: |
  How do I create a numpy array of arbitrary shape 3x4 filled with all True?
  Put the created array in the variable data.

validator:
  namespace_check:
    data:
"""

data = np.ones((3, 4), dtype=bool)
