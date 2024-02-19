'''
### Prompt ###

import pandas as pd

def get_mean_in_column(df, col_name):
    # return the column average/mean

### Solution ###

    return df[col_name].mean()

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({"A": [1, 2, 3, 4, 5]}), "A") == 3.0
    assert candidate(pd.DataFrame({"A": [1, 2, 3, 4, 5, 3]}), "A") == 3.0
    assert candidate(pd.DataFrame({'B': [1, 2, 3, 4, 5, 3]}), 'B') == 3.0
    assert candidate(pd.DataFrame({'A': [1, 2, 3, 3, 4, 5, 3]}), 'A') == 3.0
    assert candidate(pd.DataFrame({'A': [1, 3, 2, 3, 4, 5, 3]}), 'A') == 3.0
    assert candidate(pd.DataFrame({'T': [1, 2, 3, 4, 5, 3]}), 'T') == 3.0
    assert candidate(pd.DataFrame({'A': [1, 2, 3, 4, 5, 3, 3, 3]}), 'A') == 3.0
    assert candidate(pd.DataFrame({'A': [1, 2, 1, 3, 5, 4, 5, 3]}), 'A') == 3.0
    assert candidate(pd.DataFrame({'A': [1, 2, 3, 4, 5, 3, 2, 4]}), 'A') == 3.0
    assert candidate(pd.DataFrame({'A': [1, 2, 3, 4, 5, 3, 1, 5]}), 'A') == 3.0
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def get_mean_in_column(df, col_name):` that takes a DataFrame and a column name and returns the column average/mean.

validator:
  table_test:
    function_name: get_mean_in_column
    test_cases:
    - ["`pd.DataFrame({'A': [1, 2, 3, 4, 5]})`", A]
    - ["`pd.DataFrame({'A': [1, 2, 3, 4, 5, 3]})`", A]
    - ["`pd.DataFrame({'B': [1, 2, 3, 4, 5, 3]})`", B]
    - ["`pd.DataFrame({'A': [1, 2, 3, 3, 4, 5, 3]})`", A]
    - ["`pd.DataFrame({'A': [1, 3, 2, 3, 4, 5, 3]})`", A]
    - ["`pd.DataFrame({'T': [1, 2, 3, 4, 5, 3]})`", T]
    - ["`pd.DataFrame({'A': [1, 2, 3, 4, 5, 3, 3, 3]})`", A]
    - ["`pd.DataFrame({'A': [1, 2, 1, 3, 5, 4, 5, 3]})`", A]
    - ["`pd.DataFrame({'A': [1, 2, 3, 4, 5, 3, 2, 4]})`", A]
    - ["`pd.DataFrame({'A': [1, 2, 3, 4, 5, 3, 1, 5]})`", A]
"""

def get_mean_in_column(df, col_name):
    return df[col_name].mean()
