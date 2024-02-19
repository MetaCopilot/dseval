# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/Automobile.csv` into a variable `cars`.

validator:
  namespace_check:
    cars:
"""

cars = pd.read_csv('inputs/Automobile.csv')

# %%
"""
question: |
  Create a linear regression model to predict MPG based on the other features. Save it in `model`.
  The model should take the original features in `cars` as input and the output should be the MPG.
  Use one-hot encoder from sklearn to preprocess categorical features.
  Fit the model on the entire dataset.

validator:
  template: intact
  model:
    model_name: model
    inputs_name: cars_features
    labels_name: cars_labels
    metric_type: r2
    tolerance: 0.99

execution:
  max_time: 2
"""

from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

cars_features = cars.drop('mpg', axis=1)
cars_labels = cars['mpg']

# Define preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(), ['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year']),
        ('cat', OneHotEncoder(), ['origin'])
    ])

# Define model
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', LinearRegression())])


# Fit model
model.fit(cars_features, cars_labels)

# %%
"""
question: |
  Calculate the regression coefficients and interpret their meanings. Return a dict with feature names as the keys and coefficients as the values. One-hot encoded features should have names like "origin_europe", "origin_japan", and "origin_usa".
"""

dict(zip(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin_europe', 'origin_japan', 'origin_usa'], model.named_steps['regressor'].coef_))

# %%
"""
question: |
  Evaluate the model using the R-squared value. Return the R-squared value.
"""

model.score(cars_features, cars_labels)

# %%
"""
question: |
  Create a new feature that represents the age of the car (2023 minus model year) and add it to the regression model. Save the new model in a variable called `model_with_age`.

validator:
  template: intact
  namespace_check:
    cars_features:
  model:
    model_name: model_with_age
    inputs_name: cars_features
    labels_name: cars_labels
    metric_type: r2
    tolerance: 0.99
"""

# Add age feature
cars_features['age'] = 2023 - (1900 + cars_features['model_year'])

# Define preprocessor
preprocessor_with_age = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(), ['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'age']),
        ('cat', OneHotEncoder(), ['origin'])
    ])

# Define model
model_with_age = Pipeline(steps=[('preprocessor', preprocessor_with_age),
                                 ('regressor', LinearRegression())])

# Fit model
model_with_age.fit(cars_features, cars_labels)

# %%
"""
question: |
  Compare the performance of the new model with the old model. Return the R-squared value of the old model and the new model.
"""

(
    model.score(cars_features, cars_labels),
    model_with_age.score(cars_features, cars_labels)
)

# %%
"""
question: |
  Identify the car with the highest average miles per gallon (MPG) and the car with the lowest average MPG. Put their names in a tuple.
"""

cars.loc[cars['mpg'].idxmax(), 'name'], cars.loc[cars['mpg'].idxmin(), 'name']

# %%
"""
question: |
  Calculate the power-to-weight ratio for each car (horsepower divided by weight) and add it as a new feature named "power_to_weight" in the original dataframe.

validator:
  namespace_check:
    cars:
"""

cars['power_to_weight'] = cars['horsepower'] / cars['weight']

# %%
"""
question: |
  Identify the car with the highest power-to-weight ratio and the car with the lowest power-to-weight ratio.
"""

cars.loc[cars['power_to_weight'].idxmax(), 'name'], cars.loc[cars['power_to_weight'].idxmin(), 'name']

# %%
"""
question: |
  Calculate the average MPG for cars from each origin. Return a DataFrame with "Origin" and "Average MPG" as columns.

validator:
  result:
    ignore_order: true
"""

cars.groupby('origin').mean(numeric_only=True)[['mpg']].reset_index().rename(columns={'origin': 'Origin', 'mpg': 'Average MPG'})

# %%
"""
question: |
  Test the hypothesis that cars from Europe have a higher average MPG than cars from the USA using a t-test. Show the p-value.

validator:
  result:
    atol: 1.0e-19
"""

from scipy.stats import ttest_ind

usa_mpg = cars.loc[cars['origin'] == 'usa', 'mpg']
europe_mpg = cars.loc[cars['origin'] == 'europe', 'mpg']

t_stat, p_val = ttest_ind(usa_mpg, europe_mpg, alternative='less')

p_val

# %%
"""
question: |
  Create a new feature of categorical dtype that categorizes cars based on their MPG. The categories are "High" (MPG > 30), "Medium" (20 < MPG <= 30), and "Low" (MPG <= 20). Save the new feature in a new column named "mpg_category".

validator:
  namespace_check:
    cars:
"""

cars['mpg_category'] = pd.cut(cars['mpg'], bins=[0, 20, 30, np.inf], labels=['Low', 'Medium', 'High'])

# %%
"""
question: |
  Identify the most common category of MPG for cars from each origin. Return a Series with "Origin" as the index and "Most Common MPG Category" as the values.
"""

cars.groupby('origin')['mpg_category'].agg(lambda x: x.value_counts().idxmax())

# %%
"""
question: |
  Remove outliers in the data by removing cars with MPG or power-to-weight ratio values that are more than 3 standard deviations from the mean. Save the cleaned dataset in-place.

validator:
  namespace_check:
    cars:
"""

mpg_z_scores = (cars['mpg'] - cars['mpg'].mean()) / cars['mpg'].std()
power_to_weight_z_scores = (cars['power_to_weight'] - cars['power_to_weight'].mean()) / cars['power_to_weight'].std()

cars = cars.loc[(mpg_z_scores.abs() <= 3) & (power_to_weight_z_scores.abs() <= 3)]
