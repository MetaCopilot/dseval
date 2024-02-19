# %%
import pandas as pd

# %%
"""
question: |
  Import the dataset from `inputs/euro12.csv`.
  Assign it to a variable called euro12.

validator:
  namespace_check:
    euro12:

data:
  euro12.csv: https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv
"""

euro12 = pd.read_csv('inputs/euro12.csv', sep=',')

# %%
"""
question: Select only the Goal column.
"""

euro12.Goals

# %%
"""
question: How many team participated in the Euro2012?
"""

euro12.shape[0]

# %%
"""
question: What is the number of columns in the dataset?
"""

euro12.info()

# %%
"""
question: View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

validator:
  namespace_check:
    discipline:
"""

discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]

# %%
"""
question: Sort the teams by Red Cards, then to Yellow Cards
"""

discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)

# %%
"""
question: Calculate the mean Yellow Cards given per Team, rounded to the nearest integer
"""

round(discipline['Yellow Cards'].mean())

# %%
"""
question: Filter teams that scored more than 6 goals. Return the corresponding rows.
"""

euro12[euro12.Goals > 6]

# %%
"""
question: Select rows of the teams that start with G
"""

euro12[euro12.Team.str.startswith('G')]

# %%
"""
question: Select the first 7 columns
"""

# use .iloc to slices via the position of the passed integers
# : means all, 0:7 means from 0 to 7

euro12.iloc[: , 0:7]

# %%
"""
question: Select all columns except the last 3.
"""

# use negative to exclude the last 3 columns

euro12.iloc[: , :-3]

# %%
"""
question: Present only the Shooting Accuracy from England, Italy and Russia. Use Team as the index.
"""

# .loc is another way to slice, using the labels of the columns and indexes

euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']].set_index('Team')
