'''
### Prompt ###

import numpy as np

a = np.arange(8)[:,None].repeat(8,axis=1)
# How can I use reshape to divide it into 4 chucks, such that it looks like this:
# I would like to reshape a to (2, 4, 2, 4) and then transpose it by (0, 2, 1, 3) to c
b =

### Solution ###

 a.reshape(2,4,2,4)
c = b.transpose(0,2,1,3)

### Test ###

def check():
    tmp_b = a.reshape(2, 4, 2, 4)
    tmp_c = tmp_b.transpose(0, 2, 1, 3)
    assert np.array_equal(c, tmp_c)
'''

# %%
import numpy as np

a = np.arange(8)[:,None].repeat(8,axis=1)

# %%

"""
question: |
  How can I use reshape to divide it into 4 chucks, such that it looks like this:
  I would like to reshape a to (2, 4, 2, 4) and then transpose it by (0, 2, 1, 3) to c

validator:
  namespace_check:
    c:
"""

b = a.reshape(2,4,2,4)
c = b.transpose(0,2,1,3)
