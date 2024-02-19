# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Import the dataset from this [address](inputs/appl_1980_2014.csv)
  Assign it to a variable apple

validator:
  namespace_check:
    apple:

execution:
  max_time: 5

data:
  appl_1980_2014.csv: https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv
"""

apple = pd.read_csv('inputs/appl_1980_2014.csv')

# %%
"""
question: Check out the type of the columns
"""

apple.dtypes

# %%
"""
question: Transform the Date column as a datetime type

validator:
  namespace_check:
    apple:
"""

apple['Date'] = pd.to_datetime(apple['Date'])

# %%
"""
question: Set the date as the index

validator:
  namespace_check:
    apple:
"""

apple = apple.set_index('Date')

# %%
"""
question: Is there any duplicate dates?
"""

apple.index.is_unique

# %%
"""
question: Ops...it seems the index is from the most recent date. Make the first entry the oldest date.

validator:
  namespace_check:
    apple:
"""

apple = apple.sort_index(ascending = True)

# %%
"""
question: Get the last business day of each month. Return a list of pandas timestamps.
"""

apple.resample('BM').last().index.to_list()

# %%
"""
question: What is the difference in days between the first day and the oldest
"""

(apple.index.max() - apple.index.min()).days

# %%
"""
question: How many months in the data we have?
"""

apple.resample('BM').count().shape[0]
