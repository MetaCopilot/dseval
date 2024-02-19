'''
### Prompt ###

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# I would like to add a new column C that is the sum value of A and B cell.

### Solution ###

df['C'] = df.A + df.B

### Test ###

def check():
    assert df.equals(pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [5, 7, 9]}))
'''

# %%

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# %%
"""
question: |
  I would like to add a new column C that is the sum value of A and B cell.
  Modify the DataFrame `df` in-place.

validator:
  namespace_check:
    df:
"""

df['C'] = df.A + df.B
