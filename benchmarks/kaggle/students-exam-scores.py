# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Import the dataset from `inputs/Expanded_data_with_more_features.csv`. Assign it to a variable called `students`.
  Drop the unnamed columns.

validator:
  namespace_check:
    students:
"""

students = pd.read_csv('inputs/Expanded_data_with_more_features.csv').drop(columns='Unnamed: 0')

# %%
"""
question: |
  Analyze the relationship between parent education and math score, reading score, and writing score.
  Sort the education level from lowest to highest. Return a DataFrame with "ParentEduc" as the index and "MathScore", "ReadingScore", "WritingScore" as the columns.
"""

education_order = ['some high school', 'high school', 'some college', 'associate\'s degree', 'bachelor\'s degree', 'master\'s degree']
students.groupby('ParentEduc')[['MathScore', 'ReadingScore', 'WritingScore']].mean().loc[education_order]

# %%
"""
question: |
  Count the size of each ethnic group.
"""

students['EthnicGroup'].value_counts()

# %%
"""
question: |
  Detect the outliers in math score using the IQR method. Return a DataFrame with the same columns as the original dataset and only the rows that are outliers.

validator:
  namespace_check:
    outliers:
"""

Q1 = students['MathScore'].quantile(0.25)
Q3 = students['MathScore'].quantile(0.75)
IQR = Q3 - Q1

outliers = students[(students['MathScore'] < Q1 - 1.5 * IQR) | (students['MathScore'] > Q3 + 1.5 * IQR)]

outliers

# %%
"""
question: |
  Compute the mutual correlation among math, reading and writing scores. Return a DataFrame with "MathScore", "ReadingScore", "WritingScore" as both the rows and columns.
"""

students[['MathScore', 'ReadingScore', 'WritingScore']].corr()

# %%
"""
question: |
  Count the number of students for each number of siblings (from 0 to 4).
"""

students['NrSiblings'].value_counts().rename('Count').sort_index().loc[0:4]

# %%
"""
question: |
  Create a new feature 'TotalScore' which is the sum of 'MathScore', 'ReadingScore', and 'WritingScore'.
  Save the new feature in-place.

validator:
  namespace_check:
    students:
"""

students['TotalScore'] = students['MathScore'] + students['ReadingScore'] + students['WritingScore']

# %%
"""
question: |
  Analyze the Kendall's tau correlation between weekly study hours and the total score.
  Assuming less than 5 hours is 2.5, 5-10 hours is 7.5 and more than 10 hours is 15.
  Return the correlation coefficient.
"""

study_hours_mapping = {'< 5': 2.5, '5 - 10': 7.5, '> 10': 15}
students['WklyStudyHours'].replace(study_hours_mapping).corr(students['TotalScore'], method='kendall')

# %%
"""
question: |
  Create a new feature 'IsTopPerformer' which indicates if a student's 'TotalScore' is within the top 25% of the dataset.
  Save the new feature in-place.

validator:
  namespace_check:
    students:
"""

students['IsTopPerformer'] = students['TotalScore'] >= students['TotalScore'].quantile(0.75)

# %%
"""
question: |
  Import the dataset from `inputs/Original_data_with_more_rows.csv`. Assign it to a variable called `students_original`.
  Drop the unnamed columns.

validator:
  namespace_check:
    students_original:
"""

students_original = pd.read_csv('inputs/Original_data_with_more_rows.csv').drop(columns='Unnamed: 0')

# %%
"""
question: |
  Merge the data with more features with the data with more rows. Use an inner join on the index. Rename the columns of the original dataset by adding the suffix `_original`.
  Save the merged dataset in-place in `students_merged`.

validator:
  namespace_check:
    students_merged:
"""

students_merged = students.merge(students_original, left_index=True, right_index=True, suffixes=('', '_original'))

# %%
"""
question: |
  Check whether the two datasets can be perfectly matched. Show the rows in `students_merged` that can be matched.
"""

columns = students_original.columns
students1 = students_merged[columns]
students2 = students_merged[[column + '_original' for column in columns]].rename(columns={column + '_original': column for column in columns})
students_merged[((students1 == students2) | (students1.isna() & students2.isna())).all(axis=1)]
