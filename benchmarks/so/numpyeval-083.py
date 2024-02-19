'''
### Prompt ###

import numpy as np

Samples = {5.207403005022627: 0.69973543384229719, 6.8970222167794759: 0.080782939731898179, 7.8338517407140973: 0.10308033284258854, 8.5301143255505334: 0.018640838362318335, 10.418899728838058: 0.14427355015329846, 5.3983946820220501: 0.51319796560976771}
# I want to separate the keys and values into 2 numpy arrays. 
keys = np.fromiter(Samples.keys(), dtype=float)
vals =

### Solution ###

 np.fromiter(Samples.values(), dtype=float)

### Test ###

def check():
    assert np.array_equal(vals, np.fromiter(Samples.values(), dtype=float))
'''

# %%
import numpy as np

Samples = {5.207403005022627: 0.69973543384229719, 6.8970222167794759: 0.080782939731898179, 7.8338517407140973: 0.10308033284258854, 8.5301143255505334: 0.018640838362318335, 10.418899728838058: 0.14427355015329846, 5.3983946820220501: 0.51319796560976771}

# %%
"""
question: |
  I want to separate the keys and values into 2 numpy arrays: keys and vals.

validator:
  namespace_check:
    vals:
"""

keys = np.fromiter(Samples.keys(), dtype=float)
vals = np.fromiter(Samples.values(), dtype=float)
