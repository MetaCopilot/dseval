'''
### Prompt ###

import pandas as pd
import numpy as np

def delete_all_nan_columns(df):
    # Delete all columns that contain all NaN values
    # Return the result.

### Solution ###

    return df.dropna(how='all', axis=1)

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})).equals(pd.DataFrame({'A': [1, 2, 3]}))
    assert candidate(pd.DataFrame({'A': [1, 3, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})).equals(pd.DataFrame({'A': [1, 3, 3]}))
    assert candidate(pd.DataFrame({'A': [4, 2, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})).equals(pd.DataFrame({'A': [4, 2, 3]}))
    assert candidate(pd.DataFrame({'A': [6, 2, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})).equals(pd.DataFrame({'A': [6, 2, 3]}))
    assert candidate(pd.DataFrame({'A': [1, 12, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})).equals(pd.DataFrame({'A': [1, 12, 3]}))
    assert candidate(pd.DataFrame({'A': [1, 2, 33], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})).equals(pd.DataFrame({'A': [1, 2, 33]}))
    assert candidate(pd.DataFrame({'A': [13, 23, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})).equals(pd.DataFrame({'A': [13, 23, 3]}))
    assert candidate(pd.DataFrame({'A': [1, 25, 35], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})).equals(pd.DataFrame({'A': [1, 25, 35]}))
    assert candidate(pd.DataFrame({'A': [41, 2, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})).equals(pd.DataFrame({'A': [41, 2, 3]}))
    assert candidate(pd.DataFrame({'A': [1, 24, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})).equals(pd.DataFrame({'A': [1, 24, 3]}))
'''

# %%
import pandas as pd
import numpy as np

# %%

"""
question: |
  Write a function `def delete_all_nan_columns(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  Delete all columns that contain all NaN values.

validator:
  table_test:
    function_name: delete_all_nan_columns
    test_cases:
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [1, 3, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [4, 2, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [6, 2, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [1, 12, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [1, 2, 33], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [13, 23, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [1, 25, 35], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [41, 2, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [1, 24, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})`"]
"""

def delete_all_nan_columns(df):
    return df.dropna(how='all', axis=1)
