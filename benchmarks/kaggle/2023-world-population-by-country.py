# %%
import pandas as pd
import numpy as np
import json

# %%
"""
question: |
  Read the file `inputs/countries-table.json` into a dataframe variable `population`.

validator:
  namespace_check:
    population:
"""

population = pd.read_json("inputs/countries-table.json")

# %%
"""
question: List the names of the top 10 countries with the highest populations in 2023.

validator:
  result:
    ignore_order: true
    value_only: true
"""

population.nlargest(10, 'pop2023')['country'].tolist()

# %%
"""
question: List the countries with more than 1 billion people as of 2023.
"""

population.loc[population['pop2023'] > 1e9, 'country'].tolist()

# %%
"""
question: |
  Calculate the compounded annual growth rate of population for each country from 1980 to 2023.
  Put the results in a DataFrame with "Country" as the index and "Growth Rate" as the column.
"""

growth_rate = pd.DataFrame({
    'Country': population['country'],
    'Growth Rate': (population['pop2023'] / population['pop1980']) ** (1 / (2023 - 1980)) - 1,
}).set_index('Country')

growth_rate

# %%
"""
question: |
  Identify the countries with the highest and lowest population growth rates from 1980 to 2023.
  Return a tuple of `(country_with_highest_growth_rate, country_with_lowest_growth_rate)`.
"""

growth_rate.idxmax().item(), growth_rate.idxmin().item()

# %%
"""
question: |
  Compare the growth rate for each country between 1980-2000 and 2022-2023.
  Return a DataFrame with "Country" as the index and "1980-2000 Growth Rate" and "2022-2023 Growth Rate" as the columns.
"""

pd.DataFrame({
    'Country': population['country'],
    '1980-2000 Growth Rate': (population['pop2000'] / population['pop1980']) ** (1 / (2000 - 1980)) - 1,
    '2022-2023 Growth Rate': (population['pop2023'] / population['pop2022']) - 1,
}).set_index('Country')

# %%
"""
question: |
  Predict the population of the countries with the top 10 largest populations in 2060 based on the population trend from 1980 to 2023.
  Assume the population growth rate is the same as the annual growth rate of 2010-2023.
  Return a DataFrame with "Country" as the index and "2060 Population" as the column.

validator:
  result:
    ignore_order: true
"""

growth_rate_2010_2023 = (population['pop2023'] / population['pop2010']) ** (1 / (2023 - 2010)) - 1
pd.DataFrame({
    'Country': population['country'],
    '2060 Population': population['pop2023'] * (1 + growth_rate_2010_2023) ** (2060 - 2023)
}).set_index('Country').nlargest(10, '2060 Population')

# %%
"""
question: |
  Analyze the relationship between population density and land area worldwide.
  Calculate the correlation between population density (population / land area) and land area for all countries in 2023.

validator:
  namespace_intact:
    update:
    - population
"""

(population['pop2023'] / population['landAreaKm']).corr(population['landAreaKm'])

# %%
"""
question: |
  Calculate the population density for each country in 2023 and 2050.
  The result should be a DataFrame with "Country" as the index and "2023 Population Density" and "2050 Population Density" as the columns.
"""

population_density = pd.DataFrame({
    'Country': population['country'],
    '2023 Population Density': population['pop2023'] / population['landAreaKm'],
    '2050 Population Density': population['pop2050'] / population['landAreaKm'],
}).set_index('Country')

population_density

# %%
"""
question: |
  Identify the countries with the highest and lowest population density in 2023 and 2050.
  The result DataFrame should have "Year", "Highest Population Density Country", "Lowest Population Density Country", "Highest Population Density", and "Lowest Population Density" as the columns.
"""

pd.DataFrame({
    'Year': [2023, 2050],
    'Highest Population Density Country': [
        population_density['2023 Population Density'].idxmax(),
        population_density['2050 Population Density'].idxmax(),
    ],
    'Lowest Population Density Country': [
        population_density['2023 Population Density'].idxmin(),
        population_density['2050 Population Density'].idxmin(),
    ],
    'Highest Population Density': [
        population_density['2023 Population Density'].max(),
        population_density['2050 Population Density'].max(),
    ],
    'Lowest Population Density': [
        population_density['2023 Population Density'].min(),
        population_density['2050 Population Density'].min(),
    ],
})

# %%
"""
question: |
  Calculate the change of population each country from 1980 to 2023.
  Put the "Country" and "Population Change" in the columns. Sort the DataFrame by "Population Change" in descending order.
"""

pd.DataFrame({
    'Country': population['country'],
    'Population Change': population['pop2023'] - population['pop1980']
}).sort_values(by='Population Change', ascending=False)

# %%
"""
question: |
  List the countries that have always remained top-10-population countries throughout 2000 and 2023.

validator:
  result:
    ignore_order: true
    value_only: true
"""

top_10_countries_2000 = set(population.nlargest(10, 'pop2000')['country'])
top_10_countries_2023 = set(population.nlargest(10, 'pop2023')['country'])

top_10_countries_2000.intersection(top_10_countries_2023)
