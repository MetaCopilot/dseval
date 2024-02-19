'''
### Prompt ###

import pandas as pd

def make_dataframe_column_headers_lowercase(data):
    # I want to make all column headers in my pandas data frame lower case

### Solution ###

    data.columns = map(str.lower, data.columns)
    return data

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A':range(3), 'B':range(3,0,-1), 'C':list('abc')})).equals(pd.DataFrame({'a':range(3), 'b':range(3,0,-1), 'c':list('abc')}))
    assert candidate(pd.DataFrame({'M':range(3), 'S':range(3,0,-1), 'R':list('dki')})).equals(pd.DataFrame({'m':range(3), 's':range(3,0,-1), 'r':list('dki')}))
    assert candidate(pd.DataFrame({'D':range(3), 'B':range(3,0,-1), 'C':list('abc')})).equals(pd.DataFrame({'d':range(3), 'b':range(3,0,-1), 'c':list('abc')}))
    assert candidate(pd.DataFrame({'D':range(3), 'K':range(3,0,-1), 'C':list('abc')})).equals(pd.DataFrame({'d':range(3), 'k':range(3,0,-1), 'c':list('abc')}))
    assert candidate(pd.DataFrame({'D':range(3), 'K':range(3,0,-1), 'I':list('abc')})).equals(pd.DataFrame({'d':range(3), 'k':range(3,0,-1), 'i':list('abc')}))
    assert candidate(pd.DataFrame({'D':range(3), 'K':range(3,0,-1), 'I':list('ccc')})).equals(pd.DataFrame({'d':range(3), 'k':range(3,0,-1), 'i':list('ccc')}))
    assert candidate(pd.DataFrame({'D':range(3), 'K':range(3,0,-1), 'I':list('msr')})).equals(pd.DataFrame({'d':range(3), 'k':range(3,0,-1), 'i':list('msr')}))
    assert candidate(pd.DataFrame({'LO':range(3), 'K':range(3,0,-1), 'I':list('msr')})).equals(pd.DataFrame({'lo':range(3), 'k':range(3,0,-1), 'i':list('msr')}))
    assert candidate(pd.DataFrame({'LO':range(3), 'V':range(3,0,-1), 'I':list('msr')})).equals(pd.DataFrame({'lo':range(3), 'v':range(3,0,-1), 'i':list('msr')}))
    assert candidate(pd.DataFrame({'LO':range(3), 'V':range(3,0,-1), 'E':list('msr')})).equals(pd.DataFrame({'lo':range(3), 'v':range(3,0,-1), 'e':list('msr')}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def make_dataframe_column_headers_lowercase(data):` that takes a pandas DataFrame and returns a DataFrame to solve the following problem:
  I want to make all column headers in my pandas data frame lower case.

validator:
  table_test:
    function_name: make_dataframe_column_headers_lowercase
    test_cases:
    - ["`pd.DataFrame({'A':range(3), 'B':range(3,0,-1), 'C':list('abc')})`"]
    - ["`pd.DataFrame({'M':range(3), 'S':range(3,0,-1), 'R':list('dki')})`"]
    - ["`pd.DataFrame({'D':range(3), 'B':range(3,0,-1), 'C':list('abc')})`"]
    - ["`pd.DataFrame({'D':range(3), 'K':range(3,0,-1), 'C':list('abc')})`"]
    - ["`pd.DataFrame({'D':range(3), 'K':range(3,0,-1), 'I':list('abc')})`"]
    - ["`pd.DataFrame({'D':range(3), 'K':range(3,0,-1), 'I':list('ccc')})`"]
    - ["`pd.DataFrame({'D':range(3), 'K':range(3,0,-1), 'I':list('msr')})`"]
    - ["`pd.DataFrame({'LO':range(3), 'K':range(3,0,-1), 'I':list('msr')})`"]
    - ["`pd.DataFrame({'LO':range(3), 'V':range(3,0,-1), 'I':list('msr')})`"]
    - ["`pd.DataFrame({'LO':range(3), 'V':range(3,0,-1), 'E':list('msr')})`"]
"""

def make_dataframe_column_headers_lowercase(data):
    data.columns = map(str.lower, data.columns)
    return data
