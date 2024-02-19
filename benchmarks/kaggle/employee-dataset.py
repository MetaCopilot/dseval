# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/Employee.csv` into a variable `employee`.

validator:
  namespace_check:
    employee:
"""

employee = pd.read_csv('inputs/Employee.csv')

# %%
"""
question: |
  Identify the number of unique values in each column.
"""

employee.nunique()

# %%
"""
question: |
  Remove duplicates from the dataset. Show the shape of the dataframe after removing duplicates.

validator:
  namespace_check:
    employee:
"""

employee = employee.drop_duplicates()
employee.shape

# %%
"""
question: |
  Encode the 'Gender' column into binary format. Use 0 for 'Male' and 1 for 'Female'. Save the result in-place.

validator:
  namespace_check:
    employee:
"""

employee['Gender'] = employee['Gender'].map({'Male': 0, 'Female': 1})

# %%
"""
question: |
  Create a pivot table that shows the average 'PaymentTier' for each 'Education' level. Show the result in a DataFrame with 'Education' as the index and 'Average PaymentTier' as the column.
"""

employee.pivot_table(index='Education', values='PaymentTier', aggfunc='mean').rename(columns={'PaymentTier': 'Average PaymentTier'})

# %%
"""
question: |
  Create a new feature 'YearsInCompany' that represents the number of years each employee has been in the company. It is calculated as 2023 minus the 'JoiningYear'. Save the result in-place.

validator:
  namespace_check:
    employee:
"""

employee['YearsInCompany'] = 2023 - employee['JoiningYear']

# %%
"""
question: |
  Encode the categorical columns using label encoding. Save the result in-place.

validator:
  namespace_check:
    employee:
"""

from sklearn.preprocessing import LabelEncoder

categorical_columns = employee.select_dtypes(include=['object']).columns
for column in categorical_columns:
    le = LabelEncoder()
    employee[column] = le.fit_transform(employee[column])

# %%
"""
question: |
  Split the dataset into training and test sets. The test size should be 20% of the whole dataset. Random state should be set to 42. Use `X_train`, `y_train` to store the training set and `X_test`, `y_test` for test set. The goal is to predict whether the employee will leave or not.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

from sklearn.model_selection import train_test_split

X = employee.drop('LeaveOrNot', axis=1)
y = employee['LeaveOrNot']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Balance the dataset using SMOTE Oversampling technique. Save the balanced dataset in `X_train_balanced` and `y_train_balanced`. Set the random state to be 42.

validator:
  namespace_check:
    X_train_balanced:
    y_train_balanced:
"""

from imblearn.over_sampling import SMOTE

sm = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = sm.fit_resample(X_train, y_train)

# %%
"""
question: |
  Build a random forest classifier to predict the 'LeaveOrNot' variable. Save it in a variable called `model`.
  Fit the model on the balanced training set.

validator:
  template: intact
  namespace_check:
    model:
      type_only: true
  model:
    model_name: model
    inputs_name: X_test
    labels_name: y_test
    metric_type: [accuracy, roc_auc]
    tolerance: 0.99

execution:
  forbid_names:
    - X_test
    - y_test
    - X
    - y
"""

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)
model.fit(X_train_balanced, y_train_balanced)

# %%
"""
question: |
  Search the hyper-parameters of the random forest classifier using grid search. Save the best model in a variable called `model_tuned`.
  The maximum time allowed for the search is 30 seconds.

validator:
  template: intact
  namespace_check:
    model_tuned:
      type_only: true
  model:
    model_name: model_tuned
    inputs_name: X_test
    labels_name: y_test
    metric_type: [accuracy, roc_auc]
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
    'max_features': [1, 3, 10],
    'min_samples_leaf': [1, 3, 10],
    'n_estimators': [100, 200, 300]
}
clf = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3)
model_tuned = clf.fit(X_train_balanced, y_train_balanced).best_estimator_

# %%
"""
question: |
  Analyze the confusion matrix of the random forest classifier with tuned hyper-parameters. Put the results in a DataFrame with "Predicted Negative" and "Predicted Positive" as the columns and "Actual Negative" and "Actual Positive" as the index.
"""

from sklearn.metrics import confusion_matrix

y_pred_tuned = model_tuned.predict(X_test)
confusion = confusion_matrix(y_test, y_pred_tuned)
pd.DataFrame(confusion, columns=['Predicted Negative', 'Predicted Positive'], index=['Actual Negative', 'Actual Positive'])

# %%
"""
question: |
  Build a voting classifier with multiple base models, and save it in a variable called `voting_model`.
  Fit the model on the balanced training set.

validator:
  template: intact
  namespace_check:
    voting_model:
      type_only: true
  model:
    model_name: voting_model
    inputs_name: X_test
    labels_name: y_test
    metric_type: [accuracy, roc_auc]
    tolerance: 0.99

execution:
  forbid_names:
    - X_test
    - y_test
    - X
    - y
  max_time: 5
"""

from sklearn.ensemble import VotingClassifier, GradientBoostingClassifier

voting_model = VotingClassifier(estimators=[
    ('gbc', GradientBoostingClassifier(random_state=42)),
    ('gbc1', GradientBoostingClassifier(learning_rate=0.05, min_samples_split=3, n_estimators=500, random_state=42)),
    ('rf', RandomForestClassifier(max_features=3, min_samples_leaf=3, min_samples_split=3, random_state=42))
], voting='soft')
voting_model.fit(X_train_balanced, y_train_balanced)

# %%
"""
question: |
  Evaluate the voting classifier with multiple metrics. Return a dictionary with 'accuracy', 'precision', 'recall', 'f1', and 'roc_auc' as the keys and the corresponding scores as the values.
"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

y_pred_voting = voting_model.predict(X_test)

{
    'accuracy': accuracy_score(y_test, y_pred_voting),
    'precision': precision_score(y_test, y_pred_voting),
    'recall': recall_score(y_test, y_pred_voting),
    'f1': f1_score(y_test, y_pred_voting),
    'roc_auc': roc_auc_score(y_test, y_pred_voting)
}
