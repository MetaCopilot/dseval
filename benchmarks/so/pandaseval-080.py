'''
### Prompt ###

import pandas as pd
import numpy as np
def ceil_of_series(s):
    # ceiling of a pandas series
    # Return the result.

### Solution ###

    return np.ceil(s)

### Test ###

def check(candidate):
    assert candidate(pd.Series([1.2, 2.3, 3.4, 4.5, 5.6])).equals(pd.Series([2, 3, 4, 5, 6]).astype(float))
    assert candidate(pd.Series([1.1, 2.3, 3.4, 4.5, 5.6])).equals(pd.Series([2, 3, 4, 5, 6]).astype(float))
    assert candidate(pd.Series([1.2, 2.4, 3.4, 4.5, 5.6])).equals(pd.Series([2, 3, 4, 5, 6]).astype(float))
    assert candidate(pd.Series([1.2, 2.3, 3.2, 4.5, 5.6])).equals(pd.Series([2, 3, 4, 5, 6]).astype(float))
    assert candidate(pd.Series([1.2, 2.3, 3.4, 4.2, 5.6])).equals(pd.Series([2, 3, 4, 5, 6]).astype(float))
    assert candidate(pd.Series([1.2, 2.3, 3.4, 4.5, 5.1])).equals(pd.Series([2, 3, 4, 5, 6]).astype(float))
    assert candidate(pd.Series([1.2, 2.3, 3.4, 4.4, 5.6])).equals(pd.Series([2, 3, 4, 5, 6]).astype(float))
    assert candidate(pd.Series([1.2, 2.3, 3.4, 4.5, 5.2])).equals(pd.Series([2, 3, 4, 5, 6]).astype(float))
    assert candidate(pd.Series([1.4, 2.3, 3.4, 4.5, 5.6])).equals(pd.Series([2, 3, 4, 5, 6]).astype(float))
    assert candidate(pd.Series([1.2, 2.1, 3.4, 4.1, 5.6])).equals(pd.Series([2, 3, 4, 5, 6]).astype(float))
'''

# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Write a function `def ceil_of_series(s):` that takes a pandas Series and returns a pandas Series to solve the following problem:
  ceiling of a pandas series

validator:
  table_test:
    function_name: ceil_of_series
    test_cases:
    - ["`pd.Series([1.2, 2.3, 3.4, 4.5, 5.6])`"]
    - ["`pd.Series([1.1, 2.3, 3.4, 4.5, 5.6])`"]
    - ["`pd.Series([1.2, 2.4, 3.4, 4.5, 5.6])`"]
    - ["`pd.Series([1.2, 2.3, 3.2, 4.5, 5.6])`"]
    - ["`pd.Series([1.2, 2.3, 3.4, 4.2, 5.6])`"]
    - ["`pd.Series([1.2, 2.3, 3.4, 4.5, 5.1])`"]
    - ["`pd.Series([1.2, 2.3, 3.4, 4.4, 5.6])`"]
    - ["`pd.Series([1.2, 2.3, 3.4, 4.5, 5.2])`"]
    - ["`pd.Series([1.4, 2.3, 3.4, 4.5, 5.6])`"]
    - ["`pd.Series([1.2, 2.1, 3.4, 4.1, 5.6])`"]
"""

def ceil_of_series(s):
    return np.ceil(s)
