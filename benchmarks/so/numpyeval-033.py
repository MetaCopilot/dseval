'''
### Prompt ###

import numpy as np

arr = np.zeros((50,100,25))
# Is there a quick way to "sub-flatten" or flatten only some of the first dimensions in a numpy array?
# Given a numpy array of dimensions (50,100,25), the resultant dimensions would be (5000,25)
result =

### Solution ###

np.reshape(arr, (5000,25))

### Test ###

def check():
    assert np.array_equal(result, np.reshape(arr, (5000,25)))
'''

# %%
import numpy as np

arr = np.zeros((50,100,25))

# %%

"""
question: |
  Is there a quick way to "sub-flatten" or flatten only some of the first dimensions in a numpy array?
  Given a numpy array of dimensions (50,100,25), the resultant dimensions would be (5000,25)
"""

np.reshape(arr, (5000,25))
