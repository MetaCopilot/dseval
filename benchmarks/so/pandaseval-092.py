'''
### Prompt ###

import pandas as pd

def get_first_n_rows(df, n):
    # I would simply like to slice the Data Frame and take the first n rows.
    # Return the result

### Solution ###

    return df.head(n)

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')}), 1).equals(pd.DataFrame({'A':[1], 'B':[100], 'C':['a']}))
    assert candidate(pd.DataFrame({'A':[1,23,3], 'B':[100,300,500], 'C':list('abc')}), 1).equals(pd.DataFrame({'A':[1], 'B':[100], 'C':['a']}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[110,300,500], 'C':list('abc')}), 1).equals(pd.DataFrame({'A':[1], 'B':[110], 'C':['a']}))
    assert candidate(pd.DataFrame({'A':[4,2,3], 'B':[100,300,500], 'C':list('abc')}), 1).equals(pd.DataFrame({'A':[4], 'B':[100], 'C':['a']}))
    assert candidate(pd.DataFrame({'A':[13,2,3], 'B':[100,300,500], 'C':list('abc')}), 1).equals(pd.DataFrame({'A':[13], 'B':[100], 'C':['a']}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('dbc')}), 1).equals(pd.DataFrame({'A':[1], 'B':[100], 'C':['d']}))
    assert candidate(pd.DataFrame({'A':[1,2,32], 'B':[100,300,500], 'C':list('abc')}), 1).equals(pd.DataFrame({'A':[1], 'B':[100], 'C':['a']}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('rbc')}), 1).equals(pd.DataFrame({'A':[1], 'B':[100], 'C':['r']}))
    assert candidate(pd.DataFrame({'A':[1,22,3], 'B':[100,300,500], 'C':list('abc')}), 1).equals(pd.DataFrame({'A':[1], 'B':[100], 'C':['a']}))
    assert candidate(pd.DataFrame({'A':[11,2,3], 'B':[100,300,500], 'C':list('abc')}), 1).equals(pd.DataFrame({'A':[11], 'B':[100], 'C':['a']}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def get_first_n_rows(df, n):` that takes a DataFrame and an integer n and returns a DataFrame to solve the following problem:
  I would simply like to slice the Data Frame and take the first n rows.

validator:
  table_test:
    function_name: get_first_n_rows
    test_cases:
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')})`", 1]
    - ["`pd.DataFrame({'A':[1,23,3], 'B':[100,300,500], 'C':list('abc')})`", 1]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[110,300,500], 'C':list('abc')})`", 1]
    - ["`pd.DataFrame({'A':[4,2,3], 'B':[100,300,500], 'C':list('abc')})`", 1]
    - ["`pd.DataFrame({'A':[13,2,3], 'B':[100,300,500], 'C':list('abc')})`", 1]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('dbc')})`", 1]
    - ["`pd.DataFrame({'A':[1,2,32], 'B':[100,300,500], 'C':list('abc')})`", 1]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('rbc')})`", 1]
    - ["`pd.DataFrame({'A':[1,22,3], 'B':[100,300,500], 'C':list('abc')})`", 1]
    - ["`pd.DataFrame({'A':[11,2,3], 'B':[100,300,500], 'C':list('abc')})`", 1]
"""

def get_first_n_rows(df, n):
    return df.head(n)
