# %%

import pandas as pd

# %%
"""
question: |
  Load the wine dataset from `inputs/winequality-red.csv`. Save as `df`.

validator:
  namespace_check:
    df:
"""

df = pd.read_csv("inputs/winequality-red.csv")

# %%
"""
question: |
  Perform a Z-score based outlier removal on the whole dataset. Do it in-place.

validator:
  namespace_check:
    df:
"""

import numpy as np
from scipy import stats

z = np.abs(stats.zscore(df))
df[(z < 3).all(axis=1)]

# %%
"""
question: |
  Split the dataset into features (`X`) and target (`y`).

validator:
  namespace_check:
    X:
    y:
"""

from sklearn.model_selection import train_test_split

X = df.drop(columns="quality")
y = df["quality"]

# %%
"""
question: |
  Split X and y into train and test sets. Use 20% of the data for testing.
  Set random state to 42.
  Fit a RandomForestClassifier `clf` with 100 estimators on the training data, also using random state 42.

validator:
  namespace_check:
    X_train:
    X_test:
    y_train:
    y_test:

  model:
    model_name: clf
    inputs_name: X_test
    labels_name: y_test
    metric_type: accuracy
    tolerance: 0.99
"""

from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
