'''
### Prompt ###

import pandas as pd

def change_all_cols_type(df):
    # Change all columns type of DataFrame to numeric
    # And return the new DataFrame
    # The code is:

### Solution ###

    return df.apply(pd.to_numeric)

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame(data=[['5.4', 2.0, 3.2]])).equals(pd.DataFrame(data=[[5.4, 2.0, 3.2]]))
    assert candidate(pd.DataFrame(data=[['5.8', 2.0, 3.2]])).equals(pd.DataFrame(data=[[5.8, 2.0, 3.2]]))
    assert candidate(pd.DataFrame(data=[['5.8', 9.1, 3.2]])).equals(pd.DataFrame(data=[[5.8, 9.1, 3.2]]))
    assert candidate(pd.DataFrame(data=[['5.8', 9.1, 3.9]])).equals(pd.DataFrame(data=[[5.8, 9.1, 3.9]]))
    assert candidate(pd.DataFrame(data=[['5.8', '9.1', 3.9]])).equals(pd.DataFrame(data=[[5.8, 9.1, 3.9]]))
    assert candidate(pd.DataFrame(data=[['5.8', '9.1', '3.9']])).equals(pd.DataFrame(data=[[5.8, 9.1, 3.9]]))
    assert candidate(pd.DataFrame(data=[['5.8', '9.1', '6.7']])).equals(pd.DataFrame(data=[[5.8, 9.1, 6.7]]))
    assert candidate(pd.DataFrame(data=[['5.8', '9.1', 6.5]])).equals(pd.DataFrame(data=[[5.8, 9.1, 6.5]]))
    assert candidate(pd.DataFrame(data=[['5.8', '9.8', 6.5]])).equals(pd.DataFrame(data=[[5.8, 9.8, 6.5]]))
    assert candidate(pd.DataFrame(data=[[5.8, '9.8', 6.5]])).equals(pd.DataFrame(data=[[5.8, 9.8, 6.5]]))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def change_all_cols_type(df):` that takes a DataFrame and returns a new DataFrame to solve the following problem:
  Change all columns type of DataFrame to numeric.

validator:
  table_test:
    function_name: change_all_cols_type
    test_cases:
    - ["`pd.DataFrame(data=[['5.4', 2.0, 3.2]])`"]
    - ["`pd.DataFrame(data=[['5.8', 2.0, 3.2]])`"]
    - ["`pd.DataFrame(data=[['5.8', 9.1, 3.2]])`"]
    - ["`pd.DataFrame(data=[['5.8', 9.1, 3.9]])`"]
    - ["`pd.DataFrame(data=[['5.8', '9.1', 3.9]])`"]
    - ["`pd.DataFrame(data=[['5.8', '9.1', '3.9']])`"]
    - ["`pd.DataFrame(data=[['5.8', '9.1', '6.7']])`"]
    - ["`pd.DataFrame(data=[['5.8', '9.1', 6.5]])`"]
    - ["`pd.DataFrame(data=[['5.8', '9.8', 6.5]])`"]
    - ["`pd.DataFrame(data=[[5.8, '9.8', 6.5]])`"]
"""

def change_all_cols_type(df):
    return df.apply(pd.to_numeric)
