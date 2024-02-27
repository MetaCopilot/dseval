# %%

import pandas as pd
import numpy as np

# %%
"""
question: |
  Load Iris dataset from `inputs/iris.csv`, into a variable called `iris`. Set `Id` as the index column.

validator:
  namespace_check:
    iris:
"""

iris = pd.read_csv("inputs/iris.csv", index_col="Id")

# %%
"""
question: |
  Test whether SepalLengthCm is normally distributed. Show the p-value.
"""

from scipy.stats import normaltest
z, pval = normaltest(iris["SepalLengthCm"])
pval

# %%
"""
question: |
  Analyze the correlations of the dataset. Eliminate upper triangle for readability.
"""

corr = iris.select_dtypes("number").corr(method="pearson")
corr.where(np.tril(np.ones(corr.shape)).astype(bool))
