'''
### Prompt ###

import pandas as pd

def sorting_columns_based_on_column_name(df):
    # Sorting columns in pandas dataframe based on column name
    # Note that axis is one

### Solution ###

    return df.reindex(sorted(df.columns), axis=1)

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'Q1.1': [1, 2, 3], 'Q1.3': [4, 5, 6], 'Q1.2': [7, 8, 9]})).equals(pd.DataFrame({'Q1.1': [1, 2, 3], 'Q1.2': [7, 8, 9], 'Q1.3': [4, 5, 6]}))
    assert candidate(pd.DataFrame({'Q1.1': [1, 2, 4], 'Q1.3': [4, 5, 6], 'Q1.2': [7, 8, 9]})).equals(pd.DataFrame({'Q1.1': [1, 2, 4], 'Q1.2': [7, 8, 9], 'Q1.3': [4, 5, 6]}))
    assert candidate(pd.DataFrame({'Q1.1': [1, 2, 5], 'Q1.3': [4, 5, 6], 'Q1.2': [7, 8, 9]})).equals(pd.DataFrame({'Q1.1': [1, 2, 5], 'Q1.2': [7, 8, 9], 'Q1.3': [4, 5, 6]}))
    assert candidate(pd.DataFrame({'Q1.1': [1, 3, 5], 'Q1.3': [4, 5, 6], 'Q1.2': [7, 8, 9]})).equals(pd.DataFrame({'Q1.1': [1, 3, 5], 'Q1.2': [7, 8, 9], 'Q1.3': [4, 5, 6]}))
    assert candidate(pd.DataFrame({'Q1.1': [2, 3, 5], 'Q1.3': [4, 5, 6], 'Q1.2': [7, 8, 9]})).equals(pd.DataFrame({'Q1.1': [2, 3, 5], 'Q1.2': [7, 8, 9], 'Q1.3': [4, 5, 6]}))
    assert candidate(pd.DataFrame({'Q1.1': [2, 3, 5], 'Q1.3': [3, 5, 6], 'Q1.2': [7, 8, 9]})).equals(pd.DataFrame({'Q1.1': [2, 3, 5], 'Q1.2': [7, 8, 9], 'Q1.3': [3, 5, 6]}))
    assert candidate(pd.DataFrame({'Q1.1': [2, 3, 5], 'Q1.3': [3, 3, 6], 'Q1.2': [7, 8, 9]})).equals(pd.DataFrame({'Q1.1': [2, 3, 5], 'Q1.2': [7, 8, 9], 'Q1.3': [3, 3, 6]}))
    assert candidate(pd.DataFrame({'Q1.1': [4, 4, 5], 'Q1.3': [3, 3, 6], 'Q1.2': [7, 8, 9]})).equals(pd.DataFrame({'Q1.1': [4, 4, 5], 'Q1.2': [7, 8, 9], 'Q1.3': [3, 3, 6]}))
    assert candidate(pd.DataFrame({'Q1.1': [4, 4, 5], 'Q1.3': [3, 3, 6], 'Q1.2': [7, 4, 9]})).equals(pd.DataFrame({'Q1.1': [4, 4, 5], 'Q1.2': [7, 4, 9], 'Q1.3': [3, 3, 6]}))
    assert candidate(pd.DataFrame({'Q1.1': [4, 4, 5], 'Q1.3': [3, 3, 6], 'Q1.2': [7, 3, 9]})).equals(pd.DataFrame({'Q1.1': [4, 4, 5], 'Q1.2': [7, 3, 9], 'Q1.3': [3, 3, 6]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def sorting_columns_based_on_column_name(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  Sorting columns in pandas dataframe based on column name
  Note that axis is one

validator:
  table_test:
    function_name: sorting_columns_based_on_column_name
    test_cases:
    - ["`pd.DataFrame({'Q1.1': [1, 2, 3], 'Q1.3': [4, 5, 6], 'Q1.2': [7, 8, 9]})`"]
    - ["`pd.DataFrame({'Q1.1': [1, 2, 4], 'Q1.3': [4, 5, 6], 'Q1.2': [7, 8, 9]})`"]
    - ["`pd.DataFrame({'Q1.1': [1, 2, 5], 'Q1.3': [4, 5, 6], 'Q1.2': [7, 8, 9]})`"]
    - ["`pd.DataFrame({'Q1.1': [1, 3, 5], 'Q1.3': [4, 5, 6], 'Q1.2': [7, 8, 9]})`"]
    - ["`pd.DataFrame({'Q1.1': [2, 3, 5], 'Q1.3': [4, 5, 6], 'Q1.2': [7, 8, 9]})`"]
    - ["`pd.DataFrame({'Q1.1': [2, 3, 5], 'Q1.3': [3, 5, 6], 'Q1.2': [7, 8, 9]})`"]
    - ["`pd.DataFrame({'Q1.1': [2, 3, 5], 'Q1.3': [3, 3, 6], 'Q1.2': [7, 8, 9]})`"]
    - ["`pd.DataFrame({'Q1.1': [4, 4, 5], 'Q1.3': [3, 3, 6], 'Q1.2': [7, 8, 9]})`"]
    - ["`pd.DataFrame({'Q1.1': [4, 4, 5], 'Q1.3': [3, 3, 6], 'Q1.2': [7, 4, 9]})`"]
    - ["`pd.DataFrame({'Q1.1': [4, 4, 5], 'Q1.3': [3, 3, 6], 'Q1.2': [7, 3, 9]})`"]
"""

def sorting_columns_based_on_column_name(df):
    return df.reindex(sorted(df.columns), axis=1)
