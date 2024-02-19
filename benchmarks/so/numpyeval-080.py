'''
### Prompt ###

import numpy as np

x = np.arange(8.0)
# Partition array into 3 chunks with Numpy
result =

### Solution ###

np.array_split(x, 3)

### Test ###

def check():
    assert np.array_equal(result[0], np.array_split(x, 3)[0]) 
    assert np.array_equal(result[1], np.array_split(x, 3)[1]) 
    assert np.array_equal(result[2], np.array_split(x, 3)[2])
'''

# %%
import numpy as np

x = np.arange(8.0)

# %%
"""
question: |
  Partition array into 3 chunks with Numpy
"""

np.array_split(x, 3)
