'''
### Prompt ###

import numpy as np

a = np.arange(12).reshape(3,4)
# Removing columns with index 1 and 3 in numpy
# If you ever want to delete more than one columns, you just pass indices of columns you want deleted as a list to np.delete, like this:
out =

### Solution ###

 np.delete(a, [1, 3], axis=1)

### Test ###

def check():
    assert np.array_equal(out, np.array([[0, 2], [4, 6], [8, 10]]))
'''

# %%
import numpy as np

a = np.arange(12).reshape(3,4)

# %%
"""
question: |
  Removing columns with index 1 and 3 in numpy
  If you ever want to delete more than one columns, you just pass indices of columns you want deleted as a list to np.delete, like this:
"""

np.delete(a, [1, 3], axis=1)
