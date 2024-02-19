'''
### Prompt ###

import numpy as np
result = {0: 1.1, 1: 0.5, 2: 0.4, 3: 0.4, 4: 1.0, 5: 0.1, 6: 0.2}

names = ['id','data']
formats = ['f8','f8']
dtype = dict(names = names, formats=formats)
# I have a dictionary that I need to convert to a NumPy structured array. 
array =

### Solution ###

 np.array(list(result.items()), dtype=dtype)

### Test ###

def check():
    assert np.array_equal(array, np.array(list(result.items()), dtype=dtype))
'''

# %%
import numpy as np

result = {0: 1.1, 1: 0.5, 2: 0.4, 3: 0.4, 4: 1.0, 5: 0.1, 6: 0.2}

names = ['id','data']
formats = ['f8','f8']
dtype = dict(names = names, formats=formats)

# %%
"""
question: |
  I have a dictionary that I need to convert to a NumPy structured array.
"""

np.array(list(result.items()), dtype=dtype)
