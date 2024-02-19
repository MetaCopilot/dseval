'''
### Prompt ###

import pandas as pd

def get_row_count(df):
    """
    Return the row count of df
    """

### Solution ###

    return len(df.index)

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a': [1, 2, 3, 4], 'b': [4, 5, 6, 7]})) == 4
    assert candidate(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})) == 3
    assert candidate(pd.DataFrame({'a': [1, 2, 5], 'b': [8, 5, 6]})) == 3
    assert candidate(pd.DataFrame({'a': [125, 2, 5], 'b': [683, 5, 6]})) == 3
    assert candidate(pd.DataFrame({'a': [125, 2], 'b': [5, 6]})) == 2
    assert candidate(pd.DataFrame({'a': [125, 5], 'b': [182, 513]})) == 2
    assert candidate(pd.DataFrame({'a': [125], 'b': [513]})) == 1
    assert candidate(pd.DataFrame({'a': [125, 1, 2, 3, 4], 'b': [513, 0, 0, 0, 0]})) == 5
    assert candidate(pd.DataFrame({'a': [125, 1, 2, 3, 4, 6], 'b': [513, 0, 0, 0, 0, 1]})) == 6
    assert candidate(pd.DataFrame({'a': [125, 1, 2, 3, 4, 6, 7], 'b': [513, 0, 0, 0, 0, 1, 2]})) == 7
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def get_row_count(df):` that takes a DataFrame and returns the row count of the DataFrame.

validator:
  table_test:
    function_name: get_row_count
    test_cases:
    - ["`pd.DataFrame({'a': [1, 2, 3, 4], 'b': [4, 5, 6, 7]})`"]
    - ["`pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})`"]
    - ["`pd.DataFrame({'a': [1, 2, 5], 'b': [8, 5, 6]})`"]
    - ["`pd.DataFrame({'a': [125, 2, 5], 'b': [683, 5, 6]})`"]
    - ["`pd.DataFrame({'a': [125, 2], 'b': [5, 6]})`"]
    - ["`pd.DataFrame({'a': [125, 5], 'b': [182, 513]})`"]
    - ["`pd.DataFrame({'a': [125], 'b': [513]})`"]
    - ["`pd.DataFrame({'a': [125, 1, 2, 3, 4], 'b': [513, 0, 0, 0, 0]})`"]
    - ["`pd.DataFrame({'a': [125, 1, 2, 3, 4, 6], 'b': [513, 0, 0, 0, 0, 1]})`"]
    - ["`pd.DataFrame({'a': [125, 1, 2, 3, 4, 6, 7], 'b': [513, 0, 0, 0, 0, 1, 2]})`"]
"""

def get_row_count(df):
    return len(df.index)
