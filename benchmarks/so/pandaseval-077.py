'''
### Prompt ###

import pandas as pd

def find_col_a_gt_col_b_rows(df, col_a, col_b):
    # Find rows in df where col_a > col_b
    # Return the rows

### Solution ###

    return df[df[col_a] > df[col_b]]

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [5, 2, 3], 'B': [4, 5, 6]}), 'A', 'B').equals(pd.DataFrame({'A': [5], 'B': [4]}))
    assert candidate(pd.DataFrame({'A': [5, 7, 3], 'B': [4, 5, 6]}), 'A', 'B').equals(pd.DataFrame({'A': [5, 7], 'B': [4, 5]}))
    assert candidate(pd.DataFrame({'A': [5, 7, 3], 'B': [4, 2, 6]}), 'A', 'B').equals(pd.DataFrame({'A': [5, 7], 'B': [4, 2]}))
    assert candidate(pd.DataFrame({'A': [6, 7, 3], 'B': [4, 2, 6]}), 'A', 'B').equals(pd.DataFrame({'A': [6, 7], 'B': [4, 2]}))
    assert candidate(pd.DataFrame({'A': [6, 8, 3], 'B': [4, 2, 6]}), 'A', 'B').equals(pd.DataFrame({'A': [6, 8], 'B': [4, 2]}))
    assert candidate(pd.DataFrame({'A': [6, 8, 3], 'B': [4, 3, 6]}), 'A', 'B').equals(pd.DataFrame({'A': [6, 8], 'B': [4, 3]}))
    assert candidate(pd.DataFrame({'A': [6, 8, 3], 'B': [4, 3, 4]}), 'A', 'B').equals(pd.DataFrame({'A': [6, 8], 'B': [4, 3]}))
    assert candidate(pd.DataFrame({'A': [6, 8, 1], 'B': [4, 3, 4]}), 'A', 'B').equals(pd.DataFrame({'A': [6, 8], 'B': [4, 3]}))
    assert candidate(pd.DataFrame({'A': [6, 8, 1], 'B': [4, 3, 14]}), 'A', 'B').equals(pd.DataFrame({'A': [6, 8], 'B': [4, 3]}))
    assert candidate(pd.DataFrame({'A': [6, 18, 1], 'B': [4, 3, 14]}), 'A', 'B').equals(pd.DataFrame({'A': [6, 18], 'B': [4, 3]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def find_col_a_gt_col_b_rows(df, col_a, col_b):` that takes a DataFrame and two column names and returns a DataFrame to solve the following problem:
  Find rows in df where col_a > col_b

validator:
  table_test:
    function_name: find_col_a_gt_col_b_rows
    test_cases:
    - ["`pd.DataFrame({'A': [5, 2, 3], 'B': [4, 5, 6]})`", A, B]
    - ["`pd.DataFrame({'A': [5, 7, 3], 'B': [4, 5, 6]})`", A, B]
    - ["`pd.DataFrame({'A': [5, 7, 3], 'B': [4, 2, 6]})`", A, B]
    - ["`pd.DataFrame({'A': [6, 7, 3], 'B': [4, 2, 6]})`", A, B]
    - ["`pd.DataFrame({'A': [6, 8, 3], 'B': [4, 2, 6]})`", A, B]
    - ["`pd.DataFrame({'A': [6, 8, 3], 'B': [4, 3, 6]})`", A, B]
    - ["`pd.DataFrame({'A': [6, 8, 3], 'B': [4, 3, 4]})`", A, B]
    - ["`pd.DataFrame({'A': [6, 8, 1], 'B': [4, 3, 4]})`", A, B]
    - ["`pd.DataFrame({'A': [6, 8, 1], 'B': [4, 3, 14]})`", A, B]
    - ["`pd.DataFrame({'A': [6, 18, 1], 'B': [4, 3, 14]})`", A, B]
"""

def find_col_a_gt_col_b_rows(df, col_a, col_b):
    return df[df[col_a] > df[col_b]]
