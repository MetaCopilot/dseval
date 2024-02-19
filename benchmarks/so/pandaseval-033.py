'''
### Prompt ###

import pandas as pd

def get_last_n_rows(df, n):
    # How to get the last N rows of a pandas DataFrame?

### Solution ###

    return df.tail(n)

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]}), 2).equals(pd.DataFrame({'A': [2, 3], 'B': [300, 500]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [11, 2, 3], 'B': [100, 300, 500]}), 2).equals(pd.DataFrame({'A': [2, 3], 'B': [300, 500]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [11, 2, 3], 'B': [100, 400, 500]}), 2).equals(pd.DataFrame({'A': [2, 3], 'B': [400, 500]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [11, 2, 3], 'B': [100, 400, 600]}), 2).equals(pd.DataFrame({'A': [2, 3], 'B': [400, 600]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [11, 20, 3], 'B': [100, 400, 600]}), 2).equals(pd.DataFrame({'A': [20, 3], 'B': [400, 600]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [11, 52, 13], 'B': [100, 400, 600]}), 2).equals(pd.DataFrame({'A': [52, 13], 'B': [400, 600]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [84, 52, 13], 'B': [100, 400, 600]}), 2).equals(pd.DataFrame({'A': [52, 13], 'B': [400, 600]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [84, 52, 82], 'B': [100, 400, 600]}), 2).equals(pd.DataFrame({'A': [52, 82], 'B': [400, 600]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [84, 52, 82], 'B': [100, 512, 600]}), 2).equals(pd.DataFrame({'A': [52, 82], 'B': [512, 600]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [84, 52, 82], 'B': [100, 512, 777]}), 2).equals(pd.DataFrame({'A': [52, 82], 'B': [512, 777]}, index=[1, 2]))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def get_last_n_rows(df, n):` that takes a pandas DataFrame and an integer n and returns a DataFrame to solve the following problem:
  How to get the last N rows of a pandas DataFrame?

validator:
  table_test:
    function_name: get_last_n_rows
    test_cases:
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]})`", 2]
    - ["`pd.DataFrame({'A': [11, 2, 3], 'B': [100, 300, 500]})`", 2]
    - ["`pd.DataFrame({'A': [11, 2, 3], 'B': [100, 400, 500]})`", 2]
    - ["`pd.DataFrame({'A': [11, 2, 3], 'B': [100, 400, 600]})`", 2]
    - ["`pd.DataFrame({'A': [11, 20, 3], 'B': [100, 400, 600]})`", 2]
    - ["`pd.DataFrame({'A': [11, 52, 13], 'B': [100, 400, 600]})`", 2]
    - ["`pd.DataFrame({'A': [84, 52, 13], 'B': [100, 400, 600]})`", 2]
    - ["`pd.DataFrame({'A': [84, 52, 82], 'B': [100, 400, 600]})`", 2]
    - ["`pd.DataFrame({'A': [84, 52, 82], 'B': [100, 512, 600]})`", 2]
    - ["`pd.DataFrame({'A': [84, 52, 82], 'B': [100, 512, 777]})`", 2]
"""

def get_last_n_rows(df, n):
    return df.tail(n)
