'''
### Prompt ###

import numpy as np
import pandas as pd

df = pd.DataFrame({'A': [5, 6, 7], 'B': [7, 8, 9]})
# What's the best way to sum all values in a Pandas dataframe?
# the result is a numeric value
sum_value =

### Solution ###

 df.to_numpy().sum()

### Test ###

def check():
    assert sum_value == 42
'''

# %%
import numpy as np
import pandas as pd

df = pd.DataFrame({'A': [5, 6, 7], 'B': [7, 8, 9]})

# %%
"""
question: |
  What's the best way to sum all values in a Pandas dataframe?
  The result is a numeric value.
"""

df.to_numpy().sum()
