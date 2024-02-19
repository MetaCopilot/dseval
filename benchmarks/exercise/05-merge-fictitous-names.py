# %%
import pandas as pd

raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

# %%
"""
question: |
  Create the 3 DataFrames based on raw_data_1, raw_data_2 and raw_data_3.
  Assign each to a variable called data1, data2, data3

validator:
  namespace_check:
    data1:
    data2:
    data3:
"""

data1 = pd.DataFrame(raw_data_1, columns = ['subject_id', 'first_name', 'last_name'])
data2 = pd.DataFrame(raw_data_2, columns = ['subject_id', 'first_name', 'last_name'])
data3 = pd.DataFrame(raw_data_3, columns = ['subject_id','test_id'])

# %%
"""
question: Join the two dataframes data1 and data2 along rows, and assign to all_data

validator:
  namespace_check:
    all_data:
"""

all_data = pd.concat([data1, data2])

# %%
"""
question: Join the two dataframes along columns and assign to all_data_col

validator:
  namespace_check:
    all_data_col:
"""

all_data_col = pd.concat([data1, data2], axis = 1)

# %%
"""
question: Merge all_data and data3 along the subject_id value
"""

pd.merge(all_data, data3, on='subject_id')

# %%
"""
question: Merge only the data that has the same 'subject_id' on both data1 and data2
"""

pd.merge(data1, data2, on='subject_id', how='inner')

# %%
"""
question: Merge all values in data1 and data2, with matching records from both sides where available.
"""

pd.merge(data1, data2, on='subject_id', how='outer')
