# %%
import numpy as np
import pandas as pd

# %%
"""
question: |
  Import the dataset from `inputs/weekly.csv`.
  Assign it to a variable called flow

validator:
  namespace_check:
    flow:

data:
  weekly.csv: https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv
"""

flow = pd.read_csv("inputs/weekly.csv")

# %%
"""
question: Set the column Date as the index and set the index to a DatetimeIndex type. Modify the flow dataframe in place.

validator:
  namespace_check:
    flow:
"""

flow = flow.set_index('Date')
flow.index = pd.to_datetime(flow.index)

# %%
"""
question: What is the frequency of the dataset?
"""

pd.infer_freq(flow.index[-3:])

# %%
"""
question: What is the type of the index?
"""

flow.index.dtype

# %%
"""
question: Change the frequency to monthly, sum the values and assign it to monthly.

validator:
  namespace_check:
    monthly:
"""

monthly = flow.resample('M').sum()

# %%
"""
question: You will notice that it filled the dataFrame with months that don't have any data with 0. Let's drop these rows and save it back to monthly.

validator:
  namespace_check:
    monthly:
"""

monthly = monthly[monthly.sum(axis=1) != 0]

# %%
"""
question: Good, now we have the monthly data. Now change the frequency to year.
"""

monthly.resample('Y').sum()
