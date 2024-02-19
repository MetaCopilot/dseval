# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Import the dataset from `inputs/heart_attack_prediction_dataset.csv`. Assign it to a variable called `heart`.

validator:
  namespace_check:
    heart:
"""

heart = pd.read_csv('inputs/heart_attack_prediction_dataset.csv')

# %%
"""
question: |
  Compute the correlation of heart attack risk against other numeric features. Sort the factors by the absolute values of the correlation coefficients in descending order.
"""

heart.select_dtypes('number').corr()['Heart Attack Risk'].drop('Heart Attack Risk').sort_values(ascending=False, key=abs)

# %%
"""
question: |
  Compute and sort the average BMI for each country in ascending order.
"""

heart.groupby('Country')['BMI'].mean().sort_values()

# %%
"""
question: |
  Convert the 'Diet' column into an ordinal feature. Use 1, 2, 3 for 'Healthy', 'Average', and 'Unhealthy' respectively. Save the result in-place.

validator:
  namespace_check:
    heart:
"""

diet_mapping = {'Healthy': 1, 'Average': 2, 'Unhealthy': 3}
heart['Diet'] = heart['Diet'].map(diet_mapping)

# %%
"""
question: |
  Split the 'Blood Pressure' column into two new columns 'BP Systolic' and 'BP Diastolic'. Save the result in-place.

validator:
  namespace_check:
    heart:
"""

heart[['BP Systolic', 'BP Diastolic']] = heart['Blood Pressure'].str.split('/', expand=True).astype(int)
heart.drop('Blood Pressure', axis=1, inplace=True)

# %%
"""
question: |
  Convert the 'Sex' column into two binary columns 'Sex Female' and 'Sex Male'. Convert the data types to integer. Save the result in-place.

validator:
  namespace_check:
    heart:
"""

heart = pd.get_dummies(heart, columns=['Sex'], prefix_sep=' ')
heart['Sex Male'] = heart['Sex Male'].astype(int)
heart['Sex Female'] = heart['Sex Female'].astype(int)

# %%
"""
question: |
  Define the feature matrix X and the target vector y for model building. X should contain all numerical columns except 'Heart Attack Risk'. y should be 'Heart Attack Risk'.

validator:
  namespace_check:
    X:
    y:
"""

X = heart.select_dtypes('number').drop(columns=['Heart Attack Risk'])
y = heart['Heart Attack Risk']

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Standardize the features using StandardScaler. Fit the scaler on the training set and transform both the training and test sets to numpy array (in-place).

validator:
  namespace_check:
    X_train:
    X_test:
"""

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# %%
"""
question: |
  Build a RandomForest model to predict the outcome variable using all features. Save it in a variable called `model`.
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
  max_time: 5
"""

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# %%
"""
question: |
  Cross-validate the random forest classifier. Use 5-fold cross-validation and accuracy as the scoring metric. Return the average accuracy.

validator:
  result:
    atol: 0.02

execution:
  max_time: 15
"""

from sklearn.model_selection import cross_val_score

cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy').mean()

# %%
"""
question: |
  Evaluate the performance of the RandomForest model on the test set. Return f1 and roc_auc scores in a tuple.
"""

from sklearn.metrics import f1_score, roc_auc_score

y_pred = model.predict(X_test)

(f1_score(y_test, y_pred), roc_auc_score(y_test, y_pred))

# %%
"""
question: |
  Use ensemble methods (e.g., a voting classifier) to boost the performance of the random forest model. Save the ensemble model in a variable called `model_ensemble`.
  Fit the model on the training set.

validator:
  template: intact
  namespace_check:
    model_ensemble:
      type_only: true
  model:
    model_name: model_ensemble
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
  max_time: 30
"""

from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

model_ensemble = VotingClassifier(estimators=[
    ('rf', RandomForestClassifier(random_state=42)),
    ('lr', LogisticRegression()),
    ('svc', SVC(probability=True, random_state=42))
], voting='soft')
model_ensemble.fit(X_train, y_train)

# %%
"""
question: |
  Compute the AUC curve of the model. The results should be two numpy arrays: the false positive rates and the true positive rates.
"""

from sklearn.metrics import roc_curve

y_score = model_ensemble.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_score)

fpr, tpr

# %%
"""
question: |
  Calculate the classification report for the best-performing model. Return a DataFrame with "precision", "recall", "f1-score", and "support" as the columns and `0`, `1`, and `accuracy` in the index.
"""

from sklearn.metrics import classification_report

classification_report_df = pd.DataFrame(classification_report(y_test, y_pred, output_dict=True)).transpose()
classification_report_df.drop(index=['macro avg', 'weighted avg'], inplace=True)
classification_report_df
