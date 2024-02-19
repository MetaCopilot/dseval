'''
### Prompt ###

import pandas as pd

# Example DataFrame
df = pd.DataFrame.from_dict({'Name'  : ['May21', 'James', 'Adi22', 'Hello', 'Girl90'],
                             'Volume': [23, 12, 11, 34, 56],
                             'Value' : [21321, 12311, 4435, 32454, 654654]})

# Want to remove all the numbers from the Name column.
# Any idea how to do it in a better way at the series/dataframe level.
df['Name'] =

### Solution ###

 df['Name'].str.replace('\d+', '')

### Test ###

def check():
    assert df.equals(pd.DataFrame({'Name'  : ['May', 'James', 'Adi', 'Hello', 'Girl'],
                             'Volume': [23, 12, 11, 34, 56],
                             'Value' : [21321, 12311, 4435, 32454, 654654]}))
'''

# %%

import pandas as pd

# Example DataFrame
df = pd.DataFrame.from_dict({'Name'  : ['May21', 'James', 'Adi22', 'Hello', 'Girl90'],
                             'Volume': [23, 12, 11, 34, 56],
                             'Value' : [21321, 12311, 4435, 32454, 654654]})

# %%

"""
question: |
  Want to remove all the numbers from the Name column.
  Any idea how to do it in a better way at the series/dataframe level.
  Modify the DataFrame `df` in-place.

validator:
  namespace_check:
    df:
"""

df['Name'] = df['Name'].str.replace(r'\d+', '', regex=True)
