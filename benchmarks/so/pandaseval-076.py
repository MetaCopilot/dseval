'''
### Prompt ###

import pandas as pd

source_series = pd.Series([32, 434, 542, 'BC2'])
target_series = pd.Series(['B1', 'B3', 'B4', 123, 43, 54])

# Appending the source series to the target series, with ignoring the index or resetting index
merged_series =

### Solution ###

target_series.append(source_series, ignore_index=True)

### Test ###

def check():
    assert merged_series.equals(pd.Series(['B1', 'B3', 'B4', 123, 43, 54, 32, 434, 542, 'BC2']))
'''

# %%
import pandas as pd

source_series = pd.Series([32, 434, 542, 'BC2'])
target_series = pd.Series(['B1', 'B3', 'B4', 123, 43, 54])

# %%

"""
question: |
  Appending the source series to the target series, with ignoring the index or resetting index

validator:
  namespace_check:
    target_series:
"""

target_series = pd.concat([target_series, source_series], ignore_index=True).reset_index(drop=True)
