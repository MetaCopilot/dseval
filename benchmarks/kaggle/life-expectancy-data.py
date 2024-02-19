# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/Life_Expectancy_Data.csv` into a variable `health`.

validator:
  namespace_check:
    health:
"""

health = pd.read_csv('inputs/Life_Expectancy_Data.csv')

# %%
"""
question: |
  Identify the country with the highest average life expectancy over the years.
"""

health.groupby('Country')['Life expectancy '].mean().idxmax()

# %%
"""
question: |
  Calculate the average life expectancy for each development status.
"""

health.groupby('Status')['Life expectancy '].mean()

# %%
"""
question: |
  Conduct a chi-squared test to examine the relationship between development status and the presence of Hepatitis B. Assume that a country has Hepatitis B if the Hepatitis B immunization coverage is greater than 90%. Return the chi-squared statistic and p-value.
"""

from scipy.stats import chi2_contingency

# Create contingency table
contingency = pd.crosstab(health['Status'], health['Hepatitis B'] > 90)

# Conduct chi-squared test
chi2, p, dof, expected = chi2_contingency(contingency)

chi2, p

# %%
"""
question: |
  Conduct an ANOVA test to examine the difference in life expectancy between different development statuses. Return the F-value and p-value.
"""

from scipy.stats import f_oneway

# Conduct ANOVA test
f_oneway(health.loc[health['Status'] == 'Developing', 'Life expectancy '], health.loc[health['Status'] == 'Developed', 'Life expectancy '])

# %%
"""
question: |
  Compute the annual growth rate of average life expectancy. The growth rate is calculated as (value_next_year - value_this_year) / value_this_year. Drop the last year from the result.
  Return a Series with "Year" as the index and "Growth Rate" as the values.
"""

life_expectancy_growth = (health.groupby('Year')['Life expectancy '].mean().shift(-1) - health.groupby('Year')['Life expectancy '].mean()) / health.groupby('Year')['Life expectancy '].mean()
life_expectancy_growth.rename('Growth Rate').iloc[:-1]

# %%
"""
question: |
  Identify the top 5 countries with the highest increase in life expectancy over the recent years. The increase in life expectancy is calculated as life_expectancy_in_latest_year - life_expectancy_in_earliest_year.
  Return a Series with "Country" as the index and "Increase in Life Expectancy" as the values.
"""

life_expectancy_increase = health.groupby('Country')['Life expectancy '].last() - health.groupby('Country')['Life expectancy '].first()
life_expectancy_increase.nlargest(5).rename('Increase in Life Expectancy')

# %%
"""
question: |
  Categorize the GDP into several bins and analyze the life expectancy for each bin. The GDP bins are defined as follows:
  - "Low GDP": GDP per capita <= $1,000
  - "Medium GDP": $1,000 < GDP per capita <= $10,000
  - "High GDP": GDP per capita > $10,000
  Return a DataFrame with "GDP Category" and "Average Life Expectancy" as the columns.
"""

health['GDP Category'] = pd.cut(health['GDP'], bins=[-np.inf, 1000, 10000, np.inf], labels=['Low GDP', 'Medium GDP', 'High GDP'])
health.groupby('GDP Category')['Life expectancy '].mean().rename('Average Life Expectancy').to_frame().reset_index()

# %%
"""
question: |
  Use PCA for feature selection. Standardize numerical features first, and then transform the features with PCA (random state = 37) and use the first two principal components. The result should be a DataFrame with "Country", "Year", "PC1" and "PC2" as the columns.

validator:
  result:
    ignore_index: true
"""

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Standardize the features
features = health.select_dtypes(include=np.number).dropna()
features_standardized = StandardScaler().fit_transform(features)

# Apply PCA
pca = PCA(n_components=2, random_state=37)
principal_components = pca.fit_transform(features_standardized)

# Create a DataFrame with the principal components
principal_components_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
principal_components_df = pd.concat([health[['Country', 'Year']], principal_components_df], axis=1)

principal_components_df

# %%
"""
question: |
  Use the principal components to predict life expectancy. Split the dataset into training and test sets. The test size should be 20% of the whole dataset. Random state should be set to 42. Use `X_train`, `y_train` to store the training set and `X_test`, `y_test` for test set.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

from sklearn.model_selection import train_test_split

X = principal_components_df[['PC1', 'PC2']]
y = health.loc[features.index, 'Life expectancy ']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Create a predictive model to predict life expectancy based on the selected features. Use Linear regression as the model. Save it in a variable called `model`.
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
    - X
    - y
"""

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

# %%
"""
question: |
  Evaluate the performance of the model using R-squared score.
"""

from sklearn.metrics import r2_score

y_pred = model.predict(X_test)
r2_score(y_test, y_pred)
