'''
### Prompt ###

import numpy as np

a = np.arange(1, 10)
a = a.reshape(len(a), 1)
# I want to access the elements from index 4 to the end:
b =

### Solution ###

 a[4:]

### Test ###

def check():
    assert np.array_equal(b, a[4:])
'''

# %%
import numpy as np

a = np.arange(1, 10)
a = a.reshape(len(a), 1)

# %%
"""
question: |
  I want to access the elements from index 4 to the end of the numpy array `a`.
"""

a[4:]
