'''
### Prompt ###

import pandas as pd

def create_empty_df(col_names):
    # Pandas create empty DataFrame with only column names
    # Return: DataFrame

### Solution ###

    return pd.DataFrame(columns=col_names)

### Test ###

def check(candidate):
    assert candidate(['A', 'B', 'C']).equals(pd.DataFrame(columns=['A', 'B', 'C']))
    assert candidate(['A', 'd', 'C']).equals(pd.DataFrame(columns=['A', 'd', 'C']))
    assert candidate(['A', 'B', 'E']).equals(pd.DataFrame(columns=['A', 'B', 'E']))
    assert candidate(['A', 'Q', 'C']).equals(pd.DataFrame(columns=['A', 'Q', 'C']))
    assert candidate(['X', 'B', 'C']).equals(pd.DataFrame(columns=['X', 'B', 'C']))
    assert candidate(['A', 'B', 'N']).equals(pd.DataFrame(columns=['A', 'B', 'N']))
    assert candidate(['A', 'G', 'C']).equals(pd.DataFrame(columns=['A', 'G', 'C']))
    assert candidate(['T', 'B', 'C']).equals(pd.DataFrame(columns=['T', 'B', 'C']))
    assert candidate(['A', 'S', 'C']).equals(pd.DataFrame(columns=['A', 'S', 'C']))
    assert candidate(['A', 'B', 'V']).equals(pd.DataFrame(columns=['A', 'B', 'V']))
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def create_empty_df(col_names):` that takes a list of column names and returns an empty DataFrame with only column names.

validator:
  table_test:
    function_name: create_empty_df
    test_cases:
    - [['A', 'B', 'C']]
    - [['A', 'd', 'C']]
    - [['A', 'B', 'E']]
    - [['A', 'Q', 'C']]
    - [['X', 'B', 'C']]
    - [['A', 'B', 'N']]
    - [['A', 'G', 'C']]
    - [['T', 'B', 'C']]
    - [['A', 'S', 'C']]
    - [['A', 'B', 'V']]
"""

def create_empty_df(col_names):
    return pd.DataFrame(columns=col_names)
