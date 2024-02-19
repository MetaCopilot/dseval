# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Import the data from `inputs/Housing.csv` into a variable `housing`.

validator:
  namespace_check:
    housing:
"""

housing = pd.read_csv('inputs/Housing.csv')

# %%
"""
question: |
  Rename the column "area" to "area(m2)".

validator:
  namespace_check:
    housing:
"""

housing = housing.rename(columns={'area': 'area(m2)'})

# %%
"""
question: |
  Identify the data types for each column.
"""

housing.dtypes

# %%
"""
question: |
  Analyze the ratio of "yes" and "no" for the following columns: "mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea".
  Put the results in a DataFrame with "Column" as the index and "Yes" and "No" as the columns.
"""

columns = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea"]
percentages = housing[columns].apply(lambda x: x.value_counts(normalize=True)).transpose().rename(columns={'no': 'No', 'yes': 'Yes'})
percentages[['Yes', 'No']]

# %%
"""
question: |
  Check the skewness of each numeric feature and "price". If a feature is skewed (skewness > 0.5 or skewness < -0.5), apply a suitable transformation (e.g., log1p) to reduce its skewness. Save the transformed dataset in-place.

validator:
  namespace_check:
    housing:
"""

numeric_features = housing.select_dtypes(include='number')
skewed_features = numeric_features.apply(lambda x: x.skew()).sort_values(ascending=False)
skewed_features = skewed_features[abs(skewed_features) > 0.5]
print(skewed_features)

# Apply log transformation to skewed features
for feat in skewed_features.index:
    housing[feat] = np.log1p(housing[feat])

# %%
"""
question: |
  Encode the categorical features using label encoder from sklearn. Save the encoded dataset in-place.

validator:
  namespace_check:
    housing:
"""

from sklearn.preprocessing import LabelEncoder

categorical_features = housing.select_dtypes(include=[object])
label_encoders = {}
for i in categorical_features:
    label_encoders[i] = LabelEncoder()
    housing[i] = label_encoders[i].fit_transform(housing[i])

# %%
"""
question: |
  Split the dataset into a training set and a test set. The test size should be 20% of the whole dataset. Random state should be set to 42. Use `X_train`, `y_train` to store the training set and `X_test`, `y_test` for test set.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

from sklearn.model_selection import train_test_split

X = housing.drop('price', axis=1)
y = housing['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Build a linear regression model to predict the 'price' using the other features. Save the model in a variable called `model`. Fit the model on the training set.

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
  Evaluate the performance of the model on the test set using RMSE.
"""

from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)

mean_squared_error(y_test, y_pred, squared=False)

# %%
"""
question: |
  Identify the feature name with the highest predictive importance.
"""

feature_importances = pd.Series(model.coef_, index=X_train.columns)
feature_importances.idxmax()

# %%
"""
question: |
  Write a function `predict_price` to predict a house price given an input. The function should take multiple keyword arguments, where the argument names are column names in the original dataset and the values are the corresponding values for the input house. The function should return the predicted price.

validator:
  table_test:
    function_name: predict_price
    test_cases:
    - area: 7420
      bedrooms: 4
      bathrooms: 2
      stories: 3
      mainroad: "yes"
      guestroom: "no"
      basement: "no"
      hotwaterheating: "no"
      airconditioning: "yes"
      parking: 2
      prefarea: "yes"
      furnishingstatus: "furnished"
    - area: 9960
      bedrooms: 3
      bathrooms: 2
      stories: 2
      mainroad: "yes"
      guestroom: "no"
      basement: "yes"
      hotwaterheating: "no"
      airconditioning: "no"
      parking: 2
      prefarea: "yes"
      furnishingstatus: "semi-furnished"
"""

def predict_price(**input_data):
    input_data['area(m2)'] = input_data.pop('area')
    for feat in skewed_features.index:
        if feat != 'price':
            input_data[feat] = np.log1p(input_data[feat])
    for i in categorical_features:
        input_data[i] = label_encoders[i].transform([input_data[i]])[0]
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df[model.feature_names_in_])[0]
    return np.expm1(prediction)
