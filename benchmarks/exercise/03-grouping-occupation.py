# %%
import pandas as pd

# %%
"""
question: |
  Import the dataset from this [address](inputs/u.user). Columns are separated with `|`.
  Use the `user_id` as index.
  Assign it to a variable called users.

validator:
  namespace_check:
    users:

data:
  u.user: https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user
"""

users = pd.read_table('inputs/u.user', sep='|', index_col='user_id')

# %%
"""
question: Discover what is the mean age per occupation
"""

users.groupby('occupation').age.mean()

# %%
"""
question: Discover the Male percentage (0-100) per occupation and sort it from the most to the least
"""

# create a function
def gender_to_numeric(x):
    if x == 'M':
        return 1
    if x == 'F':
        return 0

# apply the function to the gender column and create a new column
users['gender_n'] = users['gender'].apply(gender_to_numeric)


a = users.groupby('occupation').gender_n.sum() / users.occupation.value_counts() * 100 

# sort to the most male 
a.sort_values(ascending = False)

# %%
"""
question: For each occupation, calculate the minimum and maximum ages
"""

users.groupby('occupation').age.agg(['min', 'max'])

# %%
"""
question: For each combination of occupation and gender, calculate the mean age. Use multilevel groupby
"""

users.groupby(['occupation', 'gender']).age.mean()

# %%
"""
question: For each occupation present the percentage of women and men
"""

# create a data frame and apply count to gender
gender_ocup = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})

# create a DataFrame and apply count for each occupation
occup_count = users.groupby(['occupation']).agg('count')

# divide the gender_ocup per the occup_count and multiply per 100
occup_gender = gender_ocup.div(occup_count, level = "occupation") * 100

# present all rows from the 'gender column'
occup_gender.loc[: , 'gender']

