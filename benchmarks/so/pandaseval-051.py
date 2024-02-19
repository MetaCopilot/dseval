'''
### Prompt ###

import pandas as pd
import numpy as np

df = pd.DataFrame({'Apples': [2, 1, np.nan],
              'Bananas': [3, 3, 7],
              'Grapes': [np.nan, 2, 3],})

# Add a new column named 'Fruit Total' that sums the values of the other columns
# Note that igonring the NaN values

### Solution ###

df['Fruit Total'] = df.apply(lambda x: sum(x.values), axis=1)

### Test ###

def check():
    tmp = pd.DataFrame({'Apples': [2, 1, np.nan],'Bananas': [3, 3, 7],'Grapes': [np.nan, 2, 3],})
    tmp['Fruit Total'] = tmp.apply(lambda x: sum(x.values), axis=1)
    assert df.equals(tmp)
'''

# %%

import pandas as pd
import numpy as np

df = pd.DataFrame({'Apples': [2, 1, np.nan],
              'Bananas': [3, 3, 7],
              'Grapes': [np.nan, 2, 3],})

# %%

"""
question: |
  Add a new column named 'Fruit Total' that sums the values of the other columns
  When NaN is present, the sum should be NaN too.
  Modify the DataFrame `df` in-place.

validator:
  namespace_check:
    df:
"""

df['Fruit Total'] = df.apply(lambda x: sum(x.values), axis=1)
