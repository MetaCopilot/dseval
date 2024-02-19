'''
### Prompt ###

import pandas as pd

def dataframe2list_of_dict(df):
    # Pandas DataFrame to List of Dictionaries
    # Use df.to_dict() to solve it and return the result

### Solution ###

    return df.to_dict(orient='records')

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'a':[1,1,1], 'b':[10,20,20]})) == [{'a': 1, 'b': 10}, {'a': 1, 'b': 20}, {'a': 1, 'b': 20}]
    assert candidate(pd.DataFrame({'a':[2,1,1], 'b':[10,20,20]})) == [{'a': 2, 'b': 10}, {'a': 1, 'b': 20}, {'a': 1, 'b': 20}]
    assert candidate(pd.DataFrame({'a':[2,1,4], 'b':[10,20,20]})) == [{'a': 2, 'b': 10}, {'a': 1, 'b': 20}, {'a': 4, 'b': 20}]
    assert candidate(pd.DataFrame({'a':[2,3,4], 'b':[10,20,20]})) == [{'a': 2, 'b': 10}, {'a': 3, 'b': 20}, {'a': 4, 'b': 20}]
    assert candidate(pd.DataFrame({'a':[2,3,4], 'b':[12,20,20]})) == [{'a': 2, 'b': 12}, {'a': 3, 'b': 20}, {'a': 4, 'b': 20}]
    assert candidate(pd.DataFrame({'a':[2,3,4], 'b':[12,33,20]})) == [{'a': 2, 'b': 12}, {'a': 3, 'b': 33}, {'a': 4, 'b': 20}]
    assert candidate(pd.DataFrame({'a':[2,3,4], 'b':[12,33,4]})) == [{'a': 2, 'b': 12}, {'a': 3, 'b': 33}, {'a': 4, 'b': 4}]
    assert candidate(pd.DataFrame({'a':[2,3,41], 'b':[12,33,4]})) == [{'a': 2, 'b': 12}, {'a': 3, 'b': 33}, {'a': 41, 'b': 4}]
    assert candidate(pd.DataFrame({'a':[2,33,41], 'b':[12,33,4]})) == [{'a': 2, 'b': 12}, {'a': 33, 'b': 33}, {'a': 41, 'b': 4}]
    assert candidate(pd.DataFrame({'a':[21,33,41], 'b':[12,33,4]})) == [{'a': 21, 'b': 12}, {'a': 33, 'b': 33}, {'a': 41, 'b': 4}]
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def dataframe2list_of_dict(df):` that takes a pandas DataFrame and returns a list of dictionaries to solve the following problem:
  Pandas DataFrame to List of Dictionaries
  Use df.to_dict() to solve it and return the result.

validator:
  table_test:
    function_name: dataframe2list_of_dict
    test_cases:
    - ["`pd.DataFrame({'a':[1,1,1], 'b':[10,20,20]})`"]
    - ["`pd.DataFrame({'a':[2,1,1], 'b':[10,20,20]})`"]
    - ["`pd.DataFrame({'a':[2,1,4], 'b':[10,20,20]})`"]
    - ["`pd.DataFrame({'a':[2,3,4], 'b':[10,20,20]})`"]
    - ["`pd.DataFrame({'a':[2,3,4], 'b':[12,20,20]})`"]
    - ["`pd.DataFrame({'a':[2,3,4], 'b':[12,33,20]})`"]
    - ["`pd.DataFrame({'a':[2,3,4], 'b':[12,33,4]})`"]
    - ["`pd.DataFrame({'a':[2,3,41], 'b':[12,33,4]})`"]
    - ["`pd.DataFrame({'a':[2,33,41], 'b':[12,33,4]})`"]
    - ["`pd.DataFrame({'a':[21,33,41], 'b':[12,33,4]})`"]
"""

def dataframe2list_of_dict(df):
    return df.to_dict(orient='records')
