'''
### Prompt ###

import numpy as np

list_of_arrays = map(lambda x: x*np.ones(2), range(5))
# I generate a list of one dimensional numpy arrays in a loop and later convert this list to a 2d numpy array.
# I would've preallocated a 2d numpy array if i knew the number of items ahead of time, but I don't, therefore I put everything in a list.
# s there a better way (performancewise) to go about the task of collecting sequential numerical data (in my case numpy arrays) than putting them in a list and then making a numpy.array out of it (I am creating a new obj and copying the data)? Is there an "expandable" matrix data structure available in a well tested module?
myarray =

### Solution ###

 np.stack(list_of_arrays)

### Test ###

def check():
    tmp = map(lambda x: x*np.ones(2), range(5))
    assert np.array_equal(myarray, np.vstack(tmp))
'''

# %%
import numpy as np

list_of_arrays = list(map(lambda x: x*np.ones(2), range(5)))

# %%
"""
question: |
  I generate a list of one dimensional numpy arrays in a loop and later convert this list to a 2d numpy array.
  I would've preallocated a 2d numpy array if i knew the number of items ahead of time, but I don't, therefore I put everything in a list.
  Is there a better way (performancewise) to go about the task of collecting sequential numerical data (in my case numpy arrays) than putting them in a list and then making a numpy.array out of it (I am creating a new obj and copying the data)? Is there an "expandable" matrix data structure available in a well tested module?
"""

np.stack(list_of_arrays)
