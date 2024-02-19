'''
### Prompt ###

import numpy as np

x = np.array([[1], [2], [3]])
# Numpy Vector (N,1) dimension -> (N,) dimension conversion
out =

### Solution ###

 x.reshape(3,)

### Test ###

def check():
    assert out.shape == (3,)
'''

# %%
import numpy as np

x = np.array([[1], [2], [3]])

# %%
"""
question: |
  Numpy Vector (N,1) dimension -> (N,) dimension conversion
"""

x.reshape(3,)
