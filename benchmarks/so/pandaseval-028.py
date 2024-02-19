'''
### Prompt ###

import pandas as pd

def is_df_exist(df):
    # In my code, I have several variables which can either contain a pandas DataFrame or nothing at all.
    # Let's say I want to test and see if a certain DataFrame has been created yet or not.

### Solution ###

    if df is None:
        return False
    else:
        return True

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')})) == True
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[2,300,500], 'C':list('abc')})) == True
    assert candidate(pd.DataFrame({'A':[13,2,3], 'B':[2,300,500], 'C':list('abc')})) == True
    assert candidate(pd.DataFrame({'D':[1,2,3], 'B':[2,300,500], 'C':list('dct')})) == True
    assert candidate(pd.DataFrame({'A':[1,25,34], 'B':[2,300,500], 'C':list('abc')})) == True
    assert candidate(pd.DataFrame({'A':[1,23,3], 'S':[2,300,500], 'C':list('abc')})) == True
    assert candidate(None) == False
    assert candidate(pd.DataFrame({'A':[1,23,3], 'S':[2,3,500], 'C':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,23,3], 'S':[2,3,5], 'C':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,23,3], 'S':[5,2,1], 'C':list('abc')}))
'''

# %%
import pandas as pd

# %%
"""
question: |
  Write a function `def is_df_exist(df):` that takes a pandas DataFrame and returns a boolean to solve the following problem:

  In my code, I have several variables which can either contain a pandas DataFrame or nothing at all.
  Let's say I want to test and see if a certain DataFrame has been created yet or not.

validator:
  table_test:
    function_name: is_df_exist
    test_cases:
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[2,300,500], 'C':list('abc')})`"]
    - ["`pd.DataFrame({'A':[13,2,3], 'B':[2,300,500], 'C':list('abc')})`"]
    - ["`pd.DataFrame({'D':[1,2,3], 'B':[2,300,500], 'C':list('dct')})`"]
    - ["`pd.DataFrame({'A':[1,25,34], 'B':[2,300,500], 'C':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,23,3], 'S':[2,300,500], 'C':list('abc')})`"]
    - [null]
    - ["`pd.DataFrame({'A':[1,23,3], 'S':[2,3,500], 'C':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,23,3], 'S':[2,3,5], 'C':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,23,3], 'S':[5,2,1], 'C':list('abc')})`"]
"""

def is_df_exist(df):
    if df is None:
        return False
    else:
        return True
