'''
### Prompt ###

import pandas as pd

data = pd.DataFrame({'A':range(3), 'B':range(3,0,-1), 'C':list('abc')})
# How do I change the column labels of a pandas DataFrame from ['A', 'B', 'C'] to ['a', 'b', 'c']?
data.columns =

### Solution ###

['a', 'b', 'c']

### Test ###

def check():
    assert data.equals(pd.DataFrame({'a':range(3), 'b':range(3,0,-1), 'c':list('abc')}))
'''

# %%

import pandas as pd

data = pd.DataFrame({'A':range(3), 'B':range(3,0,-1), 'C':list('abc')})

# %%

"""
question: |
  How do I change the column labels of a pandas DataFrame from ['A', 'B', 'C'] to ['a', 'b', 'c']?
  Modify the DataFrame `data` in-place.

validator:
  namespace_check:
    data:
"""

data.columns = ['a', 'b', 'c']
