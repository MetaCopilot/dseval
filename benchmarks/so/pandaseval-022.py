'''
### Prompt ###

import pandas as pd

def normalize(df):
    # Normalization using pandas
    # We simply subtract the mean and divide by standard deviation on df.iloc[:,0,-1] obj with axis is zero.
    # Return the normalized dataframe

### Solution ###

df.iloc[:,0:-1] = df.iloc[:,0:-1].apply(lambda x: (x-x.mean())/ x.std(), axis=0)
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')})).equals(pd.DataFrame({'A':[-1.0,0.0,1.0],'B':[-1.0,0.0,1.0],'C':list('abc')}))
    assert candidate(pd.DataFrame({'M':[1,2,3], 'S':[100,300,500], 'R':list('zan')})).equals(pd.DataFrame({'M':[-1.0,0.0,1.0],'S':[-1.0, 0.0, 1.0],'R':list('zan')}))
    assert candidate(pd.DataFrame({'U':[2,4,6], 'C':[100,300,500], 'S':list('yao')})).equals(pd.DataFrame({'U':[-1.0, 0.0, 1.0], 'C':[-1.0, 0.0, 1.0], 'S':list('yao')}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('bbc')})).equals(pd.DataFrame({'A':[-1.0,0.0,1.0],'B':[-1.0,0.0,1.0],'C':list('bbc')}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('bbb')})).equals(pd.DataFrame({'A':[-1.0,0.0,1.0],'B':[-1.0,0.0,1.0],'C':list('bbb')}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'D':list('bbb')})).equals(pd.DataFrame({'A':[-1.0,0.0,1.0],'B':[-1.0,0.0,1.0],'D':list('bbb')}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,200,300], 'D':list('bbb')})).equals(pd.DataFrame({'A':[-1.0,0.0,1.0],'B':[-1.0,0.0,1.0],'D':list('bbb')}))
    assert candidate(pd.DataFrame({'A':[1,2,3], 'B':[100,200,300], 'e':list('cdf')})).equals(pd.DataFrame({'A':[-1.0,0.0,1.0],'B':[-1.0,0.0,1.0],'e':list('cdf')}))
    assert candidate(pd.DataFrame({'A':[3,4,5], 'B':[300,400,500], 'e':list('cdf')})).equals(pd.DataFrame({'A':[-1.0,0.0,1.0],'B':[-1.0,0.0,1.0],'e':list('cdf')}))
    assert candidate(pd.DataFrame({'A':[3,4,5], 'B':[300,400,500], 'R':list('abc')})).equals(pd.DataFrame({'A':[-1.0,0.0,1.0],'B':[-1.0,0.0,1.0],'R':list('abc')}))
    assert candidate(pd.DataFrame({'A':[3,4,5], 'B':[300,400,500], 'P':list('abc')})).equals(pd.DataFrame({'A':[-1.0,0.0,1.0],'B':[-1.0,0.0,1.0],'P':list('abc')}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def normalize(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  Normalization using pandas
  We simply subtract the mean and divide by standard deviation on df.iloc[:,0,-1] obj with axis is zero.

validator:
  table_test:
    function_name: normalize
    test_cases:
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('abc')})`"]
    - ["`pd.DataFrame({'M':[1,2,3], 'S':[100,300,500], 'R':list('zan')})`"]
    - ["`pd.DataFrame({'U':[2,4,6], 'C':[100,300,500], 'S':list('yao')})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('bbc')})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'C':list('bbb')})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,300,500], 'D':list('bbb')})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,200,300], 'D':list('bbb')})`"]
    - ["`pd.DataFrame({'A':[1,2,3], 'B':[100,200,300], 'e':list('cdf')})`"]
    - ["`pd.DataFrame({'A':[3,4,5], 'B':[300,400,500], 'e':list('cdf')})`"]
    - ["`pd.DataFrame({'A':[3,4,5], 'B':[300,400,500], 'R':list('abc')})`"]
    - ["`pd.DataFrame({'A':[3,4,5], 'B':[300,400,500], 'P':list('abc')})`"]
"""

def normalize(df):
    df.iloc[:,0:-1] = df.iloc[:,0:-1].apply(lambda x: (x-x.mean())/ x.std(), axis=0)
    return df
