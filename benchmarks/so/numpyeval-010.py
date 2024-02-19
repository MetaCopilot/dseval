'''
### Prompt ###

import numpy as np

a = np.arange(2*3*2).reshape((2,3,2))
# How to count values in a certain range in a Numpy array?
# the number of elements fulfilling 2 < x < 8 is:
count_value =

### Solution ###

 ((2 < a) & (a < 8)).sum()

### Test ###

def check():
    assert count_value == 5
'''

# %%
import numpy as np

a = np.arange(2*3*2).reshape((2,3,2))

# %%
"""
question: |
  How to count values in a certain range in a Numpy array?
  the number of elements fulfilling 2 < x < 8 is:
"""

((2 < a) & (a < 8)).sum()
