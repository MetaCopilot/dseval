'''
### Prompt ###

import numpy as np

# We array `data` defines the columns of the nonzero elements in the output array. 
data = np.array([1, 0, 3])
# We need to also define the rows and then use fancy indexing in the following way:
result = np.zeros((data.size, data.max()+1))
# Convert array of indices to 1-hot encoded numpy array
result

### Solution ###

[np.arange(data.size), data] = 1

### Test ###

def check():
    assert np.array_equal(result, np.array([[0., 1., 0., 0.], [1., 0., 0., 0.], [0., 0., 0., 1.]]))
'''

# %%

import numpy as np

data = np.array([1, 0, 3])

result = np.zeros((data.size, data.max()+1))

# %%

"""
question: |
  Convert array of indices to 1-hot encoded numpy array
  Modify the array `result` in-place.

validator:
  namespace_check:
    result:
"""

result[np.arange(data.size), data] = 1
