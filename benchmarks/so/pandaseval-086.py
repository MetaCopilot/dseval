'''
### Prompt ###

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3],'B': [100, 300, 500],'C': list('abc')})

# How can I delete multiple columns in one pass?
# In detail, I would like to delete columns A and C, but I don't know how to do it in one pass.
new_df =

### Solution ###

 df.drop(['A', 'C'], axis=1)

### Test ###

def check():
    assert new_df.equals(pd.DataFrame({'B': [100, 300, 500]}))
'''

# %%

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3],'B': [100, 300, 500],'C': list('abc')})

# %%

"""
question: |
  How can I delete multiple columns in one pass?
  In detail, I would like to delete columns A and C, but I don't know how to do it in one pass.
"""

df.drop(['A', 'C'], axis=1)
