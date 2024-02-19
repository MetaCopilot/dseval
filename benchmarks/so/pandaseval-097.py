'''
### Prompt ###

import pandas as pd

def rename_column(df, old_name, new_name):
    # How would I rename the only one column header?
    # return the changed dataframe

### Solution ###

    df = df.rename(columns={old_name: new_name})
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]}), 'A', 'D').equals(pd.DataFrame({'D': [1, 2, 3], 'B': [100, 300, 500]}))
    assert candidate(pd.DataFrame({'A': [1, 2, 3], 'B': [21, 300, 500]}), 'A', 'D').equals(pd.DataFrame({'D': [1, 2, 3], 'B': [21, 300, 500]}))
    assert candidate(pd.DataFrame({'A': [1, 3, 3], 'B': [21, 300, 500]}), 'A', 'D').equals(pd.DataFrame({'D': [1, 3, 3], 'B': [21, 300, 500]}))
    assert candidate(pd.DataFrame({'A': [4, 3, 3], 'B': [21, 300, 500]}), 'A', 'D').equals(pd.DataFrame({'D': [4, 3, 3], 'B': [21, 300, 500]}))
    assert candidate(pd.DataFrame({'A': [4, 3, 3], 'B': [21, 42, 500]}), 'A', 'D').equals(pd.DataFrame({'D': [4, 3, 3], 'B': [21, 42, 500]}))
    assert candidate(pd.DataFrame({'A': [4, 3, 4], 'B': [21, 42, 500]}), 'A', 'D').equals(pd.DataFrame({'D': [4, 3, 4], 'B': [21, 42, 500]}))
    assert candidate(pd.DataFrame({'A': [4, 3, 4], 'B': [21, 42, 32]}), 'A', 'D').equals(pd.DataFrame({'D': [4, 3, 4], 'B': [21, 42, 32]}))
    assert candidate(pd.DataFrame({'A': [4, 4, 4], 'B': [21, 42, 32]}), 'A', 'D').equals(pd.DataFrame({'D': [4, 4, 4], 'B': [21, 42, 32]}))
    assert candidate(pd.DataFrame({'A': [4, 4, 4], 'B': [21, 12, 32]}), 'A', 'D').equals(pd.DataFrame({'D': [4, 4, 4], 'B': [21, 12, 32]}))
    assert candidate(pd.DataFrame({'A': [4, 4, 4], 'B': [21, 12, 21]}), 'A', 'D').equals(pd.DataFrame({'D': [4, 4, 4], 'B': [21, 12, 21]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def rename_column(df, old_name, new_name):` that takes a DataFrame, an old column name, and a new column name and returns a DataFrame to solve the following problem:
  How would I rename the only one column header?

validator:
  table_test:
    function_name: rename_column
    test_cases:
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [100, 300, 500]})`", A, D]
    - ["`pd.DataFrame({'A': [1, 2, 3], 'B': [21, 300, 500]})`", A, D]
    - ["`pd.DataFrame({'A': [1, 3, 3], 'B': [21, 300, 500]})`", A, D]
    - ["`pd.DataFrame({'A': [4, 3, 3], 'B': [21, 300, 500]})`", A, D]
    - ["`pd.DataFrame({'A': [4, 3, 3], 'B': [21, 42, 500]})`", A, D]
    - ["`pd.DataFrame({'A': [4, 3, 4], 'B': [21, 42, 500]})`", A, D]
    - ["`pd.DataFrame({'A': [4, 3, 4], 'B': [21, 42, 32]})`", A, D]
    - ["`pd.DataFrame({'A': [4, 4, 4], 'B': [21, 42, 32]})`", A, D]
    - ["`pd.DataFrame({'A': [4, 4, 4], 'B': [21, 12, 32]})`", A, D]
    - ["`pd.DataFrame({'A': [4, 4, 4], 'B': [21, 12, 21]})`", A, D]
"""

def rename_column(df, old_name, new_name):
    df = df.rename(columns={old_name: new_name})
    return df
