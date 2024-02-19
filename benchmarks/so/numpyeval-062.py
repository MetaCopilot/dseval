'''
### Prompt ###

import numpy as np

myarray = np.array([("Hello",2.5,3),("World",3.6,2)])
# Converting a 2D numpy array to a structured array
# You can 'create a record array from a (flat) list of arrays' using numpy.core.records.fromarrays as follows:
# Note that we need conduct the transpose on the array, and the names reset to 'col1, co2, col3'
newrecarray =

### Solution ###

 np.core.records.fromarrays(myarray.T, names='col1, col2, col3')

### Test ###

def check():
    assert np.array_equal(newrecarray, np.core.records.fromarrays(myarray.T, names='col1, col2, col3'))
'''

# %%
import numpy as np

myarray = np.array([("Hello",2.5,3),("World",3.6,2)])

# %%
"""
question: |
  Converting a 2D numpy array to a structured array
  You can 'create a record array from a (flat) list of arrays' using numpy.core.records.fromarrays as follows:
  Note that we need conduct the transpose on the array, and the names reset to 'col1, co2, col3'
  Save it to a variable named `newrecarray`.

validator:
  namespace_check:
    newrecarray:
"""

newrecarray = np.core.records.fromarrays(myarray.T, names='col1, col2, col3')
