# %%

import pandas as pd

dataset = pd.read_csv("inputs/movie_metadata.csv")

# %%

"""
question: |
  Show number of missing values in each column.
"""

dataset.isnull().sum()

# %%

"""
question: |
  Show the number of movies for each major genre, in a DataFrame with genre as index and count as the only column.
  The results can be in any order.

validator:
  result:
    ignore_order: true
"""

pd.Series(dataset["genres"].apply(lambda x: x.split("|")[0])).value_counts().rename("count").to_frame()
