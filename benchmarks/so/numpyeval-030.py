'''
### Prompt ###

import numpy as np

a = np.zeros(4,dtype="float64")
# Convert numpy array type and values from Float64 to Float32
b =

### Solution ###

 a.astype("float32")

### Test ###

def check():
    assert np.array_equal(b, np.zeros(4,dtype="float32"))
    assert b.dtype == np.dtype("float32")
'''

# %%
import numpy as np

a = np.zeros(4,dtype="float64")

# %%

"""
question: |
  Convert numpy array type and values from Float64 to Float32

validator:
  result:
    strict_type: true
"""

a.astype("float32")
