'''
### Prompt ###

import pandas as pd

# I want to create a dataframe with one of the column as a list or array.
df = pd.DataFrame({'Name':['Juda','Pri']})
emails = {'a@a.com','b@b.com'}
df['Email'] = ''
# After you assign a list like or array like value to the columns, the column should be considered as type object
# Now I want to assign the emails to first row and the 'Email' column

### Solution ###

df.Email = df.Email.astype(object)
df.loc[0].Email = emails

### Test ###

def check():
    assert df.equals(pd.DataFrame({'Name':['Juda','Pri'],'Email':[{'a@a.com','b@b.com'}, '']}))
'''

# %%

import pandas as pd

df = pd.DataFrame({'Name':['Juda','Pri']})
emails = {'a@a.com','b@b.com'}
df['Email'] = ''

# %%

"""
question: |
  I want to create a dataframe with one of the column as a list.
  After you assign a list like or array like value to the columns, the column should be considered as type object
  Now I want to assign the emails to first row and the 'Email' column
  Modify the DataFrame `df` in-place.

validator:
  namespace_check:
    df:
"""

df.Email = df.Email.astype(object)
df.loc[0].Email = list(emails)
