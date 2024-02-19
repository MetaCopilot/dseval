'''
### Prompt ###

import pandas as pd

def is_contain_particular_value(series, value):
    # How to determine whether a Pandas Column contains a particular value?
    # Return the result

### Solution ###

    return value in series.unique()

### Test ###

def check(candidate):
    assert candidate(pd.Series([1, 2, 3]), 2) == True
    assert candidate(pd.Series([1, 2, 3]), 3) == True
    assert candidate(pd.Series([1, 2, 4]), 4) == True
    assert candidate(pd.Series([1, 3, 4]), 4) == True
    assert candidate(pd.Series([2, 3, 4]), 4) == True
    assert candidate(pd.Series([2, 3, 4]), 5) == False
    assert candidate(pd.Series([2, 3, 4]), 6) == False
    assert candidate(pd.Series([2, 3, 4]), 7) == False
    assert candidate(pd.Series([2, 3, 4]), 8) == False
    assert candidate(pd.Series([2, 3, 4]), 0) == False
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def is_contain_particular_value(series, value):` that takes a pandas Series and a value and returns a boolean to solve the following problem:
  How to determine whether a Pandas Column contains a particular value?

validator:
  table_test:
    function_name: is_contain_particular_value
    test_cases:
    - ["`pd.Series([1, 2, 3])`", 2]
    - ["`pd.Series([1, 2, 3])`", 3]
    - ["`pd.Series([1, 2, 4])`", 4]
    - ["`pd.Series([1, 3, 4])`", 4]
    - ["`pd.Series([2, 3, 4])`", 4]
    - ["`pd.Series([2, 3, 4])`", 5]
    - ["`pd.Series([2, 3, 4])`", 6]
    - ["`pd.Series([2, 3, 4])`", 7]
    - ["`pd.Series([2, 3, 4])`", 8]
    - ["`pd.Series([2, 3, 4])`", 0]
"""

def is_contain_particular_value(series, value):
    return value in series.unique()
