# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/Sleep_health_and_lifestyle_dataset.csv` into a variable `sleep`.

validator:
  namespace_check:
    sleep:
"""

sleep = pd.read_csv('inputs/Sleep_health_and_lifestyle_dataset.csv')

# %%
"""
question: |
  Compute the percentage (0-100) of people with sleep disorder.
"""

sleep['Sleep Disorder'].notna().mean() * 100

# %%
"""
question: |
  Compute the sleep disorder percentage for each gender. Return a Series with "Gender" as the index and "Sleep Disorder Percentage" as the values.
"""

sleep.groupby('Gender')['Sleep Disorder'].apply(lambda x: x.notna().mean() * 100).rename('Sleep Disorder Percentage')

# %%
"""
question: |
  Identify the most common job for each type of sleep disorder. Return a Series with "Sleep Disorder" as the index and "Most Common Job" as the values.
"""

sleep.groupby('Sleep Disorder')['Occupation'].apply(lambda x: x.mode()[0]).rename('Most Common Job')

# %%
"""
question: |
  Split the "Blood Pressure" column into two separate columns: "Systolic Blood Pressure" and "Diastolic Blood Pressure". Save the changes in-place.

validator:
  namespace_check:
    sleep:
"""

sleep[['Systolic Blood Pressure', 'Diastolic Blood Pressure']] = sleep['Blood Pressure'].str.split('/', expand=True).astype(int)

# %%
"""
question: |
  Categorize the blood pressure into "Normal" and "Abnormal" based on the following rules:
  - Normal: Systolic blood pressure is less than or equal to 130 and diastolic blood pressure is less than or equal to 80.
  - Abnormal: Otherwise.
  Save the result in a new column named "Blood Pressure Category".

validator:
  namespace_check:
    sleep:
"""

sleep['Blood Pressure Category'] = np.where((sleep['Systolic Blood Pressure'] <= 130) & (sleep['Diastolic Blood Pressure'] <= 80), 'Normal', 'Abnormal')

# %%
"""
question: |
  Cut the "Age", "Sleep Duration", "Physical Activity Level", "Stress Level", "Heart Rate", and "Daily Steps" columns into 3 bins each. The bin edges should be determined by the quantiles of the data. Save the results in new columns with the same names but with " Bin" appended. Each bin should be named "Low", "Medium", and "High".

validator:
  namespace_check:
    sleep:
"""

for column in ['Age', 'Sleep Duration', 'Physical Activity Level', 'Stress Level', 'Heart Rate', 'Daily Steps']:
    sleep[f'{column} Bin'] = pd.qcut(sleep[column], 3, labels=['Low', 'Medium', 'High'])

# %%
"""
question: |
  Fill the empty values in "Sleep Disorder" column with "Normal".

validator:
  namespace_check:
    sleep:
"""
sleep['Sleep Disorder'] = sleep['Sleep Disorder'].fillna('Normal')

# %%
"""
question: |
  Drop ID, Blood Pressure and convert non-numeric data into numbers using label encoding. Save the changes in-place.

validator:
  namespace_check:
    sleep:
"""

from sklearn.preprocessing import LabelEncoder

sleep = sleep.drop(columns=['Person ID', 'Blood Pressure'])

le = LabelEncoder()
for column in sleep.columns:
    if sleep[column].dtype in ['object', 'category']:
        sleep[column] = le.fit_transform(sleep[column])

# %%
"""
question: |
  Find out the maximum six features affect Sleep Disorder with chi2 metric. Return a list of feature names.

validator:
  result:
    ignore_order: true
"""

from sklearn.feature_selection import SelectKBest, chi2

X = sleep.drop(columns='Sleep Disorder')
y = sleep['Sleep Disorder']

selector = SelectKBest(chi2, k=6)
selector.fit(X, y)

X.columns[selector.get_support()].tolist()

# %%
"""
question: |
  Split the data into `X_train`, `X_test`, `y_train`, `y_test`. The test size should be 0.2 of the whole dataset. Random state should be 42.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

from sklearn.model_selection import train_test_split

X = sleep.drop(columns='Sleep Disorder')
y = sleep['Sleep Disorder']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Use Logistic regression, XGBoost and CatBoost classifier to fit the data. Save the models in `lr_model`, `xgb_model`, `cb_model` respectively.

validator:
  template: intact
  namespace_check:
    lr_model:
      type_only: true
    xgb_model:
      type_only: true
    cb_model:
      type_only: true

execution:
  max_time: 30
"""

from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from catboost import CatBoostClassifier

lr_model = LogisticRegression(max_iter=5000)
lr_model.fit(X_train, y_train)

xgb_model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
xgb_model.fit(X_train, y_train)

cb_model = CatBoostClassifier(verbose=0)
cb_model.fit(X_train, y_train)

# %%
"""
question: |
  Evaluate the models and compare them. Return a DataFrame with "Logistic Regression", "XGBoost" and "CatBoost" as the index and "Accuracy", "Precision", "Recall" as the columns. Use weighted average for precision and recall.
"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

models = {'Logistic Regression': lr_model, 'XGBoost': xgb_model, 'CatBoost': cb_model}
metrics = pd.DataFrame(index=models.keys(), columns=['Accuracy', 'Precision', 'Recall'], dtype=float)

for model_name, model in models.items():
    y_pred = model.predict(X_test)
    metrics.loc[model_name, 'Accuracy'] = accuracy_score(y_test, y_pred)
    metrics.loc[model_name, 'Precision'] = precision_score(y_test, y_pred, average='weighted')
    metrics.loc[model_name, 'Recall'] = recall_score(y_test, y_pred, average='weighted')

metrics
