'''
### Prompt ###

import pandas as pd

def counting_occurrences_of_a_value(series, value):
    # Count the number of occurrences of a value in a series
    # Return the count

### Solution ###

    return series.value_counts()[value]

### Test ###

def check(candidate):
    assert candidate(pd.Series([1, 2, 3, 1, 2, 3, 1, 2, 3]), 1) == 3
    assert candidate(pd.Series([1, 2, 3, 1, 1, 3, 1, 2, 3]), 1) == 4
    assert candidate(pd.Series([1, 4, 3, 1, 1, 3, 1, 2, 3]), 1) == 4
    assert candidate(pd.Series([1, 2, 3, 1, 1, 35, 1, 2, 3]), 1) == 4
    assert candidate(pd.Series([1, 2, 13, 1, 1, 3, 1, 12, 3]), 1) == 4
    assert candidate(pd.Series([11, 2, 3, 1, 1, 3, 1, 2, 3]), 1) == 3
    assert candidate(pd.Series([1, 2, 3, 1, 1, 43, 1, 42, 35]), 1) == 4
    assert candidate(pd.Series([1, 2, 3, 1, 1, 3, 1, 2, 3]), 2) == 2
    assert candidate(pd.Series([1, 2, 3, 1, 1, 3, 1, 2, 3]), 3) == 3
    assert candidate(pd.Series([1, 2, 3, 1, 1, 3, 1, 2, 33]), 33) == 1
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def counting_occurrences_of_a_value(series, value):` that takes a pandas Series and a value and returns an integer to solve the following problem:
  Count the number of occurrences of a value in a series.

validator:
  table_test:
    function_name: counting_occurrences_of_a_value
    test_cases:
    - ["`pd.Series([1, 2, 3, 1, 2, 3, 1, 2, 3])`", 1]
    - ["`pd.Series([1, 2, 3, 1, 1, 3, 1, 2, 3])`", 1]
    - ["`pd.Series([1, 4, 3, 1, 1, 3, 1, 2, 3])`", 1]
    - ["`pd.Series([1, 2, 3, 1, 1, 35, 1, 2, 3])`", 1]
    - ["`pd.Series([1, 2, 13, 1, 1, 3, 1, 12, 3])`", 1]
    - ["`pd.Series([11, 2, 3, 1, 1, 3, 1, 2, 3])`", 1]
    - ["`pd.Series([1, 2, 3, 1, 1, 43, 1, 42, 35])`", 1]
    - ["`pd.Series([1, 2, 3, 1, 1, 3, 1, 2, 3])`", 2]
    - ["`pd.Series([1, 2, 3, 1, 1, 3, 1, 2, 3])`", 3]
    - ["`pd.Series([1, 2, 3, 1, 1, 3, 1, 2, 33])`", 33]
"""

def counting_occurrences_of_a_value(series, value):
    return series.value_counts()[value]
