# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/Salary_Data.csv` into a variable `salary`.

validator:
  namespace_check:
    salary:
"""

salary = pd.read_csv('inputs/Salary_Data.csv')

# %%
"""
question: |
  Remove the rows that contain null fields. Save the cleaned dataset in-place.

validator:
  namespace_check:
    salary:
"""

salary = salary.dropna()

# %%
"""
question: |
  Clean the "Education Level" column by unifying the inconsistent values. For example, "Bachelor's" and "Bachelor's Degree" should be considered "Bachelor".
  The cleaned values should be one of "Bachelor", "Master", "PhD", "High School". Save the cleaned dataset in-place.

validator:
  namespace_check:
    salary:
"""

def unify_education_level(s):
    for e in ['Bachelor', 'Master', 'PhD']:
        if e.lower() in s.lower(): return e
    return s
salary['Education Level'] = salary['Education Level'].map(unify_education_level)

# %%
"""
question: |
  Check the number of duplicated entries.
"""

salary.duplicated().sum()

# %%
"""
question: |
  Put the top 3 popular job titles in a single list.

validator:
  result:
    ignore_order: true
"""

salary['Job Title'].value_counts().head(3).index.tolist()

# %%
"""
question: |
  Compute the average salary for each degree. Sort the degrees from low to high based on the average salary. Return a Series with "Degree" as the index and "Average Salary" as the values.
"""

salary.groupby('Education Level')['Salary'].mean().sort_values().rename('Average Salary').rename_axis('Degree')

# %%
"""
question: |
  Compute the correlation between salary and age and YoE.
  Output a dict `{ "Age": <correlation with age>, "YoE": <correlation with YoE> }`.
"""

{
    'Age': salary['Salary'].corr(salary['Age']),
    'YoE': salary['Salary'].corr(salary['Years of Experience'])
}

# %%
"""
question: |
  Compute the correlation between salary and age under the same YoE. Return a DataFrame with "YoE" and "Correlation" as the columns.
"""

pd.DataFrame({
    'YoE': YoE,
    'Correlation': group['Salary'].corr(group['Age'])
} for YoE, group in salary.groupby('Years of Experience'))

# %%
"""
question: |
  Show the most popular 10 jobs and the salary range of these jobs in the decreasing order of the median of salary. Return a DataFrame with "Job Title" as the index and "Count", "Min Salary", "Max Salary", "Median Salary" as the columns.
"""

popular_jobs = salary['Job Title'].value_counts().head(10).index
job_stats = salary.groupby('Job Title').agg({'Salary': ['count', 'min', 'max', 'median']}).loc[popular_jobs]
job_stats.columns = ['Count', 'Min Salary', 'Max Salary', 'Median Salary']
job_stats = job_stats.sort_values(by='Median Salary', ascending=False)

job_stats

# %%
"""
question: |
  Compute the growth rates of salary with respect to the education level. The growth rate is defined as the percentage increase (0-1) in the average salary when moving up one education level. Show a list of tuple `(from, to, growth rate)` sorted by the growth rate in descending order.
"""

education_order = ['High School', 'Bachelor', 'Master', 'PhD']
average_salaries = salary.groupby('Education Level')['Salary'].mean().loc[education_order]
[tuple(t) for t in pd.DataFrame({
    'From': education_order[:-1],
    'To': education_order[1:],
    'Rate': ((average_salaries - average_salaries.shift(1)) / average_salaries.shift(1)).values[1:]
}).sort_values(by='Rate', ascending=False).values]

# %%
"""
question: |
  For each of the most popular 10 jobs, check the relationship between YoE and salary. Use linear regression to compute the slope coefficients. Return a DataFrame with "Job Title" and "Slope" as the columns.

execution:
  max_time: 2
"""

from sklearn.linear_model import LinearRegression

pd.DataFrame([
    {
        'Job Title': job,
        'Slope': LinearRegression().fit(salary.loc[salary['Job Title'] == job, 'Years of Experience'].values.reshape(-1, 1), salary.loc[salary['Job Title'] == job, 'Salary']).coef_[0]
    } for job in popular_jobs
])

# %%
"""
question: |
  Compare the median salary for each combination of education level and gender. Pivot the table with "Education Level" as rows and "Gender" as columns.
"""

salary.pivot_table(index='Education Level', columns='Gender', values='Salary', aggfunc='median')

# %%
"""
question: |
  Collect the most popular 10 job titles for both male and female. Show the result in a DataFrame with Male and Female as columns and popular job titles (ranked by popularity) as rows.
"""

popular_jobs_gender = pd.DataFrame({
    'Male': salary[salary['Gender'] == 'Male']['Job Title'].value_counts().head(10).index.tolist(),
    'Female': salary[salary['Gender'] == 'Female']['Job Title'].value_counts().head(10).index.tolist(),
})

popular_jobs_gender

# %%
"""
question: |
  Compute the median salary for each popular combination of gender and job title. Return a DataFrame with "Gender" and "Job Title" as the index and "Median Salary" as the values.
"""

pd.DataFrame([
    {
        'Gender': gender,
        'Job Title': job,
        'Median Salary': salary[(salary['Gender'] == gender) & (salary['Job Title'] == job)]['Salary'].median()
    } for gender in popular_jobs_gender for job in popular_jobs_gender[gender]
]).set_index(['Gender', 'Job Title'])
# %%
