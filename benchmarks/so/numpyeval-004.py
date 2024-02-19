'''
### Prompt ###

import numpy as np

import itertools
data = [[1], [1, 2]]
# Convert Python sequence to NumPy array, filling missing values with 0
result =

### Solution ###

 np.array(list(itertools.zip_longest(*data, fillvalue=0)))

### Test ###

def check():
    assert np.array_equal(result, np.array([[1, 1], [0, 2]]))
'''

# %%
import numpy as np
import itertools

data = [[1], [1, 2]]

# %%

"""
question: |
  Convert Python sequence to NumPy array, filling missing values with 0
"""

np.array(list(itertools.zip_longest(*data, fillvalue=0)))
