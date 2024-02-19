'''
### Prompt ###

import pandas as pd

a = [['a', '1.2'], ['b', '70'], ['x', '5']]
# I want to convert a table, represented as a list of lists, into a pandas DataFrame.
# The columns are ['one', 'two']
# What is the best way to convert the columns to the appropriate types, in this case the 'two' column into floats?
df =

### Solution ###

 pd.DataFrame(a, columns=['one', 'two'])
df['two'] = df['two'].astype(float)

### Test ###

def check():
    assert df.equals(pd.DataFrame({'one': ['a', 'b', 'x'], 'two': [1.2, 70.0, 5.0]}))
'''

# %%

import pandas as pd

a = [['a', '1.2'], ['b', '70'], ['x', '5']]

# %%

"""
question: |
  I want to convert a table, represented as a list of lists, into a pandas DataFrame.
  The columns are ['one', 'two']
  What is the best way to convert the columns to the appropriate types, in this case the 'two' column into floats?
"""

df = pd.DataFrame(a, columns=['one', 'two'])
df['two'] = df['two'].astype(float)
df
