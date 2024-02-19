'''
### Prompt ###

import pandas as pd

df = pd.DataFrame({'A': [1000, 765, 800], 'B': [10, 5, 7]})
# I have a dataframe in pandas where each column has different value range.
# Any idea how I can normalize the columns of this dataframe where each value is between 0 and 1?
normalized_df =

### Solution ###

 df.apply(lambda x: (x - x.min()) / (x.max() - x.min()))

### Test ###

def check():
    assert normalized_df.equals(df.apply(lambda x: (x - x.min()) / (x.max() - x.min())))
'''

# %%
import pandas as pd

df = pd.DataFrame({'A': [1000, 765, 800], 'B': [10, 5, 7]})

# %%

"""
question: |
  I have a dataframe in pandas where each column has different value range.
  Any idea how I can normalize the columns of this dataframe where each value is between 0 and 1?
"""

df.apply(lambda x: (x - x.min()) / (x.max() - x.min()))
