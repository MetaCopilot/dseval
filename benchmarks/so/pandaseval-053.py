'''
### Prompt ###

import pandas as pd

def get_number_columns(df):
    # How do I retrieve the number of columns in a Pandas data frame?
    # Return the number of columns in the dataframe

### Solution ###

    return len(df.columns)

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({"pear": [1,2,3], "apple": [2,3,4], "orange": [3,4,5]})) == 3
    assert candidate(pd.DataFrame({'pear': [1,2,3], 'apple': [2,3,4]})) == 2
    assert candidate(pd.DataFrame({'pear': [1,2,3], 'apple': [2,3,5]})) == 2
    assert candidate(pd.DataFrame({'pear': [1,4,3], 'apple': [2,3,4]})) == 2
    assert candidate(pd.DataFrame({'pear': [3,2,3], 'apple': [2,3,4]})) == 2
    assert candidate(pd.DataFrame({'pear': [1,2,3], 'apple': [2,3,5]})) == 2
    assert candidate(pd.DataFrame({'pear': [1,2,3]})) == 1
    assert candidate(pd.DataFrame({'pear': [11,2,3], 'apple': [2,3,4]})) == 2
    assert candidate(pd.DataFrame({'pear': [1,2,3], 'apple': [2,412,4]})) == 2
    assert candidate(pd.DataFrame({'pear': [1,2,3], 'apple': [22,33,44]})) == 2
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def get_number_columns(df):` that takes a DataFrame and returns an integer to solve the following problem:
  How do I retrieve the number of columns in a Pandas data frame?
  Return the number of columns in the dataframe.

validator:
  table_test:
    function_name: get_number_columns
    test_cases:
    - ["`pd.DataFrame({'pear': [1,2,3], 'apple': [2,3,4], 'orange': [3,4,5]})`"]
    - ["`pd.DataFrame({'pear': [1,2,3], 'apple': [2,3,4]})`"]
    - ["`pd.DataFrame({'pear': [1,2,3], 'apple': [2,3,5]})`"]
    - ["`pd.DataFrame({'pear': [1,4,3], 'apple': [2,3,4]})`"]
    - ["`pd.DataFrame({'pear': [3,2,3], 'apple': [2,3,4]})`"]
    - ["`pd.DataFrame({'pear': [1,2,3], 'apple': [2,3,5]})`"]
    - ["`pd.DataFrame({'pear': [1,2,3]})`"]
    - ["`pd.DataFrame({'pear': [11,2,3], 'apple': [2,3,4]})`"]
    - ["`pd.DataFrame({'pear': [1,2,3], 'apple': [2,412,4]})`"]
    - ["`pd.DataFrame({'pear': [1,2,3], 'apple': [22,33,44]})`"]
"""

def get_number_columns(df):
    return len(df.columns)
