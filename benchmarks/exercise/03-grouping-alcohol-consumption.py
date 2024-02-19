# %%
import pandas as pd

# %%
"""
question: |
  Import the dataset from this [address](inputs/drinks.csv).
  Assign it to a variable called drinks.

validator:
  namespace_check:
    drinks:

data:
  drinks.csv: https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv
"""

drinks = pd.read_csv('inputs/drinks.csv')

# %%
"""
question: Which continent drinks more beer on average?
"""

# Group by continent and calculate the mean of beer_servings
beer_avg_by_continent = drinks.groupby('continent')['beer_servings'].mean()

# Find the continent with the highest average beer consumption
beer_avg_by_continent.idxmax()

# %%
"""
question: For each continent show the statistics for wine consumption.
"""

drinks.groupby('continent').wine_servings.describe()

# %%
"""
question: Return the mean alcohol consumption per continent for every column
"""

drinks.groupby('continent').mean(numeric_only=True)

# %%
"""
question: Return the median alcohol consumption per continent for every column
"""

drinks.groupby('continent').median(numeric_only=True)

# %%
"""
question: |
  Show the mean, min and max values for spirit consumption.
  Return a DataFrame.
"""

drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max'])

