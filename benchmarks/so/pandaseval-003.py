'''
### Prompt ###

import pandas as pd

def add_zeros_to_string(df, col_name):
    # Add Leading Zeros to Strings at `col_name` in Pandas Dataframe
    # The maximum length of the string is 15
    # Return the dataframe

### Solution ###

    df[col_name] = df[col_name].apply(lambda x: '{0:0>15}'.format(x))
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [1234556,3456], 'B': ["abc", "def"]}), "A").equals(pd.DataFrame({'A': ['000000001234556', '000000000003456'], 'B': ["abc", "def"]}))
    assert candidate(pd.DataFrame({'A': [1234556,3456], 'B': ['abc', 'ddd']}), 'A').equals(pd.DataFrame({'A': ['000000001234556', '000000000003456'], 'B': ['abc', 'ddd']}))
    assert candidate(pd.DataFrame({'A': [1234556,3456], 'B': ['rsc', 'ddd']}), 'A').equals(pd.DataFrame({'A': ['000000001234556', '000000000003456'], 'B': ['rsc', 'ddd']}))
    assert candidate(pd.DataFrame({'A': [1234556,34561], 'B': ['rsc', 'ddd']}), 'A').equals(pd.DataFrame({'A': ['000000001234556', '000000000034561'], 'B': ['rsc', 'ddd']}))
    assert candidate(pd.DataFrame({'A': [1234553,34561], 'B': ['rsc', 'ddd']}), 'A').equals(pd.DataFrame({'A': ['000000001234553', '000000000034561'], 'B': ['rsc', 'ddd']}))
    assert candidate(pd.DataFrame({'A': [1234553,34561], 'B': ['aaa', 'ddd']}), 'A').equals(pd.DataFrame({'A': ['000000001234553', '000000000034561'], 'B': ['aaa', 'ddd']}))
    assert candidate(pd.DataFrame({'A': [1234553,34561], 'B': ['aaa', 'cas']}), 'A').equals(pd.DataFrame({'A': ['000000001234553', '000000000034561'], 'B': ['aaa', 'cas']}))
    assert candidate(pd.DataFrame({'A': [1234553,34561], 'B': ['csd', 'cas']}), 'A').equals(pd.DataFrame({'A': ['000000001234553', '000000000034561'], 'B': ['csd', 'cas']}))
    assert candidate(pd.DataFrame({'A': [1234553,34561], 'B': ['rrr', 'cas']}), 'A').equals(pd.DataFrame({'A': ['000000001234553', '000000000034561'], 'B': ['rrr', 'cas']}))
    assert candidate(pd.DataFrame({'A': [1234553,34561], 'B': ['rrr', 'ras']}), 'A').equals(pd.DataFrame({'A': ['000000001234553', '000000000034561'], 'B': ['rrr', 'ras']}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def add_zeros_to_string(df, col_name):` that takes a DataFrame and a column name and returns a DataFrame to solve the following problem:
  Add Leading Zeros to Strings at `col_name` in Pandas Dataframe
  The maximum length of the string is 15

validator:
  table_test:
    function_name: add_zeros_to_string
    test_cases:
    - ["`pd.DataFrame({'A': [1234556,3456], 'B': ['abc', 'def']})`", "A"]
    - ["`pd.DataFrame({'A': [1234556,3456], 'B': ['abc', 'ddd']})`", "A"]
    - ["`pd.DataFrame({'A': [1234556,3456], 'B': ['rsc', 'ddd']})`", "A"]
    - ["`pd.DataFrame({'A': [1234556,34561], 'B': ['rsc', 'ddd']})`", "A"]
    - ["`pd.DataFrame({'A': [1234553,34561], 'B': ['rsc', 'ddd']})`", "A"]
    - ["`pd.DataFrame({'A': [1234553,34561], 'B': ['aaa', 'ddd']})`", "A"]
    - ["`pd.DataFrame({'A': [1234553,34561], 'B': ['aaa', 'cas']})`", "A"]
    - ["`pd.DataFrame({'A': [1234553,34561], 'B': ['csd', 'cas']})`", "A"]
    - ["`pd.DataFrame({'A': [1234553,34561], 'B': ['rrr', 'cas']})`", "A"]
    - ["`pd.DataFrame({'A': [1234553,34561], 'B': ['rrr', 'ras']})`", "A"]
"""

def add_zeros_to_string(df, col_name):
    df[col_name] = df[col_name].apply(lambda x: '{0:0>15}'.format(x))
    return df
