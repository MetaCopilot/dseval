'''
### Prompt ###

import pandas as pd

df1 = pd.DataFrame({'a': [0, 1], 'b': [5, 3]})
df2 = pd.DataFrame({'c': [0, 1], 'd': [10, 20]})
# How do I merge two dataframes by index?
# Set left&right indexs to True
merged_df =

### Solution ###

pd.merge(df1, df2, left_index=True, right_index=True)

### Test ###

def check():
    assert merged_result.equals(pd.merge(df1, df2, left_index=True, right_index=True))
'''

# %%

import pandas as pd

df1 = pd.DataFrame({'a': [0, 1], 'b': [5, 3]})
df2 = pd.DataFrame({'c': [0, 1], 'd': [10, 20]})

# %%

"""
question: |
  How do I merge two dataframes by index?
  Set left&right indexs to True
"""

pd.merge(df1, df2, left_index=True, right_index=True)
