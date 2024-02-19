'''
### Prompt ###

import numpy as np

a = np.array([[1, 2],
           [3, 4]])
b = np.array([1,1])
# I'd like to use b in index a, I would like to get 4 instead of [a[1], a[1]]
# the code below is the solution
out =

### Solution ###

 a[tuple(b)]

### Test ###

def check():
    assert out == 4
'''

# %%
import numpy as np

a = np.array([[1, 2],
           [3, 4]])
b = np.array([1,1])

# %%
"""
question: |
  I'd like to use b in index a, I would like to get 4 instead of [a[1], a[1]]
"""

a[tuple(b)]
