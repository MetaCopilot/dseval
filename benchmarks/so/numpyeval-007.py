'''
### Prompt ###

import numpy as np

a = np.array([[[10, 1, 1, 2], [2, 2, 2, 3], [3, 3, 3, 4]],
              [[1, 1, 1, 2], [2, 2, 2, 3], [3, 3, 3, 4]]])

# Conducting the reverse operation along with the last dimension

b =

### Solution ###

 a[:, :, ::-1]

### Test ###

def check():
    assert np.array_equal(b, a[:, :, ::-1])
'''

# %%
import numpy as np

a = np.array([[[10, 1, 1, 2], [2, 2, 2, 3], [3, 3, 3, 4]],
              [[1, 1, 1, 2], [2, 2, 2, 3], [3, 3, 3, 4]]])

# %%
"""
question: Conducting the reverse operation along with the last dimension
"""

a[:, :, ::-1]
