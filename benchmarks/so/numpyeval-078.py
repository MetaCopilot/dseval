'''
### Prompt ###

import numpy as np

a = np.array([[1,2,3],
              [3,2,4]])

my_dict = {1:23, 2:34, 3:36, 4:45}
# I am trying to translate every element of a numpy.array according to a given key
# I don't know about efficient, but you could use np.vectorize on the .get method of dictionaries:
out =

### Solution ###

 np.vectorize(my_dict.get)(a)

### Test ###

def check():
    assert np.array_equal(out, np.array([[23,34,36], [36,34,45]]))
'''

# %%
import numpy as np

a = np.array([[1,2,3],
              [3,2,4]])

my_dict = {1:23, 2:34, 3:36, 4:45}

# %%
"""
question: |
  I am trying to translate every element of a numpy.array according to a given key
  I don't know about efficient, but you could use np.vectorize on the .get method of dictionaries:
"""

np.vectorize(my_dict.get)(a)
