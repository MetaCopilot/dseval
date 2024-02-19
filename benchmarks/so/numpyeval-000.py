'''
### Prompt ###

import numpy as np

a = np.array([1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 3, 4, 3, 4, 3, 4, 5, 5, 5])
# Is there an efficient numpy way to find each index where the value changes? 
# You can get this functionality in numpy by comparing each element with it's neighbor
# and then using np.where(condition).
result =

### Solution ###

 np.where(a[1:] != a[:-1])[0]

### Test ###

def check():
    assert np.array_equal(result, np.array([4, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
'''

# %%
import numpy as np

a = np.array([1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 3, 4, 3, 4, 5, 5, 5])

# %%
"""
question: |
  Is there an efficient numpy way to find each index where the value changes? 
  You can get this functionality in numpy by comparing each element with it's neighbor
  and then using np.where(condition).
"""

np.where(a[1:] != a[:-1])[0] + 1
