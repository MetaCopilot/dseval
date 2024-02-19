'''
### Prompt ###

import pandas as pd

def delete_column(df, column_name):
    # deleting a column from a Pandas DataFrame
    # return the changged dataframe

### Solution ###

    return df.drop(column_name, axis=1)

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')}), 'A').equals(pd.DataFrame({'B':[100,300,500], 'C':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')}), 'B').equals(pd.DataFrame({'A':[1,2,3], 'C':list('abc')}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')}), 'C').equals(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('dfg')}), 'C').equals(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[200,300,500], 'C':list('dfg')}), 'C').equals(pd.DataFrame({'A':[1,2,3], 'B':[200,300,500]}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[200,350,500], 'C':list('dfg')}), 'C').equals(pd.DataFrame({'A':[1,2,3], 'B':[200,350,500]}))
    assert candidate(pd.DataFrame({'A':[5,2,3], 'B':[200,350,500], 'C':list('dfg')}), 'C').equals(pd.DataFrame({'A':[5,2,3], 'B':[200,350,500]}))
    assert candidate(pd.DataFrame({'A':[5,2,1], 'B':[200,350,500], 'C':list('dfg')}), 'C').equals(pd.DataFrame({'A':[5,2,1], 'B':[200,350,500]}))
    assert candidate(pd.DataFrame({'A':[5,2,1], 'B':[521,350,500], 'C':list('dfg')}), 'C').equals(pd.DataFrame({'A':[5,2,1], 'B':[521,350,500]}))
    assert candidate(pd.DataFrame({'A':[5,2,1], 'B':[521,350,125], 'C':list('dfg')}), 'C').equals(pd.DataFrame({'A':[5,2,1], 'B':[521,350,125]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def delete_column(df, column_name):` that takes a DataFrame and a column name and returns a DataFrame to solve the following problem:
  deleting a column from a Pandas DataFrame

validator:
  table_test:
    function_name: delete_column
    test_cases:
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')})`", A]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')})`", B]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')})`", C]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('dfg')})`", C]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[200,300,500], 'C':list('dfg')})`", C]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[200,350,500], 'C':list('dfg')})`", C]
    - ["`pd.DataFrame({'A':[5,2,3], 'B':[200,350,500], 'C':list('dfg')})`", C]
    - ["`pd.DataFrame({'A':[5,2,1], 'B':[200,350,500], 'C':list('dfg')})`", C]
    - ["`pd.DataFrame({'A':[5,2,1], 'B':[521,350,500], 'C':list('dfg')})`", C]
    - ["`pd.DataFrame({'A':[5,2,1], 'B':[521,350,125], 'C':list('dfg')})`", C]
"""

def delete_column(df, column_name):
    return df.drop(column_name, axis=1)
