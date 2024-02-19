'''
### Prompt ###

import pandas as pd
import numpy as np

my_df = pd.DataFrame({'col1': [1,2,3], 'col2': [1.0,2.0,3.0]})
# I need to change the dtype of multiple columns but the dataframe has different kind of dtypes. 
# Some columns dtypes are float64 whereas some columns are int64
# I need to change all float64 to float32.
cols =

### Solution ###

 my_df.select_dtypes(include=['float64']).columns
my_df[cols] = my_df[cols].astype(np.float32)

### Test ###

def check():
    assert my_df.equals(pd.DataFrame({'col1': [1,2,3], 'col2': [np.float32(1.0),np.float32(2.0),np.float32(3.0)]}))
'''

# %%

import pandas as pd
import numpy as np

my_df = pd.DataFrame({'col1': [1,2,3], 'col2': [1.0,2.0,3.0]})

# %%

"""
question: |
  I need to change the dtype of multiple columns but the dataframe has different kind of dtypes. 
  Some columns dtypes are float64 whereas some columns are int64
  I need to change all float64 to float32.
  Modify the DataFrame `my_df` in-place.

validator:
  namespace_check:
    my_df:
"""

cols = my_df.select_dtypes(include=['float64']).columns
my_df[cols] = my_df[cols].astype(np.float32)
