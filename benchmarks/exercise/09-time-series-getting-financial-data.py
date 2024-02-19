# %%
import numpy as np
import pandas as pd

# %%
"""
question: |
  Read the data from `inputs/appl-stock.csv`. Set the first unnamed column as index column. Save the data in a DataFrame called `df_apple`.

validator:
  namespace_check:
    df_apple:
"""

df_apple = pd.read_csv('inputs/appl-stock.csv', index_col=0)

# %%
"""
question: Add a new column "stock" to the dataframe and add the ticker symbol

validator:
  namespace_check:
    df_apple:
"""

df_apple['stock'] = 'AAPL'

# %%
"""
question: |
  Repeat the previous steps for a few other stocks, always creating a new dataframe: Tesla, IBM and Microsoft. (Ticker symbols TSLA, IBM and MSFT.)
  Combine the four separate dataFrames into one combined dataFrame df that holds the information for all four stocks

validator:
  namespace_check:
    df:
"""

dfs = [df_apple]
for stock in ['TSLA', 'IBM', 'MSFT']:
    df = pd.read_csv('inputs/{}-stock.csv'.format(stock.lower()), index_col=0)
    df.to_csv('inputs/{}-stock.csv'.format(stock.lower()))
    df['stock'] = stock
    dfs.append(df)
df = pd.concat(dfs)

# %%
"""
question: Shift the stock column into the index (making it a multi-level index consisting of the ticker symbol and the date). Modify df in place.

validator:
  namespace_check:
    df:
"""

df.set_index('stock', append=True, inplace=True)

# %%
"""
question: Create a dataFrame called vol, with the volume values.

validator:
  namespace_check:
    vol:
"""

vol = df[['volume']]

# %%
"""
question: |
  Aggregate the data of volume to weekly. The index should be a multi-level index consisting of the year, the week number. The columns should be the ticker symbols.
  Hint: Be careful to not sum data from the same week of 2015 and other years.

execution:
  max_time: 3
"""

vol.index = vol.index.set_levels(df.index.levels[0].map(pd.to_datetime), level=0)
vol.groupby([vol.index.get_level_values(0).year, pd.Index(vol.index.get_level_values(0).isocalendar().week), vol.index.get_level_values(1)]).sum().unstack()

# %%
"""
question: Find all the volume traded in the year of 2015
"""

vol[vol.index.get_level_values(0).year == 2015].groupby('stock').sum()
