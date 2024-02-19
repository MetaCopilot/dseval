'''
### Prompt ###

import pandas as pd

def divide_multiple_cols_by_first_col(df):
    # I need to divide all ['B','C'] columns but the first column 'A' in a DataFrame by the first column.
    # Return the result.

### Solution ###

    df[['B','C']] = df[['B','C']].div(df.A, axis=0)
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A':[1,3,5], 'B':[10,30,50], 'C':[100,300,500]})).equals(pd.DataFrame({'A':[1,3,5], 'B':[10.0, 10.0, 10.0], 'C':[100.0, 100.0, 100.0]}))
    assert candidate(pd.DataFrame({'A':[1,3], 'B':[10,30], 'C':[100,300]})).equals(pd.DataFrame({'A':[1,3], 'B':[10.0, 10.0], 'C':[100.0, 100.0]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def divide_multiple_cols_by_first_col(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  I need to divide all ['B','C'] columns but the first column 'A' in a DataFrame by the first column.

validator:
  table_test:
    function_name: divide_multiple_cols_by_first_col
    test_cases:
    - ["`pd.DataFrame({'A':[1,3,5], 'B':[10,30,50], 'C':[100,300,500]})`"]
    - ["`pd.DataFrame({'A':[1,3], 'B':[10,30], 'C':[100,300]})`"]
"""

def divide_multiple_cols_by_first_col(df):
    df[['B','C']] = df[['B','C']].div(df.A, axis=0)
    return df
