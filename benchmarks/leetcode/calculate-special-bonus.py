'''
### Description ###

Table: `Employees`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.
```

Write a solution to calculate the bonus of each employee. The bonus of an employee is `100%` of their salary if the ID of the employee is **an odd number** and **the employee's name does not start with the character** `'M'`. The bonus of an employee is `0` otherwise.

Return the result table ordered by `employee_id`.

Theresult format is in the following example.

**Example 1:**

```
**Input:** 
Employees table:
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+
**Output:** 
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
+-------------+-------+
**Explanation:** 
The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
The employee with ID 3 gets 0 bonus because their name starts with 'M'.
The rest of the employees get a 100% bonus.
```

### Schema ###

data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
Employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})

### Code snippet ###

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame`.

  `employees` is a DataFrame with the following columns:
  - employee_id: int
  - name: str
  - salary: int
  Each row of this table indicates the employee ID, employee name, and salary.

  The function should calculate the bonus of each employee. The bonus of an employee is `100%` of their salary if the ID of the employee is **an odd number** and **the employee's name does not start with the character** `'M'`. The bonus of an employee is `0` otherwise.

  Return the result table ordered by `employee_id`.

  The result format is in the following example.

  Example input:
  ```
  Employees table:
  +-------------+---------+--------+
  | employee_id | name    | salary |
  +-------------+---------+--------+
  | 2           | Meir    | 3000   |
  | 3           | Michael | 3800   |
  | 7           | Addilyn | 7400   |
  | 8           | Juan    | 6100   |
  | 9           | Kannon  | 7700   |
  +-------------+---------+--------+
  ```

  Example output:
  ```
  +-------------+-------+
  | employee_id | bonus |
  +-------------+-------+
  | 2           | 0     |
  | 3           | 0     |
  | 7           | 7400  |
  | 8           | 0     |
  | 9           | 7700  |
  +-------------+-------+
  ```

  Example explanation:
  - The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
  - The employee with ID 3 gets 0 bonus because their name starts with 'M'.
  - The rest of the employees get a 100% bonus.

validator:
  table_test:
    function_name: calculate_special_bonus
    input_validator: |
      def _validate(employees):
        assert employees.shape[0] > 0
        assert employees.dtypes.equals(pd.Series({'employee_id': 'int64', 'name': 'object', 'salary': 'int64'}))
        assert employees.employee_id.is_unique
        assert employees.salary.between(0, 10**6).all()

    output_checker:
      ignore_index: true

    test_cases:
    - # example
      - "`pd.DataFrame({'employee_id': [2, 3, 7, 8, 9], 'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'], 'salary': [3000, 3800, 7400, 6100, 7700]})`"
    - # corner case: only one employee
      - "`pd.DataFrame({'employee_id': [1], 'name': ['Alice'], 'salary': [1000]})`"
    - # corner case: all employees have even IDs
      - "`pd.DataFrame({'employee_id': [2, 4, 6, 8, 10], 'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'], 'salary': [3000, 3800, 7400, 6100, 7700]})`"
    - # corner case: all employees have names starting with 'M'
      - "`pd.DataFrame({'employee_id': [1, 3, 5, 7, 9], 'name': ['Meir', 'Michael', 'Maddilyn', 'Muan', 'Mannon'], 'salary': [3000, 3800, 7400, 6100, 7700]})`"
    - # corner case: all employees have odd IDs and names not starting with 'M'
      - "`pd.DataFrame({'employee_id': [1, 3, 5, 7, 9], 'name': ['Alice', 'Bob', 'Cathy', 'David', 'Eva'], 'salary': [1000, 2000, 3000, 4000, 5000]})`"
    - | # generate random cases
      ```
      def _generate():
        employee_id = np.arange(1, 1001)
        name = np.random.choice(['Alice', 'Bob', 'Cathy', 'David', 'Eva', 'Meir', 'Michael', 'Maddilyn', 'Muan', 'Mannon'], size=1000)
        salary = np.random.randint(0, 10**6, size=1000)
        employees = pd.DataFrame({'employee_id': employee_id, 'name': name, 'salary': salary})
        return employees,
      ```
    # 10 random cases
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

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate the bonus for each employee based on the conditions
    employees["bonus"] = employees.apply(
        lambda row: row["salary"] if row["employee_id"] % 2 == 1 and row["name"][0] != "M" else 0,
        axis=1,
    )

    # Return the result table ordered by employee_id
    return employees[["employee_id", "bonus"]].sort_values(by="employee_id")
