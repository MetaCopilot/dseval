'''
### Prompt ###

import pandas as pd

s1 = pd.Series([3,4,5])
s2 = pd.Series([1,2,3,5])
# Finding the intersection between two series
# In detail, first we create two sets, one for each series.
# Then we find the intersection of the two sets.
s1, s2 = set(s1), set(s2)
intersection_result =

### Solution ###

 s1.intersection(s2)

### Test ###

def check():
    assert intersection_result == {3, 5}
'''

# %%
import pandas as pd

s1 = pd.Series([3,4,5])
s2 = pd.Series([1,2,3,5])

# %%
"""
question: |
  Finding the intersection between two series
  In detail, first we create two sets, one for each series.
  Then we find the intersection of the two sets.
"""

s1, s2 = set(s1), set(s2)
s1.intersection(s2)
