'''
### Prompt ###

import pandas as pd
import numpy as np

def display_rows_with_gt_1_nan(df):
    # Return the dataframe with the rows with one or more NaN values

### Solution ###

    return df[df.isna().any(axis=1)]

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a': [np.nan, 3, 2], 'b': [4, 4, 2]})).equals(pd.DataFrame({'a': [np.nan], 'b': [4]}, index=[0]))
    assert candidate(pd.DataFrame({'a': [np.nan, 3, 2], 'b': [5, 4, 2]})).equals(pd.DataFrame({'a': [np.nan], 'b': [5]}, index=[0]))
    assert candidate(pd.DataFrame({'a': [np.nan, 332, 2], 'b': [4, 4, 2]})).equals(pd.DataFrame({'a': [np.nan], 'b': [4]}, index=[0]))
    assert candidate(pd.DataFrame({'a': [np.nan, 3, 2], 'b': [4, 4122, 2]})).equals(pd.DataFrame({'a': [np.nan], 'b': [4]}, index=[0]))
    assert candidate(pd.DataFrame({'a': [np.nan, 3, 2], 'b': [4, 4, 2123]})).equals(pd.DataFrame({'a': [np.nan], 'b': [4]}, index=[0]))
    assert candidate(pd.DataFrame({'a': [np.nan, 31, 22], 'b': [4, 4, 2]})).equals(pd.DataFrame({'a': [np.nan], 'b': [4]}, index=[0]))
    assert candidate(pd.DataFrame({'a': [np.nan, 3, 2], 'b': [4, 34, 22]})).equals(pd.DataFrame({'a': [np.nan], 'b': [4]}, index=[0]))
    assert candidate(pd.DataFrame({'a': [np.nan, 31, 12], 'b': [4, 4, 2]})).equals(pd.DataFrame({'a': [np.nan], 'b': [4]}, index=[0]))
    assert candidate(pd.DataFrame({'a': [np.nan, 3, 2], 'b': [14, 14, 12]})).equals(pd.DataFrame({'a': [np.nan], 'b': [4]}, index=[0]))
    assert candidate(pd.DataFrame({'a': [np.nan, 33, 32], 'b': [4, 4, 2]})).equals(pd.DataFrame({'a': [np.nan], 'b': [4]}, index=[0]))
'''

# %%
import pandas as pd
import numpy as np

# %%

"""
question: |
  Write a function `def display_rows_with_gt_1_nan(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  Return the dataframe with the rows with one or more NaN values.

validator:
  table_test:
    function_name: display_rows_with_gt_1_nan
    test_cases:
    - ["`pd.DataFrame({'a': [np.nan, 3, 2], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [np.nan, 3, 2], 'b': [5, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [np.nan, 332, 2], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [np.nan, 3, 2], 'b': [4, 4122, 2]})`"]
    - ["`pd.DataFrame({'a': [np.nan, 3, 2], 'b': [4, 4, 2123]})`"]
    - ["`pd.DataFrame({'a': [np.nan, 31, 22], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [np.nan, 3, 2], 'b': [4, 34, 22]})`"]
    - ["`pd.DataFrame({'a': [np.nan, 31, 12], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [np.nan, 3, 2], 'b': [14, 14, 12]})`"]
    - ["`pd.DataFrame({'a': [np.nan, 33, 32], 'b': [4, 4, 2]})`"]
"""

def display_rows_with_gt_1_nan(df):
    return df[df.isna().any(axis=1)]
