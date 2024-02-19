'''
### Prompt ###

import pandas as pd

df = pd.DataFrame({
'date': ["2022-01-01", "2022-01-02", "2022-01-03", "friday"],
'value': [1, 2, 3, 4]
})

# transfer column date to datetime type
# when there is a string that is not capable of beeing turned into datetime format, skip that row,
# use errors='coerce' for this
df['date'] =

### Solution ###

 pd.to_datetime(df['date'], errors='coerce')

### Test ###

def check():
    tmp = pd.DataFrame({'date': ["2022-01-01", "2022-01-02", "2022-01-03", "friday"],'value': [1, 2, 3, 4]})
    tmp['date'] = pd.to_datetime(tmp['date'], errors='coerce')
    df.equals(tmp)
'''

# %%

import pandas as pd

df = pd.DataFrame({
'date': ["2022-01-01", "2022-01-02", "2022-01-03", "friday"],
'value': [1, 2, 3, 4]
})

# %%
"""
question: |
  transfer column date to datetime type
  when there is a string that is not capable of beeing turned into datetime format, skip that row,
  use errors='coerce' for this
  modify df in-place

validator:
  namespace_check:
    df:
"""

df['date'] = pd.to_datetime(df['date'], errors='coerce')
