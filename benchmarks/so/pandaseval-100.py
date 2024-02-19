'''
### Prompt ###

import pandas as pd

# This is my DataFrame that should be repeated for 5 times:
x = pd.DataFrame({'a':1,'b':2}, index = range(1))
# I haven't found anything practical, including those like np.repeat ---- it just doesn't work on a DataFrame.
# You can use the concat function:
repeated_x =

### Solution ###

 pd.concat([x]*5)

### Test ###

def check():
    assert repeated_x.equals(pd.concat([x]*5))
'''

# %%

import pandas as pd

x = pd.DataFrame({'a':1,'b':2}, index = range(1))

# %%

"""
question: |
  This is my DataFrame that should be repeated for 5 times:
  x = pd.DataFrame({'a':1,'b':2}, index = range(1))
  I haven't found anything practical, including those like np.repeat ---- it just doesn't work on a DataFrame.
  You can use the concat function.

validator:
  result:
    compare_fn:
      ignore_index: true
"""

pd.concat([x]*5)
