'''
### Prompt ###

import pandas as pd

def remove_duplicates_by_column(df, col1, col2):
    # I have a dataframe with repeat values in column `col1`. I want to drop duplicates, keeping the row with the last value in column `col2`.
    # How would I do that?
    # return the final dataframe

### Solution ###

    return df.drop_duplicates(subset=col1, keep="last")

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A': [1, 1, 3], 'B': [100, 300, 500]}), 'A', 'B').equals(pd.DataFrame({'A': [1, 3], 'B': [300, 500]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [1, 1, 3], 'B': [100, 350, 500]}), 'A', 'B').equals(pd.DataFrame({'A': [1, 3], 'B': [350, 500]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [1, 1, 3], 'B': [100, 350, 600]}), 'A', 'B').equals(pd.DataFrame({'A': [1, 3], 'B': [350, 600]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [1, 1, 3], 'B': [120, 350, 600]}), 'A', 'B').equals(pd.DataFrame({'A': [1, 3], 'B': [350, 600]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [1, 1, 3], 'B': [531, 350, 600]}), 'A', 'B').equals(pd.DataFrame({'A': [1, 3], 'B': [350, 600]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [1, 1, 3], 'B': [123, 350, 600]}), 'A', 'B').equals(pd.DataFrame({'A': [1, 3], 'B': [350, 600]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [1, 1, 3], 'B': [123, 125, 600]}), 'A', 'B').equals(pd.DataFrame({'A': [1, 3], 'B': [125, 600]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [1, 1, 3], 'B': [123, 125, 532]}), 'A', 'B').equals(pd.DataFrame({'A': [1, 3], 'B': [125, 532]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [1, 1, 3], 'B': [74, 125, 532]}), 'A', 'B').equals(pd.DataFrame({'A': [1, 3], 'B': [125, 532]}, index=[1, 2]))
    assert candidate(pd.DataFrame({'A': [1, 1, 3], 'B': [74, 125, 45]}), 'A', 'B').equals(pd.DataFrame({'A': [1, 3], 'B': [125, 45]}, index=[1, 2]))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def remove_duplicates_by_column(df, col1, col2):` that takes a DataFrame and two column names and returns a DataFrame to solve the following problem:
  I have a dataframe with repeat values in column `col1`. I want to drop duplicates, keeping the row with the last value in column `col2`.

validator:
  table_test:
    function_name: remove_duplicates_by_column
    test_cases:
    - ["`pd.DataFrame({'A': [1, 1, 3], 'B': [100, 300, 500]})`", "A", "B"]
    - ["`pd.DataFrame({'A': [1, 1, 3], 'B': [100, 350, 500]})`", "A", "B"]
    - ["`pd.DataFrame({'A': [1, 1, 3], 'B': [100, 350, 600]})`", "A", "B"]
    - ["`pd.DataFrame({'A': [1, 1, 3], 'B': [120, 350, 600]})`", "A", "B"]
    - ["`pd.DataFrame({'A': [1, 1, 3], 'B': [531, 350, 600]})`", "A", "B"]
    - ["`pd.DataFrame({'A': [1, 1, 3], 'B': [123, 350, 600]})`", "A", "B"]
    - ["`pd.DataFrame({'A': [1, 1, 3], 'B': [123, 125, 600]})`", "A", "B"]
    - ["`pd.DataFrame({'A': [1, 1, 3], 'B': [123, 125, 532]})`", "A", "B"]
    - ["`pd.DataFrame({'A': [1, 1, 3], 'B': [74, 125, 532]})`", "A", "B"]
    - ["`pd.DataFrame({'A': [1, 1, 3], 'B': [74, 125, 45]})`", "A", "B"]
"""

def remove_duplicates_by_column(df, col1, col2):
    return df.drop_duplicates(subset=col1, keep="last")
