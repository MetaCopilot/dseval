'''
### Prompt ###

import numpy as np

a = np.array([[1,11], [3,9], [5,7]])
# Firstly, We need to find the minimun value of each column with axis 0,
# Then conduct subtract operation between each element of the column and the minimum value.
result =

### Solution ###

 a - a.min(axis=0)

### Test ###

def check():
    assert np.array_equal(result, a - a.min(axis=0))
'''

# %%
import numpy as np

a = np.array([[1,11], [3,9], [5,7]])

# %%
"""
question: |
  Firstly, We need to find the minimun value of each column with axis 0,
  Then conduct subtract operation between each element of the column and the minimum value.
"""

a - a.min(axis=0)
