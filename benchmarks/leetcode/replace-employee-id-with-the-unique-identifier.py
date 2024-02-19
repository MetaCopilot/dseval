'''
### Description ###

Table: `Employees`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.
```

Table: `EmployeeUNI`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.
```

Write a solution to show the **unique ID** of each user, If a user does not have a unique ID replace just show `null`.

Return the result table in **any** order.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
**Output:** 
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
**Explanation:** 
Alice and Bob do not have a unique ID, We will show null instead.
The unique ID of Meir is 2.
The unique ID of Winston is 3.
The unique ID of Jonathan is 1.
```

### Schema ###

data = [[1, 'Alice'], [7, 'Bob'], [11, 'Meir'], [90, 'Winston'], [3, 'Jonathan']]
Employees = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'int64', 'name':'object'})
data = [[3, 1], [11, 2], [90, 3]]
EmployeeUNI = pd.DataFrame(data, columns=['id', 'unique_id']).astype({'id':'int64', 'unique_id':'int64'})

### Code snippet ###

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame`.

  `employees` is a DataFrame with the following columns:
  - id: int
  - name: str
  Each row of this table contains the id and the name of an employee in a company.

  `employee_uni` is a DataFrame with the following columns:
  - id: int
  - unique_id: int
  Each row of this table contains the id and the corresponding unique id of an employee in the company.

  The function should show the **unique ID** of each user. If a user does not have a unique ID, just make it N/A.

  Return the result table in **any** order.

  The result format is in the following example.

  Example input:
  ```
  employees:
  +----+----------+
  | id | name     |
  +----+----------+
  | 1  | Alice    |
  | 7  | Bob      |
  | 11 | Meir     |
  | 90 | Winston  |
  | 3  | Jonathan |
  +----+----------+
  employee_uni:
  +----+-----------+
  | id | unique_id |
  +----+-----------+
  | 3  | 1         |
  | 11 | 2         |
  | 90 | 3         |
  +----+-----------+
  ```

  Example output:
  ```
  +-----------+----------+
  | unique_id | name     |
  +-----------+----------+
  | NaN       | Alice    |
  | NaN       | Bob      |
  | 2         | Meir     |
  | 3         | Winston  |
  | 1         | Jonathan |
  +-----------+----------+
  ```

  Example explanation:
  - Alice and Bob do not have a unique ID, We will show N/A instead.
  - The unique ID of Meir is 2.
  - The unique ID of Winston is 3.
  - The unique ID of Jonathan is 1.

validator:
  table_test:
    function_name: replace_employee_id
    input_validator: |
      def _validate(employees, employee_uni):
        assert employees.shape[0] > 0 and employee_uni.shape[0] > 0
        assert employees.dtypes.equals(pd.Series({'id': 'int64', 'name': 'object'}))
        assert employee_uni.dtypes.equals(pd.Series({'id': 'int64', 'unique_id': 'int64'}))
        assert employees.id.is_unique
        assert employee_uni.id.is_unique
        assert employee_uni.id.isin(employees.id).all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'id': [1, 7, 11, 90, 3], 'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']})`"
      - "`pd.DataFrame({'id': [3, 11, 90], 'unique_id': [1, 2, 3]})`"
    - # corner case: only one employee
      - "`pd.DataFrame({'id': [1], 'name': ['Alice']})`"
      - "`pd.DataFrame({'id': [1], 'unique_id': [1]})`"
    - # corner case: all employees have unique IDs
      - "`pd.DataFrame({'id': [1, 7, 11, 90, 3], 'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']})`"
      - "`pd.DataFrame({'id': [1, 7, 11, 90, 3], 'unique_id': [1, 2, 3, 4, 5]})`"
    - | # random cases
      ```
      def _generate():
        employees = pd.DataFrame({'id': np.arange(1, 1001), 'name': [f'Employee {i}' for i in range(1, 1001)]})
        employee_uni = pd.DataFrame({'id': np.random.choice(np.arange(1, 1001), 500, replace=False), 'unique_id': np.random.choice(np.arange(1, 1001), 500, replace=False)})
        return employees, employee_uni
      ```
    # 10 more random cases
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

def replace_employee_id(
    employees: pd.DataFrame, employee_uni: pd.DataFrame
) -> pd.DataFrame:
    # Merge the two dataframes on the id column
    result = employees.merge(employee_uni, on="id", how="left")

    # Rename the columns for clarity
    result = result.rename(columns={"unique_id": "unique_id", "name": "name"})

    # Reorder the columns
    result = result[["unique_id", "name"]]

    return result
