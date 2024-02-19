# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Import the dataset from `inputs/Customer-Churn-Records.csv`. Assign it to a variable called `churn`.

validator:
  namespace_check:
    churn:
"""

churn = pd.read_csv("inputs/Customer-Churn-Records.csv")

# %%
"""
question: |
  Calculate the churn rate for each region. Return a pandas DataFrame with "Geography" and "Churn Rate" as the columns, sorted by "Churn Rate" in descending order.

validator:
  result:
    ignore_index: true
"""

churn.groupby("Geography")["Exited"].mean().sort_values(ascending=False).rename(
    "Churn Rate"
).reset_index()

# %%
"""
question: |
  Which region has the highest churn rate?
"""

churn.groupby("Geography")["Exited"].mean().idxmax()

# %%
"""
question: |
  Calculate the average balance for each region. Return a Series with "Geography" as the index and "Balance" as the values.
"""

churn.groupby("Geography")["Balance"].mean()

# %%
"""
question: |
  Which region has the highest average balance?
"""

churn.groupby("Geography")["Balance"].mean().idxmax()

# %%
"""
question: |
  Drop the columns that will not be interesting to models, such as "CustomerId", and "Surname". Drop the column named "Complain". Save the cleaned dataset in-place.

validator:
  namespace_check:
    churn:
"""

churn = churn.drop(columns=["RowNumber", "CustomerId", "Surname", "Complain"])

# %%
"""
question: |
  Encode the categorical variables into continuous variables. Use one-hot encoding for "Geography" and "Card Type", and use label encoding for "Gender" (male: 0, female: 1). Save the encoded dataset in-place.

validator:
  namespace_check:
    churn:
"""

churn = pd.get_dummies(churn, columns=["Geography", "Card Type"])
churn["Gender"] = churn["Gender"].map({"Male": 0, "Female": 1})

# %%
"""
question: |
  Calculate the correlation between 'Point Earned' and 'Exited'.
"""

churn[["Point Earned", "Exited"]].corr().iloc[0, 1]

# %%
"""
question: |
  Compare the average 'Satisfaction Score' for churned and non-churned customers. The result DataFrame should have "Churned" and "Non-churned" as the index (Churn as the index name) and "Average Satisfaction Score" as the only column.

validator:
  result:
    ignore_order: true
"""

churn.groupby(churn["Exited"].map({0: "Non-churned", 1: "Churned"}))[
    ["Satisfaction Score"]
].mean().reset_index().rename(
    columns={"Exited": "Churn", "Satisfaction Score": "Average Satisfaction Score"}
).set_index(
    "Churn"
)

# %%
"""
question: |
  Conduct an ANOVA test to examine the difference in 'Estimated Salary' between churned and non-churned customers. Show the F-value and p-value in a tuple.

validator:
  result:
    atol: 0.01
"""

from scipy.stats import f_oneway

group1 = churn.loc[churn["Exited"] == 0, "EstimatedSalary"]
group2 = churn.loc[churn["Exited"] == 1, "EstimatedSalary"]

tuple(f_oneway(group1, group2))

# %%
"""
question: |
  Separate feature varaibles from target varaible. Use a standard scaler to put the data in the same scale. Save the scaled features in `X` and the target in `y`.

validator:
  namespace_check:
    X:
    y:
"""

from sklearn.preprocessing import StandardScaler

X = churn.drop("Exited", axis=1)
y = churn["Exited"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

# %%
"""
question: |
  Transform the data into training set and test set. The test size should be 20% of the whole dataset. Random state should be set to 101. Use `X_train`, `y_train` to store the training set and `X_test`, `y_test` for test set.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=101
)

# %%
"""
question: |
  Use over-sampling to make the training set balanced. Save the balanced training set in `X_train_balanced` and `y_train_balanced`.
  Use RandomOverSampler with random seed 102.

validator:
  namespace_check:
    X_train_balanced:
    y_train_balanced:
"""

from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=102)
X_train_balanced, y_train_balanced = ros.fit_resample(X_train, y_train)

# %%
"""
question: |
  Construct a model using XGBClassifier to predict heart disease. Save it in a variable called `model`.
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
    metric_type: [roc_auc, f1]
    tolerance: 0.99

execution:
  forbid_names:
    - X_test
    - y_test
    - X
    - y
  max_time: 60
"""

from xgboost import XGBClassifier

model = XGBClassifier(
    subsample=0.7,
    reg_lambda=0.3,
    reg_alpha=0.3,
    n_estimators=500,
    min_child_weight=3,
    max_depth=6,
    learning_rate=0.3,
    gamma=0.9,
    colsample_bytree=0.3,
    random_state=0,
)
model.fit(X_train_balanced, y_train_balanced)

# %%
"""
question: |
  Make predictions on the test set with `model.predict`. Compute area under ROC curve.
"""

from sklearn.metrics import roc_curve, auc

y_pred = model.predict(X_test)

fpr_optimized, tpr_optimized, _ = roc_curve(y_test, y_pred)
roc_auc_optimized = auc(fpr_optimized, tpr_optimized)
roc_auc_optimized
