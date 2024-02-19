'''
### Prompt ###

import pandas as pd

def get_percentage_of_each_gender(series):
    # Given a pandas series that represents frequencies of a value, how can I turn those frequencies into percentages?
    # Return the percentage of each gender.

### Solution ###

    return series.value_counts(normalize=True)

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'sex': ['male'] * 5 + ['female'] * 3}).sex).equals(pd.DataFrame({'sex': ['male'] * 5 + ['female'] * 3}).sex.value_counts(normalize=True))
    assert candidate(pd.DataFrame({'sex': ['male'] * 4 + ['female'] * 3}).sex).equals(pd.DataFrame({'sex': ['male'] * 4 + ['female'] * 3}).sex.value_counts(normalize=True))
    assert candidate(pd.DataFrame({'sex': ['male'] * 6 + ['female'] * 3}).sex).equals(pd.DataFrame({'sex': ['male'] * 6 + ['female'] * 3}).sex.value_counts(normalize=True))
    assert candidate(pd.DataFrame({'sex': ['male'] * 5 + ['female'] * 1}).sex).equals(pd.DataFrame({'sex': ['male'] * 5 + ['female'] * 1}).sex.value_counts(normalize=True))
    assert candidate(pd.DataFrame({'sex': ['male'] * 2 + ['female'] * 3}).sex).equals(pd.DataFrame({'sex': ['male'] * 2 + ['female'] * 3}).sex.value_counts(normalize=True))
    assert candidate(pd.DataFrame({'sex': ['male'] * 4 + ['female'] * 13}).sex).equals(pd.DataFrame({'sex': ['male'] * 4 + ['female'] * 13}).sex.value_counts(normalize=True))
    assert candidate(pd.DataFrame({'sex': ['male'] * 15 + ['female'] * 13}).sex).equals(pd.DataFrame({'sex': ['male'] * 15 + ['female'] * 13}).sex.value_counts(normalize=True))
    assert candidate(pd.DataFrame({'sex': ['male'] * 43 + ['female'] * 3}).sex).equals(pd.DataFrame({'sex': ['male'] * 43 + ['female'] * 3}).sex.value_counts(normalize=True))
    assert candidate(pd.DataFrame({'sex': ['male'] * 53 + ['female'] * 33}).sex).equals(pd.DataFrame({'sex': ['male'] * 53 + ['female'] * 33}).sex.value_counts(normalize=True))
    assert candidate(pd.DataFrame({'sex': ['male'] * 25 + ['female'] * 32}).sex).equals(pd.DataFrame({'sex': ['male'] * 25 + ['female'] * 32}).sex.value_counts(normalize=True))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def get_percentage_of_each_gender(series):` that takes a pandas series that represents frequencies of a value and returns the percentage of each gender to solve the following problem:
  Given a pandas series that represents frequencies of a value, how can I turn those frequencies into percentages?

validator:
  table_test:
    function_name: get_percentage_of_each_gender
    test_cases:
    - ["`pd.DataFrame({'sex': ['male'] * 5 + ['female'] * 3}).sex`"]
    - ["`pd.DataFrame({'sex': ['male'] * 4 + ['female'] * 3}).sex`"]
    - ["`pd.DataFrame({'sex': ['male'] * 6 + ['female'] * 3}).sex`"]
    - ["`pd.DataFrame({'sex': ['male'] * 5 + ['female'] * 1}).sex`"]
    - ["`pd.DataFrame({'sex': ['male'] * 2 + ['female'] * 3}).sex`"]
    - ["`pd.DataFrame({'sex': ['male'] * 4 + ['female'] * 13}).sex`"]
    - ["`pd.DataFrame({'sex': ['male'] * 15 + ['female'] * 13}).sex`"]
    - ["`pd.DataFrame({'sex': ['male'] * 43 + ['female'] * 3}).sex`"]
    - ["`pd.DataFrame({'sex': ['male'] * 53 + ['female'] * 33}).sex`"]
    - ["`pd.DataFrame({'sex': ['male'] * 25 + ['female'] * 32}).sex`"]
"""

def get_percentage_of_each_gender(series):
    return series.value_counts(normalize=True)
