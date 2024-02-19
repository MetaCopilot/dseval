### Dataset name ###

Employee dataset

### Dataset description ###

**Context:**
This dataset contains information about employees in a company, including their educational backgrounds, work history, demographics, and employment-related factors. It has been anonymized to protect privacy while still providing valuable insights into the workforce.

**Columns:**

1. **Education:** The educational qualifications of employees, including degree, institution, and field of study.

2. **Joining Year:** The year each employee joined the company, indicating their length of service.

3. **City:** The location or city where each employee is based or works.

4. **Payment Tier:** Categorization of employees into different salary tiers.

5. **Age:** The age of each employee, providing demographic insights.

6. **Gender:** Gender identity of employees, promoting diversity analysis.

7. **Ever Benched:** Indicates if an employee has ever been temporarily without assigned work.

8. **Experience in Current Domain:** The number of years of experience employees have in their current field.

9. **Leave or Not:** a target column

**Usage:**
This dataset can be used for various HR and workforce-related analyses, including employee retention, salary structure assessments, diversity and inclusion studies, and leave pattern analyses. Researchers, data analysts, and HR professionals can gain valuable insights from this dataset.

**Potential Research Questions:**
1. What is the distribution of educational qualifications among employees?
2. How does the length of service (Joining Year) vary across different cities?
3. Is there a correlation between Payment Tier and Experience in Current Domain?
4. What is the gender distribution within the workforce?
5. Are there any patterns in leave-taking behavior among employees?


**Acknowledgments:**
We would like to acknowledge the contributions of our HR department in providing this dataset for research and analysis purposes.

### Dataset files ###

- Employee.csv

    pandas.DataFrame(shape=(4653, 9), columns=["Education", "JoiningYear", "City", "PaymentTier", "Age", "Gender", "EverBenched", "ExperienceInCurrentDomain", "LeaveOrNot"])
              Education  JoiningYear       City  PaymentTier  Age  Gender EverBenched  ExperienceInCurrentDomain  LeaveOrNot
        0     Bachelors         2017  Bangalore            3   34    Male          No                    0                 0
        1     Bachelors         2013       Pune            1   28  Female          No                    3                 1
        2     Bachelors         2014  New Delhi            3   38  Female          No                    2                 0
        3       Masters         2016  Bangalore            3   27    Male          No                    5                 1
        4       Masters         2017       Pune            3   24    Male         Yes                    2                 1
        ...         ...          ...        ...          ...  ...     ...         ...                  ...               ...
        4648  Bachelors         2013  Bangalore            3   26  Female          No                    4                 0
        4649    Masters         2013       Pune            2   37    Male          No                    2                 1
        4650    Masters         2018  New Delhi            3   27    Male          No                    5                 1
        4651  Bachelors         2012  Bangalore            3   30    Male         Yes                    2                 0
        4652  Bachelors         2015  Bangalore            3   33    Male         Yes                    4                 0

