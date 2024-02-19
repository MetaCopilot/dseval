'''
### Prompt ###

import pandas as pd

def select_rows_from_column(df, col_name, values):
    # How do I select rows from a DataFrame df based on column values?
    # Return rows whose column value named `col_name` is in an iterable `values`

### Solution ###

    return df[df[col_name].isin(values)]

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]}), 'c1', [11, 12]).equals(pd.DataFrame({'c1': [11, 12], 'c2': [110, 120]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]}), 'c1', [11]).equals(pd.DataFrame({'c1': [11], 'c2': [110]}, index=[1]))
    assert candidate(pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]}), 'c1', [12]).equals(pd.DataFrame({'c1': [12], 'c2': [120]}, index=[2]))
    assert candidate(pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 122]}), 'c1', [12]).equals(pd.DataFrame({'c1': [12], 'c2': [122]}, index=[2]))
    assert candidate(pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 238]}), 'c1', [12]).equals(pd.DataFrame({'c1': [12], 'c2': [238]}, index=[2]))
    assert candidate(pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 1100, 238]}), 'c1', [11]).equals(pd.DataFrame({'c1': [11], 'c2': [1100]}, index=[1]))
    assert candidate(pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 1800, 238]}), 'c1', [11]).equals(pd.DataFrame({'c1': [11], 'c2': [1800]}, index=[1]))
    assert candidate(pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 521, 238]}), 'c1', [11]).equals(pd.DataFrame({'c1': [11], 'c2': [521]}, index=[1]))
    assert candidate(pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 521, 238]}), 'c1', [10]).equals(pd.DataFrame({'c1': [10], 'c2': [100]}, index=[0]))
    assert candidate(pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 521, 238]}), 'c1', [10, 12]).equals(pd.DataFrame({'c1': [10, 12], 'c2': [100, 238]}, index=[0, 2]))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def select_rows_from_column(df, col_name, values):` that takes a DataFrame, a column name, and an iterable of values and returns a DataFrame to solve the following problem:
  How do I select rows from a DataFrame df based on column values?
  Return rows whose column value named `col_name` is in an iterable `values`.

validator:
  table_test:
    function_name: select_rows_from_column
    test_cases:
    - ["`pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})`", c1, [11, 12]]
    - ["`pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})`", c1, [11]]
    - ["`pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})`", c1, [12]]
    - ["`pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 122]})`", c1, [12]]
    - ["`pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 238]})`", c1, [12]]
    - ["`pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 1100, 238]})`", c1, [11]]
    - ["`pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 1800, 238]})`", c1, [11]]
    - ["`pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 521, 238]})`", c1, [11]]
    - ["`pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 521, 238]})`", c1, [10]]
    - ["`pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 521, 238]})`", c1, [10, 12]]
"""

def select_rows_from_column(df, col_name, values):
    return df[df[col_name].isin(values)]
