# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Import the dataset from `inputs/supermarket_sales.csv`. Assign it to a variable called `sales`.

validator:
  namespace_check:
    sales:
"""

sales = pd.read_csv('inputs/supermarket_sales.csv')

# %%
"""
question: |
  Clean the 'Date' and 'Time' columns and combine them into a single 'DateTime' column. The 'DateTime' column should be in datetime format.

validator:
  namespace_check:
    sales:
"""

# Convert 'Date' to datetime
sales['Date'] = pd.to_datetime(sales['Date'])

# Combine 'Date' and 'Time' into 'DateTime'
sales['DateTime'] = pd.to_datetime(sales['Date'].dt.strftime('%Y-%m-%d') + ' ' + sales['Time'])

# Drop the original 'Date' and 'Time' columns
sales = sales.drop(columns=['Date', 'Time'])

# %%
"""
question: |
  Calculate the value counts of the product lines.
"""

sales['Product line'].value_counts()

# %%
"""
question: |
  Calculate the average total sales for each day of the week. Return a Series with "Day of Week" as the index and "Average Sales" as the values. The index should be sorted in the order of Monday to Sunday.
"""

sales.groupby(sales['DateTime'].dt.day_name())['Total'].mean().rename('Average Sales').rename_axis('Day of Week').reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# %%
"""
question: |
  Calculate the average total sales for each hour of the day. Return a Series with "Hour of Day" as the index and "Average Sales" as the values.
"""

sales.groupby(sales['DateTime'].dt.hour)['Total'].mean().rename('Average Sales').rename_axis('Hour of Day')

# %%
"""
question: |
  Calculate the average total sales for each payment method. Return a Series with "Payment Method" as the index and "Average Sales" as the values.
"""

sales.groupby('Payment')['Total'].mean().rename('Average Sales').rename_axis('Payment Method')

# %%
"""
question: |
  Compute the maximum absolute difference between the total cost of the transaction (unit price times quantity plus tax) and the "Total" column.

validator:
  result:
    atol: 1.0e-15
"""

(sales['Unit price'] * sales['Quantity'] + sales['Tax 5%'] - sales['Total']).abs().max()

# %%
"""
question: |
  Use label encoder to encode categorical features into numbers. Save the encoded dataset in-place.

validator:
  namespace_check:
    sales:
"""

from sklearn.preprocessing import LabelEncoder

# Initialize label encoder
le = LabelEncoder()

# Encode categorical features
categorical_features = sales.select_dtypes(include=['object']).columns
sales[categorical_features] = sales[categorical_features].apply(le.fit_transform)

# %%
"""
question: |
  Try to predict the rating of the invoice based on the other features. Split the dataset into training and test sets. The test size should be 20% of the whole dataset. Random state should be set to 42. Use `X_train`, `y_train` to store the training set and `X_test`, `y_test` for test set. Drop DateTime as it can't be processed by the model.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

from sklearn.model_selection import train_test_split

X = sales.drop(['Rating', 'DateTime'], axis=1)
y = sales['Rating']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Build a K Nearest Neighbor regressor to predict the rating. Save it in a variable called `knn`.
  Fit the model on the training set.

validator:
  template: intact
  namespace_check:
    knn:
      type_only: true
  model:
    model_name: knn
    inputs_name: X_test
    labels_name: y_test
    metric_type: rmse
    tolerance: 1.05

execution:
  forbid_names:
    - X_test
    - y_test
    - X
    - y
"""

from sklearn.neighbors import KNeighborsRegressor

knn = KNeighborsRegressor()
knn.fit(X_train, y_train)

# %%
"""
question: |
  Build a decision tree regressor to predict the rating of the invoice. Save it in a variable called `dt`.
  Fit the model on the training set.

validator:
  template: intact
  namespace_check:
    dt:
      type_only: true
  model:
    model_name: dt
    inputs_name: X_test
    labels_name: y_test
    metric_type: rmse
    tolerance: 1.05

execution:
  forbid_names:
    - X_test
    - y_test
    - X
    - y
"""

from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)

# %%
"""
question: |
  Build a gradient boosting regressor to predict the rating. Save it in a variable called `gb`.
  Fit the model on the training set.

validator:
  template: intact
  namespace_check:
    gb:
      type_only: true
  model:
    model_name: gb
    inputs_name: X_test
    labels_name: y_test
    metric_type: rmse
    tolerance: 1.05

execution:
  forbid_names:
    - X_test
    - y_test
    - X
    - y
"""

from sklearn.ensemble import GradientBoostingRegressor

gb = GradientBoostingRegressor(random_state=42)
gb.fit(X_train, y_train)

# %%
"""
question: |
  Ensemble the three classifiers to get a better model. Save it in a variable called `ensemble`.
  Fit the model on the training set.

validator:
  template: intact
  namespace_check:
    ensemble:
      type_only: true
  model:
    model_name: ensemble
    inputs_name: X_test
    labels_name: y_test
    metric_type: rmse
    tolerance: 1.05

execution:
  forbid_names:
    - X_test
    - y_test
    - X
    - y
"""

from sklearn.ensemble import VotingRegressor

ensemble = VotingRegressor(estimators=[('knn', knn), ('dt', dt), ('gb', gb)])
ensemble.fit(X_train, y_train)
