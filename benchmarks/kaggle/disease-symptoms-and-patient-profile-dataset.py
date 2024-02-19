# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Import the dataset from `inputs/Disease_symptom_and_patient_profile_dataset.csv`. Assign it to a variable called `disease`.

validator:
  namespace_check:
    disease:
"""

disease = pd.read_csv('inputs/Disease_symptom_and_patient_profile_dataset.csv')

# %%
"""
question: |
  Check the balance of the dataset. Count the number of positive and negative outcomes. Put them in a Series with "Positive" and "Negative" as the index.
"""

disease['Outcome Variable'].value_counts()

# %%
"""
question: |
  Handle the imbalance in the dataset using oversampling. Randomly duplicate some rows from the minority class to make it have the same number of rows as the majority class (use `resample` in sklearn with `random_state` 123 please). Save the balanced dataset in `disease_balanced`.

validator:
  namespace_check:
    disease_balanced:
      ignore_order: true
"""

from sklearn.utils import resample

# Separate majority and minority classes
df_majority = disease[disease['Outcome Variable']=='Positive']
df_minority = disease[disease['Outcome Variable']=='Negative']

# Upsample minority class
df_minority_upsampled = resample(df_minority, 
                                 replace=True,     # sample with replacement
                                 n_samples=df_majority.shape[0],    # to match majority class
                                 random_state=123) # reproducible results

# Combine majority class with upsampled minority class
disease_balanced = pd.concat([df_majority, df_minority_upsampled])

# %%
"""
question: |
  Convert binary features into indicator (0/1) variables, and other categorical features (except "Disease" column) into numerical features using one-hot encoding. Save the encoded dataset in-place.

validator:
  namespace_check:
    disease_balanced:
"""

for column in ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing']:
    disease_balanced[column] = disease_balanced[column].map({'Yes': 1, 'No': 0})
disease_balanced['Outcome Variable'] = disease_balanced['Outcome Variable'].map({'Positive': 1, 'Negative': 0})

categorical_columns = [column for column in disease_balanced.columns if disease_balanced[column].dtype == 'object' and column != "Disease"]
disease_balanced = pd.get_dummies(disease_balanced, columns=categorical_columns)

# %%
"""
question: |
  Let's assume the name of disease irrelevant for the following case study.
  Split the dataset into training and test sets. The test size should be 20% of the whole dataset. Random state should be set to 42. Use `X_train`, `y_train` to store the training set and `X_test`, `y_test` for test set.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

from sklearn.model_selection import train_test_split

X = disease_balanced.drop(['Outcome Variable', 'Disease'], axis=1)
y = disease_balanced['Outcome Variable']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Build a logistic regression model to predict the outcome variable using all features. Save it in a variable called `model`.
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
    metric_type: [accuracy, roc_auc]
    tolerance: [0.99, 0.99]

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

# %%
"""
question: |
  Evaluate the performance of the logistic regression model on the test set using metrics including accuracy, precision, recall, F1 score and AUC-ROC. Return a dictionary with these metrics.

validator:
  result:
    ignore_index: true
"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

y_pred = model.predict(X_test)

metrics = {
    'accuracy': accuracy_score(y_test, y_pred),
    'precision': precision_score(y_test, y_pred),
    'recall': recall_score(y_test, y_pred),
    'f1': f1_score(y_test, y_pred),
    'roc_auc': roc_auc_score(y_test, y_pred)
}

metrics

# %%
"""
question: |
  Use a feature selection technique such as recursive feature elimination to select the most important features. Use logistic regression as the model and select 5 features. Return a list of the selected feature names.

validator:
  # only check type and length
  result: |
    def compare_fn(ref, sub):
      if type(ref) != type(sub):
        return {"match": False, "reason": f"Type mismatch: {type(ref)} vs {type(sub)}"}
      if len(ref) != len(sub):
        return {"match": False, "reason": f"Length: {len(ref)} vs {len(sub)}"}
      return {"match": True, "reason": ""}
"""

from sklearn.feature_selection import RFE
selector = RFE(estimator=LogisticRegression(max_iter=1000), n_features_to_select=5)
selector = selector.fit(X_train, y_train)

selected_features = X_train.columns[selector.support_].tolist()
selected_features

# %%
"""
question: |
  Build a logistic regression model using only the selected features. Save it in a variable called `model_selected`.
  Fit the model on the training set.

validator:
  template: intact
  namespace_check:
    model_selected: |
      def compare_fn(ref, sub):
        if type(ref) != type(sub):
          return {"match": False, "reason": f"Type mismatch: {type(ref)} vs {type(sub)}"}
        if ref.n_features_in_ != sub.n_features_in_:
          return {"match": False, "reason": f"n_features_in_ mismatch: {ref.n_features_in_} vs {sub.n_features_in_}"}
        return {"match": True, "reason": ""}
  # Need to check X_test[selected_features], which is unsupported yet.
  # model:
  #   model_name: model_selected
  #   inputs_name: X_test
  #   labels_name: y_test
  #   metric_type: [accuracy, roc_auc]
  #   tolerance: [0.99, 0.99]

execution:
  forbid_names:
    - y_test
    - X
    - y
"""

model_selected = LogisticRegression(max_iter=1000)
model_selected.fit(X_train[selected_features], y_train)

# %%
"""
question: |
  Evaluate the performance of the logistic regression model with selected features on the test set with the same metrics as before.

validator:
  result:
    ignore_index: true
"""

y_pred_selected = model_selected.predict(X_test[selected_features])

metrics_selected = {
    'accuracy': accuracy_score(y_test, y_pred_selected),
    'precision': precision_score(y_test, y_pred_selected),
    'recall': recall_score(y_test, y_pred_selected),
    'f1': f1_score(y_test, y_pred_selected),
    'roc_auc': roc_auc_score(y_test, y_pred_selected)
}

metrics_selected

# %%
"""
question: |
  Tune the hyperparameters of the logistic regression model (with original unselected features) using techniques such as grid search. Save the best model in a variable called `model_tuned`.
  The max time limit for the search is 10 seconds.

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
    tolerance: [0.99, 0.99]

execution:
  forbid_names:
    - X_test
    - y_test
    - X
    - y
  max_time: 20
"""

from sklearn.model_selection import GridSearchCV

param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'penalty': ['l1', 'l2']}
clf = GridSearchCV(LogisticRegression(solver='liblinear'), param_grid, cv=5)
model_tuned = clf.fit(X_train, y_train).best_estimator_

# %%
"""
question: |
  Evaluate the model with tuned hyper-parameters. Return the same metrics as before.

validator:
  result:
    ignore_index: true
"""

y_pred_tuned = model_tuned.predict(X_test)

metrics_tuned = {
    'accuracy': accuracy_score(y_test, y_pred_tuned),
    'precision': precision_score(y_test, y_pred_tuned),
    'recall': recall_score(y_test, y_pred_tuned),
    'f1': f1_score(y_test, y_pred_tuned),
    'roc_auc': roc_auc_score(y_test, y_pred_tuned)
}

metrics_tuned

# %%
"""
question: |
  Interpret the results of the models. Identify which features are the most influential in predicting the outcome variable. Return a list of the top 5 most influential features.

validator:
  result:
    ignore_order: true
"""

# Get feature importances
importances = model_tuned.coef_[0]

# Sort feature importances in descending order
indices = np.argsort(np.abs(importances))[::-1]

# Rearrange feature names so they match the sorted feature importances
names = [X_train.columns[i] for i in indices]

# Get top 5 features
names[:5]
