'''
### Prompt ###

import pandas as pd

df = pd.DataFrame({"Code": [2, 2, 4, 4], "Country": ["Afghanistan", "Afghanistan", "Angola", "Angola"], "Item_Code": [15, 25, 15, 25], "Y1961": [10, 10, 30, 30], "Y1962": [20, 20, 40, 40], "Y1963": [30, 30, 50, 50]})
# What is the best way to do a groupby on a Pandas dataframe, but exclude some columns from that groupby?
# I want to groupby the column `Country` and `Item_Code` and only compute the sum of the rows falling under the columns ['Y1961', 'Y1962' and 'Y1963']. 
new_df =

### Solution ###

 df.groupby(['Country', 'Item_Code'])[['Y1961', 'Y1962', 'Y1963']].sum()

### Test ###

def check():
    assert new_df.equals(pd.DataFrame({"Code": [2, 2, 4, 4], "Country": ["Afghanistan", "Afghanistan", "Angola", "Angola"], "Item_Code": [15, 25, 15, 25], "Y1961": [10, 10, 30, 30], "Y1962": [20, 20, 40, 40], "Y1963": [30, 30, 50, 50]}).groupby(['Country', 'Item_Code'])[['Y1961', 'Y1962', 'Y1963']].sum())
'''

# %%

import pandas as pd

df = pd.DataFrame({"Code": [2, 2, 4, 4], "Country": ["Afghanistan", "Afghanistan", "Angola", "Angola"], "Item_Code": [15, 25, 15, 25], "Y1961": [10, 10, 30, 30], "Y1962": [20, 20, 40, 40], "Y1963": [30, 30, 50, 50]})

# %%

"""
question: |
  What is the best way to do a groupby on a Pandas dataframe, but exclude some columns from that groupby?
  I want to groupby the column `Country` and `Item_Code` and only compute the sum of the rows falling under the columns ['Y1961', 'Y1962' and 'Y1963']. 

validator:
  result:
    compare_fn:
      ignore_index: true
"""

df.groupby(['Country', 'Item_Code'])[['Y1961', 'Y1962', 'Y1963']].sum()
