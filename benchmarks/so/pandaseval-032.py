'''
### Prompt ###

import pandas as pd

# creating a Series from a list [56, 24, 421, 90]
my_series =

### Solution ###

pd.Series([56, 24, 421, 90])

### Test ###

def check():
    assert my_series.equals(pd.Series([56, 24, 421, 90]))
'''

# %%

import pandas as pd

# %%

"""
question: |
  Create a pandas Series from a list [56, 24, 421, 90].
"""

pd.Series([56, 24, 421, 90])
