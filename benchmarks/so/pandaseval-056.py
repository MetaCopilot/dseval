'''
### Prompt ###

import pandas as pd

df = pd.DataFrame({'a': [3.0, 2.0, 4.0, 1.0],'b': [1.0, 4.0 , 2.0, 3.0]})
# How to get the first largest value in column a？
# Using nlargest and iloc to implemente this
first_value =

### Solution ###

df.a.nlargest(1).iloc[-1]

### Test ###

def check():
    assert first_value == 4.0
'''

# %%
import pandas as pd

df = pd.DataFrame({'a': [3.0, 2.0, 4.0, 1.0],'b': [1.0, 4.0 , 2.0, 3.0]})

# %%
"""
question: |
  How to get the first largest value in column a？
  Using nlargest and iloc to implement this.
"""

df.a.nlargest(1).iloc[-1]
