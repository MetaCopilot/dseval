# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/df_arabica_clean.csv` into a variable `coffee`.

validator:
  namespace_check:
    coffee:
"""

coffee = pd.read_csv('inputs/df_arabica_clean.csv')

# %%
"""
question: |
  Drop duplicated rows from the dataset. Then count the unique values for each column. Return a Series with column names as the index and the number of unique values as the values.

validator:
  namespace_check:
    coffee:
"""

coffee = coffee.drop_duplicates()
coffee.nunique()

# %%
"""
question: |
  Map the "Processing Method" into three categories: "Washed / Wet", "Pulped natural / Honey", and "Natural / Dry". Fill the missing values with "Washed / Wet". Save the result in-place.

validator:
  namespace_check:
    coffee:
"""

coffee['Processing Method'] = coffee['Processing Method'].map({
    'Washed / Wet': 'Washed / Wet',
    'Pulped natural / honey': 'Pulped natural / Honey',
    'Natural / Dry': 'Natural / Dry',
    'Double Anaerobic Washed': 'Washed / Wet',
    'Semi Washed': 'Washed / Wet',
    'Honey,Mossto': 'Pulped natural / Honey',
    'Double Carbonic Maceration / Natural': 'Natural / Dry',
    'Wet Hulling': 'Washed / Wet',
    'Anaerobico 1000h': 'Washed / Wet',
    'SEMI-LAVADO': 'Natural / Dry'
}).fillna('Washed / Wet')

# %%
"""
question: |
  Clean the "Altitude" column. If it's a range, compute its mean. If it's a single value, keep it as is. If it's missing, fill it with the mean of the column. Save the result in-place.

validator:
  namespace_check:
    coffee:
"""

# Extract the altitude range
altitude_range = coffee['Altitude'].str.extract(r'(\d+)[\-\sA~]+(\d+)')

# Compute the mean of the altitude range
altitude_mean = altitude_range.astype(float).mean(axis=1)

# If it's a single value, keep it as is
altitude_single = coffee['Altitude'].str.extract(r'^(\d+)$').astype(float)

# Combine the two
coffee['Altitude'] = altitude_mean.combine_first(altitude_single)

# Fill missing values with the mean of the column
coffee['Altitude'] = coffee['Altitude'].fillna(coffee['Altitude'].mean())

# %%
"""
question: |
  Extract the prior year from the "Harvest Year" column. If it's a range, extract the earlier year. If it's a single year, keep it as is. Save the result in-place.

validator:
  namespace_check:
    coffee:
"""

# Extract the harvest year range
harvest_year_range = coffee['Harvest Year'].str.extract(r'(\d+) / (\d+)')

# Extract the earlier year
earlier_year = harvest_year_range[0]

# If it's a single year, keep it as is
single_year = coffee['Harvest Year'].str.extract(r'^(\d+)$')

# Combine the two
coffee['Harvest Year'] = earlier_year.combine_first(single_year).astype(int)

# %%
"""
question: |
  Convert the "Harvest Year" and "Expiration" columns to datetime objects. Save the results in-place.

validator:
  namespace_check:
    coffee:
"""

# Convert Harvest Year to datetime
coffee['Harvest Year'] = pd.to_datetime(coffee['Harvest Year'].astype(str), format='%Y')

# Convert Expiration to datetime
coffee['Expiration'] = pd.to_datetime(coffee['Expiration'].str.replace(r"\b([0123]?[0-9])(st|th|nd|rd)\b",r"\1", regex=True))

# %%
"""
question: |
  Calculate the difference between "Expiration" and "Harvest Year" in days. Save the result in a new column named "Coffee Age".

validator:
  namespace_check:
    coffee:
"""

coffee['Coffee Age'] = (coffee['Expiration'] - coffee['Harvest Year']).dt.days

# %%
"""
question: |
  Drop the following columns from the dataset: "ID", "ICO Number", "Owner", "Region", "Certification Contact", "Certification Address", "Farm Name", "Lot Number", "Mill", "ICO Number", "Producer", "Company", "Expiration", "Harvest Year", "Unnamed: 0", "Number of Bags", "Bag Weight", "In-Country Partner", "Grading Date", "Variety", "Status", "Defects", "Uniformity", "Clean Cup", "Sweetness", and "Certification Body". Save the cleaned dataset in-place.

validator:
  namespace_check:
    coffee:
"""

coffee = coffee.drop(columns=["ID", "ICO Number", "Owner", "Region", "Certification Contact", "Certification Address", "Farm Name", "Lot Number", "Mill", "ICO Number", "Producer", "Company", "Expiration", "Harvest Year", "Unnamed: 0", "Number of Bags", "Bag Weight", "In-Country Partner", "Grading Date", "Variety", "Status", "Defects", "Uniformity", "Clean Cup", "Sweetness", "Certification Body"])

# %%
"""
question: |
  Preprocess the dataset for prediction of Total Cup Points. For categorical columns, use one-hot encoding to create columns named `{column_name}_{category_name}`. For numerical columns, use min-max scaler. Save the preprocessed dataset in a variable `coffee_preprocessed`.

validator:
  namespace_check:
    coffee_preprocessed:
"""

from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

# One-hot encode categorical columns
categorical_columns = coffee.select_dtypes(include=['object']).columns
one_hot_encoder = OneHotEncoder(sparse_output=False)
categorical_encoded = one_hot_encoder.fit_transform(coffee[categorical_columns])
categorical_encoded_df = pd.DataFrame(categorical_encoded, columns=one_hot_encoder.get_feature_names_out(categorical_columns))

# Scale numerical columns
numerical_columns = coffee.select_dtypes(include=['float64', 'int64']).columns
min_max_scaler = MinMaxScaler()
numerical_scaled = min_max_scaler.fit_transform(coffee[numerical_columns])
numerical_scaled_df = pd.DataFrame(numerical_scaled, columns=numerical_columns)

# Combine the two
coffee_preprocessed = pd.concat([categorical_encoded_df, numerical_scaled_df], axis=1)

# %%
"""
question: |
  Split the dataset into inputs and labels, as well as training set and testing set. Use 20% of the data as the testing set. Use random state 42 for reproducibility. Save the training set as `X_train`, `y_train`, and the testing set as `X_test`, `y_test`.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

from sklearn.model_selection import train_test_split

X = coffee_preprocessed.drop('Total Cup Points', axis=1)
y = coffee_preprocessed['Total Cup Points']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Build a regressor on the training set with RandomForestRegressor. Save it in a variable `model`.

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

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# %%
"""
question: |
  Evaluate the mean-squared error and R2 for the model on the testing set. Present the results in a tuple.
"""

from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

mse, r2
