'''
### Prompt ###

import pandas as pd

df = pd.DataFrame({'a': [0, 1], 'b': [5, 3]})
# How to obtain pandas DataFrame without index
# I want to print the whole dataframe, but I don't want to print the index
df_string =

### Solution ###

 df.to_string(index=False)

### Test ###

def check():
    assert df_string == ' a  b
 0  5
 1  3'
'''

# %%
import pandas as pd

df = pd.DataFrame({'a': [0, 1], 'b': [5, 3]})

# %%
"""
question: |
  How to obtain pandas DataFrame without index
  I want to convert the whole dataframe to a string, but I don't want to include the index
"""

df.to_string(index=False)
