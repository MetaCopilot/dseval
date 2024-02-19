'''
### Prompt ###

import numpy as np

# List of arrays.
L = [np.random.randn(5,4,2,5,1,2) for i in range(10)]
# Stack them using axis that is negative one .
M =

### Solution ###

np.stack(L, axis=-1)

### Test ###

def check():
    assert np.array_equal(M, np.stack(L, axis=-1))
'''

# %%
import numpy as np

# List of arrays.
L = [np.random.randn(5,4,2,5,1,2) for i in range(10)]

# %%
"""
question: |
  Stack the list of arrays `L` using axis that is negative one.
"""

np.stack(L, axis=-1)
