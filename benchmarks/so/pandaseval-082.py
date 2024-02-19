'''
### Prompt ###

from typing import List
import pandas as pd
import numpy as np

def append_in_dataframe(df, list_to_append, column_name_list) -> pd.DataFrame:
    """    
    Params:
        df: The dataframe to append to.
        list_to_append: The list to append.
        column_name_list: The column names of the list to append.

    Returns:
        The dataframe with the list appended.
    """

### Solution ###

    list_to_append = pd.DataFrame(list_to_append, columns=column_name_list)
    df = df.append(list_to_append)
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'col1': [1, 2], 'col2': [4, 5]}), [5, 6] , ['col1']).equals(pd.DataFrame({'col1': [1, 2, 5, 6], 'col2': [4, 5, np.nan, np.nan]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'col1': [5, 2], 'col2': [4, 5]}), [5, 6] , ['col1']).equals(pd.DataFrame({'col1': [5, 2, 5, 6], 'col2': [4, 5, np.nan, np.nan]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'col1': [5, 2], 'col2': [1, 5]}), [5, 6] , ['col1']).equals(pd.DataFrame({'col1': [5, 2, 5, 6], 'col2': [1, 5, np.nan, np.nan]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'col1': [5, 2], 'col2': [1, 7]}), [5, 6] , ['col1']).equals(pd.DataFrame({'col1': [5, 2, 5, 6], 'col2': [1, 7, np.nan, np.nan]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'col1': [5, 2], 'col2': [1, 7]}), [5, 9] , ['col1']).equals(pd.DataFrame({'col1': [5, 2, 5, 9], 'col2': [1, 7, np.nan, np.nan]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'col1': [5, 2], 'col2': [1, 7]}), [15, 9] , ['col1']).equals(pd.DataFrame({'col1': [5, 2, 15, 9], 'col2': [1, 7, np.nan, np.nan]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'col1': [5, 2], 'col2': [11, 7]}), [15, 9] , ['col1']).equals(pd.DataFrame({'col1': [5, 2, 15, 9], 'col2': [11, 7, np.nan, np.nan]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'col1': [5, 12], 'col2': [11, 7]}), [15, 9] , ['col1']).equals(pd.DataFrame({'col1': [5, 12, 15, 9], 'col2': [11, 7, np.nan, np.nan]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'col1': [15, 12], 'col2': [11, 7]}), [15, 9] , ['col1']).equals(pd.DataFrame({'col1': [15, 12, 15, 9], 'col2': [11, 7, np.nan, np.nan]}, index=[0, 1, 0, 1]))
    assert candidate(pd.DataFrame({'col1': [15, 12], 'col2': [11, 7]}), [15, 19] , ['col1']).equals(pd.DataFrame({'col1': [15, 12, 15, 19], 'col2': [11, 7, np.nan, np.nan]}, index=[0, 1, 0, 1]))
'''

# %%
import pandas as pd
import numpy as np
from typing import List

# %%

"""
question: |
  Write a function `def append_in_dataframe(df, list_to_append, column_name_list) -> pd.DataFrame:` that takes a DataFrame, a list to append, and a list of column names and returns a DataFrame to solve the following problem:
  Append the list to the dataframe with the given column names.

validator:
  table_test:
    function_name: append_in_dataframe
    test_cases:
    - ["`pd.DataFrame({'col1': [1, 2], 'col2': [4, 5]})`", [5, 6], ['col1']]
    - ["`pd.DataFrame({'col1': [5, 2], 'col2': [4, 5]})`", [5, 6], ['col1']]
    - ["`pd.DataFrame({'col1': [5, 2], 'col2': [1, 5]})`", [5, 6], ['col1']]
    - ["`pd.DataFrame({'col1': [5, 2], 'col2': [1, 7]})`", [5, 6], ['col1']]
    - ["`pd.DataFrame({'col1': [5, 2], 'col2': [1, 7]})`", [5, 9], ['col1']]
    - ["`pd.DataFrame({'col1': [5, 2], 'col2': [1, 7]})`", [15, 9], ['col1']]
    - ["`pd.DataFrame({'col1': [5, 2], 'col2': [11, 7]})`", [15, 9], ['col1']]
    - ["`pd.DataFrame({'col1': [5, 12], 'col2': [11, 7]})`", [15, 9], ['col1']]
    - ["`pd.DataFrame({'col1': [15, 12], 'col2': [11, 7]})`", [15, 9], ['col1']]
    - ["`pd.DataFrame({'col1': [15, 12], 'col2': [11, 7]})`", [15, 19], ['col1']]
"""

def append_in_dataframe(df, list_to_append, column_name_list) -> pd.DataFrame:
    list_to_append = pd.DataFrame(list_to_append, columns=column_name_list)
    df = pd.concat([df, list_to_append], ignore_index=True)
    return df
