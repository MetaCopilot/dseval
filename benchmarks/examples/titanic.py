# %%

import numpy as np
import pandas as pd

# %%
"""
question: |
  Load train set of titanic dataset from `inputs/titanic_train.csv` into `train_data` and return the number of rows and columns.

validator:
  namespace_check:
    train_data:
"""

train_data = pd.read_csv("inputs/titanic_train.csv")
train_data.shape

# %%
"""
question: |
  Similarly load the test data.

validator:
  namespace_check:
    test_data:
"""

test_data = pd.read_csv("inputs/titanic_test.csv")
test_data.shape

# %%
"""
question: |
  Compute the % of women (0-100) who survived in the train set.
"""

women = train_data.loc[train_data.Sex == "female"]["Survived"]
sum(women) / len(women) * 100

# %%
"""
question: |
  List out the names with age 42.
"""

train_data.loc[train_data.Age == 42, "Name"].tolist()
