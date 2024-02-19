'''
### Prompt ###

import pandas as pd

def set_value_to_entire_col(df, value):
    # Set value to an entire column `B` of a pandas dataframe
    # Return the changed dataframe.

### Solution ###

    df = df.assign(B=value)
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]}), '1').equals(pd.DataFrame({'A': [1, 2, 3], 'B': ['1', '1', '1']}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [21, 300, 500]}), '1').equals(pd.DataFrame({'A': [1, 2, 3], 'B': ['1', '1', '1']}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [21, 31, 500]}), '1').equals(pd.DataFrame({'A': [1, 2, 3], 'B': ['1', '1', '1']}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [21, 300, 21]}), '1').equals(pd.DataFrame({'A': [1, 2, 3], 'B': ['1', '1', '1']}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [21, 300, 50]}), '1').equals(pd.DataFrame({'A': [1, 2, 3], 'B': ['1', '1', '1']}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [21, 312, 500]}), '1').equals(pd.DataFrame({'A': [1, 2, 3], 'B': ['1', '1', '1']}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [21, 301, 52]}), '1').equals(pd.DataFrame({'A': [1, 2, 3], 'B': ['1', '1', '1']}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [31, 3, 500]}), '1').equals(pd.DataFrame({'A': [1, 2, 3], 'B': ['1', '1', '1']}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [21, 30, 5]}), '1').equals(pd.DataFrame({'A': [1, 2, 3], 'B': ['1', '1', '1']}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [21, 13, 0]}), '1').equals(pd.DataFrame({'A': [1, 2, 3], 'B': ['1', '1', '1']}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def set_value_to_entire_col(df, value):` that takes a DataFrame and a value and returns a DataFrame to solve the following problem:
  Set value to an entire column `B` of a pandas dataframe

validator:
  table_test:
    function_name: set_value_to_entire_col
    test_cases:
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]})`", '1']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [21, 300, 500]})`", '1']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [21, 31, 500]})`", '1']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [21, 300, 21]})`", '1']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [21, 300, 50]})`", '1']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [21, 312, 500]})`", '1']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [21, 301, 52]})`", '1']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [31, 3, 500]})`", '1']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [21, 30, 5]})`", '1']
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [21, 13, 0]})`", '1']
"""

def set_value_to_entire_col(df, value):
    df = df.assign(B=value)
    return df
