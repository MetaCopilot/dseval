# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/Netflix Userbase.csv` into a variable `netflix`.

validator:
  namespace_check:
    netflix:
"""

netflix = pd.read_csv('inputs/Netflix Userbase.csv')

# %%
"""
question: |
  Calculate the number of unique values in each column.
"""

netflix.nunique()

# %%
"""
question: |
  Calculate the number of users and total monthly revenue for each country. Return a DataFrame with "Country" as the index, "Number of Users" and "Total Monthly Revenue" as the columns.

validator:
  result:
    ignore_order: true
"""

netflix.groupby('Country').agg({'User ID': 'count', 'Monthly Revenue': 'sum'}).rename(columns={'User ID': 'Number of Users', 'Monthly Revenue': 'Total Monthly Revenue'})

# %%
"""
question: |
  Group the ages into the following categories: "18-24", "25-34", "35-44", "45-54", "55-64", "65+". Find out the number of users in each age group, sorted by age.

validator:
  result:
    ignore_index: true
"""

age_bins = [18, 25, 35, 45, 55, 65, np.inf]
age_labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
age_group = pd.cut(netflix['Age'], bins=age_bins, labels=age_labels, right=False)
age_group.value_counts().sort_index()

# %%
"""
question: |
  Analyze the device usage distribution. Count the number of users for each device type.
"""

netflix['Device'].value_counts()

# %%
"""
question: |
  Estimate the churn rate (i.e., the number of users who have left the service) by comparing the current date against the last payment date. Assume that a user has churned if their last payment date is more than 15 days away from the current date, and the current date is the latest payment date across the whole dataset. Calculate the churn rate as the proportion of churned users.
"""

# Convert dates to datetime
netflix['Last Payment Date'] = pd.to_datetime(netflix['Last Payment Date'], dayfirst=True)

# Calculate churn rate
netflix['Churn'] = (netflix['Last Payment Date'].max() - netflix['Last Payment Date']).dt.days.gt(15)

netflix['Churn'].mean()

# %%
"""
question: |
  Is the subscription type related to whether the user will churn or not? Conduct a chi-squared test and show the p-value.
"""

from scipy.stats import chi2_contingency

# Create contingency table
contingency = pd.crosstab(netflix['Subscription Type'], netflix['Churn'])

# Conduct chi-squared test
chi2, p, dof, expected = chi2_contingency(contingency)

p

# %%
"""
question: |
  Drop datetime features and IDs. Perform one-hot encoding on the categorical features. Save the processed dataset in-place.

validator:
  namespace_check:
    netflix:
"""

# Drop unnecessary columns
netflix = netflix.drop(columns=['User ID', 'Join Date', 'Last Payment Date'])

# One-hot encoding
netflix = pd.get_dummies(netflix, drop_first=True)

# %%
"""
question: |
  Split the dataset into training and test sets. The test size should be 20% of the whole dataset. Random state should be set to 42. Use `X_train`, `y_train` to store the training set and `X_test`, `y_test` for test set.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

from sklearn.model_selection import train_test_split

X = netflix.drop('Churn', axis=1)
y = netflix['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Build a logistic regression model to predict whether a user will churn. Save it in a variable called `model`.
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
    metric_type: accuracy
    tolerance: 0.99

execution:
  forbid_names:
    - X_test
    - y_test
    - X
    - y
"""

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
