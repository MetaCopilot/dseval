'''
### Prompt ###

import pandas as pd

def make_df_all_cols_lower(data):
    # I want to make all column headers in my pandas data frame lower case
    # Return the changed dataframe

### Solution ###

data.columns = map(str.lower, data.columns)
    return data

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A':range(3), 'B':range(3,0,-1), 'C':list('abc')})).equals(pd.DataFrame({'a':range(3), 'b':range(3,0,-1), 'c':list('abc')}))
    assert candidate(pd.DataFrame({'A':range(3), 'D':range(3,0,-1), 'C':list('abc')})).equals(pd.DataFrame({'a':range(3), 'd':range(3,0,-1), 'c':list('abc')}))
    assert candidate(pd.DataFrame({'T':range(3), 'D':range(3,0,-1), 'C':list('abc')})).equals(pd.DataFrame({'t':range(3), 'd':range(3,0,-1), 'c':list('abc')}))
    assert candidate(pd.DataFrame({'T':range(3), 'Y':range(3,0,-1), 'C':list('abc')})).equals(pd.DataFrame({'t':range(3), 'y':range(3,0,-1), 'c':list('abc')}))
    assert candidate(pd.DataFrame({'T':range(3), 'Y':range(3,0,-1), 'i':list('abc')})).equals(pd.DataFrame({'t':range(3), 'y':range(3,0,-1), 'i':list('abc')}))
    assert candidate(pd.DataFrame({'T':range(3), 'Y':range(3,0,-1), 'L':list('abc')})).equals(pd.DataFrame({'t':range(3), 'y':range(3,0,-1), 'l':list('abc')}))
    assert candidate(pd.DataFrame({'k':range(3), 'Y':range(3,0,-1), 'L':list('abc')})).equals(pd.DataFrame({'k':range(3), 'y':range(3,0,-1), 'l':list('abc')}))
    assert candidate(pd.DataFrame({'k':range(3), 'J':range(3,0,-1), 'L':list('abc')})).equals(pd.DataFrame({'k':range(3), 'j':range(3,0,-1), 'l':list('abc')}))
    assert candidate(pd.DataFrame({'W':range(3), 'J':range(3,0,-1), 'L':list('abc')})).equals(pd.DataFrame({'w':range(3), 'j':range(3,0,-1), 'l':list('abc')}))
    assert candidate(pd.DataFrame({'W':range(3), 'A':range(3,0,-1), 'L':list('abc')})).equals(pd.DataFrame({'w':range(3), 'a':range(3,0,-1), 'l':list('abc')}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def make_df_all_cols_lower(data):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  I want to make all column headers in my pandas data frame lower case

validator:
  table_test:
    function_name: make_df_all_cols_lower
    test_cases:
    - ["`pd.DataFrame({'A':range(3), 'B':range(3,0,-1), 'C':list('abc')})`"]
    - ["`pd.DataFrame({'A':range(3), 'D':range(3,0,-1), 'C':list('abc')})`"]
    - ["`pd.DataFrame({'T':range(3), 'D':range(3,0,-1), 'C':list('abc')})`"]
    - ["`pd.DataFrame({'T':range(3), 'Y':range(3,0,-1), 'C':list('abc')})`"]
    - ["`pd.DataFrame({'T':range(3), 'Y':range(3,0,-1), 'i':list('abc')})`"]
    - ["`pd.DataFrame({'T':range(3), 'Y':range(3,0,-1), 'L':list('abc')})`"]
    - ["`pd.DataFrame({'k':range(3), 'Y':range(3,0,-1), 'L':list('abc')})`"]
    - ["`pd.DataFrame({'k':range(3), 'J':range(3,0,-1), 'L':list('abc')})`"]
    - ["`pd.DataFrame({'W':range(3), 'J':range(3,0,-1), 'L':list('abc')})`"]
    - ["`pd.DataFrame({'W':range(3), 'A':range(3,0,-1), 'L':list('abc')})`"]
"""

def make_df_all_cols_lower(data):
    data.columns = map(str.lower, data.columns)
    return data
