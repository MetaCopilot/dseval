'''
### Prompt ###

import numpy as np

a = np.arange(0,10)
# How to print a Numpy array without brackets?
# For example, I want to convert a = np.array([1,2,3,4,5]) into a_string = "1 2 3 4 5".
a_string =

### Solution ###

 " ".join(str(i) for i in a)

### Test ###

def check():
    assert a_string == "0 1 2 3 4 5 6 7 8 9"
'''

# %%
import numpy as np

a = np.arange(0,10)

# %%
"""
question: |
  How to print a Numpy array without brackets?
  For example, I want to convert a = np.array([1,2,3,4,5]) into a_string = "1 2 3 4 5".
"""

" ".join(str(i) for i in a)
