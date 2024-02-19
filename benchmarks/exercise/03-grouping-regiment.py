# %%
import pandas as pd
import numpy as np

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

# %%
"""
question: |
  Create the DataFrame with raw_data.
  Assign it to a variable called regiment.
  Don't forget to name each column

validator:
  namespace_check:
    regiment:
"""
regiment = pd.DataFrame(raw_data)

# %%
"""
question: What is the mean preTestScore from the regiment Nighthawks?
"""

regiment.groupby('regiment').mean(numeric_only=True).loc['Nighthawks', 'preTestScore']

# %%
"""
question: Describe the general statistics grouped by company
"""

regiment.groupby('company').describe()

# %%
"""
question: What is the mean of each company's preTestScore?
"""

regiment.groupby('company').mean(numeric_only=True)['preTestScore']

# %%
"""
question: Present the mean preTestScores grouped by regiment and company
"""

regiment.groupby(['regiment', 'company']).mean(numeric_only=True)['preTestScore']

# %%
"""
question: Present the mean preTestScores grouped by regiment and company without hierarchical indexing (please put regiment on the row and company on the column)
"""

regiment.groupby(['regiment', 'company']).mean(numeric_only=True)['preTestScore'].unstack()

# %%
"""
question: Group the entire dataframe by regiment and company
"""

regiment.groupby(['regiment', 'company']).mean(numeric_only=True)

# %%
"""
question: What is the number of observations in each regiment and company
"""

regiment.groupby(['regiment', 'company']).size()

# %%
"""
question: Iterate over a group and, for each group, print the name in a line and the dataframe from the regiment. Don't print extra empty lines after each group.

validator:
  output:
"""

for name, group in regiment.groupby('regiment'):
    print(name)
    print(group)
