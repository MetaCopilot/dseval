# %%
import pandas as pd

# Create an example dataframe about a fictional army
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

# %%
"""
question: |
  Create a dataframe based on raw_data and assign it to a variable called army. 
  Don't forget to include the columns names in the order presented in the dictionary ('regiment', 'company', 'deaths'...) so that the column index order is consistent with the solutions. If omitted, pandas will order the columns alphabetically.

validator:
  namespace_check:
    army:
"""

army = pd.DataFrame(data=raw_data)

# %%
"""
question: Set the 'origin' column as the index of the dataframe. Modify the original dataframe.

validator:
  namespace_check:
    army:
"""

army.set_index('origin', inplace=True)

# %%
"""
question: Extract only the column veterans
"""

army.veterans

# %%
"""
question: Extract the columns 'veterans' and 'deaths'
"""

army[["veterans", "deaths"]]

# %%
"""
question: Show the name of all the columns.

validator:
  result:
    value_only: true
"""

army.columns

# %%
"""
question: Select the 'deaths', 'size' and 'deserters' columns from Maine and Alaska
"""

army.loc[["Maine", "Alaska"], ["deaths", "size", "deserters"]]

# %%
"""
question: Select the rows 3 to 7 and the columns 3 to 6
"""

army.iloc[2:7, 2:6]

# %%
"""
question: Select every row after the fourth row and all columns
"""

army.iloc[4:, :]

# %%
"""
question: Select every row up to the 4th row and all columns
"""

army.iloc[:4, :]

# %%
"""
question: Select the 3rd column up to the 7th column
"""

army.iloc[:, 2:7]

# %%
"""
question: Select rows where df.deaths is greater than 50
"""

army[army["deaths"] > 50]

# %%
"""
question: Select rows where df.deaths is greater than 500 or less than 50
"""

army[(army["deaths"] > 500) | (army["deaths"] < 50)]

# %%
"""
question: Select all the regiments not named "Dragoons"
"""

army[army["regiment"] != "Dragoons"]

# %%
"""
question: Select the rows called Texas and Arizona
"""

army.loc[["Texas", "Arizona"], :]

# %%
"""
question: Select the third cell in the row named Arizona

validator:
  result:
    value_only: true
"""

army.loc[["Arizona"]].iloc[:, 2]

# %%
"""
question: Select the third cell down in the column named deaths

validator:
  result:
    value_only: true
"""

army.loc[:, ["deaths"]].iloc[2]
