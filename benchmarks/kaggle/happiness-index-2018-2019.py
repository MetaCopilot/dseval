# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/report_2018-2019.csv` into a variable `happiness`.

validator:
  namespace_check:
    happiness:
"""

happiness = pd.read_csv('inputs/report_2018-2019.csv')

# %%
"""
question: |
  Identify the countries with the highest and lowest Happiness Index in 2019. Return a tuple of `(country_with_highest_happiness, country_with_lowest_happiness)`.
"""

happiness_2019 = happiness[happiness['Year'] == 2019]
happiness_2019.loc[happiness_2019['Score'].idxmax(), 'Country or region'], happiness_2019.loc[happiness_2019['Score'].idxmin(), 'Country or region']

# %%
"""
question: |
  Calculate the Happiness Index growth rate for each country from 2018 to 2019. The growth rate is defined as `(score_2019 - score_2018) / score_2018`.
  Present the results in a Series with "Country" as the index and "Happiness Growth Rate" as the values.
  If a country is not present in both years, ignore it.

validator:
  result:
    ignore_order: true
"""

happiness_2018 = happiness[happiness['Year'] == 2018]
happiness_growth_rate = (happiness_2019.set_index('Country or region')['Score'] - happiness_2018.set_index('Country or region')['Score']) / happiness_2018.set_index('Country or region')['Score']
happiness_growth_rate.rename('Happiness Growth Rate').dropna()

# %%
"""
question: |
  Identify the countries with the highest and lowest Happiness Index growth rates. Return a tuple of `(country_with_highest_growth, country_with_lowest_growth)`.
"""

happiness_growth_rate.idxmax(), happiness_growth_rate.idxmin()

# %%
"""
question: |
  Test the hypothesis that countries with a higher GDP per capita (higher than median, to be specific) have a higher Happiness Index using a t-test. Show the p-value.

validator:
  result:
    atol: 1.0e-50
"""

from scipy.stats import ttest_ind

# Separate the groups
group1 = happiness.loc[happiness['GDP per capita'] > happiness['GDP per capita'].median(), 'Score']
group2 = happiness.loc[happiness['GDP per capita'] <= happiness['GDP per capita'].median(), 'Score']

# Conduct t-test
t_stat, p_val = ttest_ind(group1, group2)

p_val

# %%
"""
question: |
  Identify the most important factors on happiness score. Return a list of the top 3 factors.

validator:
  result:
    ignore_order: true
"""

correlations = happiness.select_dtypes('number').corr()['Score'].drop(['Score', 'Overall rank']).abs().sort_values(ascending=False)
correlations.head(3).index.tolist()

# %%
"""
question: |
  Cluster the countries into 3 clusters based on the score and healthy life expectancy in 2019. Use KMeans with default hyper-parameters, `n_init` "auto" and random state 37.
  Return a DataFrame with "Country" as the index and "Cluster" as the values.

validator:
  result:
    ignore_order: true
"""

from sklearn.cluster import KMeans

# Fit KMeans
kmeans = KMeans(n_clusters=3, n_init='auto', random_state=37)
clusters = kmeans.fit_predict(happiness_2019[['Score', 'Healthy life expectancy']])

# Create DataFrame
pd.DataFrame({'Country': happiness_2019['Country or region'], 'Cluster': clusters}).set_index('Country')

# %%
"""
question: |
  For each cluster, compute the average and standard deviation of score and healthy life expectancy.
  Return a DataFrame with "Cluster" as the index and "Average Score", "Std Score", "Average Healthy Life Expectancy", "Std Healthy Life Expectancy" as the columns.
"""

clustered = happiness_2019.assign(Cluster=clusters)
clustered_groups = clustered.groupby('Cluster')[['Score', 'Healthy life expectancy']].agg(['mean', 'std']).rename(columns={'mean': 'Average', 'std': 'Std'})
clustered_groups.columns = [' '.join(col[::-1]).strip().replace('Healthy life expectancy', 'Healthy Life Expectancy') for col in clustered_groups.columns.values]
clustered_groups

# %%
"""
question: |
  Try to predict the happiness index of 2019 based on GDP per capita and social support.
  Split the data into train and test sets with a test size of 0.2 and random state 42.
  Save the training set as `X_train`, `y_train`, and the testing set as `X_test`, `y_test`.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

from sklearn.model_selection import train_test_split

X = happiness_2019[['GDP per capita', 'Social support']]
y = happiness_2019['Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Create a linear regression model to predict Happiness Index based on the other features. Save it in a variable called `model`.
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
    metric_type: [r2, mse]
    tolerance: [0.99, 1.01]

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
  Create a new feature that represents the change in GDP per capita from 2018 to 2019 and fill the missing values with mean. Save the new feature as a column called "GDP Change" in `happiness_2019` and add it to the regression model.
  Save the new model in a variable called `model_with_gdp_change`.
  Fit the model on the training set.

validator:
  template: intact
  namespace_check:
    model_with_gdp_change:
      type_only: true
    happiness_2019:
  model:
    model_name: model_with_gdp_change
    inputs_name: X_test
    labels_name: y_test
    metric_type: [r2, mse]
    tolerance: [0.99, 1.01]
"""

# Create the new feature
happiness_2019['GDP Change'] = happiness_2019['GDP per capita'] - happiness_2019.merge(happiness_2018, on='Country or region', suffixes=('_2019', '_2018'), how='left')['GDP per capita_2018']

# Fill the missing values
happiness_2019['GDP Change'] = happiness_2019['GDP Change'].fillna(happiness_2019['GDP Change'].mean())

# Split the data
X = happiness_2019[['GDP per capita', 'Social support', 'GDP Change']]
y = happiness_2019['Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model
model_with_gdp_change = LinearRegression()
model_with_gdp_change.fit(X_train, y_train)

# %%
"""
question: |
  Compare the performance of the new model with the old model. Show a tuple of `(r2_score_of_old_model, r2_score_of_new_model)`.
"""

from sklearn.metrics import r2_score

y_pred_old = model.predict(X_test[['GDP per capita', 'Social support']])
y_pred_new = model_with_gdp_change.predict(X_test)

r2_score(y_test, y_pred_old), r2_score(y_test, y_pred_new)
