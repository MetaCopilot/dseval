'''
### Prompt ###

import pandas as pd

def combine_df(df1, df2):
    # How do I combine two dataframes with ignore index? Return the concated dataframe.

### Solution ###

    return df1.append(df2, ignore_index=True)

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [1, 2]}), pd.DataFrame({'A': [4, 5]})).equals(pd.DataFrame({'A': [1, 2, 4, 5]}))
    assert candidate(pd.DataFrame({'A': [1, 2]}), pd.DataFrame({'A': [4, 6]})).equals(pd.DataFrame({'A': [1, 2, 4, 6]}))
    assert candidate(pd.DataFrame({'A': [1, 4]}), pd.DataFrame({'A': [4, 5]})).equals(pd.DataFrame({'A': [1, 4, 4, 5]}))
    assert candidate(pd.DataFrame({'A': [3, 4]}), pd.DataFrame({'A': [4, 5]})).equals(pd.DataFrame({'A': [3, 4, 4, 5]}))
    assert candidate(pd.DataFrame({'A': [5, 2]}), pd.DataFrame({'A': [4, 5]})).equals(pd.DataFrame({'A': [5, 2, 4, 5]}))
    assert candidate(pd.DataFrame({'A': [4, 2]}), pd.DataFrame({'A': [4, 5]})).equals(pd.DataFrame({'A': [4, 2, 4, 5]}))
    assert candidate(pd.DataFrame({'A': [6, 2]}), pd.DataFrame({'A': [9, 5]})).equals(pd.DataFrame({'A': [6, 2, 9, 5]}))
    assert candidate(pd.DataFrame({'A': [1, 7]}), pd.DataFrame({'A': [4, 5]})).equals(pd.DataFrame({'A': [1, 7, 4, 5]}))
    assert candidate(pd.DataFrame({'A': [6, 2]}), pd.DataFrame({'A': [4, 56]})).equals(pd.DataFrame({'A': [6, 2, 4, 56]}))
    assert candidate(pd.DataFrame({'A': [11, 22]}), pd.DataFrame({'A': [4, 5]})).equals(pd.DataFrame({'A': [11, 22, 4, 5]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def combine_df(df1, df2):` that takes two DataFrames and returns a DataFrame to solve the following problem:
  How do I combine two dataframes with ignore index?

validator:
  table_test:
    function_name: combine_df
    test_cases:
    - ["`pd.DataFrame({'A': [1, 2]})`", "`pd.DataFrame({'A': [4, 5]})`"]
    - ["`pd.DataFrame({'A': [1, 2]})`", "`pd.DataFrame({'A': [4, 6]})`"]
    - ["`pd.DataFrame({'A': [1, 4]})`", "`pd.DataFrame({'A': [4, 5]})`"]
    - ["`pd.DataFrame({'A': [3, 4]})`", "`pd.DataFrame({'A': [4, 5]})`"]
    - ["`pd.DataFrame({'A': [5, 2]})`", "`pd.DataFrame({'A': [4, 5]})`"]
    - ["`pd.DataFrame({'A': [4, 2]})`", "`pd.DataFrame({'A': [4, 5]})`"]
    - ["`pd.DataFrame({'A': [6, 2]})`", "`pd.DataFrame({'A': [9, 5]})`"]
    - ["`pd.DataFrame({'A': [1, 7]})`", "`pd.DataFrame({'A': [4, 5]})`"]
    - ["`pd.DataFrame({'A': [6, 2]})`", "`pd.DataFrame({'A': [4, 56]})`"]
    - ["`pd.DataFrame({'A': [11, 22]})`", "`pd.DataFrame({'A': [4, 5]})`"]
"""

def combine_df(df1, df2):
    return pd.concat([df1, df2], ignore_index=True)
