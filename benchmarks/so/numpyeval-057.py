'''
### Prompt ###

import numpy as np

n = 2
a = np.asarray([1,2,3,4,5])
cond = (a % 2) == 0  #condition is True on even numbers
# I have an array a and I would like to repeat the elements of a n times if they are even or if they are positive. 
# I mean I want to repeat only the elements that respect some condition, other elements are not displayed.
# In detail, if a meets the condition cond, I want to repeat it n times. 
m =

### Solution ###

 np.repeat(a[cond], n)

### Test ###

def check():
    assert np.array_equal(m, np.array([2, 2, 4, 4]))
'''

# %%
import numpy as np

n = 2
a = np.asarray([1,2,3,4,5])
cond = (a % 2) == 0  #condition is True on even numbers

# %%
"""
question: |
  I have an array a and I would like to repeat the elements of a n times if they are even or if they are positive. 
  I mean I want to repeat only the elements that respect some condition, other elements are not displayed.
  In detail, if a meets the condition cond, I want to repeat it n times. 
"""

np.repeat(a[cond], n)
