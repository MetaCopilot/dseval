'''
### Prompt ###

import pandas as pd

def drop_consecutive_duplicates(series):
    # Drop consecutive duplicates
    # Return the result

### Solution ###

    return series.loc[series.shift(-1) != series]

### Test ###

def check(candidate):
    assert candidate(pd.Series([1, 2, 2, 3, 2])).equals(pd.Series([1, 2, 3, 2], index=[0, 2, 3, 4]))
    assert candidate(pd.Series([1, 2, 2, 4, 2])).equals(pd.Series([1, 2, 4, 2], index=[0, 2, 3, 4]))
    assert candidate(pd.Series([1, 2, 2, 5, 2])).equals(pd.Series([1, 2, 5, 2], index=[0, 2, 3, 4]))
    assert candidate(pd.Series([1, 2, 2, 6, 2])).equals(pd.Series([1, 2, 6, 2], index=[0, 2, 3, 4]))
    assert candidate(pd.Series([1, 2, 2, 7, 2])).equals(pd.Series([1, 2, 7, 2], index=[0, 2, 3, 4]))
    assert candidate(pd.Series([1, 2, 2, 8, 2])).equals(pd.Series([1, 2, 8, 2], index=[0, 2, 3, 4]))
    assert candidate(pd.Series([1, 2, 2, 9, 2])).equals(pd.Series([1, 2, 9, 2], index=[0, 2, 3, 4]))
    assert candidate(pd.Series([1, 2, 2, 10, 2])).equals(pd.Series([1, 2, 10, 2], index=[0, 2, 3, 4]))
    assert candidate(pd.Series([1, 2, 2, 11, 2])).equals(pd.Series([1, 2, 11, 2], index=[0, 2, 3, 4]))
    assert candidate(pd.Series([1, 2, 2, 13, 2])).equals(pd.Series([1, 2, 13, 2], index=[0, 2, 3, 4]))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def drop_consecutive_duplicates(series):` that takes a pandas Series and returns a Series to solve the following problem:
  Drop consecutive duplicates

validator:
  table_test:
    function_name: drop_consecutive_duplicates
    output_checker:
      ignore_index: true
    test_cases:
    - ["`pd.Series([1, 2, 2, 3, 2])`"]
    - ["`pd.Series([1, 2, 2, 4, 2])`"]
    - ["`pd.Series([1, 2, 2, 5, 2])`"]
    - ["`pd.Series([1, 2, 2, 6, 2])`"]
    - ["`pd.Series([1, 2, 2, 7, 2])`"]
    - ["`pd.Series([1, 2, 2, 8, 2])`"]
    - ["`pd.Series([1, 2, 2, 9, 2])`"]
    - ["`pd.Series([1, 2, 2, 10, 2])`"]
    - ["`pd.Series([1, 2, 2, 11, 2])`"]
    - ["`pd.Series([1, 2, 2, 13, 2])`"]
"""

def drop_consecutive_duplicates(series):
    return series.loc[series.shift(-1) != series]
