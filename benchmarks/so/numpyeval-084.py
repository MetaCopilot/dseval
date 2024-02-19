'''
### Prompt ###

import numpy as np

a = np.array([0 +  0.5j, 0.25 + 1.2352444e-24j, 0.25+ 0j, 2.46519033e-32 + 0j])
tol = 1e-16
# what is the fastest and easiest way to set the super low value named tol to zero?
# Handling of real and imaginary numbers separately
a.real[np.abs(a.real) < tol] = 0

### Solution ###

a.imag[np.abs(a.imag) < tol] = 0

### Test ###

def check():
    assert np.array_equal(a, np.array([0 +  0.5j, 0.25 + 0j, 0.25+ 0j, 0 + 0j]))
'''

# %%
import numpy as np

a = np.array([0 +  0.5j, 0.25 + 1.2352444e-24j, 0.25+ 0j, 2.46519033e-32 + 0j])
tol = 1e-16

# %%
"""
question: |
  what is the fastest and easiest way to set the super low value named tol to zero?
  Handling of real and imaginary numbers separately
  Modify the array `a` in-place.

validator:
  namespace_check:
    a:
"""

a.real[np.abs(a.real) < tol] = 0
a.imag[np.abs(a.imag) < tol] = 0
