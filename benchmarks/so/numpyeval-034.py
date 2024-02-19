'''
### Prompt ###

import numpy as np

y = np.array([2,1,5,2])          # y axis
# filter out values larger than 2
m = np.ma.masked_where(y>2, y)   
# remove masked values from m
out =

### Solution ###

 m.compressed()

### Test ###

def check():
    assert np.array_equal(out, np.array([2,1,2]))
'''

# %%
import numpy as np

y = np.array([2,1,5,2])          # y axis
m = np.ma.masked_where(y>2, y)   # filter out values larger than 2

# %%
"""
question: |
  Remove masked values from m
"""

m.compressed()
