'''
### Prompt ###

import numpy as np

a = np.array((1,2,3))
b = np.array((4,5,6))
# How can the Euclidean distance be calculated with NumPy?
dist =

### Solution ###

np.linalg.norm(a-b)

### Test ###

def check():
    assert np.array_equal(dist, np.linalg.norm(a-b))
'''

# %%
import numpy as np

a = np.array((1,2,3))
b = np.array((4,5,6))

# %%

"""
question: How can the Euclidean distance be calculated with NumPy?
"""

np.linalg.norm(a-b)
