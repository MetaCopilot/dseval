'''
### Prompt ###

import pandas as pd
def creating_df_with_same_as_other(df_original):
    # creating a new dataframe of all same with df_original one, but no any rows
    # return the new dataframe

### Solution ###

    df_copy = df_original.iloc[:0,:].copy()
    return df_copy

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]})).equals(pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]}).iloc[:0,:].copy())
    assert candidate(pd.DataFrame({'A': [1, 0, 3], 'B': [100, 300, 500]})).equals(pd.DataFrame({'A': [1, 0, 3], 'B': [100, 300, 500]}).iloc[:0,:].copy())
    assert candidate(pd.DataFrame({'A': [5, 0, 3], 'B': [100, 300, 500]})).equals(pd.DataFrame({'A': [5, 0, 3], 'B': [100, 300, 500]}).iloc[:0,:].copy())
    assert candidate(pd.DataFrame({'A': [5, 2, 3], 'B': [100, 300, 500]})).equals(pd.DataFrame({'A': [5, 2, 3], 'B': [100, 300, 500]}).iloc[:0,:].copy())
    assert candidate(pd.DataFrame({'A': [5, 2, 1], 'B': [100, 300, 500]})).equals(pd.DataFrame({'A': [5, 2, 1], 'B': [100, 300, 500]}).iloc[:0,:].copy())
    assert candidate(pd.DataFrame({'A': [5, 2, 1], 'B': [500, 300, 500]})).equals(pd.DataFrame({'A': [5, 2, 1], 'B': [500, 300, 500]}).iloc[:0,:].copy())
    assert candidate(pd.DataFrame({'A': [5, 2, 1], 'B': [500, 200, 500]})).equals(pd.DataFrame({'A': [5, 2, 1], 'B': [500, 200, 500]}).iloc[:0,:].copy())
    assert candidate(pd.DataFrame({'A': [5, 2, 1], 'B': [500, 200, 100]})).equals(pd.DataFrame({'A': [5, 2, 1], 'B': [500, 200, 100]}).iloc[:0,:].copy())
    assert candidate(pd.DataFrame({'A': [5, 20, 1], 'B': [500, 200, 100]})).equals(pd.DataFrame({'A': [5, 20, 1], 'B': [500, 200, 100]}).iloc[:0,:].copy())
    assert candidate(pd.DataFrame({'A': [50, 20, 1], 'B': [500, 200, 100]})).equals(pd.DataFrame({'A': [50, 20, 1], 'B': [500, 200, 100]}).iloc[:0,:].copy())
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def creating_df_with_same_as_other(df_original):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  creating a new dataframe of all same with df_original one, but no any rows

validator:
  table_test:
    function_name: creating_df_with_same_as_other
    test_cases:
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]})`"]
    - ["`pd.DataFrame({'A': [1, 0, 3], 'B': [100, 300, 500]})`"]
    - ["`pd.DataFrame({'A': [5, 0, 3], 'B': [100, 300, 500]})`"]
    - ["`pd.DataFrame({'A': [5, 2, 3], 'B': [100, 300, 500]})`"]
    - ["`pd.DataFrame({'A': [5, 2, 1], 'B': [100, 300, 500]})`"]
    - ["`pd.DataFrame({'A': [5, 2, 1], 'B': [500, 300, 500]})`"]
    - ["`pd.DataFrame({'A': [5, 2, 1], 'B': [500, 200, 500]})`"]
    - ["`pd.DataFrame({'A': [5, 2, 1], 'B': [500, 200, 100]})`"]
    - ["`pd.DataFrame({'A': [5, 20, 1], 'B': [500, 200, 100]})`"]
    - ["`pd.DataFrame({'A': [50, 20, 1], 'B': [500, 200, 100]})`"]
"""

def creating_df_with_same_as_other(df_original):
    df_copy = df_original.iloc[:0,:].copy()
    return df_copy
