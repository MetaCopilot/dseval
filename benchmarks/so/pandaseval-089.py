'''
### Prompt ###

import pandas as pd

def get_row_index_values_as_list(df):
    # Return the row-index values of the dataframe as a list

### Solution ###

    return df.index.values.tolist()

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a': [2, 3, 2], 'b': [4, 4, 2]})) == [0, 1, 2]
    assert candidate(pd.DataFrame({'a': [2, 5, 2], 'b': [4, 4, 2]})) == [0, 1, 2]
    assert candidate(pd.DataFrame({'a': [2, 8, 2], 'b': [4, 4, 2]})) == [0, 1, 2]
    assert candidate(pd.DataFrame({'a': [2, 10, 2], 'b': [4, 4, 2]})) == [0, 1, 2]
    assert candidate(pd.DataFrame({'a': [2, 10, 2], 'b': [4, 4, 2]}, index=[1, 0 ,2])) == [1, 0, 2]
    assert candidate(pd.DataFrame({'a': [2, 10, 2], 'b': [4, 412, 2]}, index=[1, 0 ,2])) == [1, 0, 2]
    assert candidate(pd.DataFrame({'a': [21, 110, 2], 'b': [4, 4, 2]}, index=[1, 0 ,2])) == [1, 0, 2]
    assert candidate(pd.DataFrame({'a': [2, 10, 2], 'b': [4, 4, 21]}, index=[1, 0 ,21])) == [1, 0, 21]
    assert candidate(pd.DataFrame({'a': [2, 110, 12], 'b': [4, 4, 2]}, index=[1, 0 ,2])) == [1, 0, 2]
    assert candidate(pd.DataFrame({'a': [32, 310, 2], 'b': [4, 4, 2]}, index=[1, 0 ,2])) == [1, 0, 2]
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def get_row_index_values_as_list(df):` that takes a DataFrame and returns a list to solve the following problem:
  Return the row-index values of the dataframe as a list.

validator:
  table_test:
    function_name: get_row_index_values_as_list
    test_cases:
    - ["`pd.DataFrame({'a': [2, 3, 2], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [2, 5, 2], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [2, 8, 2], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [2, 10, 2], 'b': [4, 4, 2]})`"]
    - ["`pd.DataFrame({'a': [2, 10, 2], 'b': [4, 4, 2]}, index=[1, 0 ,2])`"]
    - ["`pd.DataFrame({'a': [2, 10, 2], 'b': [4, 412, 2]}, index=[1, 0 ,2])`"]
    - ["`pd.DataFrame({'a': [21, 110, 2], 'b': [4, 4, 2]}, index=[1, 0 ,2])`"]
    - ["`pd.DataFrame({'a': [2, 10, 2], 'b': [4, 4, 21]}, index=[1, 0 ,21])`"]
    - ["`pd.DataFrame({'a': [2, 110, 12], 'b': [4, 4, 2]}, index=[1, 0 ,2])`"]
    - ["`pd.DataFrame({'a': [32, 310, 2], 'b': [4, 4, 2]}, index=[1, 0 ,2])`"]
"""

def get_row_index_values_as_list(df):
    return df.index.values.tolist()
