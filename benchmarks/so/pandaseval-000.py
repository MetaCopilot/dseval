'''
### Prompt ###

import pandas as pd
import numpy as np

def drop_rows_col_nan(df, col_name):
    # How to drop rows of Pandas DataFrame whose value in a certain column is NaN
    return

### Solution ###

df.dropna(subset=[col_name])

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame([[1,2,3],[np.nan,2,3],[1,np.nan,3],[1,2,np.nan]], columns=['A','B','C']), 'B').equals(pd.DataFrame([[1,2,3],[np.nan,2,3],[1,np.nan,3],[1,2,np.nan]], columns=['A','B','C']).dropna(subset=['B']))
    assert candidate(pd.DataFrame([[5,2,3],[np.nan,2,3],[1,np.nan,3],[1,2,np.nan]], columns=['A','B','C']), 'B').equals(pd.DataFrame([[5,2,3],[np.nan,2,3],[1,np.nan,3],[1,2,np.nan]], columns=['A','B','C']).dropna(subset=['B']))
    assert candidate(pd.DataFrame([[5,2,1],[np.nan,2,3],[1,np.nan,3],[1,2,np.nan]], columns=['A','B','C']), 'B').equals(pd.DataFrame([[5,2,1],[np.nan,2,3],[1,np.nan,3],[1,2,np.nan]], columns=['A','B','C']).dropna(subset=['B']))
    assert candidate(pd.DataFrame([[5,2,1],[np.nan,3,3],[1,np.nan,3],[1,2,np.nan]], columns=['A','B','C']), 'B').equals(pd.DataFrame([[5,2,1],[np.nan,3,3],[1,np.nan,3],[1,2,np.nan]], columns=['A','B','C']).dropna(subset=['B']))
    assert candidate(pd.DataFrame([[5,2,1],[np.nan,3,3],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C']), 'B').equals(pd.DataFrame([[5,2,1],[np.nan,3,3],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C']).dropna(subset=['B']))
    assert candidate(pd.DataFrame([[5,2,1],[3,3,3],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C']), 'B').equals(pd.DataFrame([[5,2,1],[3,3,3],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C']).dropna(subset=['B']))
    assert candidate(pd.DataFrame([[5,2,1],[3,3,np.nan],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C']), 'B').equals(pd.DataFrame([[5,2,1],[3,3,np.nan],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C']).dropna(subset=['B']))
    assert candidate(pd.DataFrame([[5,2,1],[3,3,np.nan],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C']), 'C').equals(pd.DataFrame([[5,2,1],[3,3,np.nan],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C']).dropna(subset=['C']))
    assert candidate(pd.DataFrame([[5,2,1],[3,3,np.nan],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C']), 'A').equals(pd.DataFrame([[5,2,1],[3,3,np.nan],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C']).dropna(subset=['A']))
    assert candidate(pd.DataFrame([[5,2,1],[3,3,np.nan],[np.nan,np.nan,3],[np.nan,2,np.nan]], columns=['A','B','C']), 'A').equals(pd.DataFrame([[5,2,1],[3,3,np.nan],[np.nan,np.nan,3],[np.nan,2,np.nan]], columns=['A','B','C']).dropna(subset=['A']))
'''

# %%
import pandas as pd
import numpy as np

# %%

"""
question: |
  Write a function `def drop_rows_col_nan(df, col_name):` that takes a DataFrame and a column name and returns a DataFrame to solve the following problem:
  How to drop rows of Pandas DataFrame whose value in a certain column is NaN

validator:
  table_test:
    function_name: drop_rows_col_nan
    test_cases:
    - ["`pd.DataFrame([[1,2,3],[np.nan,2,3],[1,np.nan,3],[1,2,np.nan]], columns=['A','B','C'])`", "B"]
    - ["`pd.DataFrame([[5,2,3],[np.nan,2,3],[1,np.nan,3],[1,2,np.nan]], columns=['A','B','C'])`", "B"]
    - ["`pd.DataFrame([[5,2,1],[np.nan,2,3],[1,np.nan,3],[1,2,np.nan]], columns=['A','B','C'])`", "B"]
    - ["`pd.DataFrame([[5,2,1],[np.nan,3,3],[1,np.nan,3],[1,2,np.nan]], columns=['A','B','C'])`", "B"]
    - ["`pd.DataFrame([[5,2,1],[np.nan,3,3],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C'])`", "B"]
    - ["`pd.DataFrame([[5,2,1],[3,3,3],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C'])`", "B"]
    - ["`pd.DataFrame([[5,2,1],[3,3,np.nan],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C'])`", "B"]
    - ["`pd.DataFrame([[5,2,1],[3,3,np.nan],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C'])`", "C"]
    - ["`pd.DataFrame([[5,2,1],[3,3,np.nan],[np.nan,np.nan,3],[1,2,np.nan]], columns=['A','B','C'])`", "A"]
    - ["`pd.DataFrame([[5,2,1],[3,3,np.nan],[np.nan,np.nan,3],[np.nan,2,np.nan]], columns=['A','B','C'])`", "A"]
"""

def drop_rows_col_nan(df, col_name):
    return df.dropna(subset=[col_name])
