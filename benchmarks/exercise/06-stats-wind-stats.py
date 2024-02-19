# %%
import pandas as pd
import datetime

# %%
"""
question: |
  Import the dataset from this `inputs/wind.data`.
  Assign it to a variable called data and replace the first 3 columns by a proper datetime column.

validator:
  namespace_check:
    data:
      value_only: true

data:
  wind.data: https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data
"""

# parse_dates gets 0, 1, 2 columns and parses them as the index
data_url = 'inputs/wind.data'
data = pd.read_csv(data_url, sep = r"\s+", parse_dates = [[0,1,2]]) 

# %%
"""
question: Year 2061? Do we really have data from this year? Create a function to fix it and apply it in-place.

validator:
  namespace_check:
    data:
"""

# The problem is that the dates are 2061 and so on...

# function that uses datetime
def fix_century(x):
  year = x.year - 100 if x.year > 1989 else x.year
  return datetime.date(year, x.month, x.day)

# apply the function fix_century on the column and replace the values to the right ones
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)

# %%
"""
question: Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].

validator:
  namespace_check:
    data:
"""

# transform Yr_Mo_Dy it to date type datetime64
data["Yr_Mo_Dy"] = pd.to_datetime(data["Yr_Mo_Dy"])

# set 'Yr_Mo_Dy' as the index
data = data.set_index('Yr_Mo_Dy')

# %%
"""
question: |
  Compute how many values are missing for each location over the entire record.  
  They should be ignored in all calculations below.
"""

data.isnull().sum()

# %%
"""
question: Compute how many non-missing values there are for each column in total.
"""

data.notnull().sum()

# %%
"""
question: |
  Calculate the mean windspeeds of the windspeeds over all the locations and all the times.
  Return a single number for the entire dataset.
"""

data.sum().sum() / data.notna().sum().sum()

# %%
"""
question: |
  Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days 
  A column of numbers for each location.

validator:
  namespace_check:
    loc_stats:
"""

loc_stats = data.describe(percentiles=[]).loc[['min', 'max', 'mean']]

# %%
"""
question: |
  Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the windspeeds across all the locations at each day.
  A different row of numbers for each day.

validator:
  namespace_check:
    day_stats:
"""

# create the dataframe
day_stats = pd.DataFrame()

# this time we determine axis equals to one so it gets each row.
day_stats['min'] = data.min(axis = 1) # min
day_stats['max'] = data.max(axis = 1) # max 
day_stats['mean'] = data.mean(axis = 1) # mean
day_stats['std'] = data.std(axis = 1) # standard deviations

# %%
"""
question: |
  Find the average windspeed in January for each location.  
  Treat January 1961 and January 1962 both as January.
"""

data.loc[data.index.month == 1].mean()

# %%
"""
question: Downsample the record to a yearly frequency for each location.

validator:
  result:
    ignore_index: true
"""

data.groupby(data.index.to_period('A')).mean()

# %%
"""
question: Downsample the record to a monthly frequency for each location.

validator:
  result:
    ignore_index: true
"""

data.groupby(data.index.to_period('M')).mean()

# %%
"""
question: Downsample the record to a weekly frequency for each location.

validator:
  result:
    ignore_index: true
"""

data.groupby(data.index.to_period('W')).mean()

# %%
"""
question: Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 52 weeks.

validator:
  result:
    value_only: true
"""

# resample data to 'W' week and use the functions
weekly = data.resample('W').agg(['min','max','mean','std'])

# slice it for the first 52 weeks and locations
weekly.loc[weekly.index[1:53], "RPT":"MAL"]
