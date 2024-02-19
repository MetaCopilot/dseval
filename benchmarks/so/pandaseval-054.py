'''
### Prompt ###

import pandas as pd

def extract_the_last_year(df, column_name):
    # I am trying to extract the last year (YY) of a fiscal date string in the format of YYYY-YY.
    # e.g The last year of this '1999-00' would be 2000.
    # I need a logic to include a case where if it is the end of the century then my apply method should add to the first two digits.
    # the column_name is the column name of the dataframe that contains the date strings.
    # return the numerical Series obj of the last year.

### Solution ###

    final_result = pd.to_numeric(df[column_name].str.split('-').str[0]) + 1
    return final_result

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame(data={'Season':['1996-97', '1997-98', '1998-99', '1999-00', '2000-01']}), 'Season').equals(pd.Series([1997, 1998, 1999, 2000, 2001]))
    assert candidate(pd.DataFrame(data={'Season':['1996-07', '1997-08', '1998-99', '1999-00', '2000-01']}), 'Season').equals(pd.Series([1997, 1998, 1999, 2000, 2001]))
    assert candidate(pd.DataFrame(data={'Season':['1996-07', '1997-08', '1998-99', '2018-00', '2000-01']}), 'Season').equals(pd.Series([1997, 1998, 1999, 2019, 2001]))
    assert candidate(pd.DataFrame(data={'Season':['1996-07', '1997-08', '1998-99', '2018-00', '2081-01']}), 'Season').equals(pd.Series([1997, 1998, 1999, 2019, 2082]))
    assert candidate(pd.DataFrame(data={'Season':['1996-07', '1997-08', '1958-99', '2018-00', '2081-01']}), 'Season').equals(pd.Series([1997, 1998, 1959, 2019, 2082]))
    assert candidate(pd.DataFrame(data={'Season':['1996-07', '1967-08', '1958-99', '2018-00', '2081-01']}), 'Season').equals(pd.Series([1997, 1968, 1959, 2019, 2082]))
    assert candidate(pd.DataFrame(data={'Season':['1946-07', '1967-08', '1958-99', '2018-00', '2081-01']}), 'Season').equals(pd.Series([1947, 1968, 1959, 2019, 2082]))
    assert candidate(pd.DataFrame(data={'Season':['1946-07', '1967-08', '1958-99', '2008-00', '2081-01']}), 'Season').equals(pd.Series([1947, 1968, 1959, 2009, 2082]))
    assert candidate(pd.DataFrame(data={'Season':['1946-07', '1967-08', '1958-99', '2088-00', '2081-01']}), 'Season').equals(pd.Series([1947, 1968, 1959, 2089, 2082]))
    assert candidate(pd.DataFrame(data={'Season':['1946-07', '1967-08', '1958-99', '2088-00', '2051-01']}), 'Season').equals(pd.Series([1947, 1968, 1959, 2089, 2052]))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def extract_the_last_year(df, column_name):` that takes a DataFrame and a column name and returns a numerical Series object to solve the following problem:
  I am trying to extract the last year (YY) of a fiscal date string in the format of YYYY-YY.
  e.g The last year of this '1999-00' would be 2000.
  I need a logic to include a case where if it is the end of the century then my apply method should add to the first two digits.
  the column_name is the column name of the dataframe that contains the date strings.

validator:
  table_test:
    function_name: extract_the_last_year
    test_cases:
    - ["`pd.DataFrame(data={'Season':['1996-97', '1997-98', '1998-99', '1999-00', '2000-01']})`", 'Season']
    - ["`pd.DataFrame(data={'Season':['1996-97', '1997-98', '1998-99', '1999-00', '2000-01']})`", 'Season']
    - ["`pd.DataFrame(data={'Season':['1996-97', '1997-98', '1998-99', '2018-19', '2000-01']})`", 'Season']
    - ["`pd.DataFrame(data={'Season':['1996-97', '1997-98', '1998-99', '2018-19', '2081-82']})`", 'Season']
    - ["`pd.DataFrame(data={'Season':['1996-97', '1997-98', '1958-59', '2018-19', '1899-00']})`", 'Season']
    - ["`pd.DataFrame(data={'Season':['1996-97', '1967-68', '1958-59', '2018-19', '1899-00']})`", 'Season']
    - ["`pd.DataFrame(data={'Season':['1946-47', '1967-68', '1958-59', '2018-19', '1899-00']})`", 'Season']
    - ["`pd.DataFrame(data={'Season':['1946-47', '1967-68', '1958-59', '2008-09', '1899-00']})`", 'Season']
    - ["`pd.DataFrame(data={'Season':['1946-47', '1967-68', '1958-59', '2088-89', '1899-00']})`", 'Season']
    - ["`pd.DataFrame(data={'Season':['1946-47', '1967-68', '1989-90', '2088-89', '2051-52']})`", 'Season']
"""

def extract_the_last_year(df, column_name):
    final_result = pd.to_numeric(df[column_name].str.split('-').str[0]) + 1
    return final_result
