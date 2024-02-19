# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Import the dataset from this [address](inputs/iris.data).
  Assign it to a variable called iris

validator:
  namespace_check:
    iris:

data:
  iris.data: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
"""

iris = pd.read_csv("inputs/iris.data", header=None)

# %%
"""
question: |
  Rename columns for the dataset inplace:
  1. sepal_length
  2. sepal_width
  3. petal_length
  4. petal_width
  5. class

validator:
  namespace_check:
    iris:
"""

iris.columns = [
   "sepal_length",
   "sepal_width",
   "petal_length",
   "petal_width",
   "class",
]

# %%
"""
question: Is there any missing value in the dataframe?
"""

bool(iris.isna().sum().any())

# %%
"""
question: Lets set the values of the rows 10 to 29 of the column 'petal_length' to NaN

validator:
  namespace_check:
    iris:
"""

iris.loc[10:29, "petal_length"] = np.nan

# %%
"""
question: Good, now lets substitute the NaN values to 1.0

validator:
  namespace_check:
    iris:
"""

iris.fillna(1.0, inplace=True)

# %%
"""
question: Now let's delete the column class

validator:
  template: intact
  namespace_check:
    iris:
"""

iris.pop("class")

# %%
"""
question: Set the first 3 rows as NaN

validator:
  namespace_check:
    iris:
"""

iris.iloc[:3, :] = np.nan

# %%
"""
question: Delete the rows that have NaN. Modify the dataframe in place.

validator:
  namespace_check:
    iris:
"""

iris.dropna(inplace=True)

# %%
"""
question: Reset the index so it begins with 0 again

validator:
  namespace_check:
    iris:
"""

iris.reset_index(drop=True, inplace=True)
