'''
### Prompt ###

import pandas as pd

def get_values_at_nth_rows(df, n, column_name):
    """
    how do I get the value at an nth row of a given column name in Pandas?
    return the value
    """

### Solution ###

    return df[column_name].iloc[n]

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]}), 0, 'A') == 1
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]}), 1, 'A') == 2
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]}), 2, 'A') == 3
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]}), 2, 'B') == 500
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]}), 1, 'B') == 300
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]}), 0, 'B') == 100
    assert candidate(pd.DataFrame({'A': [5, 2, 3], 'B': [100, 300, 500]}), 0, 'B') == 100
    assert candidate(pd.DataFrame({'A': [5, 2, 1], 'B': [100, 300, 500]}), 0, 'B') == 100
    assert candidate(pd.DataFrame({'A': [5, 2, 1], 'B': [500, 300, 500]}), 0, 'B') == 500
    assert candidate(pd.DataFrame({'A': [5, 2, 1], 'B': [500, 300, 100]}), 0, 'B') == 500
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def get_values_at_nth_rows(df, n, column_name):` that takes a DataFrame, an integer n, and a column name and returns the value at the nth row of the given column name in Pandas.

validator:
  table_test:
    function_name: get_values_at_nth_rows
    test_cases:
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]})`", 0, 'A']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]})`", 1, 'A']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]})`", 2, 'A']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]})`", 2, 'B']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]})`", 1, 'B']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]})`", 0, 'B']
    - ["`pd.DataFrame({'A': [5, 2, 3], 'B': [100, 300, 500]})`", 0, 'B']
    - ["`pd.DataFrame({'A': [5, 2, 1], 'B': [100, 300, 500]})`", 0, 'B']
    - ["`pd.DataFrame({'A': [5, 2, 1], 'B': [500, 300, 500]})`", 0, 'B']
    - ["`pd.DataFrame({'A': [5, 2, 1], 'B': [500, 300, 100]})`", 0, 'B']
"""

def get_values_at_nth_rows(df, n, column_name):
    return df[column_name].iloc[n]
