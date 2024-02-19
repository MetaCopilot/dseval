'''
### Prompt ###

import pandas as pd

def drop2rows_zero(df):
    # i want to drop 2 rows in the dataframe if zero comes in the column
    # if 0 comes on odd index drop previous row as well as current row using pandas
    # Assuming your dataframe is indexed starting from 0
    # Rows with column2 = 0 and on odd index
    idx = df[(df['column2'] == 0) & (df.index % 2 == 1)].index
    # The rows above them
    idx = idx.append(idx-1)
    # A new dataframe with those rows removed

### Solution ###

result = df.drop(idx)
    return result

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [1, 0, 2, 3, 7, 10]})).equals( pd.DataFrame({'column1': ['c', 'd', 'e', 'f'],'column2': [2, 3, 7, 10]}, index=[2, 3, 4, 5]))
    assert candidate(pd.DataFrame({'column1': ['m', 's', 'r', 'a', 'z', 'a'],'column2': [8, 7, 2, 5, 6, 1]})).equals(pd.DataFrame({'column1': ['m', 's', 'r', 'a', 'z', 'a'],'column2': [8, 7, 2, 5, 6, 1]}))
    assert candidate(pd.DataFrame({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 2, 3, 7, 10]})).equals( pd.DataFrame({'column1': ['c', 'd', 'e', 'f'],'column2': [2, 3, 7, 10]}, index=[2, 3, 4, 5]))
    assert candidate({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 2, 3, 7, 11]})).equals( pd.DataFrame({'column1': ['c', 'd', 'e', 'f'],'column2': [2, 3, 7, 11]}, index=[2, 3, 4, 5]))
    assert candidate({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 2, 3, 8, 11]})).equals( pd.DataFrame({'column1': ['c', 'd', 'e', 'f'],'column2': [2, 3, 8, 11]}, index=[2, 3, 4, 5]))
    assert candidate({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 2, 4, 8, 11]})).equals( pd.DataFrame({'column1': ['c', 'd', 'e', 'f'],'column2': [2, 4, 8, 11]}, index=[2, 3, 4, 5]))
    assert candidate({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 3, 4, 8, 11]})).equals( pd.DataFrame({'column1': ['c', 'd', 'e', 'f'],'column2': [3, 4, 8, 11]}, index=[2, 3, 4, 5]))
    assert candidate({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 3, 4, 9, 11]})).equals( pd.DataFrame({'column1': ['c', 'd', 'e', 'f'],'column2': [3, 4, 9, 11]}, index=[2, 3, 4, 5]))
    assert candidate({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 3, 4, 9, 18]})).equals( pd.DataFrame({'column1': ['c', 'd', 'e', 'f'],'column2': [3, 4, 9, 18]}, index=[2, 3, 4, 5]))
    assert candidate({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 3, 4, 12, 18]})).equals( pd.DataFrame({'column1': ['c', 'd', 'e', 'f'],'column2': [3, 4, 12, 18]}, index=[2, 3, 4, 5]))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def drop2rows_zero(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  i want to drop 2 rows in the dataframe if zero comes in the column
  if 0 comes on odd index drop previous row as well as current row using pandas
  Assuming your dataframe is indexed starting from 0

validator:
  table_test:
    function_name: drop2rows_zero
    test_cases:
    - ["`pd.DataFrame({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [1, 0, 2, 3, 7, 10]})`"]
    - ["`pd.DataFrame({'column1': ['m', 's', 'r', 'a', 'z', 'a'],'column2': [8, 7, 2, 5, 6, 1]})`"]
    - ["`pd.DataFrame({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 2, 3, 7, 10]})`"]
    - ["`pd.DataFrame({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 2, 3, 7, 11]})`"]
    - ["`pd.DataFrame({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 2, 3, 8, 11]})`"]
    - ["`pd.DataFrame({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 2, 4, 8, 11]})`"]
    - ["`pd.DataFrame({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 3, 4, 8, 11]})`"]
    - ["`pd.DataFrame({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 3, 4, 9, 11]})`"]
    - ["`pd.DataFrame({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 3, 4, 9, 18]})`"]
    - ["`pd.DataFrame({'column1': ['a', 'b', 'c', 'd', 'e', 'f'],'column2': [2, 0, 3, 4, 12, 18]})`"]
"""

def drop2rows_zero(df):
    idx = df[(df['column2'] == 0) & (df.index % 2 == 1)].index
    idx = idx.append(idx-1)
    result = df.drop(idx)
    return result
