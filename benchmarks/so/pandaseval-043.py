'''
### Prompt ###

import pandas as pd
def compute_mean_along_rows(df):
    # You can specify a new column named `mean_along_rows` that contains the mean of each row. You also need to compute the mean along the rows, so use axis=1.
    # Finally, return the dataframe with the new column.

### Solution ###

    df['mean'] = df.mean(axis=1)
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['US', 'US', 'US']})).equals(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['US', 'US', 'US'], 'mean_along_rows':[50.5, 151.0, 251.5]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['w', 'US', 'US']})).equals(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['w', 'US', 'US'], 'mean_along_rows':[50.5, 151.0, 251.5]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['CN', 'US', 'US']})).equals(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['CN', 'US', 'US'], 'mean_along_rows':[50.5, 151.0, 251.5]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['CN', 'UFC', 'US']})).equals(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['CN', 'UFC', 'US'], 'mean_along_rows':[50.5, 151.0, 251.5]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['CN', 'UFC', 'tf']})).equals(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['CN', 'UFC', 'tf'], 'mean_along_rows':[50.5, 151.0, 251.5]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['AI', 'UFC', 'tf']})).equals(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['AI', 'UFC', 'tf'], 'mean_along_rows':[50.5, 151.0, 251.5]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['AI', 'AG', 'tf']})).equals(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['AI', 'AG', 'tf'], 'mean_along_rows':[50.5, 151.0, 251.5]}))
    assert candidate(pd.DataFrame({'A':[100,2,3], 'B':[100,300,500], 'Region':['AI', 'AG', 'tf']})).equals(pd.DataFrame({'A':[100,2,3], 'B':[100,300,500], 'Region':['AI', 'AG', 'tf'], 'mean_along_rows':[100.0, 151.0, 251.5]}))
    assert candidate(pd.DataFrame({'A':[100,200,3], 'B':[100,300,500], 'Region':['AI', 'AG', 'tf']})).equals(pd.DataFrame({'A':[100,200,3], 'B':[100,300,500], 'Region':['AI', 'AG', 'tf'], 'mean_along_rows':[100.0, 250.0, 251.5]}))
    assert candidate(pd.DataFrame({'A':[100,200,500], 'B':[100,300,500], 'Region':['AI', 'AG', 'tf']})).equals(pd.DataFrame({'A':[100,200,500], 'B':[100,300,500], 'Region':['AI', 'AG', 'tf'], 'mean_along_rows':[100.0, 250.0, 500.0]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def compute_mean_along_rows(df):` that takes a DataFrame and returns a DataFrame with a new column named `mean_along_rows` to solve the following problem:
  You can specify a new column named `mean_along_rows` that contains the mean of each row. You also need to compute the mean along the rows, so use axis=1.

validator:
  table_test:
    function_name: compute_mean_along_rows
    test_cases:
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['US', 'US', 'US']})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['w', 'US', 'US']})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['CN', 'US', 'US']})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['CN', 'UFC', 'US']})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['CN', 'UFC', 'tf']})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['AI', 'UFC', 'tf']})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'Region':['AI', 'AG', 'tf']})`"]
    - ["`pd.DataFrame({'A':[100,2,3], 'B':[100,300,500], 'Region':['AI', 'AG', 'tf']})`"]
    - ["`pd.DataFrame({'A':[100,200,3], 'B':[100,300,500], 'Region':['AI', 'AG', 'tf']})`"]
    - ["`pd.DataFrame({'A':[100,200,500], 'B':[100,300,500], 'Region':['AI', 'AG', 'tf']})`"]
"""

def compute_mean_along_rows(df):
    df['mean_along_rows'] = df.mean(axis=1, numeric_only=True)
    return df
