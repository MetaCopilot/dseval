'''
### Prompt ###

import numpy as np

data = np.array([1,2,3,4,5,6,7,8,9])
# How to remove specific elements in a numpy array？
# I then want to remove 3,4,7 from a. All I know is the index of the values (index=[2,3,6]).
index = [2, 3, 6]
result =

### Solution ###

np.delete(data, index)

### Test ###

def check():
    assert np.array_equal(result, np.array([1, 2, 5, 6, 8, 9]))
'''

# %%
import numpy as np

data = np.array([1,2,3,4,5,6,7,8,9])

# %%
"""
question: |
  How to remove specific elements in a numpy array？
  I then want to remove 3,4,7 from a. All I know is the index of the values (index=[2,3,6]).
"""

index = [2, 3, 6]
np.delete(data, index)
