'''
### Prompt ###

import pandas as pd

def convert_column_to_date(df):
    # Convert Column `Date` to Date Format using pandas function
    # return the coverted dataframe

### Solution ###

    df["Date"] = pd.to_datetime(df.Date)
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame( {'Symbol':['A','A','A'] , 'Date':['02/20/2015','01/15/2016','08/21/2015']})).equals(pd.DataFrame({'Symbol':['A','A','A'] , 'Date':[pd.Timestamp('2015-02-20 00:00:00'),pd.Timestamp('2016-01-15 00:00:00'),pd.Timestamp('2015-08-21 00:00:00')]}))
    assert candidate(pd.DataFrame( {'Symbol':['A','A','A'] , 'Date':['02/20/2016','01/15/2016','08/21/2015']})).equals(pd.DataFrame({'Symbol':['A','A','A'] , 'Date':[pd.Timestamp('2016-02-20 00:00:00'),pd.Timestamp('2016-01-15 00:00:00'),pd.Timestamp('2015-08-21 00:00:00')]}))
    assert candidate(pd.DataFrame( {'Symbol':['A','A','A'] , 'Date':['02/20/2016','01/15/2017','08/21/2015']})).equals(pd.DataFrame({'Symbol':['A','A','A'] , 'Date':[pd.Timestamp('2016-02-20 00:00:00'),pd.Timestamp('2017-01-15 00:00:00'),pd.Timestamp('2015-08-21 00:00:00')]}))
    assert candidate(pd.DataFrame( {'Symbol':['A','A','A'] , 'Date':['02/20/2016','01/15/2017','08/21/2019']})).equals(pd.DataFrame({'Symbol':['A','A','A'] , 'Date':[pd.Timestamp('2016-02-20 00:00:00'),pd.Timestamp('2017-01-15 00:00:00'),pd.Timestamp('2019-08-21 00:00:00')]}))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def convert_column_to_date(df):` that takes a DataFrame and returns a DataFrame to solve the following problem:
  Convert Column `Date` to Date Format using pandas function

validator:
  table_test:
    function_name: convert_column_to_date
    test_cases:
    - ["`pd.DataFrame( {'Symbol':['A','A','A'] , 'Date':['02/20/2015','01/15/2016','08/21/2015']})`"]
    - ["`pd.DataFrame( {'Symbol':['A','A','A'] , 'Date':['02/20/2016','01/15/2016','08/21/2015']})`"]
    - ["`pd.DataFrame( {'Symbol':['A','A','A'] , 'Date':['02/20/2016','01/15/2017','08/21/2015']})`"]
    - ["`pd.DataFrame( {'Symbol':['A','A','A'] , 'Date':['02/20/2016','01/15/2017','08/21/2019']})`"]
"""

def convert_column_to_date(df):
    df["Date"] = pd.to_datetime(df.Date)
    return df
