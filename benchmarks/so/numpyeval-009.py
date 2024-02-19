'''
### Prompt ###

import numpy as np
import pandas as pd

df = pd.DataFrame({'A':[1,2,3], 'B':[1,2,3], 'C':[1,2,3]})
# I have a pandas dataframe I would like to se the diagonal to 0

### Solution ###

np.fill_diagonal(df.values, 0)

### Test ###

def check():
    assert df.equals(pd.DataFrame({'A':[0,2,3], 'B':[1,0,3], 'C':[1,2,0]}))
'''

# %%
import numpy as np
import pandas as pd

df = pd.DataFrame({'A':[1,2,3], 'B':[1,2,3], 'C':[1,2,3]})

# %%
"""
question: |
  I have a pandas dataframe I would like to se the diagonal to 0
  Modify the DataFrame `df` in-place.

validator:
  namespace_check:
    df:
"""

np.fill_diagonal(df.values, 0)
