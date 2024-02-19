'''
### Prompt ###

import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[1,4], 'B':[np.nan,301]})
# # counting the number of missing/NaN in each column
# Get a series with the number of missing/NaN in each column
count_series =

### Solution ###

 df.isnull().sum()

### Test ###

def check():
    assert count_series.equals(pd.Series([0, 1], index=['A', 'B']))
'''

# %%

import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[1,4], 'B':[np.nan,301]})

# %%

"""
question: |
  Get a series with the number of missing/NaN in each column
"""

df.isnull().sum()
