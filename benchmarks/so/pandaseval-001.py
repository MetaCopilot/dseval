'''
### Prompt ###

import pandas as pd
import numpy as np

def replacing_blank_with_nan(df):
    # replace field that's entirely space (or empty) with NaN using regex
    # return the result

### Solution ###

    return df.replace(r'^\s*$', np.nan, regex=True)

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a': [1.0, 2.0, ' '], 'b': [4.0, 5.0, 6.0]})).astype(np.float).equals(pd.DataFrame({'a': [1.0, 2.0, np.nan], 'b': [4.0, 5.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [2.0, 2.0, ' '], 'b': [4.0, 5.0, 6.0]})).astype(np.float).equals(pd.DataFrame({'a': [2.0, 2.0, np.nan], 'b': [4.0, 5.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [2.0, 2.0, ' '], 'b': [1.0, 5.0, 6.0]})).astype(np.float).equals(pd.DataFrame({'a': [2.0, 2.0, np.nan], 'b': [1.0, 5.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [2.0, 2.0, ' '], 'b': [4.0, 15.0, 6.0]})).astype(np.float).equals(pd.DataFrame({'a': [2.0, 2.0, np.nan], 'b': [4.0, 15.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [2.0, 4.0, ' '], 'b': [4.0, 5.0, 6.0]})).astype(np.float).equals(pd.DataFrame({'a': [2.0, 4.0, np.nan], 'b': [4.0, 5.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [2.0, 2.0, ' '], 'b': [4.0, 15.0, 16.0]})).astype(np.float).equals(pd.DataFrame({'a': [2.0, 2.0, np.nan], 'b': [4.0, 15.0, 16.0]}))
    assert candidate(pd.DataFrame({'a': [2.0, 2.0, ' '], 'b': [14.0, 15.0, 6.0]})).astype(np.float).equals(pd.DataFrame({'a': [2.0, 2.0, np.nan], 'b': [14.0, 15.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [21.0, 12.0, ' '], 'b': [4.0, 5.0, 6.0]})).astype(np.float).equals(pd.DataFrame({'a': [21.0, 12.0, np.nan], 'b': [4.0, 5.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [2.0, 2.0, ' '], 'b': [24.0, 25.0, 6.0]})).astype(np.float).equals(pd.DataFrame({'a': [2.0, 2.0, np.nan], 'b': [24.0, 25.0, 6.0]}))
    assert candidate(pd.DataFrame({'a': [2.0, ' ', ' '], 'b': [4.0, 5.0, 6.0]})).astype(np.float).equals(pd.DataFrame({'a': [2.0, np.nan , np.nan], 'b': [4.0, 5.0, 6.0]}))
'''

# %%
import pandas as pd
import numpy as np

# %%

"""
question: |
  Write a function `def replacing_blank_with_nan(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  replace field that's entirely space (or empty) with NaN using regex

validator:
  table_test:
    function_name: replacing_blank_with_nan
    test_cases:
    - ["`pd.DataFrame({'a': [1.0, 2.0, ' '], 'b': [4.0, 5.0, 6.0]})`"]
    - ["`pd.DataFrame({'a': [2.0, 2.0, ' '], 'b': [4.0, 5.0, 6.0]})`"]
    - ["`pd.DataFrame({'a': [2.0, 2.0, ' '], 'b': [1.0, 5.0, 6.0]})`"]
    - ["`pd.DataFrame({'a': [2.0, 2.0, ' '], 'b': [4.0, 15.0, 6.0]})`"]
    - ["`pd.DataFrame({'a': [2.0, 4.0, ' '], 'b': [4.0, 5.0, 6.0]})`"]
    - ["`pd.DataFrame({'a': [2.0, 2.0, ' '], 'b': [4.0, 15.0, 16.0]})`"]
    - ["`pd.DataFrame({'a': [2.0, 2.0, ' '], 'b': [14.0, 15.0, 6.0]})`"]
    - ["`pd.DataFrame({'a': [21.0, 12.0, ' '], 'b': [4.0, 5.0, 6.0]})`"]
    - ["`pd.DataFrame({'a': [2.0, 2.0, ' '], 'b': [24.0, 25.0, 6.0]})`"]
    - ["`pd.DataFrame({'a': [2.0, ' ', ' '], 'b': [4.0, 5.0, 6.0]})`"]
"""

def replacing_blank_with_nan(df):
    return df.replace(r'^\s*$', np.nan, regex=True)
