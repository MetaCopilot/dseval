# %%
import pandas as pd

# %%
"""
question: |
  Import the dataset from this [address](inputs/u.user).
  The data is separated by pipe (|).
  Assign it to a variable called users and use the 'user_id' as index

validator:
  namespace_check:
    users:

data:
  u.user: https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user
"""

users = pd.read_csv('inputs/u.user', sep='|', index_col='user_id')

# %%
"""
question: See the first 25 entries
"""

users.head(25)

# %%
"""
question: See the last 10 entries
"""

users.tail(10)

# %%
"""
question: What is the number of observations in the dataset?
"""

users.shape[0]

# %%
"""
question: What is the number of columns in the dataset?
"""

users.shape[1]

# %%
"""
question: The name of all the columns.

validator:
  result:
    value_only: true
"""

users.columns

# %%
"""
question: How is the dataset indexed?
"""

# "the index" (aka "the labels")
users.index

# %%
"""
question: What is the data type of each column?
"""

users.dtypes

# %%
"""
question: Extract the occupation column
"""

users.occupation

# %%
"""
question: How many different occupations are in this dataset?
"""

users.occupation.nunique()

# %%
"""
question: What is the most frequent occupation?
"""

#Because "most" is asked
users.occupation.value_counts().head(1).index[0]

# %%
"""
question: Summarize the DataFrame with Pandas describe method.
"""

users.describe() #Notice: by default, only the numeric columns are returned. 

# %%
"""
question: Include all the columns in the summarization of the DataFrame. Do it with describe method.
"""

users.describe(include = "all") #Notice: By default, only the numeric columns are returned.

# %%
"""
question: Summarize only the occupation column
"""

users.occupation.describe()

# %%
"""
question: What is the mean age of users? (rounded to integer)
"""

round(users.age.mean())

# %%
"""
question: What are the 5 ages with least occurrence? Name them.

validator:
  result:
    compare_fn:
      value_only: true
      ignore_order: true
"""

users.age.value_counts().tail(5).index.tolist()
