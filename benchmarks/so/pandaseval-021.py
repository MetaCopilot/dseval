'''
### Prompt ###

import pandas as pd
import numpy as np
df = pd.DataFrame({'a': [4, 1, 7, 3], 'b': [5, 2, 9, 6], 'c': [6, 3, 2, 8]})
# I would like to create new dataframe out of the old one in a way that there will only be values that exceed the mean value of the column. 
# We can compare values and then add NaNs by indexing or `where`
# We want remove NaNs also in first rows add custom function with `dropna`
df =

### Solution ###

df[df>df.mean()].apply(lambda x: pd.Series(x.dropna().values))

### Test ###

def check():
    assert df.equals(pd.DataFrame({'a': [4.0, 7.0], 'b': [9.0, 6.0], 'c': [6.0, 8.0]}))
'''

# %%

import pandas as pd
import numpy as np

df = pd.DataFrame({'a': [4, 1, 7, 3], 'b': [5, 2, 9, 6], 'c': [6, 3, 2, 8]})

# %%

"""
question: |
  I would like to create a new dataframe out of the old one in a way that there will only be values that exceed the mean value of the column.
  We can compare values and then add NaNs by indexing or `where`
  We want to remove NaNs also in first rows add custom function with `dropna`
"""

df[df>df.mean()].apply(lambda x: pd.Series(x.dropna().values))
