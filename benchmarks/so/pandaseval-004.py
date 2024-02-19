'''
### Prompt ###

import pandas as pd

def get_data_frame_from_list(list_of_lists):
    # list_of_lists format: [header, [row1], [row2], ...]
    # header format: [column1, column2, ...]
    # row format: [value1, value2, ...]
    # How to convert list to dataframe?
    # Return the dataframe

### Solution ###

    return pd.DataFrame(list_of_lists[1:], columns=list_of_lists[0])

### Test ###

def check(candidate):
    assert candidate([['Heading1', 'Heading2'], [1 , 2], [3, 4]]).equals(pd.DataFrame([[1, 2], [3, 4]], columns=['Heading1', 'Heading2']))
    assert candidate([['Heading1', 'Heading3'], [1 , 2], [3, 4]]).equals(pd.DataFrame([[1, 2], [3, 4]], columns=['Heading1', 'Heading3']))
    assert candidate([['Heading2', 'Heading3'], [1 , 2], [3, 4]]).equals(pd.DataFrame([[1, 2], [3, 4]], columns=['Heading2', 'Heading3']))
    assert candidate([['Heading2', 'Heading3'], [2 , 2], [3, 4]]).equals(pd.DataFrame([[2, 2], [3, 4]], columns=['Heading2', 'Heading3']))
    assert candidate([['Heading5', 'Heading3'], [1 , 2], [3, 4]]).equals(pd.DataFrame([[1, 2], [3, 4]], columns=['Heading5', 'Heading3']))
    assert candidate([['Heading2', 'Heading9'], [1 , 2], [3, 4]]).equals(pd.DataFrame([[1, 2], [3, 4]], columns=['Heading2', 'Heading9']))
    assert candidate([['Heading2', 'Heading3'], [11 , 12], [3, 4]]).equals(pd.DataFrame([[11, 12], [3, 4]], columns=['Heading2', 'Heading3']))
    assert candidate([['Heading22', 'Heading32'], [1 , 2], [3, 4]]).equals(pd.DataFrame([[1, 2], [3, 4]], columns=['Heading22', 'Heading32']))
    assert candidate([['Heading2', 'Heading3'], [14 , 42], [3, 4]]).equals(pd.DataFrame([[14, 42], [3, 4]], columns=['Heading2', 'Heading3']))
    assert candidate([['Heading2', 'Heading3'], [1 , 23], [33, 4]]).equals(pd.DataFrame([[1, 23], [33, 4]], columns=['Heading2', 'Heading3']))
'''

# %%
import pandas as pd

# %%

"""
question: |
  Write a function `def get_data_frame_from_list(list_of_lists):` that takes a list of lists and returns a DataFrame to solve the following problem:
  list_of_lists format: [header, [row1], [row2], ...]
  header format: [column1, column2, ...]
  row format: [value1, value2, ...]
  How to convert list to dataframe?

validator:
  table_test:
    function_name: get_data_frame_from_list
    test_cases:
    - [[['Heading1', 'Heading2'], [1 , 2], [3, 4]]]
    - [[['Heading1', 'Heading3'], [1 , 2], [3, 4]]]
    - [[['Heading2', 'Heading3'], [1 , 2], [3, 4]]]
    - [[['Heading2', 'Heading3'], [2 , 2], [3, 4]]]
    - [[['Heading5', 'Heading3'], [1 , 2], [3, 4]]]
    - [[['Heading2', 'Heading9'], [1 , 2], [3, 4]]]
    - [[['Heading2', 'Heading3'], [11 , 12], [3, 4]]]
    - [[['Heading22', 'Heading32'], [1 , 2], [3, 4]]]
    - [[['Heading2', 'Heading3'], [14 , 42], [3, 4]]]
    - [[['Heading2', 'Heading3'], [1 , 23], [33, 4]]]
"""

def get_data_frame_from_list(list_of_lists):
    return pd.DataFrame(list_of_lists[1:], columns=list_of_lists[0])
