'''
### Prompt ###

import pandas as pd

def round_a_single_column(df):
    # Round a single column `A`
    # Return the dataframe

### Solution ###

    df.A = df.A.round()
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [1.23, 2.34, 3.45], 'B': [4.56, 5.67, 6.78]})).equals(pd.DataFrame({'A': [1.0, 2.0, 3.0], 'B': [4.56, 5.67, 6.78]}))
    assert candidate(pd.DataFrame({'A': [1.41, 2.34, 3.45], 'B': [4.56, 5.67, 6.78]})).equals(pd.DataFrame({'A': [1.0, 2.0, 3.0], 'B': [4.56, 5.67, 6.78]}))
    assert candidate(pd.DataFrame({'A': [1.41, 2.36, 3.45], 'B': [4.56, 5.67, 6.78]})).equals(pd.DataFrame({'A': [1.0, 2.0, 3.0], 'B': [4.56, 5.67, 6.78]}))
    assert candidate(pd.DataFrame({'A': [1.41, 2.36, 3.55], 'B': [4.56, 5.67, 6.78]})).equals(pd.DataFrame({'A': [1.0, 2.0, 4.0], 'B': [4.56, 5.67, 6.78]}))
    assert candidate(pd.DataFrame({'A': [1.41, 2.56, 3.55], 'B': [4.56, 5.67, 6.78]})).equals(pd.DataFrame({'A': [1.0, 3.0, 4.0], 'B': [4.56, 5.67, 6.78]}))
    assert candidate(pd.DataFrame({'A': [1.31, 2.56, 3.55], 'B': [4.56, 5.67, 6.78]})).equals(pd.DataFrame({'A': [1.0, 3.0, 4.0], 'B': [4.56, 5.67, 6.78]}))
    assert candidate(pd.DataFrame({'A': [1.31, 1.56, 3.55], 'B': [4.56, 5.67, 6.78]})).equals(pd.DataFrame({'A': [1.0, 2.0, 4.0], 'B': [4.56, 5.67, 6.78]}))
    assert candidate(pd.DataFrame({'A': [1.31, 1.56, 3.55], 'B': [4.56, 3.67, 6.78]})).equals(pd.DataFrame({'A': [1.0, 2.0, 4.0], 'B': [4.56, 3.67, 6.78]}))
    assert candidate(pd.DataFrame({'A': [1.31, 1.56, 4.15], 'B': [4.56, 3.67, 6.78]})).equals(pd.DataFrame({'A': [1.0, 2.0, 4.0], 'B': [4.56, 3.67, 6.78]}))
    assert candidate(pd.DataFrame({'A': [1.31, 1.56, 4.05], 'B': [4.56, 3.67, 6.78]})).equals(pd.DataFrame({'A': [1.0, 2.0, 4.0], 'B': [4.56, 3.67, 6.78]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def round_a_single_column(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  Round a single column `A`

validator:
  table_test:
    function_name: round_a_single_column
    test_cases:
    - ["`pd.DataFrame({'A': [1.23, 2.34, 3.45], 'B': [4.56, 5.67, 6.78]})`"]
    - ["`pd.DataFrame({'A': [1.41, 2.34, 3.45], 'B': [4.56, 5.67, 6.78]})`"]
    - ["`pd.DataFrame({'A': [1.41, 2.36, 3.45], 'B': [4.56, 5.67, 6.78]})`"]
    - ["`pd.DataFrame({'A': [1.41, 2.36, 3.55], 'B': [4.56, 5.67, 6.78]})`"]
    - ["`pd.DataFrame({'A': [1.41, 2.56, 3.55], 'B': [4.56, 5.67, 6.78]})`"]
    - ["`pd.DataFrame({'A': [1.31, 2.56, 3.55], 'B': [4.56, 5.67, 6.78]})`"]
    - ["`pd.DataFrame({'A': [1.31, 1.56, 3.55], 'B': [4.56, 5.67, 6.78]})`"]
    - ["`pd.DataFrame({'A': [1.31, 1.56, 3.55], 'B': [4.56, 3.67, 6.78]})`"]
    - ["`pd.DataFrame({'A': [1.31, 1.56, 4.15], 'B': [4.56, 3.67, 6.78]})`"]
    - ["`pd.DataFrame({'A': [1.31, 1.56, 4.05], 'B': [4.56, 3.67, 6.78]})`"]
"""

def round_a_single_column(df):
    df.A = df.A.round()
    return df
