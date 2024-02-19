'''
### Prompt ###

import numpy as np

a1=np.array(['a','b'])
a2=np.array(['E','F'])
# I am trying to do element-wise string concatenation.
# I thought Add() was the way to do it in numpy but obviously it is not working as expected.
result =

### Solution ###

 np.core.defchararray.add(a1, a2)

### Test ###

def check():
    assert np.array_equal(result, np.char.add(a1,a2))
'''

# %%
import numpy as np

a1=np.array(['a','b'])
a2=np.array(['E','F'])

# %%
"""
question: |
  I am trying to do element-wise string concatenation.
  I thought Add() was the way to do it in numpy but obviously it is not working as expected.
"""

np.core.defchararray.add(a1, a2)
