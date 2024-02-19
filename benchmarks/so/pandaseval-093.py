'''
### Prompt ###

import pandas as pd

def transform_timestamp_to_pydatetime(timestamp):
    # transform timestamp to pydatetime object
    # return pydatetime object

### Solution ###

    return timestamp.to_pydatetime()

### Test ###

def check(candidate):
    assert candidate(pd.Timestamp('2019-01-01')) == pd.Timestamp('2019-01-01').to_pydatetime()
    assert candidate(pd.Timestamp('2022-01-01')) == pd.Timestamp('2022-01-01').to_pydatetime()
    assert candidate(pd.Timestamp('2022-03-01')) == pd.Timestamp('2022-03-01').to_pydatetime()
    assert candidate(pd.Timestamp('2022-03-04')) == pd.Timestamp('2022-03-04').to_pydatetime()
    assert candidate(pd.Timestamp('2022-02-01')) == pd.Timestamp('2022-02-01').to_pydatetime()
    assert candidate(pd.Timestamp('2022-02-09')) == pd.Timestamp('2022-02-09').to_pydatetime()
    assert candidate(pd.Timestamp('2022-03-12')) == pd.Timestamp('2022-03-12').to_pydatetime()
    assert candidate(pd.Timestamp('2022-03-16')) == pd.Timestamp('2022-03-16').to_pydatetime()
    assert candidate(pd.Timestamp('2022-02-28')) == pd.Timestamp('2022-02-28').to_pydatetime()
    assert candidate(pd.Timestamp('2021-02-28')) == pd.Timestamp('2021-02-28').to_pydatetime()
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def transform_timestamp_to_pydatetime(timestamp):` that takes a pandas Timestamp and returns a python datetime object to solve the following problem:
  transform timestamp to pydatetime object

validator:
  table_test:
    function_name: transform_timestamp_to_pydatetime
    test_cases:
    - ["`pd.Timestamp('2019-01-01')`"]
    - ["`pd.Timestamp('2022-01-01')`"]
    - ["`pd.Timestamp('2022-03-01')`"]
    - ["`pd.Timestamp('2022-03-04')`"]
    - ["`pd.Timestamp('2022-02-01')`"]
    - ["`pd.Timestamp('2022-02-09')`"]
    - ["`pd.Timestamp('2022-03-12')`"]
    - ["`pd.Timestamp('2022-03-16')`"]
    - ["`pd.Timestamp('2022-02-28')`"]
    - ["`pd.Timestamp('2021-02-28')`"]
"""

def transform_timestamp_to_pydatetime(timestamp):
    return timestamp.to_pydatetime()
