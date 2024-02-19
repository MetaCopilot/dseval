'''
### Prompt ###

import numpy as np

a = np.array([0,33,4444522])
# Converting int arrays to string arrays in numpy without truncation
a_str =

### Solution ###

 np.array([str(x) for x in a])

### Test ###

def check():
    assert np.array_equal(a_str, np.array([str(x) for x in a]))
'''

# %%
import numpy as np

a = np.array([0,33,4444522])

# %%

"""
question: |
  Converting int arrays to string arrays in numpy without truncation
"""

np.array([str(x) for x in a])
