'''
### Prompt ###

import pandas as pd
import numpy as np

df = pd.DataFrame({'group1': [0, 0, 1, 1], 'group2': [2, 2, 3, 4], 'base': [0, 1, 2, 3], 'x1': [3, 4, 5, 6], 'x2': [np.nan, 6, np.nan, 8]})

# Selecting rows where column x2 is NaN 
nan_df =

### Solution ###

 df[df['x2'].isnull()]

### Test ###

def check():
    assert nan_df.equals(pd.DataFrame({'group1': [0, 1], 'group2': [2, 3], 'base': [0, 2], 'x1': [3, 5], 'x2': [np.nan, np.nan]}, index=[0, 2]))
'''

# %%

import pandas as pd
import numpy as np

df = pd.DataFrame({'group1': [0, 0, 1, 1], 'group2': [2, 2, 3, 4], 'base': [0, 1, 2, 3], 'x1': [3, 4, 5, 6], 'x2': [np.nan, 6, np.nan, 8]})

# %%

"""
question: |
  Selecting rows where column x2 is NaN
"""

df[df['x2'].isnull()]
