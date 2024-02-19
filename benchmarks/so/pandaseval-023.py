'''
### Prompt ###

import pandas as pd
import numpy as np

def find_columns_name_lists(df):
    # How do I determine which columns contain NaN values? In particular, can I get a list of the column names containing NaNs?
    # Return a list of the column names containing NaNs

### Solution ###

    return df.columns[df.isna().any()].tolist()

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'pear': [np.nan,2,3], 'apple': [2,3,4]})) == ['pear']
    assert candidate(pd.DataFrame({'pear': [np.nan,2,3], 'apple': [np.nan,3,4]})) == ['pear', 'apple']
    assert candidate(pd.DataFrame({'pear': [np.nan,3,3], 'apple': [np.nan,3,4]})) == ['pear', 'apple']
    assert candidate(pd.DataFrame({'pear': [np.nan,2,3], 'ccc': [np.nan,3,4]})) == ['pear', 'ccc']
    assert candidate(pd.DataFrame({'ddd': [np.nan,2,3], 'apple': [np.nan,3,4]})) == ['ddd', 'apple']
    assert candidate(pd.DataFrame({'pear': [np.nan,24,3], 'apple': [np.nan,3,4]})) == ['pear', 'apple']
    assert candidate(pd.DataFrame({'pear': [np.nan,2,453], 'apple': [np.nan,3,4]})) == ['pear', 'apple']
    assert candidate(pd.DataFrame({'pear': [np.nan,2,3], 'apple': [np.nan,34,45]})) == ['pear', 'apple']
    assert candidate(pd.DataFrame({'pear': [np.nan,2,3], 'apple': [np.nan,3,433]})) == ['pear', 'apple']
    assert candidate(pd.DataFrame({'pear': [np.nan,32,33], 'apple': [np.nan,32,43]})) == ['pear', 'apple']
'''

# %%
import pandas as pd
import numpy as np

# %%

"""
question: |
  Write a function `def find_columns_name_lists(df):` that takes a DataFrame and returns a list of the column names containing NaNs to solve the following problem:
  How do I determine which columns contain NaN values? In particular, can I get a list of the column names containing NaNs?

validator:
  table_test:
    function_name: find_columns_name_lists
    test_cases:
    - ["`pd.DataFrame({'pear': [np.nan,2,3], 'apple': [2,3,4]})`"]
    - ["`pd.DataFrame({'pear': [np.nan,2,3], 'apple': [np.nan,3,4]})`"]
    - ["`pd.DataFrame({'pear': [np.nan,3,3], 'apple': [np.nan,3,4]})`"]
    - ["`pd.DataFrame({'pear': [np.nan,2,3], 'ccc': [np.nan,3,4]})`"]
    - ["`pd.DataFrame({'ddd': [np.nan,2,3], 'apple': [np.nan,3,4]})`"]
    - ["`pd.DataFrame({'pear': [np.nan,24,3], 'apple': [np.nan,3,4]})`"]
    - ["`pd.DataFrame({'pear': [np.nan,2,453], 'apple': [np.nan,3,4]})`"]
    - ["`pd.DataFrame({'pear': [np.nan,2,3], 'apple': [np.nan,34,45]})`"]
    - ["`pd.DataFrame({'pear': [np.nan,2,3], 'apple': [np.nan,3,433]})`"]
    - ["`pd.DataFrame({'pear': [np.nan,32,33], 'apple': [np.nan,32,43]})`"]
"""

def find_columns_name_lists(df):
    return df.columns[df.isna().any()].tolist()
