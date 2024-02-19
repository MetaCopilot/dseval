'''
### Prompt ###

import pandas as pd

def get_value_counts(df):
    # I want to get the counts of unique values of the dataframe. count_values implements this however I want to use its output somewhere else. 
    # How can I convert .count_values output to a pandas dataframe.
    # Use rename_axis('unique_values') for name ('counts') of column from index and reset_index
    # return the final dataframe

### Solution ###

    return df.value_counts().rename_axis('unique_values').reset_index(name='counts')

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a':[1, 1, 2, 2, 2]})).equals(pd.DataFrame({'unique_values':[2, 1], 'counts':[3, 2]}))
    assert candidate(pd.DataFrame({'iscas':[7, 5, 6, 3, 8]})).equals(pd.DataFrame({'unique_values':[3, 5, 6, 7, 8], 'counts':[1, 1, 1, 1, 1]}))
    assert candidate(pd.DataFrame({'a':[1, 2, 2, 2, 2]})).equals(pd.DataFrame({'unique_values':[2, 1], 'counts':[4, 1]}))
    assert candidate(pd.DataFrame({'a':[2, 2, 2, 2, 2]})).equals(pd.DataFrame({'unique_values':[2], 'counts':[5]}))
    assert candidate(pd.DataFrame({'a':[2, 2, 2, 5, 2]})).equals(pd.DataFrame({'unique_values':[2, 5], 'counts':[4, 1]}))
    assert candidate(pd.DataFrame({'a':[2, 2, 2, 5, 3]})).equals(pd.DataFrame({'unique_values':[2, 3, 5], 'counts':[3, 1, 1]}))
    assert candidate(pd.DataFrame({'a':[2, 2, 2, 5, 1]})).equals(pd.DataFrame({'unique_values':[2, 1, 5], 'counts':[3, 1, 1]}))
    assert candidate(pd.DataFrame({'a':[2, 1, 2, 5, 1]})).equals(pd.DataFrame({'unique_values':[1, 2, 5], 'counts':[2, 2, 1]}))
    assert candidate(pd.DataFrame({'a':[1, 1, 2, 5, 1]})).equals(pd.DataFrame({'unique_values':[1, 2, 5], 'counts':[3, 1, 1]}))
    assert candidate(pd.DataFrame({'a':[1, 1, 2, 4, 1]})).equals(pd.DataFrame({'unique_values':[1, 2, 4], 'counts':[3, 1, 1]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def get_value_counts(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  I want to get the counts of unique values of the dataframe. count_values implements this however I want to use its output somewhere else. 
  How can I convert .count_values output to a pandas dataframe.
  Use rename_axis('unique_values') for name ('counts') of column from index and reset_index

validator:
  table_test:
    function_name: get_value_counts
    test_cases:
    - ["`pd.DataFrame({'a':[1, 1, 2, 2, 2]})`"]
    - ["`pd.DataFrame({'iscas':[7, 5, 6, 3, 8]})`"]
    - ["`pd.DataFrame({'a':[1, 2, 2, 2, 2]})`"]
    - ["`pd.DataFrame({'a':[2, 2, 2, 2, 2]})`"]
    - ["`pd.DataFrame({'a':[2, 2, 2, 5, 2]})`"]
    - ["`pd.DataFrame({'a':[2, 2, 2, 5, 3]})`"]
    - ["`pd.DataFrame({'a':[2, 2, 2, 5, 1]})`"]
    - ["`pd.DataFrame({'a':[2, 1, 2, 5, 1]})`"]
    - ["`pd.DataFrame({'a':[1, 1, 2, 5, 1]})`"]
    - ["`pd.DataFrame({'a':[1, 1, 2, 4, 1]})`"]
"""

def get_value_counts(df):
    return df.value_counts().rename_axis('unique_values').reset_index(name='counts')
