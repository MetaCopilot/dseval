# %%
import pandas as pd

# %%
"""
question: |
  Import the dataset from this [address](inputs/US_Baby_Names_right.csv).
  Assign it to a variable called baby_names.

validator:
  namespace_check:
    baby_names:

data:
  US_Baby_Names_right.csv: https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv
"""

baby_names = pd.read_csv('inputs/US_Baby_Names_right.csv')

# %%
"""
question: See the first 10 entries
"""

baby_names.head(10)

# %%
"""
question: "Delete the column 'Unnamed: 0' and 'Id'"
"""

# deletes Unnamed: 0
del baby_names['Unnamed: 0']

# deletes Unnamed: 0
del baby_names['Id']

# %%
"""
question: Are there more male names than female names in the dataset?
"""

gender_counts = baby_names['Gender'].value_counts()
gender_counts['M'] > gender_counts['F']

# %%
"""
question: Delete the year column, group the dataset by name, sort by count from the biggest value to the smallest one and assign to names. Save to names.

validator:
  namespace_check:
    names:
"""

# you don't want to sum the Year column, so you delete it
names = baby_names.drop(columns='Year')

# group the data
names = baby_names.groupby("Name").sum()

# sort it from the biggest value to the smallest one
names = names.sort_values("Count", ascending = False)

# %%
"""
question: How many different names exist in the dataset?
"""

# as we have already grouped by the name, all the names are unique already. 
# get the length of names
len(names)

# %%
"""
question: What is the name with most occurrences?
"""

names.Count.idxmax()

# %%
"""
question: How many different names have the least occurrences?
"""

len(names[names.Count == names.Count.min()])

# %%
"""
question: Show the rows with median name occurrence.
"""

names[names.Count == names.Count.median()]

# %%
"""
question: What is the standard deviation of names?
"""

names.Count.std()

# %%
"""
question: Get a summary with the mean, min, max, std and quartiles of the dataset.
"""

names.describe()
