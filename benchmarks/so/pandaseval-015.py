'''
### Prompt ###

import pandas as pd
import numpy as np

def if_any_value_is_nan(df):
    # How to check if any value is NaN in a Pandas DataFrame? Return the result.

### Solution ###

return df.isnull().values.any()

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [np.nan, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]})) == True
    assert candidate(pd.DataFrame({'A': [np.nan, np.nan, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]})) == True
    assert candidate(pd.DataFrame({'A': [np.nan, np.nan, 3], 'B': [1, np.nan, 3], 'C': [1, 2, 3]})) == True
    assert candidate(pd.DataFrame({'A': [np.nan, np.nan, 3], 'B': [1, np.nan, 8], 'C': [1, 2, 3]})) == True
    assert candidate(pd.DataFrame({'A': [7, 6, 3], 'B': [1, np.nan, 8], 'C': [1, 2, 3]})) == True
    assert candidate(pd.DataFrame({'A': [7, 8, 3], 'B': [1, np.nan, 8], 'C': [1, 2, 18]})) == True
    assert candidate(pd.DataFrame({'A': [7, 6, 3], 'B': [1, np.nan, 8], 'C': [1, 2, 18]})) == True
    assert candidate(pd.DataFrame({'A': [7, 8, 3], 'B': [1, 8, 8], 'C': [1, 2, 18]})) == False
    assert candidate(pd.DataFrame({'A': [7, 8, 3], 'B': [81, 5, 8], 'C': [1, 2, 18]})) == False
    assert candidate(pd.DataFrame({'A': [7, 94, 3], 'B': [81, 5, 8], 'C': [1, 2, 18]})) == False
'''

# %%
import pandas as pd
import numpy as np

# %%

"""
question: |
  Write a function `def if_any_value_is_nan(df):` that takes a DataFrame and returns a boolean to solve the following problem:
  How to check if any value is NaN in a Pandas DataFrame?

validator:
  table_test:
    function_name: if_any_value_is_nan
    test_cases:
    - ["`pd.DataFrame({'A': [np.nan, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]})`"]
    - ["`pd.DataFrame({'A': [np.nan, np.nan, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]})`"]
    - ["`pd.DataFrame({'A': [np.nan, np.nan, 3], 'B': [1, np.nan, 3], 'C': [1, 2, 3]})`"]
    - ["`pd.DataFrame({'A': [np.nan, np.nan, 3], 'B': [1, np.nan, 8], 'C': [1, 2, 3]})`"]
    - ["`pd.DataFrame({'A': [7, 6, 3], 'B': [1, np.nan, 8], 'C': [1, 2, 3]})`"]
    - ["`pd.DataFrame({'A': [7, 8, 3], 'B': [1, np.nan, 8], 'C': [1, 2, 18]})`"]
    - ["`pd.DataFrame({'A': [7, 6, 3], 'B': [1, np.nan, 8], 'C': [1, 2, 18]})`"]
    - ["`pd.DataFrame({'A': [7, 8, 3], 'B': [1, 8, 8], 'C': [1, 2, 18]})`"]
    - ["`pd.DataFrame({'A': [7, 8, 3], 'B': [81, 5, 8], 'C': [1, 2, 18]})`"]
    - ["`pd.DataFrame({'A': [7, 94, 3], 'B': [81, 5, 8], 'C': [1, 2, 18]})`"]
"""

def if_any_value_is_nan(df):
    return df.isnull().values.any()
