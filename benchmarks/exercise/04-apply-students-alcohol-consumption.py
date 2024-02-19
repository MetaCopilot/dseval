# %%
import pandas as pd
import numpy

# %%
"""
question: |
  Import the dataset from this [address](inputs/student-mat.csv).
  Assign it to a variable called df.
  Show the first rows of the dataset.

validator:
  namespace_check:
    df:

data:
  student-mat.csv: https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv
"""

csv_url = 'inputs/student-mat.csv'
df = pd.read_csv(csv_url)
df.head()

# %%
"""
question: Slice the dataframe from 'school' until the 'guardian' column. Save it as stud_alcoh

validator:
  namespace_check:
    stud_alcoh:
"""

stud_alcoh = df.loc[: , "school":"guardian"]

# %%
"""
question: Capitalize both Mjob and Fjob. Modify in-place.

validator:
  namespace_check:
    stud_alcoh:
"""

capitalizer = lambda x: x.capitalize()
stud_alcoh['Mjob'].apply(capitalizer)
stud_alcoh['Fjob'].apply(capitalizer)

# %%
"""
question: Show the last elements of the data set.
"""

stud_alcoh.tail()

# %%
"""
question: Create a function called majority that returns a boolean value (Consider majority as older than 17 years old). Save it to stud_alcoh as a new column called legal_drinker.

validator:
  namespace_check:
    stud_alcoh:
"""

def majority(x):
    if x > 17:
        return True
    else:
        return False

stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)

# %%
"""
question: |
  Multiply every number of the dataset by 10. 
  I know this makes no sense, don't forget it is just an exercise.
"""

def times10(x):
    if type(x) is int:
        return 10 * x
    return x

stud_alcoh.applymap(times10)

