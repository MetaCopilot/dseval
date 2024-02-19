'''
### Prompt ###

import pandas as pd

def select_multiple_columns(df, columns):
    # How do I select the given columns and return the new DataFrame?

### Solution ###

    return df[columns]

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a': [2, 3], 'b': [4, 5], 'c': [6, 7]}), ['a', 'b']).equals(pd.DataFrame({'a': [2, 3], 'b': [4, 5]}))
    assert candidate(pd.DataFrame({'a': [3, 3], 'b': [4, 5], 'c': [6, 7]}), ['a', 'b']).equals(pd.DataFrame({'a': [3, 3], 'b': [4, 5]}))
    assert candidate(pd.DataFrame({'a': [3, 3], 'b': [2, 5], 'c': [6, 7]}), ['a', 'b']).equals(pd.DataFrame({'a': [3, 3], 'b': [2, 5]}))
    assert candidate(pd.DataFrame({'a': [3, 3], 'b': [2, 5], 'c': [9, 7]}), ['a', 'b']).equals(pd.DataFrame({'a': [3, 3], 'b': [2, 5]}))
    assert candidate(pd.DataFrame({'a': [3, 3], 'b': [2, 10], 'c': [9, 7]}), ['a', 'b']).equals(pd.DataFrame({'a': [3, 3], 'b': [2, 10]}))
    assert candidate(pd.DataFrame({'a': [3, 3], 'b': [2, 10], 'c': [9, 7]}), ['a', 'c']).equals(pd.DataFrame({'a': [3, 3], 'c': [9, 7]}))
    assert candidate(pd.DataFrame({'a': [3, 3], 'b': [2, 10], 'c': [9, 88]}), ['a', 'c']).equals(pd.DataFrame({'a': [3, 3], 'c': [9, 88]}))
    assert candidate(pd.DataFrame({'a': [3, 3], 'b': [2, 10], 'c': [75, 88]}), ['a', 'c']).equals(pd.DataFrame({'a': [3, 3], 'c': [75, 88]}))
    assert candidate(pd.DataFrame({'a': [3, 3], 'b': [2, 10], 'c': [75, 88]}), ['b', 'c']).equals(pd.DataFrame({'b': [2, 10], 'c': [75, 88]}))
    assert candidate(pd.DataFrame({'a': [3, 3], 'b': [55, 10], 'c': [75, 88]}), ['b', 'c']).equals(pd.DataFrame({'b': [55, 10], 'c': [75, 88]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def select_multiple_columns(df, columns):` that takes a DataFrame and a list of column names and returns a DataFrame to solve the following problem:
  How do I select the given columns and return the new DataFrame?

validator:
  table_test:
    function_name: select_multiple_columns
    test_cases:
    - ["`pd.DataFrame({'a': [2, 3], 'b': [4, 5], 'c': [6, 7]})`", ['a', 'b']]
    - ["`pd.DataFrame({'a': [3, 3], 'b': [4, 5], 'c': [6, 7]})`", ['a', 'b']]
    - ["`pd.DataFrame({'a': [3, 3], 'b': [2, 5], 'c': [6, 7]})`", ['a', 'b']]
    - ["`pd.DataFrame({'a': [3, 3], 'b': [2, 5], 'c': [9, 7]})`", ['a', 'b']]
    - ["`pd.DataFrame({'a': [3, 3], 'b': [2, 10], 'c': [9, 7]})`", ['a', 'b']]
    - ["`pd.DataFrame({'a': [3, 3], 'b': [2, 10], 'c': [9, 7]})`", ['a', 'c']]
    - ["`pd.DataFrame({'a': [3, 3], 'b': [2, 10], 'c': [9, 88]})`", ['a', 'c']]
    - ["`pd.DataFrame({'a': [3, 3], 'b': [2, 10], 'c': [75, 88]})`", ['a', 'c']]
    - ["`pd.DataFrame({'a': [3, 3], 'b': [2, 10], 'c': [75, 88]})`", ['b', 'c']]
    - ["`pd.DataFrame({'a': [3, 3], 'b': [55, 10], 'c': [75, 88]})`", ['b', 'c']]
"""

def select_multiple_columns(df, columns):
    return df[columns]
