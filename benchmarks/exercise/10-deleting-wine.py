# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Import the dataset from this [address](inputs/wine.data).
  Assign it to a variable called wine

validator:
  namespace_check:
    wine:

data:
  wine.data: https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data
"""
wine = pd.read_csv("inputs/wine.data", header=None)

# %%
"""
question: Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns. The changes should take effect on the original dataframe directly.

validator:
  namespace_check:
    wine:
"""

wine.drop([0, 3, 6, 8, 10, 12, 13], axis=1, inplace=True)

# %%
"""
question: |
  Assign the columns as below:

  The attributes are (donated by Riccardo Leardi, riclea '@' anchem.unige.it):  
  1) alcohol  
  2) malic_acid  
  3) alcalinity_of_ash  
  4) magnesium  
  5) flavanoids  
  6) proanthocyanins  
  7) hue

validator:
  namespace_check:
    wine:
"""

wine.columns = [
    "alcohol",
    "malic_acid",
    "alcalinity_of_ash",
    "magnesium",
    "flavanoids",
    "proanthocyanins",
    "hue",
]

# %%
"""
question: Set the values of the first 3 rows from alcohol as NaN

validator:
  namespace_check:
    wine:
"""

wine.loc[:2, "alcohol"] = np.nan

# %%
"""
question: Now set the value of the rows 3 and 4 of magnesium as NaN

validator:
  namespace_check:
    wine:
"""

wine.loc[2:3, "magnesium"] = np.nan

# %%
"""
question: Fill the value of NaN with the number 10 in alcohol and 100 in magnesium. Fill it in-place.

validator:
  namespace_check:
    wine:
"""

wine["alcohol"].fillna(10, inplace=True)
wine["magnesium"].fillna(100, inplace=True)

# %%
"""
question: Count the number of missing values
"""

wine.isna().sum().sum()

# %%
"""
question: |
  Create an array of 10 random integers between 0 and 9. The numbers should be generated with a np.random.RandomState with seed 42.
  Use random numbers you generated as an index and assign NaN value to each of cell.

validator:
  namespace_check:
    wine:
"""

rng = np.random.RandomState(42)
indices = rng.randint(10, size=10).tolist()
wine.loc[indices, "alcohol"] = np.nan

# %%
"""
question: How many missing values do we have?
"""

wine.isna().sum().sum()

# %%
"""
question: Delete the rows that contain missing values. Delete them in-place.

validator:
  namespace_check:
    wine:
"""

wine.dropna(inplace=True)

# %%
"""
question: Reset the index, so it starts with 0 again. Do it in-place.

validator:
  namespace_check:
    wine:
"""

wine.reset_index(drop=True, inplace=True)
