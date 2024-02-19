# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/global-data-on-sustainable-energy (1).csv` into a variable `energy`.

validator:
  namespace_check:
    energy:
"""

energy = pd.read_csv('inputs/global-data-on-sustainable-energy (1).csv')

# %%
"""
question: |
  Identify the number of missing values in each column.
"""

energy.isnull().sum()

# %%
"""
question: |
  Calculate the correlation between 'Access to electricity (% of population)' and 'Renewable energy share in the total final energy consumption (%)' as of 2019.
"""

energy.loc[energy['Year'] == 2019, ['Access to electricity (% of population)', 'Renewable energy share in the total final energy consumption (%)']].dropna().corr().iloc[0, 1]

# %%
"""
question: |
  Identify the countries with the highest and lowest access to electricity in 2020.
  Return a tuple of `(country_with_highest_access, country_with_lowest_access)`.
"""

sorted_by_access = energy.loc[energy['Year'] == 2020].sort_values('Access to electricity (% of population)')
sorted_by_access.iloc[-1, 0], sorted_by_access.iloc[0, 0]

# %%
"""
question: |
  Calculate the 'Renewable energy share in the total final energy consumption (%)' averaged over countries for each year.
"""

energy.groupby('Year')['Renewable energy share in the total final energy consumption (%)'].mean()

# %%
"""
question: |
  Calculate the yearly growth rate of 'Renewable energy share in the total final energy consumption (%)' for each country.
  The growth rate is calculated as (current_year - previous_year) / previous_year. Use forward fill before computing to avoid missing values.
  Return a DataFrame with country names as columns and years as index.
"""

energy.pivot(index='Year', columns='Entity', values='Renewable energy share in the total final energy consumption (%)').ffill().pct_change()

# %%
"""
question: |
  Identify the countries that have a slowing down growth rate of "Access to clean fuels for cooking" from 2018 to 2019, and a speeding up growth rate from 2019 to 2020.
  Return a list of the country names.
"""

growth_rate = energy.pivot(index='Entity', columns='Year', values='Access to clean fuels for cooking').apply(lambda x: (x - x.shift(1)) / x.shift(1), axis=1)
growth_rate.loc[(growth_rate[2019] < growth_rate[2018]) & (growth_rate[2020] > growth_rate[2019])].index.tolist()

# %%
"""
question: |
  Convert non-numeric columns (except "Entity") to numeric if necessary.

validator:
  namespace_check:
    energy:
"""

energy['Density\\n(P/Km2)'] = energy['Density\\n(P/Km2)'].str.replace(',', '').astype(float)

# %%
"""
question: |
  Split the dataset into a training set (2000-2015) and a testing set (2016-2020). Use `X_train`, `y_train` to store the training set and `X_test`, `y_test` for test set.
  The target variable is 'Renewable energy share in the total final energy consumption (%)'. The features are all other columns except 'Entity' and 'Year'.
  Fill NaN features with mean of the training set. Drop rows where target is NaN.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

# Prepare features.
X_train = energy.loc[energy['Year'].between(2000, 2015)].drop(['Entity', 'Year', 'Renewable energy share in the total final energy consumption (%)'], axis=1)
X_test = energy.loc[energy['Year'].between(2016, 2020)].drop(['Entity', 'Year', 'Renewable energy share in the total final energy consumption (%)'], axis=1)

# Fill NaN features with mean of the training set.
X_train, X_test = X_train.fillna(X_train.mean()), X_test.fillna(X_train.mean())

# Prepare target.
y_train = energy.loc[energy['Year'].between(2000, 2015), 'Renewable energy share in the total final energy consumption (%)']
y_test = energy.loc[energy['Year'].between(2016, 2020), 'Renewable energy share in the total final energy consumption (%)']

# Drop rows where target is NaN.
X_train, y_train = X_train[y_train.notnull()], y_train[y_train.notnull()]
X_test, y_test = X_test[y_test.notnull()], y_test[y_test.notnull()]

# %%
"""
question: |
  Build a linear regression model to predict the outcome variable using all features. Save it in a variable called `model`.
  Fit the model on the training set.

validator:
  template: intact
  namespace_check:
    model:
      type_only: true
  model:
    model_name: model
    inputs_name: X_test
    labels_name: y_test
    metric_type: r2
    tolerance: 0.99

execution:
  forbid_names:
    - X_test
    - y_test
"""

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

# %%
"""
question: |
  Evaluate the performance of the linear regression model on the test set using metrics including RMSE and R-squared.
  Return a dictionary with "RMSE" and "R2" as keys and the corresponding values as values.
"""

from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)

metrics = {
    'RMSE': mean_squared_error(y_test, y_pred, squared=False),
    'R2': r2_score(y_test, y_pred)
}

metrics

# %%
"""
question: |
  Create a new DataFrame `energy_five_years` that contains 8 columns. The first two columns are "Entity" and "Year", which are the same as the original dataset. The remaining 6 columns are "Access to electricity" in current year, and "Access to electricity" in 1, 2, 3, 4, 5 years ago. The columns are named as "Access to electricity (current year)", "Access to electricity (1 year ago)", "Access to electricity (2 years ago)", etc. If the data is unavailable, fill it with NaN.

validator:
  namespace_check:
    energy_five_years:

execution:
  max_time: 3
"""

energy_five_years = energy[['Entity', 'Year']].copy()
energy_five_years['Access to electricity (current year)'] = energy['Access to electricity (% of population)']

energy_five_years_indexed = energy_five_years.set_index(['Entity', 'Year'])

def query_access_to_electricity(entity, year):
    try:
        return energy_five_years_indexed.loc[(entity, year), 'Access to electricity (current year)']
    except KeyError:
        return np.nan

for i in range(1, 6):
    energy_five_years[f'Access to electricity ({i} year{"s" if i > 1 else ""} ago)'] = energy_five_years.apply(lambda row: query_access_to_electricity(row['Entity'], row['Year'] - i), axis=1)

# %%
"""
question: |
  Drop the rows with missing values and save it in-place. Then calculate the correlation between "Access to electricity (current year)" and "Access to electricity (1 year ago)".

validator:
  namespace_check:
    energy_five_years:
"""

energy_five_years = energy_five_years.dropna()
energy_five_years['Access to electricity (current year)'].corr(energy_five_years['Access to electricity (1 year ago)'])

# %%
"""
question: |
  Fit a linear regression model that predicts "Access to electricity (current year)" based on the data from the previous 5 years. Save the model in a variable called `model_five_years`.

validator:
  template: intact
  namespace_check:
    model:
      type_only: true
  model:
    model_name: model_five_years
    inputs_name: X_train
    labels_name: y_train
    metric_type: r2
    tolerance: 0.99
"""

X_train = energy_five_years[['Access to electricity (1 year ago)', 'Access to electricity (2 years ago)', 'Access to electricity (3 years ago)', 'Access to electricity (4 years ago)', 'Access to electricity (5 years ago)']]
y_train = energy_five_years['Access to electricity (current year)']
model_five_years = LinearRegression()
model_five_years.fit(X_train, y_train)

# %%
"""
question: |
  Use the model to predict the access to electricity for each country in 2021. Return a DataFrame with two columns: "Entity" and "Access to electricity (2021)".

validator:
  result:
    ignore_index: true
"""

features = energy.loc[energy['Year'].between(2016, 2020)].pivot(index='Entity', columns='Year', values='Access to electricity (% of population)').iloc[:, ::-1]
pd.DataFrame({
    'Entity': features.index,
    'Access to electricity (2021)': model_five_years.predict(features)
})
