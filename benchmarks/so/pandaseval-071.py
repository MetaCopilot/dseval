'''
### Prompt ###

import numpy as np
import pandas as pd
df = pd.DataFrame(
    {"x": np.arange(1_000 * 100), "section": np.repeat(np.arange(100), 1_000)}
)

# Say i have a dataframe with 100,000 entries and want to split it into 100 sections of 1000 entries.
# How do i take a random sample of say size 50 of just one of the 100 sections. 
# the data set is already ordered such that the first 1000 results are the first section the next section the next and so on.
# You could add a "section" column to your data then perform a groupby and sample(n=50):
sample =

### Solution ###

 df.groupby("section").sample(n=50)

### Test ###

def check():
    assert sample.shape == (5000, 2)
'''

# %%
import numpy as np
import pandas as pd

df = pd.DataFrame(
    {"x": np.arange(1_000 * 100), "section": np.repeat(np.arange(100), 1_000)}
)

# %%

"""
question: |
  Say i have a dataframe with 100,000 entries and want to split it into 100 sections of 1000 entries.
  How do i take a random sample of say size 50 for each of the 100 sections. 

validator:
  result: |
    def compare_fn(ref, sub):
      if ref.shape != sub.shape:
        return {"match": False, "reason": f"Shape: {ref.shape} vs {sub.shape}"}
      if ref['section'].sort_values().tolist() != sub['section'].sort_values().tolist():
        return {"match": False, "reason": f"Sections mismatch"}
      return {"match": True, "reason": ""}
"""

df.groupby("section").sample(n=50)
