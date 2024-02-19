'''
### Prompt ###

import pandas as pd

def concat_df(df1, df2):
    # Given that all the dataframes have the same columns, you can simply concat them:
    # return the concated dataframe

### Solution ###

    return pd.concat([df1, df2])

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a': [1, 2], 'b': [4, 2]}), pd.DataFrame({'a': [6, 7], 'b': [9, 6]})).equals(pd.DataFrame({'a': [1, 2, 6, 7], 'b': [4, 2, 9, 6]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'a': [1, 3], 'b': [4, 2]}), pd.DataFrame({'a': [6, 7], 'b': [9, 6]})).equals(pd.DataFrame({'a': [1, 3, 6, 7], 'b': [4, 2, 9, 6]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'a': [1, 3], 'b': [43, 2]}), pd.DataFrame({'a': [6, 7], 'b': [9, 6]})).equals(pd.DataFrame({'a': [1, 3, 6, 7], 'b': [43, 2, 9, 6]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'a': [1, 3], 'b': [43, 32]}), pd.DataFrame({'a': [6, 7], 'b': [9, 6]})).equals(pd.DataFrame({'a': [1, 3, 6, 7], 'b': [43, 32, 9, 6]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'a': [1, 3], 'b': [43, 32]}), pd.DataFrame({'a': [62, 7], 'b': [9, 6]})).equals(pd.DataFrame({'a': [1, 3, 62, 7], 'b': [43, 32, 9, 6]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'a': [1, 333], 'b': [43, 32]}), pd.DataFrame({'a': [62, 7], 'b': [9, 6]})).equals(pd.DataFrame({'a': [1, 333, 62, 7], 'b': [43, 32, 9, 6]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'a': [1, 3], 'b': [43, 32]}), pd.DataFrame({'a': [62, 7], 'b': [9, 66]})).equals(pd.DataFrame({'a': [1, 3, 62, 7], 'b': [43, 32, 9, 66]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'a': [1, 3], 'b': [43, 32]}), pd.DataFrame({'a': [62, 7], 'b': [99, 6]})).equals(pd.DataFrame({'a': [1, 3, 62, 7], 'b': [43, 32, 99, 6]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'a': [1, 3], 'b': [43, 32]}), pd.DataFrame({'a': [62, 77], 'b': [9, 6]})).equals(pd.DataFrame({'a': [1, 3, 62, 77], 'b': [43, 32, 9, 6]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'a': [1, 3], 'b': [43, 32]}), pd.DataFrame({'a': [62, 70], 'b': [9, 6]})).equals(pd.DataFrame({'a': [1, 3, 62, 70], 'b': [43, 32, 9, 6]}, index=[0, 1, 0, 1]))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def concat_df(df1, df2):` that takes two DataFrames with the same columns and returns a DataFrame to solve the following problem:
  Given that all the dataframes have the same columns, you can simply concat them.

validator:
  table_test:
    function_name: concat_df
    test_cases:
    - ["`pd.DataFrame({'a': [1, 2], 'b': [4, 2]})`", "`pd.DataFrame({'a': [6, 7], 'b': [9, 6]})`"]
    - ["`pd.DataFrame({'a': [1, 3], 'b': [4, 2]})`", "`pd.DataFrame({'a': [6, 7], 'b': [9, 6]})`"]
    - ["`pd.DataFrame({'a': [1, 3], 'b': [43, 2]})`", "`pd.DataFrame({'a': [6, 7], 'b': [9, 6]})`"]
    - ["`pd.DataFrame({'a': [1, 3], 'b': [43, 32]})`", "`pd.DataFrame({'a': [6, 7], 'b': [9, 6]})`"]
    - ["`pd.DataFrame({'a': [1, 3], 'b': [43, 32]})`", "`pd.DataFrame({'a': [62, 7], 'b': [9, 6]})`"]
    - ["`pd.DataFrame({'a': [1, 333], 'b': [43, 32]})`", "`pd.DataFrame({'a': [62, 7], 'b': [9, 6]})`"]
    - ["`pd.DataFrame({'a': [1, 3], 'b': [43, 32]})`", "`pd.DataFrame({'a': [62, 7], 'b': [9, 66]})`"]
    - ["`pd.DataFrame({'a': [1, 3], 'b': [43, 32]})`", "`pd.DataFrame({'a': [62, 7], 'b': [99, 6]})`"]
    - ["`pd.DataFrame({'a': [1, 3], 'b': [43, 32]})`", "`pd.DataFrame({'a': [62, 77], 'b': [9, 6]})`"]
    - ["`pd.DataFrame({'a': [1, 3], 'b': [43, 32]})`", "`pd.DataFrame({'a': [62, 70], 'b': [9, 6]})`"]
"""

def concat_df(df1, df2):
    return pd.concat([df1, df2])
