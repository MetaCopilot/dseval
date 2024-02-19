'''
### Prompt ###

import numpy as np

a = np.array([10, 20, 30])
b = np.array([30, 20, 20])
c = np.array([50, 20, 40])

# I'd like to calculate element-wise average between a, b and c.
mean_array =

### Solution ###

 np.mean([a, b, c], axis=0)

### Test ###

def check():
    assert np.array_equal(mean_array, np.array([30, 20, 30]))
'''

# %%
import numpy as np

a = np.array([10, 20, 30])
b = np.array([30, 20, 20])
c = np.array([50, 20, 40])

# %%
"""
question: |
  I'd like to calculate element-wise average between a, b and c.
"""

np.mean([a, b, c], axis=0)
