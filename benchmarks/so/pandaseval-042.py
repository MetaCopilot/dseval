'''
### Prompt ###

import pandas as pd

def delete_first_n_rows(df, n):
    # Delete first n rows of a dataframe
    # Input:
    #   df: DataFrame
    #   n: int
    # Return:
    #   DataFrame

### Solution ###

    return df.iloc[n:]

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')}), 2).equals(pd.DataFrame({'A':[3], 'B':[500], 'C':['c']}, index=[2]))
    assert candidate(pd.DataFrame({'A':[1,2,4], 'B':[100,300,500], 'C':list('abc')}), 2).equals(pd.DataFrame({'A':[4], 'B':[500], 'C':['c']}, index=[2]))
    assert candidate(pd.DataFrame({'A':[1,2,4], 'B':[100,300,123], 'C':list('abc')}), 2).equals(pd.DataFrame({'A':[4], 'B':[123], 'C':['c']}, index=[2]))
    assert candidate(pd.DataFrame({'A':[1,2,43], 'B':[100,300,123], 'C':list('abc')}), 2).equals(pd.DataFrame({'A':[43], 'B':[123], 'C':['c']}, index=[2]))
    assert candidate(pd.DataFrame({'A':[1,2,43], 'B':[100,300,412], 'C':list('abc')}), 2).equals(pd.DataFrame({'A':[43], 'B':[412], 'C':['c']}, index=[2]))
    assert candidate(pd.DataFrame({'A':[1,2,123], 'B':[100,300,412], 'C':list('abc')}), 2).equals(pd.DataFrame({'A':[123], 'B':[412], 'C':['c']}, index=[2]))
    assert candidate(pd.DataFrame({'A':[1,2,123], 'B':[100,223,412], 'C':list('abc')}), 2).equals(pd.DataFrame({'A':[123], 'B':[412], 'C':['c']}, index=[2]))
    assert candidate(pd.DataFrame({'A':[1,2,123], 'B':[312,223,412], 'C':list('abc')}), 2).equals(pd.DataFrame({'A':[123], 'B':[412], 'C':['c']}, index=[2]))
    assert candidate(pd.DataFrame({'A':[31,2,123], 'B':[312,223,412], 'C':list('abc')}), 2).equals(pd.DataFrame({'A':[123], 'B':[412], 'C':['c']}, index=[2]))
    assert candidate(pd.DataFrame({'A':[31,23,123], 'B':[312,223,412], 'C':list('abc')}), 2).equals(pd.DataFrame({'A':[123], 'B':[412], 'C':['c']}, index=[2]))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def delete_first_n_rows(df, n):` that takes a DataFrame and an integer n and returns a DataFrame to solve the following problem:
  Delete first n rows of a dataframe

validator:
  table_test:
    function_name: delete_first_n_rows
    test_cases:
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')})`", 2]
    - ["`pd.DataFrame({'A':[1,2,4], 'B':[100,300,500], 'C':list('abc')})`", 2]
    - ["`pd.DataFrame({'A':[1,2,4], 'B':[100,300,123], 'C':list('abc')})`", 2]
    - ["`pd.DataFrame({'A':[1,2,43], 'B':[100,300,123], 'C':list('abc')})`", 2]
    - ["`pd.DataFrame({'A':[1,2,43], 'B':[100,300,412], 'C':list('abc')})`", 2]
    - ["`pd.DataFrame({'A':[1,2,123], 'B':[100,300,412], 'C':list('abc')})`", 2]
    - ["`pd.DataFrame({'A':[1,2,123], 'B':[100,223,412], 'C':list('abc')})`", 2]
    - ["`pd.DataFrame({'A':[1,2,123], 'B':[312,223,412], 'C':list('abc')})`", 2]
    - ["`pd.DataFrame({'A':[31,2,123], 'B':[312,223,412], 'C':list('abc')})`", 2]
    - ["`pd.DataFrame({'A':[31,23,123], 'B':[312,223,412], 'C':list('abc')})`", 2]
"""

def delete_first_n_rows(df, n):
    return df.iloc[n:]
