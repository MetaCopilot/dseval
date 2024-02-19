'''
### Prompt ###

import pandas as pd

df = pd.DataFrame({'line_date': [1, 2, 3], 'line_num': [1, 0, 6], 'line_text': list('abc')})
# I need to remain the rows where line_num is not equal to 0. What's the most efficient way to do it?
# it should be as simple as:
n_df =

### Solution ###

 df[df.line_num != 0]

### Test ###

def check():
    assert df.equals(pd.DataFrame({"line_date": [1, 3], "line_num": [1, 6], "line_text": list("ac")}, index=[0, 2]))
'''

# %%

import pandas as pd

df = pd.DataFrame({'line_date': [1, 2, 3], 'line_num': [1, 0, 6], 'line_text': list('abc')})

# %%

"""
question: |
  I need to remain the rows where line_num is not equal to 0. What's the most efficient way to do it?
"""

df[df.line_num != 0]
