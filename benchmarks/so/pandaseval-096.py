'''
### Prompt ###

import pandas as pd

df1 = pd.DataFrame({'staff':[1,4], 'company':[100,301]})
df2 = pd.DataFrame({'person':[1,2], 'company':[100,300]})
# merge the above two dataframes on column 'company'
merged_df =

### Solution ###

 pd.merge(df1, df2, on='company')

### Test ###

def check():
    assert merged_df.equals(pd.DataFrame({"staff": [1], "company": [100], "person": [1]}))
'''

# %%

import pandas as pd

df1 = pd.DataFrame({'staff':[1,4], 'company':[100,301]})
df2 = pd.DataFrame({'person':[1,2], 'company':[100,300]})

# %%

"""
question: |
  Merge the above two dataframes on column 'company'.
"""

pd.merge(df1, df2, on='company')
