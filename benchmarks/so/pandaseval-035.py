'''
### Prompt ###

import pandas as pd

def remove_duplicates_by_col_names(df):
    """
    Here's a one solution to remove columns based on duplicate column names:
    Return the duplicated dataframe
    """

### Solution ###

    return df.loc[:,~df.columns.duplicated()]

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'B':list('abc')})).equals(pd.DataFrame({'A':[1,2,3], 'B':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,2,4], 'B':[100,300,500], 'B':list('abc')})).equals(pd.DataFrame({'A':[1,2,4], 'B':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,3,4], 'B':[100,300,500], 'B':list('abc')})).equals(pd.DataFrame({'A':[1,3,4], 'B':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,3,4], 'B':[100,312,500], 'B':list('abc')})).equals(pd.DataFrame({'A':[1,3,4], 'B':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,3,4], 'B':[100,312,213], 'B':list('abc')})).equals(pd.DataFrame({'A':[1,3,4], 'B':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,3,4], 'B':[973,312,213], 'B':list('abc')})).equals(pd.DataFrame({'A':[1,3,4], 'B':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,3,4], 'B':[973,312,111], 'B':list('abc')})).equals(pd.DataFrame({'A':[1,3,4], 'B':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,3,4], 'C':[973,312,111], 'C':list('abc')})).equals(pd.DataFrame({'A':[1,3,4], 'C':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,3,4], 'C':[973,312,122], 'C':list('abc')})).equals(pd.DataFrame({'A':[1,3,4], 'C':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,3,4], 'C':[973,312,55], 'C':list('abc')})).equals(pd.DataFrame({'A':[1,3,4], 'C':list('abc')}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def remove_duplicates_by_col_names(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  Remove columns based on duplicate column names.

validator:
  table_test:
    function_name: remove_duplicates_by_col_names
    test_cases:
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'B':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,2,4], 'B':[100,300,500], 'B':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,3,4], 'B':[100,300,500], 'B':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,3,4], 'B':[100,312,500], 'B':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,3,4], 'B':[100,312,213], 'B':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,3,4], 'B':[973,312,213], 'B':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,3,4], 'B':[973,312,111], 'B':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,3,4], 'C':[973,312,111], 'C':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,3,4], 'C':[973,312,122], 'C':list('abc')})`"]
    - ["`pd.DataFrame({'A':[1,3,4], 'C':[973,312,55], 'C':list('abc')})`"]
"""

def remove_duplicates_by_col_names(df):
    return df.loc[:,~df.columns.duplicated()]
