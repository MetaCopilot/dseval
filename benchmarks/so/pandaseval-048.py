'''
### Prompt ###

import pandas as pd
df = pd.DataFrame({'col': ["apple",
                           "pear",
                           "strawberry"]})
targets = ['apple', 'banana']
# Any word from `targets` are present in sentence.
result =

### Solution ###

 df.loc[df['col'].isin(targets)]

### Test ###

def check():
    assert result.equals(pd.DataFrame({'col': ["apple"]}))
'''

# %%

import pandas as pd

df = pd.DataFrame({'col': ["apple",
                           "pear",
                           "strawberry"]})
targets = ['apple', 'banana']

# %%

"""
question: |
  List the words from `targets` that are present in df.

validator:
  result:
    compare_fn:
      value_only: true
"""

df.loc[df['col'].isin(targets)]
