# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/WLD_RTFP_country_2023-10-02.csv` into a variable `inflation`.

validator:
  namespace_check:
    inflation:
"""

inflation = pd.read_csv('inputs/WLD_RTFP_country_2023-10-02.csv')

# %%
"""
question: |
  Convert the `date` column to datetime format. Set `date` and `country` as the index of the DataFrame.

validator:
  namespace_check:
    inflation:
"""

inflation['date'] = pd.to_datetime(inflation['date'])
inflation.set_index(['date', 'country'], inplace=True)

# %%
"""
question: |
  Filter out the data from Afghanistan (starting from 2009). Reshape the inflation data with year as index and month as column. Leave the missing values as NaN.

validator:
  result:
    ignore_index: true
"""

afghanistan_inflation = inflation.loc[(slice(None), 'Afghanistan'), :].reset_index()
afghanistan_inflation[afghanistan_inflation.date.dt.year >= 2009].pivot_table(index=afghanistan_inflation.date.dt.year, columns=afghanistan_inflation.date.dt.month, values='Inflation')

# %%
"""
question: |
  Use ARIMA (with order 5, 1, 0) to predict the inflation in Afghanistan in 2024. Return the predicted inflation for each month in 2024 as a Series.

validator:
  result:
    value_only: true

execution:
  max_time: 3
"""

from statsmodels.tsa.arima.model import ARIMA

afghanistan_inflation_series = afghanistan_inflation[['date', 'Inflation']].dropna().set_index('date')['Inflation']

# Fit the ARIMA model
model = ARIMA(afghanistan_inflation_series, order=(5, 1, 0))
model_fit = model.fit()

# Make prediction
forecast = model_fit.forecast(steps=14)
forecast.loc['2024-01-01':'2024-12-31']

# %%
"""
question: |
  Will the inflation be generally increasing or decreasing in 2024? Output "Increasing" or "Decreasing".
"""

"Increasing" if forecast.diff().mean() > 0 else "Decreasing"

# %%
"""
question: |
  Read the file `inputs/WLD_RTP_details_2023-10-02.csv` into a variable `details`.

validator:
  namespace_check:
    details:
"""

details = pd.read_csv('inputs/WLD_RTP_details_2023-10-02.csv')

# %%
"""
question: |
  Convert the percentages in the `details` DataFrame into float numbers. For example, "7.93%" should be converted to 0.0793.

validator:
  namespace_check:
    details:
"""

percentage_columns = ['data_coverage_food', 'data_coverage_previous_12_months_food', 'total_food_price_increase_since_start_date', 'average_annualized_food_inflation', 'maximum_food_drawdown', 'average_annualized_food_volatility']
for column in percentage_columns:
    details[column] = details[column].str.rstrip('%').astype('float') / 100

# %%
"""
question: |
  Convert the `start_date_observations` and `end_date_observations` columns to datetime format.

validator:
  namespace_check:
    details:
"""

details['start_date_observations'] = pd.to_datetime(details['start_date_observations'])
details['end_date_observations'] = pd.to_datetime(details['end_date_observations'])

# %%
"""
question: |
  Create a new DataFrame that is made up with the "components" information. For each country, add multiple rows. In each row, show the food (e.g., "Rice (Low Quality, Fresh)"), unit of measure (e.g., "1 KG") and index weight (e.g., 1).
  The result DataFrame should have columns: "country", "food", "unit_of_measure", "index_weight".
  Save the new DataFrame as `components`.

validator:
  namespace_check:
    components:
      ignore_index: true
"""

import re

components = []
for _, detail in details.iterrows():
    for match in re.findall(r'([\w\d].*?) \((\d.*?), Index Weight = ([\d\.]+)\)', detail['components']):
        components.append({
            'country': detail['country'],
            'food': match[0],
            'unit_of_measure': match[1],
            'index_weight': match[2]
        })
components = pd.DataFrame(components)

# %%
"""
question: |
  Create a new DataFrame that is made up with the "number_of_observations_food" information. For each country, add multiple rows. In each row, show the food and number of observations.
  Save the new DataFrame as `observations`, with columns: "country", "food", "number_of_observations".

validator:
  result:
    ignore_index: true
"""

observations = details['number_of_observations_food'].str.split(', ', expand=True).stack().str.split(': ', expand=True)
observations.columns = ['food', 'number_of_observations']
observations['country'] = details.loc[observations.index.get_level_values(0)]['country'].values
observations['number_of_observations'] = observations['number_of_observations'].astype(int)
observations = observations[['country', 'food', 'number_of_observations']]

# %%
"""
question: |
  For each country, create a mapping from food in `components` to food in `observations`. Save the mapping as `food_mapping`, whose keys are country names and values are dictionaries from food in `observations` to food in `components`.
  Hint: Convert to lower case, break down words, and use a max sequence matching algorithm to find the best match. If some food in `observations` cannot be matched, omit it from the mapping.

validator:
  namespace_check:
    food_mapping:
"""

from collections import Counter
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching

def break_down_words(s):
    return re.sub(r'[\(\),_]', ' ', s).lower().split()

def best_match(a, b):
    a = {s: break_down_words(s) for s in a}
    b = {s: break_down_words(s) for s in b}
    matches = {}
    match_scores = []
    graph = np.zeros((len(a), len(b)), dtype=np.int8)
    for a_idx, (a_key, a_words) in enumerate(a.items()):
        for b_idx, (b_key, b_words) in enumerate(b.items()):
            graph[a_idx, b_idx] = len(set(a_words) & set(b_words))
    matches = maximum_bipartite_matching(csr_matrix(graph), perm_type='column')
    matches_parsed = {a_key: list(b)[b_idx] for a_key, b_idx in zip(a, matches) if b_idx != -1}
    return matches_parsed

food_mapping = {}
for country in details['country']:
    food_mapping[country] = best_match(observations.loc[observations.country == country]['food'], components.loc[components.country == country]['food'])

# %%
"""
question: |
  Merge the unit of measure and index weight with number of observations, with the information provided in `food_mapping`. If it's not available in `food_mapping`, drop the row. The result DataFrame should have "country", "food", "unit_of_measure", "index_weight", "number_of_observations" as the columns. Use the food names in `components` as the "food" in the result DataFrame.
"""

observations_with_new_food = observations.assign(food=observations.apply(lambda row: food_mapping[row['country']].get(row['food']), axis=1)).dropna()

components.merge(observations_with_new_food, on=['country', 'food'])[['country', 'food', 'unit_of_measure', 'index_weight', 'number_of_observations']]

# %%
"""
question: |
  Merge the details with the Inflation Estimates of 2023-01. Add a new column called "inflation_2023" to details.

validator:
  namespace_check:
    details:
"""

inflation_2023 = inflation.reset_index()
inflation_2023 = inflation_2023[inflation_2023.date.between('2023-01-01', '2023-01-31')][['country', 'Inflation']].rename(columns={'Inflation': 'inflation_2023'})

details = details.merge(inflation_2023, on='country')
