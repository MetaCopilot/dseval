'''
### Prompt ###

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3], 'col2': ['Jimmy','Tom','Jimmy']})
# I have a dataframe that has two columns, the second column is one of only a few values. 
# I want to return a dataframe where only the rows where that col2 had a specific value 'Jimmy' are included.
new_df =

### Solution ###

 df[df.iloc[:, 1] == 'Jimmy']

### Test ###

def check():
    assert new_df.equals(pd.DataFrame({'col1': [1, 3], 'col2': ['Jimmy', 'Jimmy']}, index=[0, 2]))
'''

# %%

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3], 'col2': ['Jimmy','Tom','Jimmy']})

# %%

"""
question: |
  I have a dataframe that has two columns, the second column is one of only a few values. 
  I want to return a dataframe where only the rows where that col2 had a specific value 'Jimmy' are included.
"""

df[df.iloc[:, 1] == 'Jimmy']
