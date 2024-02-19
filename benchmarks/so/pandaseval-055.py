'''
### Prompt ###

import pandas as pd

def counting_consecutive_positive_values(y):
    # Counting consecutive positive values in Python/pandas array
    # I'm trying to count consecutive up days in equity return data; so if a positive day is 1 and a negative is 0, a list y=[0,0,1,1,1,0,0,1,0,1,1] should return z=[0,0,1,2,3,0,0,1,0,1,2].
    # Return the result

### Solution ###

    return y * (y.groupby((y != y.shift()).cumsum()).cumcount() + 1)

### Test ###

def check(candidate):
    assert candidate(pd.Series([0,0,1,1])).equals(pd.Series([0,0,1,2]))
    assert candidate(pd.Series([0,1,1,1])).equals(pd.Series([0,1,2,3]))
    assert candidate(pd.Series([0,1,1,0])).equals(pd.Series([0,1,2,0]))
    assert candidate(pd.Series([1,1,1,0])).equals(pd.Series([1,2,3,0]))
    assert candidate(pd.Series([1,1,4,0])).equals(pd.Series([1,2,4,0]))
    assert candidate(pd.Series([1,1,3,0])).equals(pd.Series([1,2,3,0]))
    assert candidate(pd.Series([1,1,2,0])).equals(pd.Series([1,2,2,0]))
    assert candidate(pd.Series([1,3,2,0])).equals(pd.Series([1,3,2,0]))
    assert candidate(pd.Series([1,3,2,1])).equals(pd.Series([1,3,2,1]))
    assert candidate(pd.Series([1,3,3,1])).equals(pd.Series([1,3,6,1]))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def counting_consecutive_positive_values(y):` that takes a pandas Series and returns a pandas Series to solve the following problem:
  Counting consecutive positive values in Python/pandas array
  I'm trying to count consecutive up days in equity return data; so if a positive day is 1 and a negative is 0, a list y=[0,0,1,1,1,0,0,1,0,1,1] should return z=[0,0,1,2,3,0,0,1,0,1,2].

validator:
  table_test:
    function_name: counting_consecutive_positive_values
    test_cases:
    - ["`pd.Series([0,0,1,1])`"]
    - ["`pd.Series([0,1,1,1])`"]
    - ["`pd.Series([0,1,1,0])`"]
    - ["`pd.Series([1,1,1,0])`"]
    - ["`pd.Series([1,1,4,0])`"]
    - ["`pd.Series([1,1,3,0])`"]
    - ["`pd.Series([1,1,2,0])`"]
    - ["`pd.Series([1,3,2,0])`"]
    - ["`pd.Series([1,3,2,1])`"]
    - ["`pd.Series([1,3,3,1])`"]
"""

def counting_consecutive_positive_values(y):
    y = (y > 0).astype(int)
    return y * (y.groupby((y != y.shift()).cumsum()).cumcount() + 1)
