'''
### Prompt ###

import pandas as pd

N = 2
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
# How to get the last N rows of a pandas DataFrame?
result =

### Solution ###

df.tail(N)

### Test ###

def check():
    assert result.equals(df.tail(N))
'''

# %%

import pandas as pd

N = 2
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})

# %%

"""
question: How to get the last N rows of a pandas DataFrame?
"""

df.tail(N)
