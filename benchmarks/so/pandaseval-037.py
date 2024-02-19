'''
### Prompt ###

import pandas as pd

data = {'col_0': ['a', 'a', 'a', 'a', 'b','b','b'], 'col_1': [-2, -7, 6, 8, -5, 2, 6]}
df = pd.DataFrame(data)
# What I want is to clip the values of `col_1` between -2 to 2 if `col_0` is `a`.
# # Using `clip` function in pandas.
df.loc[df['col_0']=='a','col_1'] =

### Solution ###

 df.loc[df['col_0']=='a','col_1'].clip(-2,2)

### Test ###

def check():
    assert df.equals(pd.DataFrame({'col_0': ['a', 'a', 'a', 'a', 'b','b','b'], 'col_1': [-2, -2, 2, 2, -5, 2, 6]}))
'''

# %%

import pandas as pd

data = {'col_0': ['a', 'a', 'a', 'a', 'b','b','b'], 'col_1': [-2, -7, 6, 8, -5, 2, 6]}
df = pd.DataFrame(data)

# %%

"""
question: |
  What I want is to clip the values of `col_1` between -2 to 2 if `col_0` is `a`.
  Modify the DataFrame `df` in-place.

validator:
  namespace_check:
    df:
"""

df.loc[df['col_0']=='a','col_1'] = df.loc[df['col_0']=='a','col_1'].clip(-2,2)
