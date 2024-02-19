'''
### Prompt ###

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,10,size=100).reshape(10,10))
# I have a Pandas dataframe and I want to find all the unique values in that dataframe...irrespective of row/columns. 
# If I have a 10 x 10 dataframe, and suppose they have 84 unique values, I need to find them - Not the count.
# Using xx.values.ravel to get the flattened array of the dataframe
# Getting the unique values by numpy.unique
unique_ndarray =

### Solution ###

 np.unique(df.values.ravel())

### Test ###

def check():
    assert np.array_equal(unique_ndarray, np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
'''

# %%

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,10,size=100).reshape(10,10))

# %%

"""
question: |
  I have a Pandas dataframe and I want to find all the unique values in that dataframe...irrespective of row/columns. 
  If I have a 10 x 10 dataframe, and suppose they have 84 unique values, I need to find them - Not the count.
  Using xx.values.ravel to get the flattened array of the dataframe
  Getting the unique values by numpy.unique
"""

np.unique(df.values.ravel())
