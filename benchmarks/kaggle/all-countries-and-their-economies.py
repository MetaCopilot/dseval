# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/All Countries and Economies.csv` into a variable `economy`.

validator:
  namespace_check:
    economy:
"""

economy = pd.read_csv('inputs/All Countries and Economies.csv')

# %%
"""
question: |
  Clean and preprocess the dataset. Convert country names to lower case. Drop unnecessary columns, fill missing values with mean and convert data types to numeric as necessary.
  Save the cleaned dataset in-place.

validator:
  namespace_check:
    economy:
"""

# Convert country names to lower case.
economy['Country'] = economy['Country'].str.lower()

# Drop the unnecessary column
economy = economy.drop(columns=['Unnamed: 25'])

# Convert columns to numeric, replacing non-numeric characters and commas
cols_to_convert = [
    'Population, total',
    'Population growth (annual %)',
    'Net migration',
    'Human Capital Index (HCI) (scale 0-1)',
    'GDP (current US$)current US$constant US$current LCUconstant LCU',
    'GDP per capita (current US$)current US$constant US$current LCUconstant LCU',
    'GDP growth (annual %)',
    'Annual freshwater withdrawals, total (% of internal resources)',
    'Foreign direct investment, net inflows (% of GDP)'
]

for col in cols_to_convert:
    economy[col] = pd.to_numeric(economy[col].str.replace(',', '').str.replace('%', '').str.replace('<', ''), errors='coerce')

# Fill missing values
economy = economy.fillna(economy.mean(numeric_only=True))

# %%
"""
question: |
  Calculate the mean, median, and standard deviation of GDP per capita for each country.
  Return a DataFrame with "Country" as the index and "Mean GDP", "Median GDP", and "Std GDP" as the columns.
"""

gdp_stats = economy.groupby('Country')['GDP per capita (current US$)current US$constant US$current LCUconstant LCU'].agg(['mean', 'median', 'std']).rename(columns={"mean": "Mean GDP", "median": "Median GDP", "std": "Std GDP"})
gdp_stats

# %%
"""
question: |
  Which country has the highest average GDP per capita? Which country has the lowest?
  Give me a tuple of `(country_with_highest_gdp, country_with_lowest_gdp)`.
"""

gdp_stats['Mean GDP'].idxmax(), gdp_stats['Mean GDP'].idxmin()

# %%
"""
question: |
  Calculate the correlation matrix of GDP per capita, life expectancy, and CO2 emissions for all countries.
  Return a DataFrame with "GDP per capita", "Life expectancy", and "CO2 emissions" as both the rows and columns.
"""

column_names = {
    'GDP per capita (current US$)current US$constant US$current LCUconstant LCU': 'GDP per capita',
    'Life expectancy at birth, total (years)': 'Life expectancy',
    'CO2 emissions (metric tons per capita)': 'CO2 emissions'
}
corr_matrix = economy[column_names.keys()].corr().rename(columns=column_names, index=column_names)
corr_matrix

# %%
"""
question: |
  Which pair of features has the highest correlation? Which pair has the lowest?
  Return a tuple of `(highest_corr_pair, lowest_corr_pair)`

# The question didn't specify the order of the pairs.

validator:
  result: |
    def compare_fn(ref, sub):
      if len(ref) != len(sub):
        return {"match": False, "reason": f"Length: {len(ref)} vs {len(sub)}"}
      if ref[0] != sub[0] and (ref[0][::-1] != sub[0]):
        return {"match": False, "reason": f"Highest correlation mismatch"}
      if ref[1] != sub[1] and (ref[1][::-1] != sub[1]):
        return {"match": False, "reason": f"Lowest correlation mismatch"}
      return {"match": True, "reason": ""}
"""

corr_matrix_stacked = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), 1).astype(bool)).stack()
corr_matrix_stacked.idxmax(), corr_matrix_stacked.idxmin()

# %%
"""
question: |
  Calculate the average GDP per capita for each region. Assume that the "Region" column is created based on the leading character (capitalized) of the "Country" column. Create a Series with "Region" as the index and "Average GDP" as the values.
"""

# Assume that the 'Region' column is created based on the 'Country' column
economy['Region'] = economy['Country'].apply(lambda x: x[0].upper())
economy.groupby('Region')['GDP per capita (current US$)current US$constant US$current LCUconstant LCU'].mean().rename("Average GDP")

# %%
"""
question: |
  Read the data from `inputs/Countries-Continents.csv`, which contains information about the continents of each country.
  Slugify the `Country` column by replacing punctuations and spaces with hyphens, and converting all characters to lowercase.
  Save the data in a DataFrame named `continents`.

validator:
  namespace_check:
    continents:

data:
  Countries-Continents.csv: https://raw.githubusercontent.com/dbouquin/IS_608/master/NanosatDB_munging/Countries-Continents.csv
"""

continents = pd.read_csv('inputs/Countries-Continents.csv')
continents['Country'] = continents['Country'].str.lower().str.replace("[^a-z]+", "-", regex=True)

# %%
"""
question: |
  Merge the economy dataset with the information about the continents of each country.
  Drop the row if the country is not found in the `continents` dataset.
  Save the merged dataset in-place in `economy_with_continents`.

validator:
  namespace_check:
    economy_with_continents:
"""

economy_with_continents = economy.merge(continents, on='Country')

# %%
"""
question: |
  Calculate the average life expectancy and CO2 emissions for each continent.
  The result should use "Continent" as the index and "Average Life Expectancy" and "Average CO2 Emissions" as the columns.
"""

column_names = {'Life expectancy at birth, total (years)': 'Average Life Expectancy', 'CO2 emissions (metric tons per capita)': 'Average CO2 Emissions'}
economy_with_continents.groupby('Continent')[list(column_names)].mean().rename(columns=column_names)

# %%
"""
question: |
  Based on `economy_with_continents`, create a new categorical feature based on the "GDP growth (annual %)" column.
  The categories are "High" (GDP growth > 5%), "Medium" (2% < GDP growth <= 5%), and "Low" (GDP growth <= 2%).
  Save the new feature in a new column named "GDP Growth Category" in-place.

validator:
  namespace_check:
    economy_with_continents:
"""

economy_with_continents['GDP Growth Category'] = pd.cut(economy_with_continents['GDP growth (annual %)'], bins=[-np.inf, 2, 5, np.inf], labels=['Low', 'Medium', 'High'])

# %%
"""
question: |
  Analyze the distribution of the "GDP Growth Category" for each continent. Count the countries with high, medium and low GDP growth for each continent. The index should be "GDP Growth Category". The columns should be the continents.
"""

economy_with_continents.groupby(['Continent', 'GDP Growth Category']).size().unstack(fill_value=0).transpose()
