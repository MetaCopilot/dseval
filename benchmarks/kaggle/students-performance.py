# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/StudentsPerformance_with_headers.csv` into a variable `students`.

validator:
  namespace_check:
    students:
"""

students = pd.read_csv('inputs/StudentsPerformance_with_headers.csv')

# %%
"""
question: |
  Create a new dataframe `students_anon` by replacing the column names with "col1", "col2", ..., "col33". The first column should be "col1", the second column should be "col2", and so on.

validator:
  namespace_check:
    students_anon:
"""

students_anon = students.copy()
students_anon.columns = [f'col{i+1}' for i in range(students.shape[1])]

# %%
"""
question: |
  Calculate the Cramer's V for each pair of columns in `students_anon` (except categorical columns). Return a DataFrame with the column names as both the rows and columns. The values should be the Cramer's V between the two variables.

validator:
  result:
    ignore_order: true

execution:
  max_time: 10
"""

from scipy.stats import chi2_contingency

def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min((kcorr-1), (rcorr-1)))

numerical_columns = list(students_anon.select_dtypes(include='int64').columns)
cramers_v_table = pd.DataFrame(index=numerical_columns, columns=numerical_columns)
for col1 in numerical_columns:
    for col2 in numerical_columns:
        cramers_v_table.loc[col1, col2] = cramers_v(students_anon[col1], students_anon[col2])
cramers_v_table

# %%
"""
question: |
  Summarize the Cramer's V table by showing the top-10 pairs of variables with the highest Cramer's V. Return a DataFrame with "Variable 1", "Variable 2", and "Cramer's V" as the columns. For each pair, the first variable should be lexicographically smaller than the second variable.

validator:
  result:
    ignore_index: true
"""

# Stack the DataFrame and reset the index
cramers_v_stacked = cramers_v_table.stack().reset_index()
cramers_v_stacked.columns = ['Variable 1', 'Variable 2', "Cramer's V"]

# Remove self-pairs and duplicates
cramers_v_stacked = cramers_v_stacked[cramers_v_stacked['Variable 1'] < cramers_v_stacked['Variable 2']]

# Sort by Cramer's V and get the top 10
cramers_v_stacked.sort_values("Cramer's V", ascending=False).head(10)

# %%
"""
question: |
  Find the original column names of the top-10 pairs. Return a DataFrame with "Original Name 1", "Original Name 2" as the columns.
"""

# Get the top 10 pairs
top_10_pairs = cramers_v_stacked.sort_values("Cramer's V", ascending=False).head(10)

# Map the anonymized column names back to the original names
pd.DataFrame({
    'Original Name 1': top_10_pairs['Variable 1'].apply(lambda x: students.columns[int(x[3:]) - 1]),
    'Original Name 2': top_10_pairs['Variable 2'].apply(lambda x: students.columns[int(x[3:]) - 1]),
})

# %%
"""
question: |
  Read the description from `inputs/description.md`. Assign it to a variable `description`.

validator:
  namespace_check:
    description:
"""

with open('inputs/description.md', 'r') as f:
    description = f.read()

# %%
"""
question: |
  For each column, create the mapping from number to label according to the description. Return a dict of dicts. The keys of the outer dict should be the column names in the original CSV. The keys of the inner dicts should be the numbers and the values should be the labels. Take care of the HTML character entities inside the markdown.
  Save the mapping in a dict called `column_mapping`.

validator:
  namespace_check:
    column_mapping:
"""

import re

column_mapping = {}
for line in description.splitlines(True):
    line_match = re.match(r'([\d]+)\-.*\((.*)\)', line)
    if line_match is None:
        continue
    column_name = students.columns[int(line_match.group(1))]
    for label_match in line_match.group(2).replace(':,', ':').split(', '):
        number, label = int(label_match.split(': ')[0]), label_match.split(': ')[1].replace('&lt;', '<')
        column_mapping.setdefault(column_name, {})[number] = label

column_mapping

# %%
"""
question: |
  Apply the mapping to the original dataset. Save the result in-place in `students`.

validator:
  namespace_check:
    students:
"""

for column, mapping in column_mapping.items():
    students[column] = students[column].map(mapping)

# %%
"""
question: |
  Compute the average of student age. If the age is a range, take the average. If the age is for example "above xxx", assume the age is xxx.
"""

students['Student Age'].apply(lambda x: sum(map(int, x.split('-'))) / 2 if '-' in x else int(x.split()[-1])).mean()

# %%
"""
question: |
  Compute the pearson correlation between cumulative GPA in the last semester and Expected cumulative GPA in the graduation. Process the GPA data with a similar method as the age data.
"""

def processor(x):
    if '-' in x:
        return sum(map(float, x.split('-'))) / 2
    elif 'above' in x:
        return float(x.split()[-1])
    elif '<' in x:
        return float(x[1:])
    else:
        raise ValueError()

gpa_last_semester = students['Cumulative grade point average in the last semester (/4.00)'].apply(processor)
gpa_expected = students['Expected Cumulative grade point average in the graduation (/4.00)'].apply(processor)
gpa_last_semester.corr(gpa_expected)
