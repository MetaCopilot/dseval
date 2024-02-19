'''
### Prompt ###

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5])
# if function is c(i, j) = a(i) + b(j)*2:
c =

### Solution ###

 a[:, None] + b*2

### Test ###

def check():
    assert np.array_equal(c, a[:, None] + b*2)
'''

# %%
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5])

# %%
"""
question: |
  Compute a matrix c, where c(i, j) = a(i) + b(j)*2.

validator:
  namespace_check:
    c:
"""

c = a[:, None] + b*2
