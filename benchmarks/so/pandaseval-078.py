'''
### Prompt ###

import pandas as pd
import numpy as np

df = pd.DataFrame({'mycol':np.arange(5), 'dummy':np.arange(5)})
# I find myself often having to check whether a column or row exists in a dataframe before trying to reference it.
# Is there any way to do this more nicely? 
# For example on an arbitrary object I can do x = getattr(anobject, 'id', default) - is there anything similar to this in pandas? Really any way to achieve what I'm doing more gracefully?
# Output the second row of data in `mycol` column if it exists, otherwise output NaN
value =

### Solution ###

 df.mycol.get(1, np.nan)

### Test ###

def check():
    assert value == 1
'''

# %%
import pandas as pd
import numpy as np

df = pd.DataFrame({'mycol':np.arange(5), 'dummy':np.arange(5)})

# %%
"""
question: |
  I find myself often having to check whether a column or row exists in a dataframe before trying to reference it.
  Is there any way to do this more nicely? 
  For example on an arbitrary object I can do x = getattr(anobject, 'id', default) - is there anything similar to this in pandas? Really any way to achieve what I'm doing more gracefully?
  Output the second row of data in `mycol` column if it exists, otherwise output NaN
"""

df.mycol.get(1, np.nan)
