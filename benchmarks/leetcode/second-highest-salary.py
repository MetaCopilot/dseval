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

Write a solution to findthe second highest salary from the `Employee` table. If there is no second highest salary,return`null (returnNone in Pandas)`.

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
**Output:** 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
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
**Output:** 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
```

### Schema ###

data = [[1, 100], [2, 200], [3, 300]]
Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})

### Code snippet ###

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame`.

  `employee` is a DataFrame with the following columns:
  - id: int
  - salary: int
  Each row of this table contains information about the salary of an employee.

  The function should find the second highest salary from the `Employee` table. If there is no second highest salary, return `None`.

  The result format is in the following example.

  Example input:
  ```
  employee:
  +----+--------+
  | id | salary |
  +----+--------+
  | 1  | 100    |
  | 2  | 200    |
  | 3  | 300    |
  +----+--------+
  ```

  Example output:
  ```
  +---------------------+
  | SecondHighestSalary |
  +---------------------+
  | 200                 |
  +---------------------+
  ```

  Example input:
  ```
  employee:
  +----+--------+
  | id | salary |
  +----+--------+
  | 1  | 100    |
  +----+--------+
  ```

  Example output:
  ```
  +---------------------+
  | SecondHighestSalary |
  +---------------------+
  | None                |
  +---------------------+
  ```

validator:
  table_test:
    function_name: second_highest_salary
    input_validator: |
      def _validate(employee):
        assert employee.shape[0] > 0
        assert employee.dtypes.equals(pd.Series({'id': 'int64', 'salary': 'int64'}))
        assert employee.id.is_unique
        assert employee.salary.between(1, 1000000).all()

    test_cases:
    - # example 1
      - "`pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})`"
    - # example 2
      - "`pd.DataFrame({'id': [1], 'salary': [100]})`"
    - # corner case: only two employees
      - "`pd.DataFrame({'id': [1, 2], 'salary': [100, 200]})`"
    - # corner case: all employees have the same salary
      - "`pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 100, 100]})`"
    - # corner case: all employees have different salaries
      - "`pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})`"
    - # corner case: all employees have the highest salary
      - "`pd.DataFrame({'id': [1, 2, 3], 'salary': [1000000, 1000000, 1000000]})`"
    - |
      ```
      def _generate():
        return pd.DataFrame({
          'id': np.random.choice(np.arange(1, 100001), size=10000, replace=False),
          'salary': np.random.randint(1, np.random.choice([10, 100, 1000, 5000]), size=10000)
        }),
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

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salary = np.sort(employee["salary"].unique())
    if sorted_salary.size > 1:
        second_highest_salary = sorted_salary[-2]
    else:
        second_highest_salary = None
    return pd.DataFrame({"SecondHighestSalary": [second_highest_salary]})
