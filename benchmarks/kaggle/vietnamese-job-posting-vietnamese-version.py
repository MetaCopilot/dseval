# %%
import pandas as pd
import numpy as np
import re

# %%
"""
question: |
  Read the file `inputs/vietnamese-job-posting.csv` into a variable `jobs`.

validator:
  namespace_check:
    jobs:
"""

jobs = pd.read_csv('inputs/vietnamese-job-posting.csv')

# %%
"""
question: |
  List out the job titles that have appeared more than once.

validator:
  result:
    ignore_order: true
"""

jobs['job_title'].value_counts().loc[lambda x: x > 1].index.tolist()

# %%
"""
question: |
  Extract the numeric part from the 'salary' column and create a new column 'salary_numeric'. If the salary is a range, take the average. If the salary is not available, fill it with the mean salary. The salary should be measured by millions of VND.

validator:
  namespace_check:
    jobs:
"""

def salary_to_numeric(salary):
    match = re.search(r'([\d,]+) Tr - ([\d,]+) Tr', salary)
    if match is not None:
        return (float(match.group(1).replace(',', '.')) + float(match.group(2).replace(',', '.'))) / 2
    match = re.search(r'Trên ([\d,]+) Tr', salary)
    if match is not None:
        return float(match.group(1).replace(',', '.'))
    match = re.search(r'Dưới([\d,]+) Tr', salary)
    if match is not None:
        return float(match.group(1).replace(',', '.'))
    if salary == 'Lương: Cạnh tranh':
        return float('nan')
    raise ValueError(f'Invalid salary: {salary}')

# Extract numeric part from salary
salary_numeric = jobs['salary'].map(salary_to_numeric)

# Fill missing values with mean salary
salary_numeric = salary_numeric.fillna(salary_numeric.mean())

jobs['salary_numeric'] = salary_numeric

# %%
"""
question: |
  Convert 'announcement_date' and 'expiration_date' columns to pandas datetime format. Save the converted columns in-place.

validator:
  namespace_check:
    jobs:
"""

jobs['announcement_date'] = pd.to_datetime(jobs['announcement_date'].str.strip(), dayfirst=True)
jobs['expiration_date'] = pd.to_datetime(jobs['expiration_date'].str.strip(), dayfirst=True)

# %%
"""
question: |
  Create a new feature 'days_open' which is calculated as the difference between 'expiration_date' and 'announcement_date'.

validator:
  namespace_check:
    jobs:
"""

jobs['days_open'] = (jobs['expiration_date'] - jobs['announcement_date']).dt.days

# %%
"""
question: |
  List out the top-10 job titles with the highest average 'days_open'.

validator:
  result:
    ignore_order: true
"""

jobs.groupby('job_title')['days_open'].mean().nlargest(10).index.tolist()

# %%
"""
question: |
  Analyze the appearance count of different locations. If a job has multiple locations, count each of them. Sorting them in descending order.

validator:
  result:
    ignore_index: true
"""

jobs['location'].str.split(' | ', regex=False).explode().value_counts()

# %%
"""
question: |
  Use regular expressions ("\d+ năm") to extract the required experience years from the 'job_requirements' column. If there are multiple matches, use the first one. Save the result in a new numerical column 'experience_required'.

validator:
  namespace_check:
    jobs:
"""

def extract_experience_years(text):
    if pd.isna(text):
        return float('nan')
    match = re.search(r'(\d+) năm', text)
    if match is not None:
        return float(match.group(1))
    return float('nan')

experience_required = jobs['job_requirements'].map(extract_experience_years)
jobs['experience_required'] = experience_required

# %%
"""
question: |
  Count the number of records with different 'experience_required' levels. The levels are defined as follows:
  - "Entry Level": experience_required <= 1
  - "Intermediate": 1 < experience_required <= 3
  - "Senior": 3 < experience_required <= 5
  - "Expert": experience_required > 5
  - "Unspecified": experience_required is NaN
  Present the results in a Series with the levels as the index and the counts as the values in the descending order.

validator:
  result:
    ignore_index: true
"""

experience_levels = pd.cut(jobs['experience_required'], bins=[-np.inf, 1, 3, 5, np.inf], labels=['Entry Level', 'Intermediate', 'Senior', 'Expert'])
experience_levels = experience_levels.cat.add_categories('Unspecified').fillna('Unspecified')
experience_levels.value_counts()

# %%
"""
question: |
  Drop columns containing HTMLs. Save the cleaned dataset in-place.

validator:
  namespace_check:
    jobs:
"""

html_columns = ['job_description', 'job_requirements', 'other_info']
jobs = jobs.drop(columns=html_columns)
