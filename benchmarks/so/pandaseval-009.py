'''
### Prompt ###

import pandas as pd

def extract_first_and_last_df(df):
    # Extract first and last row of a dataframe in pandas
    # Return the dataframe with the first and last row

### Solution ###

    return df.iloc[[0, -1]]

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a': [1, 3, 2], 'b': [4, 4, 2]})).equals(pd.DataFrame({'a': [1, 2], 'b': [4, 2]}, index=[0, 2]))
    assert candidate(pd.DataFrame({'a': [12, 3, 2], 'b': [4, 4, 2]})).equals(pd.DataFrame({'a': [12, 2], 'b': [4, 2]}, index=[0, 2]))
    assert candidate(pd.DataFrame({'a': [1, 3, 23], 'b': [4, 4, 2]})).equals(pd.DataFrame({'a': [1, 23], 'b': [4, 2]}, index=[0, 2]))
    assert candidate(pd.DataFrame({'a': [1, 33, 2], 'b': [4, 4, 2]})).equals(pd.DataFrame({'a': [1, 2], 'b': [4, 2]}, index=[0, 2]))
    assert candidate(pd.DataFrame({'a': [1, 23, 2], 'b': [4, 43, 2]})).equals(pd.DataFrame({'a': [1, 2], 'b': [4, 2]}, index=[0, 2]))
    assert candidate(pd.DataFrame({'a': [123, 3, 2], 'b': [4, 4, 2]})).equals(pd.DataFrame({'a': [123, 2], 'b': [4, 2]}, index=[0, 2]))
    assert candidate(pd.DataFrame({'a': [1, 3, 2], 'b': [4, 344, 2]})).equals(pd.DataFrame({'a': [1, 2], 'b': [4, 2]}, index=[0, 2]))
    assert candidate(pd.DataFrame({'a': [1, 3, 342], 'b': [4, 4, 2]})).equals(pd.DataFrame({'a': [1, 342], 'b': [4, 2]}, index=[0, 2]))
    assert candidate(pd.DataFrame({'a': [1, 3, 2], 'b': [4, 4, 234]})).equals(pd.DataFrame({'a': [1, 2], 'b': [4, 234]}, index=[0, 2]))
    assert candidate(pd.DataFrame({'a': [1, 3, 223], 'b': [4, 4, 2]})).equals(pd.DataFrame({'a': [1, 223], 'b': [4, 2]}, index=[0, 2]))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def extract_first_and_last_df(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  Extract first and last row of a dataframe in pandas

validator:
  table_test:
    function_name: extract_first_and_last_df
    test_cases:
    - ["`pd.DataFrame({'a': [1, 3, 2], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [12, 3, 2], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [1, 3, 23], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [1, 33, 2], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [1, 23, 2], 'b': [4, 43, 2]})`"]
    - ["`pd.DataFrame({'a': [123, 3, 2], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [1, 3, 2], 'b': [4, 344, 2]})`"]
    - ["`pd.DataFrame({'a': [1, 3, 342], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [1, 3, 2], 'b': [4, 4, 234]})`"]
    - ["`pd.DataFrame({'a': [1, 3, 223], 'b': [4, 4, 2]})`"]
"""

def extract_first_and_last_df(df):
    return df.iloc[[0, -1]]
