# %%
import numpy as np
import pandas as pd

# %%
"""
question: |
  Import the dataset from this `inputs/US_Crime_Rates_1960_2014.csv`.
  Assign it to a variable called crime.

validator:
  namespace_check:
    crime:

data:
  US_Crime_Rates_1960_2014.csv: https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv
"""

url = "inputs/US_Crime_Rates_1960_2014.csv"
crime = pd.read_csv(url)

# %%
"""
question: What is the type of the columns?
"""

crime.dtypes

# %%
"""
question: Have you noticed that the type of Year is int64. But pandas has a different type to work with Time Series. Let's convert the type of the column Year to datetime64. Save it in-place.

validator:
  namespace_check:
    crime:
"""

crime.Year = pd.to_datetime(crime.Year, format='%Y')

# %%
"""
question: Set the Year column as the index of the dataframe. Save it in-place.

validator:
  namespace_check:
    crime:
"""

crime = crime.set_index('Year', drop = True)

# %%
"""
question: Delete the Total column

validator:
  namespace_check:
    crime:
"""

del crime['Total']

# %%
"""
question: |
  Group the year by decades and sum the values
  Pay attention to the Population column number, summing this column is a mistake (taking maximum instead). Put the results in a variable called crimes.

validator:
  namespace_check:
    crimes:
"""

# Uses resample to sum each decade
crimes = crime.resample('10AS').sum()

# Uses resample to get the max value only for the "Population" column
population = crime['Population'].resample('10AS').max()

# Updating the "Population" column
crimes['Population'] = population

# %%
"""
question: What is the most dangerous decade to live in the US? Write it in the format of `19XXs` or `20XXs`.
"""

crimes.idxmax(0)['Violent'].strftime('%Y') + 's'
