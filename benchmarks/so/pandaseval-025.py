'''
### Prompt ###

import pandas as pd
df = pd.DataFrame({
    'id': [220, 220, 220, 826, 826, 826, 901, 901, 901],
    'product': [6647, 6647, 6647, 3380, 3380, 3380, 4555, 4555, 4555],
    'date': ['2014-09-01', '2014-09-03', '2014-10-16', '2014-11-11', '2014-12-09', '2015-05-19', '2014-09-01', '2014-10-05', '2014-11-01']
})

# How to group values of pandas dataframe and select the latest by date from each group?
# Sorting values by `date` (ascending is True), and then grouping by `id`
last_df =

### Solution ###

 df.sort_values('date', ascending=True)
last_df = last_df.groupby('id').last()

### Test ###

def check():
    assert last_df.equals(df.sort_values('date', ascending=True).groupby('id').last())
'''

# %%

import pandas as pd
df = pd.DataFrame({
    'id': [220, 220, 220, 826, 826, 826, 901, 901, 901],
    'product': [6647, 6647, 6647, 3380, 3380, 3380, 4555, 4555, 4555],
    'date': ['2014-09-01', '2014-09-03', '2014-10-16', '2014-11-11', '2014-12-09', '2015-05-19', '2014-09-01', '2014-10-05', '2014-11-01']
})

# %%

"""
question: |
  How to group values of pandas dataframe and select the latest by date from each group?
  Sorting values by `date` (ascending is True), and then grouping by `id`
"""

last_df = df.sort_values('date', ascending=True)
last_df.groupby('id').last()
