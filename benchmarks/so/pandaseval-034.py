'''
### Prompt ###

import pandas as pd

def append_dict_to_df(df, dictionary):
    # append dictionary to data frame
    # return the data frame

### Solution ###

    df = df.append(dictionary, ignore_index=True)
    return df

### Test ###

def check(candidate):
    assert candidate(pd.DataFrame(), {'B': 100, 'C': 200}).equals(pd.DataFrame({'B': [100.0], 'C': [200.0]}))
    assert candidate(pd.DataFrame(), {'B': 110, 'C': 200}).equals(pd.DataFrame({'B': [110.0], 'C': [200.0]}))
    assert candidate(pd.DataFrame(), {'B': 120, 'C': 200}).equals(pd.DataFrame({'B': [120.0], 'C': [200.0]}))
    assert candidate(pd.DataFrame(), {'B': 150, 'C': 200}).equals(pd.DataFrame({'B': [150.0], 'C': [200.0]}))
    assert candidate(pd.DataFrame(), {'B': 150, 'C': 220}).equals(pd.DataFrame({'B': [150.0], 'C': [220.0]}))
    assert candidate(pd.DataFrame(), {'B': 154, 'C': 220}).equals(pd.DataFrame({'B': [154.0], 'C': [220.0]}))
    assert candidate(pd.DataFrame(), {'B': 164, 'C': 220}).equals(pd.DataFrame({'B': [164.0], 'C': [220.0]}))
    assert candidate(pd.DataFrame(), {'B': 164, 'C': 240}).equals(pd.DataFrame({'B': [164.0], 'C': [240.0]}))
    assert candidate(pd.DataFrame(), {'B': 164, 'C': 244}).equals(pd.DataFrame({'B': [164.0], 'C': [244.0]}))
    assert candidate(pd.DataFrame(), {'B': 184, 'C': 244}).equals(pd.DataFrame({'B': [184.0], 'C': [244.0]}))
'''

# %%
import pandas as pd

# %%
"""
question: |
  Write a function `def append_dict_to_df(df, dictionary):` that takes a DataFrame and a dictionary and returns a DataFrame to solve the following problem:
  append dictionary to data frame

validator:
  table_test:
    function_name: append_dict_to_df
    test_cases:
    - ["`pd.DataFrame()`", {'B': 100, 'C': 200}]
    - ["`pd.DataFrame()`", {'B': 110, 'C': 200}]
    - ["`pd.DataFrame()`", {'B': 120, 'C': 200}]
    - ["`pd.DataFrame()`", {'B': 150, 'C': 200}]
    - ["`pd.DataFrame()`", {'B': 150, 'C': 220}]
    - ["`pd.DataFrame()`", {'B': 154, 'C': 220}]
    - ["`pd.DataFrame()`", {'B': 164, 'C': 220}]
    - ["`pd.DataFrame()`", {'B': 164, 'C': 240}]
    - ["`pd.DataFrame()`", {'B': 164, 'C': 244}]
    - ["`pd.DataFrame()`", {'B': 184, 'C': 244}]
"""

def append_dict_to_df(df, dictionary):
    return pd.concat([df, pd.DataFrame([dictionary])], ignore_index=True)
