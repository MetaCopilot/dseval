'''
### Prompt ###

import pandas as pd

def convert_bool_to_int(df, col_name):
    # How can I map True/False to 1/0 in a Pandas DataFrame?
    # return the dataframe with the column converted to int

### Solution ###

    df[col_name] = df[col_name].astype(int)
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[True,True,False]}), 'B').equals(pd.DataFrame({'A':[1,2,3], 'B':[1,1,0]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[True,True,True]}), 'B').equals(pd.DataFrame({'A':[1,2,3], 'B':[1,1,1]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[True,False,False]}), 'B').equals(pd.DataFrame({'A':[1,2,3], 'B':[1,0,0]}))
    assert candidate(pd.DataFrame({'A':[1,2,33], 'B':[True,True,False]}), 'B').equals(pd.DataFrame({'A':[1,2,33], 'B':[1,1,0]}))
    assert candidate(pd.DataFrame({'A':[1,22,3], 'B':[True,True,False]}), 'B').equals(pd.DataFrame({'A':[1,22,3], 'B':[1,1,0]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[False,True,False]}), 'B').equals(pd.DataFrame({'A':[1,2,3], 'B':[0,1,0]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[False,False,False]}), 'B').equals(pd.DataFrame({'A':[1,2,3], 'B':[0,0,0]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[False,False,True]}), 'B').equals(pd.DataFrame({'A':[1,2,3], 'B':[0,0,1]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[True,False,True]}), 'B').equals(pd.DataFrame({'A':[1,2,3], 'B':[1,0,1]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[True,True,True]}), 'B').equals(pd.DataFrame({'A':[1,2,3], 'B':[1,1,1]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def convert_bool_to_int(df, col_name):` that takes a DataFrame and a column name and returns a DataFrame to solve the following problem:
  How can I map True/False to 1/0 in a Pandas DataFrame?
  Return the dataframe with the column converted to int.

validator:
  table_test:
    function_name: convert_bool_to_int
    test_cases:
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[True,True,False]})`", B]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[True,True,True]})`", B]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[True,False,False]})`", B]
    - ["`pd.DataFrame({'A':[1,2,33], 'B':[True,True,False]})`", B]
    - ["`pd.DataFrame({'A':[1,22,3], 'B':[True,True,False]})`", B]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[False,True,False]})`", B]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[False,False,False]})`", B]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[False,False,True]})`", B]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[True,False,True]})`", B]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[True,True,True]})`", B]
"""

def convert_bool_to_int(df, col_name):
    df[col_name] = df[col_name].astype(int)
    return df
