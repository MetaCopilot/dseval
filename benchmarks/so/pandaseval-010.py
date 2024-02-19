'''
### Prompt ###

import pandas as pd

df = pd.DataFrame({'Sp': ['MM1', 'MM1', 'MM1', 'MM2', 'MM2', 'MM2', 'MM4', 'MM4', 'MM4'],
                   'Mt': ['S1', 'S1', 'S3', 'S3', 'S4', 'S4', 'S2', 'S2', 'S2'],
                   'Value': ['a', 'n', 'cb', 'mk', 'bg', 'dgd', 'rd', 'cb', 'uyi'],
                   'num': [3, 2, 5, 8, 10, 1, 2, 2, 7]})

# How do I find all rows in a pandas DataFrame which have the max value for 'num' column, after grouping by 'Mt' column?
new_df =

### Solution ###

 df.groupby('Mt').apply(lambda x: x.loc[x.num == x.num.max()])

### Test ###

def check():
    assert new_df.equals(df.groupby('Mt').apply(lambda x: x.loc[x.num == x.num.max()]))
'''

# %%

import pandas as pd

df = pd.DataFrame({'Sp': ['MM1', 'MM1', 'MM1', 'MM2', 'MM2', 'MM2', 'MM4', 'MM4', 'MM4'],
                   'Mt': ['S1', 'S1', 'S3', 'S3', 'S4', 'S4', 'S2', 'S2', 'S2'],
                   'Value': ['a', 'n', 'cb', 'mk', 'bg', 'dgd', 'rd', 'cb', 'uyi'],
                   'num': [3, 2, 5, 8, 10, 1, 2, 2, 7]})

# %%

"""
question: How do I find all rows in a pandas DataFrame which have the max value for 'num' column, after grouping by 'Mt' column?

validator:
  result:
    compare_fn:
      ignore_index: true
"""

df.groupby('Mt').apply(lambda x: x.loc[x.num == x.num.max()])
