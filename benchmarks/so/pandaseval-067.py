'''
### Prompt ###

import pandas as pd

df = pd.DataFrame({'name': ['jon','sam','jane','bob'],
           'age': [30,25,18,26],
           'sex':['male','male','female','male']})

row = ['45', 'Dean', 'male']
# add the row at top in df
df.loc[-1] = row
df.index = df.index + 1
# resort the index by inplace

### Solution ###

df.sort_index(inplace=True)

### Test ###

def check():
    assert df.equals(pd.DataFrame({'name': ['Dean', 'jon','sam','jane','bob'], 'age': [45, 30,25,18,26], 'sex':['male', 'male','male','female','male']}))
'''

# %%
import pandas as pd

df = pd.DataFrame({'name': ['jon','sam','jane','bob'],
           'age': [30,25,18,26],
           'sex':['male','male','female','male']})

row = ['45', 'Dean', 'male']
# add the row at top in df
df.loc[-1] = row
df.index = df.index + 1

# %%
"""
question: resort the index by inplace

validator:
  namespace_check:
    df:
"""

df.sort_index(inplace=True)
