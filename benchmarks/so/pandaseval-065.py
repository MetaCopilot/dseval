'''
### Prompt ###

import pandas as pd
import numpy as np
def merge_df(df1, df2):
    # How to merge two dataframes with different column names but same number of rows?
    # I have two different data frames in pandas. Example:
    # df1=a b  df2= c
    # 0 1       1 
    # 1 2       2 
    # 2 3       3 
    # I want to merge them so
    # df1= a b c  
    #  0 1 1
    #  1 2 2
    #  2 3 3
    # In order to merge two dataframes you can use this two examples. Both returns the same goal
    # Using merge plus additional arguments instructing it to use the indexes
    # Specially, we can set left_index and right_index to True

### Solution ###

return pd.merge(df1, df2, left_index=True, right_index=True)

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a':[0, 1, 2],'b':[1,2,3]}), pd.DataFrame({'c':[1, 2, 3]})).equals(pd.DataFrame({'a':[0, 1, 2],'b':[1,2,3], 'c':[1, 2, 3]}))
    assert candidate(pd.DataFrame({'m':[7,7,9],'s':[5,3,6]}), pd.DataFrame({'r':[9,9,2]})).equals(pd.DataFrame({'m':[7,7,9],'s':[5,3,6],'r':[9,9,2]}))
    assert candidate(pd.DataFrame({'a':[0, 2, 2],'b':[1,2,3]}), pd.DataFrame({'c':[1, 2, 3]})).equals(pd.DataFrame({'a':[0, 2, 2],'b':[1,2,3], 'c':[1, 2, 3]}))
    assert candidate(pd.DataFrame({'a':[0, 2, 4],'b':[1,2,3]}), pd.DataFrame({'c':[1, 2, 3]})).equals(pd.DataFrame({'a':[0, 2, 4],'b':[1,2,3], 'c':[1, 2, 3]}))
    assert candidate(pd.DataFrame({'a':[0, 2, 4],'b':[4,2,3]}), pd.DataFrame({'c':[1, 2, 3]})).equals(pd.DataFrame({'a':[0, 2, 4],'b':[4,2,3], 'c':[1, 2, 3]}))
    assert candidate(pd.DataFrame({'a':[0, 2, 4],'b':[4,2,3]}), pd.DataFrame({'c':[14, 2, 3]})).equals(pd.DataFrame({'a':[0, 2, 4],'b':[4,2,3], 'c':[14, 2, 3]}))
    assert candidate(pd.DataFrame({'a':[0, 2, 4],'b':[4,2,3]}), pd.DataFrame({'c':[14, 12, 3]})).equals(pd.DataFrame({'a':[0, 2, 4],'b':[4,2,3], 'c':[14, 12, 3]}))
    assert candidate(pd.DataFrame({'a':[0, 2, 4],'b':[4,2,3]}), pd.DataFrame({'c':[14, 12, 13]})).equals(pd.DataFrame({'a':[0, 2, 4],'b':[4,2,3], 'c':[14, 12, 13]}))
    assert candidate(pd.DataFrame({'a':[0, 2, 4],'b':[14,2,3]}), pd.DataFrame({'c':[14, 12, 13]})).equals(pd.DataFrame({'a':[0, 2, 4],'b':[14,2,3], 'c':[14, 12, 13]}))
    assert candidate(pd.DataFrame({'a':[0, 2, 4],'b':[14,2,13]}), pd.DataFrame({'c':[14, 12, 13]})).equals(pd.DataFrame({'a':[0, 2, 4],'b':[14,2,13], 'c':[14, 12, 13]}))
'''

# %%
import pandas as pd
import numpy as np

# %%

"""
question: |
  Write a function `def merge_df(df1, df2):` that takes two DataFrames with different column names but the same number of rows and returns a merged DataFrame to solve the following problem:
  How to merge two dataframes with different column names but same number of rows?
  I have two different data frames in pandas. Example:
  df1=a b  df2= c
  0 1       1 
  1 2       2 
  2 3       3 
  I want to merge them so
  df1= a b c  
  0 1 1
  1 2 2
  2 3 3
  In order to merge two dataframes you can use this two examples. Both returns the same goal
  Using merge plus additional arguments instructing it to use the indexes
  Specially, we can set left_index and right_index to True

validator:
  table_test:
    function_name: merge_df
    test_cases:
    - ["`pd.DataFrame({'a':[0, 1, 2],'b':[1,2,3]})`", "`pd.DataFrame({'c':[1, 2, 3]})`"]
    - ["`pd.DataFrame({'m':[7,7,9],'s':[5,3,6]})`", "`pd.DataFrame({'r':[9,9,2]})`"]
    - ["`pd.DataFrame({'a':[0, 2, 2],'b':[1,2,3]})`", "`pd.DataFrame({'c':[1, 2, 3]})`"]
    - ["`pd.DataFrame({'a':[0, 2, 4],'b':[1,2,3]})`", "`pd.DataFrame({'c':[1, 2, 3]})`"]
    - ["`pd.DataFrame({'a':[0, 2, 4],'b':[4,2,3]})`", "`pd.DataFrame({'c':[1, 2, 3]})`"]
    - ["`pd.DataFrame({'a':[0, 2, 4],'b':[4,2,3]})`", "`pd.DataFrame({'c':[14, 2, 3]})`"]
    - ["`pd.DataFrame({'a':[0, 2, 4],'b':[4,2,3]})`", "`pd.DataFrame({'c':[14, 12, 3]})`"]
    - ["`pd.DataFrame({'a':[0, 2, 4],'b':[4,2,3]})`", "`pd.DataFrame({'c':[14, 12, 13]})`"]
    - ["`pd.DataFrame({'a':[0, 2, 4],'b':[14,2,3]})`", "`pd.DataFrame({'c':[14, 12, 13]})`"]
    - ["`pd.DataFrame({'a':[0, 2, 4],'b':[14,2,13]})`", "`pd.DataFrame({'c':[14, 12, 13]})`"]
"""

def merge_df(df1, df2):
    return pd.merge(df1, df2, left_index=True, right_index=True)
