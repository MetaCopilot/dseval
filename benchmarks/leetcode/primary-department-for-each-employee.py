'''
### Description ###

Table: `Employee`

```
+---------------+---------+
| Column Name   |  Type   |
+---------------+---------+
| employee_id   | int     |
| department_id | int     |
| primary_flag  | varchar |
+---------------+---------+
(employee_id, department_id) is the primary key (combination of columns with unique values) for this table.
employee_id is the id of the employee.
department_id is the id of the department to which the employee belongs.
primary_flag is an ENUM (category) of type ('Y', 'N'). If the flag is 'Y', the department is the primary department for the employee. If the flag is 'N', the department is not the primary.
```

Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is `'N'`.

Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department.

Return the result table in **any order**.

Theresult format is in the following example.

**Example 1:**

```
**Input:** 
Employee table:
+-------------+---------------+--------------+
| employee_id | department_id | primary_flag |
+-------------+---------------+--------------+
| 1           | 1             | N            |
| 2           | 1             | Y            |
| 2           | 2             | N            |
| 3           | 3             | N            |
| 4           | 2             | N            |
| 4           | 3             | Y            |
| 4           | 4             | N            |
+-------------+---------------+--------------+
**Output:** 
+-------------+---------------+
| employee_id | department_id |
+-------------+---------------+
| 1           | 1             |
| 2           | 1             |
| 3           | 3             |
| 4           | 3             |
+-------------+---------------+
**Explanation:** 
- The Primary department for employee 1 is 1.
- The Primary department for employee 2 is 1.
- The Primary department for employee 3 is 3.
- The Primary department for employee 4 is 3.
```

### Schema ###

data = [['1', '1', 'N'], ['2', '1', 'Y'], ['2', '2', 'N'], ['3', '3', 'N'], ['4', '2', 'N'], ['4', '3', 'Y'], ['4', '4', 'N']]
Employee = pd.DataFrame(data, columns=['employee_id', 'department_id', 'primary_flag']).astype({'employee_id':'Int64', 'department_id':'Int64', 'primary_flag':'object'})

### Code snippet ###

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame`.

  `employee` is a DataFrame with the following columns:
  - employee_id: int
  - department_id: int
  - primary_flag: str
  `employee` holds information about employees and their departments. Each record has a unique combination of `employee_id` and `department_id`. `primary_flag` must be either 'Y' or 'N'. If the flag is 'Y', the department is the primary department for the employee. If the flag is 'N', the department is not the primary.

  Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is `'N'`.

  The function should return all the employees with their primary department. For employees who belong to one department, report their only department.

  Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  employee:
  +-------------+---------------+--------------+
  | employee_id | department_id | primary_flag |
  +-------------+---------------+--------------+
  | 1           | 1             | N            |
  | 2           | 1             | Y            |
  | 2           | 2             | N            |
  | 3           | 3             | N            |
  | 4           | 2             | N            |
  | 4           | 3             | Y            |
  | 4           | 4             | N            |
  +-------------+---------------+--------------+
  ```

  Example output:
  ```
  +-------------+---------------+
  | employee_id | department_id |
  +-------------+---------------+
  | 1           | 1             |
  | 2           | 1             |
  | 3           | 3             |
  | 4           | 3             |
  +-------------+---------------+
  ```

  Example explanation:
  - The Primary department for employee 1 is 1.
  - The Primary department for employee 2 is 1.
  - The Primary department for employee 3 is 3.
  - The Primary department for employee 4 is 3.

validator:
  table_test:
    function_name: find_primary_department
    input_validator: |
      def _validate(employee):
        assert employee.shape[0] > 0
        assert employee.dtypes.equals(pd.Series({'employee_id': 'int64', 'department_id': 'int64', 'primary_flag': 'object'}))
        assert employee.primary_flag.isin(['Y', 'N']).all()
        single_dep_employees = employee.groupby('employee_id').size()
        single_dep_employees = single_dep_employees[single_dep_employees == 1].index
        assert (employee[employee.employee_id.isin(single_dep_employees)].primary_flag == 'N').all()
        assert (employee[employee.primary_flag == 'Y'].groupby('employee_id').size() == 1).all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'employee_id': [1, 2, 2, 3, 4, 4, 4], 'department_id': [1, 1, 2, 3, 2, 3, 4], 'primary_flag': ['N', 'Y', 'N', 'N', 'N', 'Y', 'N']})`"
    - # corner case: only one employee with one department
      - "`pd.DataFrame({'employee_id': [1], 'department_id': [1], 'primary_flag': ['N']})`"
    - # corner case: only one employee with multiple departments
      - "`pd.DataFrame({'employee_id': [1, 1, 1], 'department_id': [1, 2, 3], 'primary_flag': ['N', 'Y', 'N']})`"
    - # corner case: all employees have only one department
      - "`pd.DataFrame({'employee_id': [1, 2, 3, 4], 'department_id': [1, 2, 3, 4], 'primary_flag': ['N', 'N', 'N', 'N']})`"
    - # corner case: all employees have multiple departments
      - "`pd.DataFrame({'employee_id': [1, 1, 2, 2, 3, 3, 4, 4], 'department_id': [1, 2, 1, 2, 3, 4, 3, 4], 'primary_flag': ['N', 'Y', 'Y', 'N', 'N', 'Y', 'Y', 'N']})`"
    # - # this case from leetcode is invalid
    #   - "`pd.DataFrame({'employee_id': [1, 2, 3, 4, 5], 'department_id': [59, 44, 27, 29, 40], 'primary_flag': ['N', 'N', 'N', 'N', 'Y']})`"
    - | # generate random cases
      ```
      def _generate():
        records = []
        for i in range(1, 1001):
          departments = np.random.choice(np.arange(1, 1001), size=np.random.randint(1, 11), replace=False)
          if len(departments) == 1:
            records.append((i, departments[0], 'N'))
          else:
            records.append((i, departments[0], 'Y'))
            records += [(i, d, 'N') for d in departments[1:]]
        np.random.shuffle(records)
        return pd.DataFrame(records, columns=['employee_id', 'department_id', 'primary_flag']),
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

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # Find the primary department for each employee
    primary_departments = employee[employee["primary_flag"] == "Y"]

    # Find employees with only one department
    single_department_employees = (
        employee.groupby("employee_id").size().reset_index(name="count")
    )
    single_department_employees = single_department_employees[
        single_department_employees["count"] == 1
    ]

    # Merge the single department employees with the primary departments
    result = pd.merge(
        single_department_employees,
        employee,
        on="employee_id",
        how="left",
    ).drop(columns=["count"])

    # Concatenate the primary departments and single department employees
    result = pd.concat([primary_departments, result], ignore_index=True)

    # Drop the primary_flag column and return the result
    return result.drop(columns=["primary_flag"])
