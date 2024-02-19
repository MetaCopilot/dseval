'''
### Description ###

Table: `Employee`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
```

Write a solution to find the `nth` highest salary from the `Employee` table. If there is no `nth` highest salary, return`null`.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
**Output:** 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```

**Example 2:**

```
**Input:** 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
**Output:** 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
```

### Schema ###



### Code snippet ###

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame`.

  `employee` is a DataFrame with the following columns:
  - id: int
  - salary: int
  `employee` contains information about the salary of an employee. Each row has a unique `id`.

  The function should find the `nth` highest salary from the `Employee` table. If there is no `nth` highest salary, return `None`.

  The result format is in the following example.

  Example input 1:
  ```
  employee:
  +----+--------+
  | id | salary |
  +----+--------+
  | 1  | 100    |
  | 2  | 200    |
  | 3  | 300    |
  +----+--------+
  N = 2
  ```

  Example output 1:
  ```
  +------------------------+
  | getNthHighestSalary(2) |
  +------------------------+
  | 200                    |
  +------------------------+
  ```

  Example input 2:
  ```
  employee:
  +----+--------+
  | id | salary |
  +----+--------+
  | 1  | 100    |
  +----+--------+
  N = 2
  ```

  Example output 2:
  ```
  +------------------------+
  | getNthHighestSalary(2) |
  +------------------------+
  | None                   |
  +------------------------+
  ```

validator:
  table_test:
    function_name: nth_highest_salary
    input_validator: |
      def _validate(employee, N):
        assert employee.shape[0] > 0
        assert employee.dtypes.equals(pd.Series({'id': 'int64', 'salary': 'int64'}))
        assert employee.id.is_unique
        assert employee.salary.between(0, 10**6).all()
        assert 1 <= N <= 10**5

    test_cases:
    - # example 1
      - "`pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})`"
      - 2
    - # example 2
      - "`pd.DataFrame({'id': [1], 'salary': [100]})`"
      - 2
    - # corner case: only one employee
      - "`pd.DataFrame({'id': [1], 'salary': [100]})`"
      - 1
    - # corner case: all employees have the same salary
      - "`pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 100, 100]})`"
      - 1
    - # corner case: all the same but N > 1
      - "`pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 100, 100]})`"
      - 2
    - # corner case: all employees have different salaries
      - "`pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})`"
      - 3
    - # corner case: all different but N > number of employees
      - "`pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})`"
      - 4
    - |
      ```
      def _generate():
        ids = np.random.choice(np.arange(1, 100001), size=10000, replace=False)
        return pd.DataFrame({'id': ids, 'salary': np.random.randint(1, np.random.randint(100, 10000), size=10000)}), np.random.randint(1, 10000)
      ```
    - //
    - //
    - //
    - //
    - //
    - //
    - //
    - //
    - //
    - //
"""

import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Find the unique salaries and sort them in descending order
    sorted_salaries = np.sort(employee["salary"].unique())[::-1]

    # Check if there is an nth highest salary
    if N <= len(sorted_salaries):
        nth_salary = sorted_salaries[N - 1]
        return pd.DataFrame({f"getNthHighestSalary({N})": [nth_salary]})
    else:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
