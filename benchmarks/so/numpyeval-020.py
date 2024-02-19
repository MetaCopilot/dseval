'''
### Prompt ###

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Convert a numpy.ndarray to string
# and convert it back to numpy.ndarray with dtype=int
ts = arr.tostring()
new_arr =

### Solution ###

 np.fromstring(ts, dtype=int)

### Test ###

def check():
    assert np.array_equal(new_arr, np.array([1, 2, 3, 4, 5, 6]))
'''

# %%
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# %%
"""
question: |
  Convert a numpy.ndarray to string `ts`
  and convert it back to numpy.ndarray with dtype=int

validator:
  namespace_check:
    ts:
"""

ts = arr.tostring()
np.fromstring(ts, dtype=int)
