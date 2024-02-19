'''
### Prompt ###

import pandas as pd

df = pd.DataFrame({'MSRA': [10, 11, 12], 'THU': [100, 110, 120]})
df = df.reset_index()  # make sure indexes pair with number of rows
# (for index, row in DataFrame.iterrows) is a generator which yields both the index and row (as a Series)
# for each row in the DataFrame, we need put the row['MSRA'] (as key) and row['THU'] (as value) into a rows_dict
rows_dict = {} # {MSRA: THU, ...}

### Solution ###

for index, row in df.iterrows():
    rows_dict[row['MSRA']] = row['THU']

### Test ###

def check():
    assert rows_dict == {10: 100, 11: 110, 12: 120}
'''

# %%
import pandas as pd

df = pd.DataFrame({'MSRA': [10, 11, 12], 'THU': [100, 110, 120]})
df = df.reset_index()  # make sure indexes pair with number of rows

# %%
"""
question: |
  Create a dictionary `rows_dict` from a DataFrame `df` with the following structure:
  {MSRA: THU, ...}
  where MSRA and THU are column names in the DataFrame.

validator:
  namespace_check:
    rows_dict:
"""

rows_dict = {}
for index, row in df.iterrows():
    rows_dict[row['MSRA']] = row['THU']
