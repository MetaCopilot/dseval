# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Import the first dataset [cars1](inputs/cars1.csv) and [cars2](inputs/cars2.csv).
  Assign each to a to a variable called cars1 and cars2

validator:
  namespace_check:
    cars1:
    cars2:

data:
  cars1.csv: https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv
  cars2.csv: https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv
"""

cars1 = pd.read_csv("inputs/cars1.csv")
cars2 = pd.read_csv("inputs/cars2.csv")

# %%
"""
question: Oops, it seems our first dataset has some unnamed blank columns, fix cars1

validator:
  namespace_check:
    cars1:
"""

cars1 = cars1.loc[:, "mpg":"car"]

# %%
"""
question: What is the number of observations in each dataset? Return the answers as a tuple.
"""

cars1.shape[0], cars2.shape[0]

# %%
"""
question: Join cars1 and cars2 into a single DataFrame called cars

validator:
  namespace_check:
    cars:
      ignore_index: true
"""

cars = pd.concat([cars1, cars2])

# %%
"""
question: Oops, there is a column missing, called owners. Create a random number Series from 15,000 to 73,000. Use numpy random's randint function to generate this Series, with seed 0. Save this to a column of cars called owners.

validator:
  namespace_check:
    cars:
"""

cars['owners'] = np.random.RandomState(0).randint(15000, high=73001, size=398, dtype='l')
