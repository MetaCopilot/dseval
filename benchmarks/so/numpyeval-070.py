'''
### Prompt ###

import numpy as np

dat = np.array([[1,2,3], [4,5,np.nan], [np.nan,6,np.nan]])
mdat = np.ma.masked_array(dat,np.isnan(dat))
# How can I calculate matrix mean values along the row of matrix, but to remove nan values from calculation?
# If all row values is NaNs, the mean value is set to NaN.
mm =

### Solution ###

 np.mean(mdat,axis=1).filled(np.nan)

### Test ###

def check():
    assert np.array_equal(mm, np.array([2., 4.5, 6.]))
'''

# %%
import numpy as np

dat = np.array([[1,2,3], [4,5,np.nan], [np.nan,6,np.nan]])
mdat = np.ma.masked_array(dat,np.isnan(dat))

# %%
"""
question: |
  How can I calculate matrix mean values along the row of matrix, but to remove nan values from calculation?
  If all row values is NaNs, the mean value is set to NaN.
"""

np.mean(mdat,axis=1).filled(np.nan)
