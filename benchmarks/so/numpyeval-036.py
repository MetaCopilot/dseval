'''
### Prompt ###

import numpy as np

# I have a NumPy array that looks like this:
arr = np.array([100.10, 200.42, 4.14, 89.00, 34.55, 1.12])
# How can I get multiple values from this array by index?
# How can I get the values at the index positions 1 and 4?
result_arr =

### Solution ###

 arr[[1, 4]]

### Test ###

def check():
    assert np.array_equal(result_arr,np.array([200.42, 34.55]))
'''

# %%
import numpy as np

arr = np.array([100.10, 200.42, 4.14, 89.00, 34.55, 1.12])

# %%
"""
question: |
  How can I get multiple values from this array by index?
  How can I get the values at the index positions 1 and 4?
"""

arr[[1, 4]]
