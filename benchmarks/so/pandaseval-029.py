'''
### Prompt ###

import pandas as pd
import numpy as np
df = pd.DataFrame({'A': [1, 4, 7, np.nan], 'B': [np.nan, 2, 5, np.nan], 'C': [np.nan, np.nan, 3, 6]})
# Move next value to first empty row pandas
# how do i move each value from a column to the first empty "row/cell" in pandas?
# use sorted to align non NULL data at the top, use dropna to drop all rows with all NaN
new_df =

### Solution ###

 df.apply(lambda x: sorted(x, key=pd.isnull)).dropna(how = 'all')

### Test ###

def check(candidate):
    assert new_df.equals(pd.DataFrame({'A': [1.0, 4.0, 7.0], 'B': [2.0, 5.0, np.nan], 'C': [3.0, 6.0, np.nan]}))
'''

# %%

import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 4, 7, np.nan], 'B': [np.nan, 2, 5, np.nan], 'C': [np.nan, np.nan, 3, 6]})

# %%

"""
question: |
  Move each value from a column to the first empty "row/cell" in pandas.
  Use sorted to align non NULL data at the top, use dropna to drop all rows with all NaN.
"""

df.apply(lambda x: sorted(x, key=pd.isnull)).dropna(how='all')
