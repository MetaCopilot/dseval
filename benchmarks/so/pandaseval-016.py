'''
### Prompt ###

import pandas as pd

def add_column_to_dataframe(df, column_name, column_data):
    # How to add a new column to an existing DataFrame?
    # I would like to add a new column data with the column name, to the existing dataframe

### Solution ###

    df[column_name] = column_data
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}), 'e', [10, 11, 12]).equals(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'e': [10, 11, 12]}))
    assert candidate(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}), 'd', [10, 11, 12]).equals(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'd': [10, 11, 12]}))
    assert candidate(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'f': [7, 8, 9]}), 'd', [10, 11, 12]).equals(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'f': [7, 8, 9], 'd': [10, 11, 12]}))
    assert candidate(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'f': [7, 8, 9]}), 'd', [5, 2, 1]).equals(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'f': [7, 8, 9], 'd': [5, 2, 1]}))
    assert candidate(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'f': [7, 8, 9]}), 'h', [5, 2, 1]).equals(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'f': [7, 8, 9], 'h': [5, 2, 1]}))
    assert candidate(pd.DataFrame({'g': [1, 2, 3], 'b': [4, 5, 6], 'f': [7, 8, 9]}), 'h', [5, 2, 1]).equals(pd.DataFrame({'g': [1, 2, 3], 'b': [4, 5, 6], 'f': [7, 8, 9], 'h': [5, 2, 1]}))
    assert candidate(pd.DataFrame({'g': [1, 2, 3], 'r': [4, 5, 6], 'f': [7, 8, 9]}), 'h', [5, 2, 1]).equals(pd.DataFrame({'g': [1, 2, 3], 'r': [4, 5, 6], 'f': [7, 8, 9], 'h': [5, 2, 1]}))
    assert candidate(pd.DataFrame({'g': [1, 2, 3], 'r': [4, 5, 6], 'f': [7, 6, 6]}), 'h', [5, 6, 6]).equals(pd.DataFrame({'g': [1, 2, 3], 'r': [4, 5, 6], 'f': [7, 6, 6], 'h': [5, 6, 6]}))
    assert candidate(pd.DataFrame({'g': [1, 2, 3], 'r': [4, 5, 6], 'f': [7, 6, 6]}), 'h', [5, 8, 8]).equals(pd.DataFrame({'g': [1, 2, 3], 'r': [4, 5, 6], 'f': [7, 6, 6], 'h': [5, 8, 8]}))
    assert candidate(pd.DataFrame({'g': [1, 2, 3], 'r': [6, 6, 6], 'f': [7, 6, 6]}), 'h', [5, 8, 8]).equals(pd.DataFrame({'g': [1, 2, 3], 'r': [6, 6, 6], 'f': [7, 6, 6], 'h': [5, 8, 8]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def add_column_to_dataframe(df, column_name, column_data):` that takes a DataFrame, a column name, and column data and returns a DataFrame to solve the following problem:
  How to add a new column to an existing DataFrame?
  I would like to add a new column data with the column name, to the existing dataframe

validator:
  table_test:
    function_name: add_column_to_dataframe
    test_cases:
    - ["`pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})`", "e", [10, 11, 12]]
    - ["`pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})`", "d", [10, 11, 12]]
    - ["`pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'f': [7, 8, 9]})`", "d", [10, 11, 12]]
    - ["`pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'f': [7, 8, 9]})`", "d", [5, 2, 1]]
    - ["`pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'f': [7, 8, 9]})`", "h", [5, 2, 1]]
    - ["`pd.DataFrame({'g': [1, 2, 3], 'b': [4, 5, 6], 'f': [7, 8, 9]})`", "h", [5, 2, 1]]
    - ["`pd.DataFrame({'g': [1, 2, 3], 'r': [4, 5, 6], 'f': [7, 8, 9]})`", "h", [5, 2, 1]]
    - ["`pd.DataFrame({'g': [1, 2, 3], 'r': [4, 5, 6], 'f': [7, 6, 6]})`", "h", [5, 6, 6]]
    - ["`pd.DataFrame({'g': [1, 2, 3], 'r': [4, 5, 6], 'f': [7, 6, 6]})`", "h", [5, 8, 8]]
    - ["`pd.DataFrame({'g': [1, 2, 3], 'r': [6, 6, 6], 'f': [7, 6, 6]})`", "h", [5, 8, 8]]
"""

def add_column_to_dataframe(df, column_name, column_data):
    df[column_name] = column_data
    return df
