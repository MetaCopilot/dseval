# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the data `inputs/v5_Latest_Data_Science_Salaries.csv` and save it as `salaries`.

validator:
  namespace_check:
    salaries:
"""

salaries = pd.read_csv('inputs/v5_Latest_Data_Science_Salaries.csv')

# %%
"""
question: |
  Read the file `inputs/exchange_rates.csv` into a variable `exchange_rates`. The file contains exchange rates between USD and other currencies.

validator:
  namespace_check:
    exchange_rates:
"""

exchange_rates = pd.read_csv('inputs/exchange_rates.csv')

# %%
"""
question: |
  Convert all salaries to USD using the exchange rates. Save the converted salaries in the "Salary in USD" column.

validator:
  namespace_check:
    salaries:
"""

# Exchange rates + USD
exchange_rates_with_usd = pd.concat([
    exchange_rates,
    pd.DataFrame.from_records([{'Currency': 'United States Dollar', 'Currency Code': 'USD', 'Exchange Rate': 1}])
])

# Merge salaries with exchange rates
salaries = salaries.merge(exchange_rates_with_usd, left_on='Salary Currency', right_on='Currency', how='left')

# Convert salaries to USD
salaries['Salary in USD'] = salaries['Salary'] * salaries['Exchange Rate']

# %%
"""
question: |
  Find out the top 20 job titles with the most occurrences. Return the titles as list.

validator:
  result:
    ignore_order: true
"""

salaries['Job Title'].value_counts().head(20).index.tolist()

# %%
"""
question: |
  List out the names of top 10 countries with the highest average salaries. Do not include countries with too few (less than 10) data points.

validator:
  result:
    ignore_order: true
"""

salaries.groupby('Company Location').filter(lambda group: len(group) >= 10).groupby('Company Location')['Salary in USD'].mean().sort_values(ascending=False).head(10).index.tolist()

# %%
"""
question: |
  Run a statistical analysis (ANOVA) to see if there are any significant differences in salaries based on employment type (Full-Time, Part-Time, etc.). Return a named tuple of statistic and pvalue.
"""

from scipy.stats import f_oneway

# Group salaries by employment type
groups = [group['Salary in USD'].dropna() for _, group in salaries.groupby('Employment Type')]

# Perform ANOVA
f_oneway(*groups)

# %%
"""
question: |
  Count the unique job titles for employees who work in Full-Time positions in the United States.
"""

salaries.loc[(salaries['Employment Type'] == 'Full-Time') & (salaries['Company Location'] == 'United States'), 'Job Title'].nunique()

# %%
"""
question: |
  Compute the average salary in USD for employees with Senior-level expertise (above Intermediate) who work in Medium-sized companies in the United States.
"""

salaries.loc[(salaries['Expertise Level'].isin(['Expert',  'Director'])) & (salaries['Company Size'] == 'Medium') & (salaries['Company Location'] == 'United States'), 'Salary in USD'].mean()

# %%
"""
question: |
  Identify the highest salaries by employment type.

validator:
  result:
    ignore_order: true
"""

salaries.groupby('Employment Type')['Salary in USD'].max()

# %%
"""
question: |
  Identify the year with the highest and lowest salary growth rate. The growth rate is calculated as the percentage change from the previous year. Put the results in a tuple of `(year_with_highest_growth, year_with_lowest_growth)`.
"""

# Calculate the average salary for each year
average_salaries_per_year = salaries.groupby('Year')['Salary in USD'].mean()

# Calculate the growth rate for each year
growth_rates = average_salaries_per_year.pct_change()

# Identify the year with the highest and lowest growth rate
year_with_highest_growth = growth_rates.idxmax()
year_with_lowest_growth = growth_rates.idxmin()

(year_with_highest_growth, year_with_lowest_growth)

# %%
"""
question: |
  Compute the annual salary growth rate for each employment type. The growth rate is calculated as the percentage change from the previous year. Return a DataFrame with "Employment Type" and "Year" as the index and "Salary Growth Rate" as the values. If the growth rate is not available for a particular year, fill it with `NaN`.
"""

# Calculate the total salary for each employment type and year
total_salaries_by_employment_type = salaries.groupby(['Employment Type', 'Year'])['Salary in USD'].mean()

# Calculate the growth rate for each employment type and year
growth_rates_by_employment_type = total_salaries_by_employment_type.groupby(level=0).pct_change()

# Convert to DataFrame
growth_rates_by_employment_type = growth_rates_by_employment_type.reset_index().rename(columns={'Salary in USD': 'Salary Growth Rate'}).set_index(['Employment Type', 'Year'])

growth_rates_by_employment_type

# %%
"""
question: |
  Identify the employment type with the highest average salary growth rate.
"""

growth_rates_by_employment_type.groupby('Employment Type').mean().idxmax().item()

# %%
"""
question: |
  Create a pivot table to show the average salary for each combination of expertise level and experience level. The pivot table should have "Expertise Level" as the index and "Experience Level" as the columns.
"""

salaries.pivot_table(index='Expertise Level', columns='Experience Level', values='Salary in USD', aggfunc='mean')

# %%
"""
question: |
  Create a cross-tabulation to show the count of employees for each combination of company size and company location. The cross-tabulation should have "Company Size" as the index, "Company Location" as the columns, and the counts as the values.
"""

pd.crosstab(salaries['Company Size'], salaries['Company Location'])

# %%
"""
question: |
  For each company size, calculate the interquartile range (IQR) of salary and identify outliers (salaries that are below Q1 - 1.5*IQR or above Q3 + 1.5*IQR). Return a DataFrame with "Company Size" as the index and "Lower Bound", "Upper Bound", "Number of Outliers" as the columns.
"""

# Calculate Q1, Q3, and IQR for each company size
stats = salaries.groupby('Company Size')['Salary in USD'].describe(percentiles=[0.25, 0.75])
stats['IQR'] = stats['75%'] - stats['25%']

# Calculate lower and upper bounds for outliers
stats['Lower Bound'] = stats['25%'] - 1.5 * stats['IQR']
stats['Upper Bound'] = stats['75%'] + 1.5 * stats['IQR']

# Count the number of outliers for each company size
outliers = salaries.groupby('Company Size').apply(lambda group: ((group['Salary in USD'] < stats.loc[group.name, 'Lower Bound']) | (group['Salary in USD'] > stats.loc[group.name, 'Upper Bound'])).sum())
stats['Number of Outliers'] = outliers.astype(int)

stats[['Lower Bound', 'Upper Bound', 'Number of Outliers']]

# %%
"""
question: |
  For each company size, replace the outliers with the median salary of the corresponding company size. Save the cleaned salaries in a new column "Cleaned Salary".

validator:
  namespace_check:
    salaries:
"""

# Calculate the median salary for each company size
medians = salaries.groupby('Company Size')['Salary in USD'].median()

# Replace outliers with median
salaries['Cleaned Salary'] = salaries.apply(lambda row: medians[row['Company Size']] if row['Salary in USD'] < stats.loc[row['Company Size'], 'Lower Bound'] or row['Salary in USD'] > stats.loc[row['Company Size'], 'Upper Bound'] else row['Salary in USD'], axis=1)

# %%
"""
question: |
  For each job title, calculate the annual salary growth rate. Return a DataFrame with "Job Title" and "Year" as the index and "Salary Growth Rate" as the values.
"""

# Calculate the total salary for each job title and year
total_salaries_by_job_title = salaries.groupby(['Job Title', 'Year'])['Cleaned Salary'].sum()

# Calculate the growth rate for each job title and year
growth_rates_by_job_title = total_salaries_by_job_title.groupby(level=0).pct_change()

# Convert to DataFrame
growth_rates_by_job_title = growth_rates_by_job_title.reset_index().rename(columns={'Cleaned Salary': 'Salary Growth Rate'}).set_index(['Job Title', 'Year'])

growth_rates_by_job_title

# %%
"""
question: |
  For each year, test the independence of employee residence and company location using the chi-squared test. Return a DataFrame with "Chi-Squared Statistic" and "p-value" as the columns and "Year" as the index.
"""

from scipy.stats import chi2_contingency

salaries.groupby('Year').apply(lambda group: chi2_contingency(pd.crosstab(group['Company Location'], group['Employee Residence']))[:2]).apply(pd.Series).rename(columns={0: 'Chi-Squared Statistic', 1: 'p-value'})
