'''
### Prompt ###

import pandas as pd
import numpy as np

def drop_all_nan_rows(df):
    # We will drop all Nan rows.
    # Return the changed dataframe.

### Solution ###

    return df.dropna()

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, np.nan, np.nan], 'C': [2, np.nan, np.nan]})).equals(pd.DataFrame({'A': [1], 'B': [100.0], 'C': [2.0]}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, np.nan, np.nan], 'C': [4, np.nan, np.nan]})).equals(pd.DataFrame({'A': [1], 'B': [100.0], 'C': [4.0]}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, np.nan, np.nan], 'C': [6, np.nan, np.nan]})).equals(pd.DataFrame({'A': [1], 'B': [100.0], 'C': [6.0]}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})).equals(pd.DataFrame({'A': [1], 'B': [110.0], 'C': [6.0]}))
    assert candidate(pd.DataFrame({'A': [2, 2, 3], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})).equals(pd.DataFrame({'A': [2], 'B': [110.0], 'C': [6.0]}))
    assert candidate(pd.DataFrame({'A': [22, 2, 3], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})).equals(pd.DataFrame({'A': [22], 'B': [110.0], 'C': [6.0]}))
    assert candidate(pd.DataFrame({'A': [22, 2, 33], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})).equals(pd.DataFrame({'A': [22], 'B': [110.0], 'C': [6.0]}))
    assert candidate(pd.DataFrame({'A': [22, 24, 33], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})).equals(pd.DataFrame({'A': [22], 'B': [110.0], 'C': [6.0]}))
    assert candidate(pd.DataFrame({'A': [22, 24, 52], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})).equals(pd.DataFrame({'A': [22], 'B': [110.0], 'C': [6.0]}))
    assert candidate(pd.DataFrame({'A': [22, 24, 13], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})).equals(pd.DataFrame({'A': [22], 'B': [110.0], 'C': [6.0]}))
'''

# %%
import pandas as pd
import numpy as np

# %%

"""
question: |
  Write a function `def drop_all_nan_rows(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  We will drop all Nan rows.

validator:
  table_test:
    function_name: drop_all_nan_rows
    test_cases:
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, np.nan, np.nan], 'C': [2, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, np.nan, np.nan], 'C': [4, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, np.nan, np.nan], 'C': [6, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [2, 2, 3], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [22, 2, 3], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [22, 2, 33], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [22, 24, 33], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [22, 24, 52], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})`"]
    - ["`pd.DataFrame({'A': [22, 24, 13], 'B': [110, np.nan, np.nan], 'C': [6, np.nan, np.nan]})`"]
"""

def drop_all_nan_rows(df):
    return df.dropna()
