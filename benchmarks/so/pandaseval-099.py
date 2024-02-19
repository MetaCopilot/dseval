'''
### Prompt ###

import pandas as pd
import numpy as np

def find_non_numeric_rows(df):
    # Finding non-numeric rows in dataframe in pandas
    # Return the raws that contain non-numeric values
    # So to get the subDataFrame of rouges, (Note: the negation, ~, of the above finds the ones which have at least one rogue non-numeric):

### Solution ###

    return df[~df.applymap(np.isreal).all(1)]

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,'bad',500]})).equals(pd.DataFrame({'A':[2], 'B':['bad']}, index=[1]))
    assert candidate(pd.DataFrame({'A':[21,2,3], 'B':[100,'bad',500]})).equals(pd.DataFrame({'A':[2], 'B':['bad']}, index=[1]))
    assert candidate(pd.DataFrame({'A':[1,2,32], 'B':[100,'bad',500]})).equals(pd.DataFrame({'A':[2], 'B':['bad']}, index=[1]))
    assert candidate(pd.DataFrame({'A':[121,2,3], 'B':[100,'bad',500]})).equals(pd.DataFrame({'A':[2], 'B':['bad']}, index=[1]))
    assert candidate(pd.DataFrame({'A':[1,21,3], 'B':[100,'bad',500]})).equals(pd.DataFrame({'A':[21], 'B':['bad']}, index=[1]))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,'bads',500]})).equals(pd.DataFrame({'A':[2], 'B':['bads']}, index=[1]))
    assert candidate(pd.DataFrame({'A':[12,2,3], 'B':[100,'bad',3500]})).equals(pd.DataFrame({'A':[2], 'B':['bad']}, index=[1]))
    assert candidate(pd.DataFrame({'A':[11,2,3], 'B':[100,'bad',500]})).equals(pd.DataFrame({'A':[2], 'B':['bad']}, index=[1]))
    assert candidate(pd.DataFrame({'A':[1,2,32], 'B':[100,'bad',2500]})).equals(pd.DataFrame({'A':[2], 'B':['bad']}, index=[1]))
    assert candidate(pd.DataFrame({'A':[1,42,3], 'B':[100,'good',500]})).equals(pd.DataFrame({'A':[42], 'B':['good']}, index=[1]))
'''

# %%
import pandas as pd
import numpy as np

# %%

"""
question: |
  Write a function `def find_non_numeric_rows(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  Finding non-numeric rows in dataframe in pandas
  Return the rows that contain non-numeric values

validator:
  table_test:
    function_name: find_non_numeric_rows
    test_cases:
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,'bad',500]})`"]
    - ["`pd.DataFrame({'A':[21,2,3], 'B':[100,'bad',500]})`"]
    - ["`pd.DataFrame({'A':[1,2,32], 'B':[100,'bad',500]})`"]
    - ["`pd.DataFrame({'A':[121,2,3], 'B':[100,'bad',500]})`"]
    - ["`pd.DataFrame({'A':[1,21,3], 'B':[100,'bad',500]})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,'bads',500]})`"]
    - ["`pd.DataFrame({'A':[12,2,3], 'B':[100,'bad',3500]})`"]
    - ["`pd.DataFrame({'A':[11,2,3], 'B':[100,'bad',500]})`"]
    - ["`pd.DataFrame({'A':[1,2,32], 'B':[100,'bad',2500]})`"]
    - ["`pd.DataFrame({'A':[1,42,3], 'B':[100,'good',500]})`"]
"""

def find_non_numeric_rows(df):
    return df[~df.applymap(np.isreal).all(1)]
