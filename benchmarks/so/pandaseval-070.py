'''
### Prompt ###

import pandas as pd

web_stats = {'Day': [1, 2, 3, 4, 2, 6],
             'Visitors': [43, 43, 34, 23, 43, 23],
             'Bounce_Rate': [3, 2, 4, 3, 5, 5]}
df = pd.DataFrame(web_stats)
# I would like to drop all data in a pandas dataframe
# Using df.index to drop all rows

### Solution ###

df.drop(df.index, inplace=True)

### Test ###

def check():
    tmp = pd.DataFrame({'Day': [1, 2, 3], 'Visitors': [4, 5, 6], 'Bounce_Rate': [7, 8, 9]})
    tmp.drop(tmp.index, inplace=True)
    assert df.equals(tmp)
'''

# %%
import pandas as pd

web_stats = {'Day': [1, 2, 3, 4, 2, 6],
             'Visitors': [43, 43, 34, 23, 43, 23],
             'Bounce_Rate': [3, 2, 4, 3, 5, 5]}
df = pd.DataFrame(web_stats)

# %%
"""
question: |
  I would like to drop all data in a pandas dataframe
  Using df.index to drop all rows
"""

df.drop(df.index, inplace=True)
