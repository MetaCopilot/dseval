'''
### Prompt ###

import pandas as pd

def insert_row_at_arbitrary_in_dataframe(df, row_to_insert):
    """
    Inserts a row into a dataframe at a specified row with no ingore index, and sort & reset the index with drop=True. 
    Returns the new dataframe.
    """

### Solution ###

    df = df.append(row_to_insert, ignore_index=False)
    df = df.sort_index().reset_index(drop=True)
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'onset':[23.107, 41.815, 61.606], 'length':[1,2,3]}), pd.DataFrame({'onset': 30.0, 'length': 1.3}, index=[3])).equals(pd.DataFrame({'onset':[23.107, 41.815, 61.606, 30.0], 'length':[1,2,3,1.3]}))
    assert candidate(pd.DataFrame({'onset':[28.604, 41.815, 61.606], 'length':[1,2,3]}), pd.DataFrame({'onset': 30.0, 'length': 1.3}, index=[3])).equals(pd.DataFrame({'onset':[28.604, 41.815, 61.606, 30.0], 'length':[1,2,3,1.3]}))
    assert candidate(pd.DataFrame({'onset':[28.604, 41.815, 61.606], 'length':[1,2,4]}), pd.DataFrame({'onset': 30.0, 'length': 1.3}, index=[3])).equals(pd.DataFrame({'onset':[28.604, 41.815, 61.606, 30.0], 'length':[1,2,4,1.3]}))
    assert candidate(pd.DataFrame({'onset':[28.604, 41.815, 61.606], 'length':[1,3,4]}), pd.DataFrame({'onset': 30.0, 'length': 1.3}, index=[3])).equals(pd.DataFrame({'onset':[28.604, 41.815, 61.606, 30.0], 'length':[1,3,4,1.3]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def insert_row_at_arbitrary_in_dataframe(df, row_to_insert):` that takes a DataFrame and a row to insert (also in DataFrame type) and returns a DataFrame to solve the following problem:
  Inserts a row into a dataframe at a specified row with no ingore index, and sort & reset the index with drop=True. 

validator:
  table_test:
    function_name: insert_row_at_arbitrary_in_dataframe
    test_cases:
    - ["`pd.DataFrame({'onset':[23.107, 41.815, 61.606], 'length':[1,2,3]})`", "`pd.DataFrame({'onset': 30.0, 'length': 1.3}, index=[3])`"]
    - ["`pd.DataFrame({'onset':[28.604, 41.815, 61.606], 'length':[1,2,3]})`", "`pd.DataFrame({'onset': 30.0, 'length': 1.3}, index=[3])`"]
    - ["`pd.DataFrame({'onset':[28.604, 41.815, 61.606], 'length':[1,2,4]})`", "`pd.DataFrame({'onset': 30.0, 'length': 1.3}, index=[3])`"]
    - ["`pd.DataFrame({'onset':[28.604, 41.815, 61.606], 'length':[1,3,4]})`", "`pd.DataFrame({'onset': 30.0, 'length': 1.3}, index=[3])`"]
"""

def insert_row_at_arbitrary_in_dataframe(df, row_to_insert):
    df = pd.concat([df, row_to_insert], ignore_index=False)
    df = df.sort_index().reset_index(drop=True)
    return df
