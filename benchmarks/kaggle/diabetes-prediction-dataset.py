# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Load the file `inputs/diabetes_prediction_dataset.csv` into a variable `diabetes`.

validator:
  namespace_check:
    diabetes:
"""

diabetes = pd.read_csv('inputs/diabetes_prediction_dataset.csv')

# %%
"""
question: |
  Drop duplicate rows from the dataset. Then describe the dataset (include all the columns).

validator:
  namespace_check:
    diabetes:
"""

diabetes = diabetes.drop_duplicates()
diabetes.describe(include='all')

# %%
"""
question: |
  Recategorize the "smoking_history" column into three categories: "non-smoker", "current", and "past-smoker".
  Please recategorize "No Info" as "non-smoker".
  Save the recategorized column in-place.

validator:
  namespace_check:
    diabetes:
"""

diabetes['smoking_history'] = diabetes['smoking_history'].map({'never': 'non-smoker', 'No Info': 'non-smoker', 'current': 'current', 'former': 'past-smoker', 'not current': 'past-smoker', 'ever': 'past-smoker'})

# %%
"""
question: |
  Perform one-hot encoding on the "gender" and "smoking_history" columns. Save the encoded dataset in-place.

validator:
  namespace_check:
    diabetes:
"""

diabetes = pd.get_dummies(diabetes, columns=['gender', 'smoking_history'])

# %%
"""
question: |
  Analyze the correlations among features. Return a DataFrame with the correlation coefficients.
"""

diabetes.corr()

# %%
"""
question: |
  Handle outliers in the "bmi", "HbA1c_level", and "blood_glucose_level" columns using winsorization. Cap the outliers at the 5th and 95th percentiles. Save the winsorized dataset in-place.

validator:
  namespace_check:
    diabetes:
"""

from scipy.stats.mstats import winsorize

diabetes['bmi'] = winsorize(diabetes['bmi'], limits=[0.05, 0.05])
diabetes['HbA1c_level'] = winsorize(diabetes['HbA1c_level'], limits=[0.05, 0.05])
diabetes['blood_glucose_level'] = winsorize(diabetes['blood_glucose_level'], limits=[0.05, 0.05])

# %%
"""
question: |
  The dataset is imbalanced (with only around 10% positive cases). Use SMOTE (with random state 42) and RandomUnderSampler (random state 42, downsamples to 50%) to rebalance the classes. The ratio of positive to negative cases should be 1:1. Save the rebalanced DataFrame in `diabetes_balanced`.

validator:
  namespace_check:
    diabetes_balanced:
"""

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline

# Define pipeline
over = SMOTE(sampling_strategy=0.1, random_state=42)
under = RandomUnderSampler(sampling_strategy=0.5, random_state=42)
steps = [('o', over), ('u', under)]
pipeline = Pipeline(steps=steps)

# Transform the dataset
X = diabetes.drop('diabetes', axis=1)
y = diabetes['diabetes']
X, y = pipeline.fit_resample(X, y)

diabetes_balanced = X.copy()
diabetes_balanced['diabetes'] = y

# %%
"""
question: |
  Normalize the "age", "bmi", "HbA1c_level", and "blood_glucose_level" columns using standard scalers. Save the normalized dataset in-place.

validator:
  namespace_check:
    diabetes_balanced:
"""

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
diabetes_balanced[['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']] = scaler.fit_transform(diabetes_balanced[['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']])

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

X = diabetes_balanced.drop('diabetes', axis=1)
y = diabetes_balanced['diabetes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Build a random forest classifier to predict diabetes using all features. Save it in a variable called `model`.
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
    metric_type: roc_auc
    tolerance: 0.99

execution:
  forbid_names:
    - X_test
    - y_test
    - X
    - y
  max_time: 5
"""

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# %%
"""
question: |
  Use grid search to tune the hyperparameters of the random forest classifier. The time limit is 30 seconds.
  Save the best model in a variable called `model_tuned`.

validator:
  template: intact
  namespace_check:
    model_tuned:
      type_only: true
  model:
    model_name: model_tuned
    inputs_name: X_test
    labels_name: y_test
    metric_type: roc_auc
    tolerance: 0.99

execution:
  forbid_names:
    - X_test
    - y_test
    - X
    - y
  max_time: 60
"""

from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 2, 6],
}

grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42), param_grid=param_grid, cv=3, scoring='roc_auc')
model_tuned = grid_search.fit(X_train, y_train).best_estimator_

# %%
"""
question: |
  Show all the parameters of the best model.
"""

model_tuned.get_params()

# %%
"""
question: |
  Show the confusion matrix for the model.

validator:
  result:
    value_only: true
"""

from sklearn.metrics import confusion_matrix

y_pred = model_tuned.predict(X_test)
confusion_matrix(y_test, y_pred)

# %%
"""
question: |
  Rank the most important features. Return a Series with feature names as the index and feature importances as the values, sorted in descending order.
"""

pd.Series(model_tuned.feature_importances_, index=X_train.columns).sort_values(ascending=False)