'''
### Prompt ###

import pandas as pd
import numpy as np

def shift_column_up_by_one(df):
    # Shift column in pandas dataframe up by one?
    # In detail, in 'gdp' column, shift up by one and return dataframe with the changed gdp column.

### Solution ###

df['gdp'] = df['gdp'].shift(1)
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'y': [1,2],'gdp': [2.0,4.0],'cap': [8, 7]})).equals(pd.DataFrame({'y': [1,2],'gdp': [np.nan,2.0],'cap': [8, 7]}))
    assert candidate(pd.DataFrame({'y': [1,2],'gdp': [2.0,4.0],'cap': [9, 7]})).equals(pd.DataFrame({'y': [1,2],'gdp': [np.nan,2.0],'cap': [9, 7]}))
    assert candidate(pd.DataFrame({'y': [1,2],'gdp': [2.0,4.0],'cap': [9, 3]})).equals(pd.DataFrame({'y': [1,2],'gdp': [np.nan,2.0],'cap': [9, 3]}))
    assert candidate(pd.DataFrame({'y': [1,2],'gdp': [3.0,4.0],'cap': [9, 3]})).equals(pd.DataFrame({'y': [1,2],'gdp': [np.nan,3.0],'cap': [9, 3]}))
    assert candidate(pd.DataFrame({'y': [5,2],'gdp': [3.0,4.0],'cap': [9, 3]})).equals(pd.DataFrame({'y': [5,2],'gdp': [np.nan,3.0],'cap': [9, 3]}))
    assert candidate(pd.DataFrame({'y': [5,1],'gdp': [3.0,4.0],'cap': [9, 3]})).equals(pd.DataFrame({'y': [5,1],'gdp': [np.nan,3.0],'cap': [9, 3]}))
    assert candidate(pd.DataFrame({'y': [5,1],'gdp': [3.0,8.0],'cap': [9, 3]})).equals(pd.DataFrame({'y': [5,1],'gdp': [np.nan,3.0],'cap': [9, 3]}))
    assert candidate(pd.DataFrame({'y': [5,1],'gdp': [3.0,8.0],'cap': [19, 3]})).equals(pd.DataFrame({'y': [5,1],'gdp': [np.nan,3.0],'cap': [19, 3]}))
    assert candidate(pd.DataFrame({'y': [5,1],'gdp': [3.0,8.0],'cap': [19, 13]})).equals(pd.DataFrame({'y': [5,1],'gdp': [np.nan,3.0],'cap': [19, 13]}))
    assert candidate(pd.DataFrame({'y': [5,1],'gdp': [13.0,8.0],'cap': [19, 13]})).equals(pd.DataFrame({'y': [5,1],'gdp': [np.nan,13.0],'cap': [19, 13]}))
'''

# %%
import pandas as pd
import numpy as np

# %%

"""
question: |
  Write a function `def shift_column_up_by_one(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  Shift column in pandas dataframe up by one? (up means towards the tail of the dataframe)
  In detail, in 'gdp' column, shift up by one and return dataframe with the changed gdp column.

validator:
  table_test:
    function_name: shift_column_up_by_one
    test_cases:
    - ["`pd.DataFrame({'y': [1,2],'gdp': [2.0,4.0],'cap': [8, 7]})`"]
    - ["`pd.DataFrame({'y': [1,2],'gdp': [2.0,4.0],'cap': [9, 7]})`"]
    - ["`pd.DataFrame({'y': [1,2],'gdp': [2.0,4.0],'cap': [9, 3]})`"]
    - ["`pd.DataFrame({'y': [1,2],'gdp': [3.0,4.0],'cap': [9, 3]})`"]
    - ["`pd.DataFrame({'y': [5,2],'gdp': [3.0,4.0],'cap': [9, 3]})`"]
    - ["`pd.DataFrame({'y': [5,1],'gdp': [3.0,4.0],'cap': [9, 3]})`"]
    - ["`pd.DataFrame({'y': [5,1],'gdp': [3.0,8.0],'cap': [9, 3]})`"]
    - ["`pd.DataFrame({'y': [5,1],'gdp': [3.0,8.0],'cap': [19, 3]})`"]
    - ["`pd.DataFrame({'y': [5,1],'gdp': [3.0,8.0],'cap': [19, 13]})`"]
    - ["`pd.DataFrame({'y': [5,1],'gdp': [13.0,8.0],'cap': [19, 13]})`"]
"""

def shift_column_up_by_one(df):
    df['gdp'] = df['gdp'].shift(1)
    return df
