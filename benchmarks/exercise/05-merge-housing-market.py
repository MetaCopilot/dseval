# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  First create a numpy random state with seed 123 and save it to a variable called rng.
  Use the random state to create 3 different Series, each of length 100, as follows: 
  1. Variable s1: The first a random number from 1 to 4 
  2. Variable s2: The second a random number from 1 to 3
  3. Variable s3: The third a random number from 10,000 to 30,000
  The data type of all three should be int64.

validator:
  namespace_check:
    s1:
    s2:
    s3:
"""

rng = np.random.RandomState(123)
s1 = pd.Series(rng.randint(1, high=5, size=100, dtype='l'))
s2 = pd.Series(rng.randint(1, high=4, size=100, dtype='l'))
s3 = pd.Series(rng.randint(10000, high=30001, size=100, dtype='l'))

# %%
"""
question: |
  Let's create a DataFrame by joinning the Series by column
  The name of the columns should be bedrs, bathrs, price_sqr_meter.
  Save the result to a variable called housemkt
"""

housemkt = pd.concat([s1, s2, s3], axis=1)
housemkt.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'}, inplace=True)

# %%
"""
question: Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'

validator:
  namespace_check:
    bigcolumn:
"""

# join concat the values
bigcolumn = pd.concat([s1, s2, s3], axis=0)

# it is still a Series, so we need to transform it to a DataFrame
bigcolumn = bigcolumn.to_frame()

# %%
"""
question: Oops, it seems it is going only until index 99. Is it true?
"""

# no the index are kept but the length of the DataFrame is 300
len(bigcolumn) == 100

# %%
"""
question: Reindex the DataFrame so it goes from 0 to 299

validator:
  namespace_check:
    bigcolumn:
"""

bigcolumn.reset_index(drop=True, inplace=True)
