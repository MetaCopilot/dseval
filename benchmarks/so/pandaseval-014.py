'''
### Prompt ###

import pandas as pd

def f(x):
    a = x['Value'].iat[2] - x['Value'].iat[1]
    b = x['Value'].iat[3] - x['Value'].iat[0]
    c = x['ID'].iat[2] + ' - ' + x['ID'].iat[1]
    d = x['ID'].iat[3] + ' - ' + x['ID'].iat[0]
    return pd.DataFrame({'Value': [a,b], 'ID':[c,d]})

def calculate_row_diff_groupwise(df):
    # I need to calculate the difference between two rows groupwise using pandas.
    # To calculate the sum I would use pandas.groupby('Group').sum(), but how do you calculate the difference between rows where the row ordering is important?
    # I think we need custom function with apply which return DataFrame for each group, for select by position is used iat:
    # Return the result

### Solution ###

    return df.groupby('Group').apply(f).reset_index(level=1, drop=True).reset_index()

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 5, 4], 'ID': ['dki', 'two', 'three', 'msra']})).equals(pd.DataFrame({'Group': ['M1', 'M1'], 'Value': [2, 1], 'ID': ['three - two', 'msra - dki']}))
    assert candidate(pd.DataFrame({'Group': ['Tom', 'Tom', 'Tom', 'Tom'], 'Value': [3, 3, 5, 4], 'ID': ['pku', 'dki', 'msra', 'thu']})).equals(pd.DataFrame({'Group': ['Tom', 'Tom'], 'Value': [2, 1], 'ID': ['msra - dki', 'thu - pku']}))
    assert candidate(pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 4], 'ID': ['dki', 'two', 'three', 'msra']})).equals(pd.DataFrame({'Group': ['M1', 'M1'], 'Value': [3, 1], 'ID': ['three - two', 'msra - dki']}))
    assert candidate(pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 4], 'ID': ['dki', 'four', 'three', 'msra']})).equals(pd.DataFrame({'Group': ['M1', 'M1'], 'Value': [3, 1], 'ID': ['three - four', 'msra - dki']}))
    assert candidate(pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 4], 'ID': ['dki', 'four', 'five', 'msra']})).equals(pd.DataFrame({'Group': ['M1', 'M1'], 'Value': [3, 1], 'ID': ['five - four', 'msra - dki']}))
    assert candidate(pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 4], 'ID': ['dki', 'four', 'five', 'ucas']})).equals(pd.DataFrame({'Group': ['M1', 'M1'], 'Value': [3, 1], 'ID': ['five - four', 'ucas - dki']}))
    assert candidate(pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 4], 'ID': ['iscas', 'four', 'five', 'ucas']})).equals(pd.DataFrame({'Group': ['M1', 'M1'], 'Value': [3, 1], 'ID': ['five - four', 'ucas - iscas']}))
    assert candidate(pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 5], 'ID': ['iscas', 'four', 'five', 'ucas']})).equals(pd.DataFrame({'Group': ['M1', 'M1'], 'Value': [3, 2], 'ID': ['five - four', 'ucas - iscas']}))
    assert candidate(pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 5], 'ID': ['iscas', 'four', 'five', 'PKU']})).equals(pd.DataFrame({'Group': ['M1', 'M1'], 'Value': [3, 2], 'ID': ['five - four', 'PKU - iscas']}))
    assert candidate(pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 5], 'ID': ['thu', 'four', 'five', 'PKU']})).equals(pd.DataFrame({'Group': ['M1', 'M1'], 'Value': [3, 2], 'ID': ['five - four', 'PKU - thu']}))
'''

# %%

import pandas as pd

def f(x):
    a = x['Value'].iat[2] - x['Value'].iat[1]
    b = x['Value'].iat[3] - x['Value'].iat[0]
    c = x['ID'].iat[2] + ' - ' + x['ID'].iat[1]
    d = x['ID'].iat[3] + ' - ' + x['ID'].iat[0]
    return pd.DataFrame({'Value': [a,b], 'ID':[c,d]})

# %%

"""
question: |
  Write a function `def calculate_row_diff_groupwise(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:

  I need to calculate the difference between two rows groupwise using pandas.
  To calculate the sum I would use pandas.groupby('Group').sum(), but how do you calculate the difference between rows where the row ordering is important?
  I think we need custom function with apply which return DataFrame for each group, for select by position is used iat:

validator:
  table_test:
    function_name: calculate_row_diff_groupwise
    test_cases:
    - ["`pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 5, 4], 'ID': ['dki', 'two', 'three', 'msra']})`"]
    - ["`pd.DataFrame({'Group': ['Tom', 'Tom', 'Tom', 'Tom'], 'Value': [3, 3, 5, 4], 'ID': ['pku', 'dki', 'msra', 'thu']})`"]
    - ["`pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 4], 'ID': ['dki', 'two', 'three', 'msra']})`"]
    - ["`pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 4], 'ID': ['dki', 'four', 'three', 'msra']})`"]
    - ["`pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 4], 'ID': ['dki', 'four', 'five', 'msra']})`"]
    - ["`pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 4], 'ID': ['dki', 'four', 'five', 'ucas']})`"]
    - ["`pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 4], 'ID': ['iscas', 'four', 'five', 'ucas']})`"]
    - ["`pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 5], 'ID': ['iscas', 'four', 'five', 'ucas']})`"]
    - ["`pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 5], 'ID': ['iscas', 'four', 'five', 'PKU']})`"]
    - ["`pd.DataFrame({'Group': ['M1', 'M1', 'M1', 'M1'], 'Value': [3, 3, 6, 5], 'ID': ['thu', 'four', 'five', 'PKU']})`"]
"""

def calculate_row_diff_groupwise(df):
    return df.groupby('Group').apply(f).reset_index(level=1, drop=True).reset_index()
