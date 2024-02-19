'''
### Prompt ###

import pandas as pd
import numpy as np

def get_value_when_condition(df):
    # How can I get the values of column `A` when column `B`=3?

### Solution ###

    return df[df['B'] == 3]['A'].values

### Test ###

def check(candidate):
    assert np.array_equal(candidate(pd.DataFrame({'A': ['p1', 'p1', 'p2', 'p2', 'p3'], 'B': [1, 2, 3, 4, 5]})), np.array(['p2']))
    assert np.array_equal(candidate(pd.DataFrame({'A': ['p1', 'p1', 'p2', 'p2', 'p3'], 'B': [1, 4, 3, 4, 5]})), np.array(['p2']))
    assert np.array_equal(candidate(pd.DataFrame({'A': ['p1', 'p1', 'p2', 'p2', 'p3'], 'B': [1, 4, 8, 4, 5]})), np.array([]))
    assert np.array_equal(candidate(pd.DataFrame({'A': ['p1', 'p1', 'p2', 'p2', 'p5'], 'B': [2, 4, 8, 4, 5]})), np.array([]))
    assert np.array_equal(candidate(pd.DataFrame({'A': ['p1', 'p1', 'p2', 'p2', 'p3'], 'B': [2, 3, 4, 4, 5]})), np.array(['p1']))
    assert np.array_equal(candidate(pd.DataFrame({'A': ['p2', 'p1', 'p2', 'p2', 'p3'], 'B': [2, 3, 4, 4, 5]})), np.array(['p1']))
    assert np.array_equal(candidate(pd.DataFrame({'A': ['p2', 'p1', 'p2', 'p3', 'p3'], 'B': [2, 3, 4, 5, 5]})), np.array(['p1']))
    assert np.array_equal(candidate(pd.DataFrame({'A': ['p2', 'p1', 'p1', 'p3', 'p3'], 'B': [2, 3, 4, 5, 5]})), np.array(['p1']))
    assert np.array_equal(candidate(pd.DataFrame({'A': ['p2', 'p1', 'p1', 'p1', 'p3'], 'B': [2, 3, 4, 5, 5]})), np.array(['p1']))
    assert np.array_equal(candidate(pd.DataFrame({'A': ['p2', 'p1', 'p1', 'p1', 'p2'], 'B': [2, 3, 4, 5, 5]})), np.array(['p1']))
'''

# %%
import pandas as pd
import numpy as np

# %%

"""
question: |
  Write a function `def get_value_when_condition(df):` that takes a DataFrame and returns a numpy array to solve the following problem:
  How can I get the values of column `A` when column `B`=3?

validator:
  table_test:
    function_name: get_value_when_condition
    test_cases:
    - ["`pd.DataFrame({'A': ['p1', 'p1', 'p2', 'p2', 'p3'], 'B': [1, 2, 3, 4, 5]})`"]
    - ["`pd.DataFrame({'A': ['p1', 'p1', 'p2', 'p2', 'p3'], 'B': [1, 4, 3, 4, 5]})`"]
    - ["`pd.DataFrame({'A': ['p1', 'p1', 'p2', 'p2', 'p3'], 'B': [1, 4, 8, 4, 5]})`"]
    - ["`pd.DataFrame({'A': ['p1', 'p1', 'p2', 'p2', 'p5'], 'B': [2, 4, 8, 4, 5]})`"]
    - ["`pd.DataFrame({'A': ['p1', 'p1', 'p2', 'p2', 'p3'], 'B': [2, 3, 4, 4, 5]})`"]
    - ["`pd.DataFrame({'A': ['p2', 'p1', 'p2', 'p2', 'p3'], 'B': [2, 3, 4, 4, 5]})`"]
    - ["`pd.DataFrame({'A': ['p2', 'p1', 'p2', 'p3', 'p3'], 'B': [2, 3, 4, 5, 5]})`"]
    - ["`pd.DataFrame({'A': ['p2', 'p1', 'p1', 'p3', 'p3'], 'B': [2, 3, 4, 5, 5]})`"]
    - ["`pd.DataFrame({'A': ['p2', 'p1', 'p1', 'p1', 'p3'], 'B': [2, 3, 4, 5, 5]})`"]
    - ["`pd.DataFrame({'A': ['p2', 'p1', 'p1', 'p1', 'p2'], 'B': [2, 3, 4, 5, 5]})`"]
"""

def get_value_when_condition(df):
    return df[df['B'] == 3]['A'].values
