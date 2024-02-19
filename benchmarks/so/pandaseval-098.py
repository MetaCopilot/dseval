'''
### Prompt ###

import pandas as pd

def get_list_from_dataframe(df):
    # I want to get a list of the column headers from a Pandas DataFrame. 
    # The DataFrame will come from user input, so I won't know how many columns there will be or what they will be called.
    # Return a list of the column headers.

### Solution ###

    return df.columns.tolist()

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a':[1,2,3], 'b':[100,300,500], 'c':list('abc')})) == ['a', 'b', 'c']
    assert candidate(pd.DataFrame({'e':[1,2,3], 'b':[100,300,500], 'c':list('abc')})) == ['e', 'b', 'c']
    assert candidate(pd.DataFrame({'e':[1,2,3], 't':[100,300,500], 'c':list('abc')})) == ['e', 't', 'c']
    assert candidate(pd.DataFrame({'e':[1,2,3], 't':[100,300,500], 'r':list('abc')})) == ['e', 't', 'r']
    assert candidate(pd.DataFrame({'e':[1,2,3], 'w':[1,2,3], 't':[100,300,500], 'r':list('abc')})) == ['e', 'w', 't', 'r']
    assert candidate(pd.DataFrame({'u':[1,2,3], 'w':[1,2,3], 't':[100,300,500], 'r':list('abc')})) == ['u', 'w', 't', 'r']
    assert candidate(pd.DataFrame({'l':[1,2,3], 'w':[1,2,3], 't':[100,300,500], 'r':list('abc')})) == ['l', 'w', 't', 'r']
    assert candidate(pd.DataFrame({'k':[1,2,3], 'w':[1,2,3], 't':[100,300,500], 'r':list('abc')})) == ['k', 'w', 't', 'r']
    assert candidate(pd.DataFrame({'i':[1,2,3], 'w':[5,'t', '1'], 't':[100,300,500], 'r':list('abc')})) == ['i', 'w', 't', 'r']
    assert candidate(pd.DataFrame({'l':[1,2,3], 'o':[1,2,3], 'v':[5,'t', '1'], 'e':[100,300,500], 'u':list('abc')})) == ['l', 'o', 'v', 'e', 'u']
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def get_list_from_dataframe(df):` that takes a DataFrame and returns a list of the column headers to solve the following problem:
  I want to get a list of the column headers from a Pandas DataFrame. 
  The DataFrame will come from user input, so I won't know how many columns there will be or what they will be called.

validator:
  table_test:
    function_name: get_list_from_dataframe
    test_cases:
    - ["`pd.DataFrame({'a':[1,2,3], 'b':[100,300,500], 'c':list('abc')})`"]
    - ["`pd.DataFrame({'e':[1,2,3], 'b':[100,300,500], 'c':list('abc')})`"]
    - ["`pd.DataFrame({'e':[1,2,3], 't':[100,300,500], 'c':list('abc')})`"]
    - ["`pd.DataFrame({'e':[1,2,3], 't':[100,300,500], 'r':list('abc')})`"]
    - ["`pd.DataFrame({'e':[1,2,3], 'w':[1,2,3], 't':[100,300,500], 'r':list('abc')})`"]
    - ["`pd.DataFrame({'u':[1,2,3], 'w':[1,2,3], 't':[100,300,500], 'r':list('abc')})`"]
    - ["`pd.DataFrame({'l':[1,2,3], 'w':[1,2,3], 't':[100,300,500], 'r':list('abc')})`"]
    - ["`pd.DataFrame({'k':[1,2,3], 'w':[1,2,3], 't':[100,300,500], 'r':list('abc')})`"]
    - ["`pd.DataFrame({'i':[1,2,3], 'w':[5,'t', '1'], 't':[100,300,500], 'r':list('abc')})`"]
    - ["`pd.DataFrame({'l':[1,2,3], 'o':[1,2,3], 'v':[5,'t', '1'], 'e':[100,300,500], 'u':list('abc')})`"]
"""

def get_list_from_dataframe(df):
    return df.columns.tolist()
