'''
### Prompt ###

import pandas as pd
import numpy as np

def fill_none_with_zero(df, col_names):
    # Pandas dataframe fillna() only some columns in place
    # This function fills all columns with 0
    # Return the changed dataframe

### Solution ###

    df[col_names] = df[col_names].fillna(0)
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a': [1.0, 2.0, None], 'b': [4.0, 5.0, 6.0]}), ['a']).equals(pd.DataFrame({'a': [1.0, 2.0, 0.0], 'b': [4.0, 5.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [1.0, 2.0, None], 'b': [4.0, 5.0, 6.0]}), ['b']).equals(pd.DataFrame({'a': [1.0, 2.0, None], 'b': [4.0, 5.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [1.0, 2.0, None], 'b': [4.0, 5.0, 6.0]}), ['a', 'b']).equals(pd.DataFrame({'a': [1.0, 2.0, 0.0], 'b': [4.0, 5.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [4.0, 2.0, None], 'b': [4.0, 5.0, 6.0]}), ['a', 'b']).equals(pd.DataFrame({'a': [4.0, 2.0, 0.0], 'b': [4.0, 5.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [1.0, 4.0, None], 'b': [4.0, 5.0, 6.0]}), ['a', 'b']).equals(pd.DataFrame({'a': [1.0, 4.0, 0.0], 'b': [4.0, 5.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [1.0, 2.0, None], 'b': [42.0, 5.0, 6.0]}), ['a', 'b']).equals(pd.DataFrame({'a': [1.0, 2.0, 0.0], 'b': [42.0, 5.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [1.0, 2.0, None], 'b': [4.0, 52.0, 62.0]}), ['a', 'b']).equals(pd.DataFrame({'a': [1.0, 2.0, 0.0], 'b': [4.0, 52.0, 62.0]}))
    assert candidate(pd.DataFrame({'a': [11.0, 21.0, None], 'b': [4.0, 5.0, 6.0]}), ['a', 'b']).equals(pd.DataFrame({'a': [11.0, 21.0, 0.0], 'b': [4.0, 5.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [1.0, 2.0, None], 'b': [4.0, 15.0, 16.0]}), ['a', 'b']).equals(pd.DataFrame({'a': [1.0, 2.0, 0.0], 'b': [4.0, 15.0, 16.0]}))
    assert candidate(pd.DataFrame({'a': [1.0, 23.0, None], 'b': [43.0, 5.0, 6.0]}), ['a', 'b']).equals(pd.DataFrame({'a': [1.0, 23.0, 0.0], 'b': [43.0, 5.0, 6.0]}))
'''

# %%
import pandas as pd
import numpy as np

# %%

"""
question: |
  Write a function `def fill_none_with_zero(df, col_names):` that takes a DataFrame and a list of column names and returns a DataFrame to solve the following problem:
  Pandas dataframe fillna() only some columns in place
  This function fills all columns with 0

validator:
  table_test:
    function_name: fill_none_with_zero
    test_cases:
    - ["`pd.DataFrame({'a': [1.0, 2.0, None], 'b': [4.0, 5.0, 6.0]})`", ['a']]
    - ["`pd.DataFrame({'a': [1.0, 2.0, None], 'b': [4.0, 5.0, 6.0]})`", ['b']]
    - ["`pd.DataFrame({'a': [1.0, 2.0, None], 'b': [4.0, 5.0, 6.0]})`", ['a', 'b']]
    - ["`pd.DataFrame({'a': [4.0, 2.0, None], 'b': [4.0, 5.0, 6.0]})`", ['a', 'b']]
    - ["`pd.DataFrame({'a': [1.0, 4.0, None], 'b': [4.0, 5.0, 6.0]})`", ['a', 'b']]
    - ["`pd.DataFrame({'a': [1.0, 2.0, None], 'b': [42.0, 5.0, 6.0]})`", ['a', 'b']]
    - ["`pd.DataFrame({'a': [1.0, 2.0, None], 'b': [4.0, 52.0, 62.0]})`", ['a', 'b']]
    - ["`pd.DataFrame({'a': [11.0, 21.0, None], 'b': [4.0, 5.0, 6.0]})`", ['a', 'b']]
    - ["`pd.DataFrame({'a': [1.0, 2.0, None], 'b': [4.0, 15.0, 16.0]})`", ['a', 'b']]
    - ["`pd.DataFrame({'a': [1.0, 23.0, None], 'b': [43.0, 5.0, 6.0]})`", ['a', 'b']]
"""

def fill_none_with_zero(df, col_names):
    df[col_names] = df[col_names].fillna(0)
    return df
