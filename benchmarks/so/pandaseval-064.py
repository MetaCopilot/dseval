'''
### Prompt ###

import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2.2, 'three']], columns=['A', 'B', 'C'])
# I was wondering if there is an elegant and shorthand way in Pandas DataFrames to select columns by data type (dtype). 
# i.e. Select only float64 columns from a DataFrame
new_df =

### Solution ###

df.select_dtypes(include=['float64'])

### Test ###

def check():
    assert new_df.equals(df.select_dtypes(include=['float64']))
'''

# %%

import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2.2, 'three']], columns=['A', 'B', 'C'])

# %%

"""
question: |
  I was wondering if there is an elegant and shorthand way in Pandas DataFrames to select columns by data type (dtype).
  i.e. Select only float64 columns from a DataFrame
"""

df.select_dtypes(include=['float64'])
