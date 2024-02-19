'''
### Prompt ###

import pandas as pd

def change_col_names_of_df(df, origin_names, new_names):
    # How do I change the column labels of df？
    # And return the dataframe that has been renamed

### Solution ###

    return df.rename(columns={origin_names:new_names})

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame('x', index=range(3), columns=list('abcde')), 'a', 'Y').equals(pd.DataFrame('x', index=range(3), columns=list('Ybcde')))
    assert candidate(pd.DataFrame('x', index=range(3), columns=list('abcde')), 'a', 'Z').equals(pd.DataFrame('x', index=range(3), columns=list('Zbcde')))
    assert candidate(pd.DataFrame('x', index=range(3), columns=list('abcde')), 'a', 'W').equals(pd.DataFrame('x', index=range(3), columns=list('Wbcde')))
    assert candidate(pd.DataFrame('x', index=range(3), columns=list('abcde')), 'b', 'W').equals(pd.DataFrame('x', index=range(3), columns=list('aWcde')))
    assert candidate(pd.DataFrame('x', index=range(3), columns=list('abcde')), 'b', 'P').equals(pd.DataFrame('x', index=range(3), columns=list('aPcde')))
    assert candidate(pd.DataFrame('x', index=range(3), columns=list('abcde')), 'b', 'O').equals(pd.DataFrame('x', index=range(3), columns=list('aOcde')))
    assert candidate(pd.DataFrame('x', index=range(3), columns=list('abcde')), 'c', 'O').equals(pd.DataFrame('x', index=range(3), columns=list('abOde')))
    assert candidate(pd.DataFrame('x', index=range(3), columns=list('abcde')), 'd', 'O').equals(pd.DataFrame('x', index=range(3), columns=list('abcOe')))
    assert candidate(pd.DataFrame('x', index=range(3), columns=list('abcde')), 'd', 'E').equals(pd.DataFrame('x', index=range(3), columns=list('abcEe')))
    assert candidate(pd.DataFrame('x', index=range(3), columns=list('abcde')), 'e', 'E').equals(pd.DataFrame('x', index=range(3), columns=list('abcdE')))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def change_col_names_of_df(df, origin_name, new_name):` that takes a DataFrame, a original column name, and a new column name and returns a DataFrame to solve the following problem:
  How do I change the column labels of df？

validator:
  table_test:
    function_name: change_col_names_of_df
    test_cases:
    - ["`pd.DataFrame('x', index=range(3), columns=list('abcde'))`", a, Y]
    - ["`pd.DataFrame('x', index=range(3), columns=list('abcde'))`", a, Z]
    - ["`pd.DataFrame('x', index=range(3), columns=list('abcde'))`", a, W]
    - ["`pd.DataFrame('x', index=range(3), columns=list('abcde'))`", b, W]
    - ["`pd.DataFrame('x', index=range(3), columns=list('abcde'))`", b, P]
    - ["`pd.DataFrame('x', index=range(3), columns=list('abcde'))`", b, O]
    - ["`pd.DataFrame('x', index=range(3), columns=list('abcde'))`", c, O]
    - ["`pd.DataFrame('x', index=range(3), columns=list('abcde'))`", d, O]
    - ["`pd.DataFrame('x', index=range(3), columns=list('abcde'))`", d, E]
    - ["`pd.DataFrame('x', index=range(3), columns=list('abcde'))`", e, E]
"""

def change_col_names_of_df(df, origin_name, new_name):
    return df.rename(columns={origin_name:new_name})
