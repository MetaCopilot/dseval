# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Import the data of `inputs/world-data-2023.csv` into a variable `world_data`.

validator:
  namespace_check:
    world_data:
"""

world_data = pd.read_csv('inputs/world-data-2023.csv')

# %%
"""
question: |
  Clean and preprocess the dataset. Convert the columns that should be numeric to numeric. Remove excessive spaces from the column names. Save the cleaned dataset in-place.

validator:
  namespace_check:
    world_data:
"""

# Convert columns to numeric, replacing non-numeric characters and commas
cols_to_convert = [
    'Density\n(P/Km2)', 'Agricultural Land( %)', 'Land Area(Km2)',
    'Birth Rate', 'Co2-Emissions', 'Forested Area (%)',
    'CPI', 'CPI Change (%)', 'Fertility Rate', 'Gasoline Price', 'GDP',
    'Gross primary education enrollment (%)', 'Armed Forces size',
    'Gross tertiary education enrollment (%)', 'Infant mortality',
    'Life expectancy', 'Maternal mortality ratio', 'Minimum wage', 
    'Out of pocket health expenditure', 'Physicians per thousand', 
    'Population', 'Population: Labor force participation (%)', 
    'Tax revenue (%)', 'Total tax rate', 'Unemployment rate', 'Urban_population'
]

for col in cols_to_convert:
    world_data[col] = world_data[col].apply(lambda x: float(str(x).replace(',', '').replace('$', '').replace('%', '')))

# %%
"""
question: |
  Fill missing values in the dataset. For numerical columns, fill with the mean of the column. For categorical columns, fill with the mode of the column.

validator:
  namespace_check:
    world_data:
"""

# Fill missing values
numerical_columns = world_data.select_dtypes(include=[np.number]).columns
categorical_columns = world_data.select_dtypes(include=[object]).columns

world_data[numerical_columns] = world_data[numerical_columns].fillna(world_data[numerical_columns].mean())
world_data[categorical_columns] = world_data[categorical_columns].fillna(world_data[categorical_columns].mode().iloc[0])

# %%
"""
question: |
  List out the top 10 countries' names with the highest unemployment rates.

validator:
  result:
    ignore_order: true
"""

world_data[['Country', 'Unemployment rate']].set_index('Country').sort_values(by='Unemployment rate', ascending=False).head(10).index.tolist()

# %%
"""
question: |
  Show the top 10 countries with the highest populations. Return a DataFrame with "Country" as the index and "Population" as the column.
"""

world_data[['Country', 'Population']].set_index('Country').sort_values(by='Population', ascending=False).head(10)

# %%
"""
question: |
  Find the most popular languages. Show the top 5 languages and the number of countries that speak each language. Return a Series with "Language" as the index and "Number of Countries" as the values.
"""

world_data['Official language'].value_counts().head(5).rename('Number of Countries')

# %%
"""
question: |
  Identify the countries that speak the most popular language. The result should form a list.

validator:
  result:
    ignore_order: true
"""

most_popular_language = world_data['Official language'].value_counts().idxmax()
world_data.loc[world_data['Official language'] == most_popular_language]['Country'].tolist()

# %%
"""
question: |
  Calculate the correlation coefficient between birth rate and GDP.
"""

world_data['Birth Rate'].corr(world_data['GDP'])

# %%
"""
question: |
  Analyze the pairwise correlations among economic indicators including GDP, CPI, CPI Change (%), Tax revenue (%), and Total tax rate. Return a DataFrame with the economic indicators as both the rows and columns.
"""

world_data[['GDP', 'CPI', 'CPI Change (%)', 'Tax revenue (%)', 'Total tax rate']].corr()

# %%
"""
question: |
  Compare the countries with top-5 currency codes versus other countries in terms of GDP and population. The result should have "Within Top-5" and "Not Within Top-5" as the columns and "Average GDP" and "Total Population" as the index.
"""

top_5_currency_codes = world_data['Currency-Code'].value_counts().head(5).index
within_top_5 = world_data['Currency-Code'].isin(top_5_currency_codes)
pd.DataFrame({
    'Within Top-5': [
        world_data.loc[within_top_5, 'GDP'].mean(),
        world_data.loc[within_top_5, 'Population'].sum()
    ],
    'Not Within Top-5': [
        world_data.loc[~within_top_5, 'GDP'].mean(),
        world_data.loc[~within_top_5, 'Population'].sum()
    ]
}).rename(index={0: 'Average GDP', 1: 'Total Population'})

