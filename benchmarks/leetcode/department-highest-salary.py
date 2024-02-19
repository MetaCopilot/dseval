'''
### Description ###

Table: `Employee`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
```

Table: `Department`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
```

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
**Output:** 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
**Explanation:** Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.
```

### Schema ###

data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
Employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
Department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})

### Code snippet ###

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame`.

  `employee` is a DataFrame with the following columns:
  - id: int
  - name: str
  - salary: int
  - departmentId: int
  Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.

  `department` is a DataFrame with the following columns:
  - id: int
  - name: str
  Each row of this table indicates the ID of a department and its name.

  The function should return employees who have the highest salary in each of the departments. Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  employee:
  +----+-------+--------+--------------+
  | id | name  | salary | departmentId |
  +----+-------+--------+--------------+
  | 1  | Joe   | 70000  | 1            |
  | 2  | Jim   | 90000  | 1            |
  | 3  | Henry | 80000  | 2            |
  | 4  | Sam   | 60000  | 2            |
  | 5  | Max   | 90000  | 1            |
  +----+-------+--------+--------------+
  department:
  +----+-------+
  | id | name  |
  +----+-------+
  | 1  | IT    |
  | 2  | Sales |
  +----+-------+
  ```

  Example output:
  ```
  +------------+----------+--------+
  | Department | Employee | Salary |
  +------------+----------+--------+
  | IT         | Jim      | 90000  |
  | Sales      | Henry    | 80000  |
  | IT         | Max      | 90000  |
  +------------+----------+--------+
  ```

  Example explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

validator:
  table_test:
    function_name: department_highest_salary
    input_validator: |
      def _validate(employee, department):
        assert employee.shape[0] > 0 and department.shape[0] > 0
        assert employee.dtypes.equals(pd.Series({'id': 'int64', 'name': 'object', 'salary': 'int64', 'departmentId': 'int64'}))
        assert department.dtypes.equals(pd.Series({'id': 'int64', 'name': 'object'}))
        assert employee.id.is_unique
        assert employee.departmentId.isin(department.id).all()
        assert department.id.is_unique

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'id': [1, 2, 3, 4, 5], 'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'], 'salary': [70000, 90000, 80000, 60000, 90000], 'departmentId': [1, 1, 2, 2, 1]})`"
      - "`pd.DataFrame({'id': [1, 2], 'name': ['IT', 'Sales']})`"
    - # corner case: only one employee
      - "`pd.DataFrame({'id': [1], 'name': ['Joe'], 'salary': [70000], 'departmentId': [1]})`"
      - "`pd.DataFrame({'id': [1], 'name': ['IT']})`"
    - # corner case: only one department
      - "`pd.DataFrame({'id': [1, 2, 3, 4, 5], 'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'], 'salary': [70000, 90000, 80000, 60000, 90000], 'departmentId': [1, 1, 1, 1, 1]})`"
      - "`pd.DataFrame({'id': [1], 'name': ['IT']})`"
    - # corner case: all employees have the same salary
      - "`pd.DataFrame({'id': [1, 2, 3, 4, 5], 'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'], 'salary': [70000, 70000, 70000, 70000, 70000], 'departmentId': [1, 1, 2, 2, 1]})`"
      - "`pd.DataFrame({'id': [1, 2], 'name': ['IT', 'Sales']})`"
    - | # generate random cases
      ```
      def _generate():
        department = pd.DataFrame({'id': np.arange(1, 101), 'name': [f'Department {i}' for i in range(1, 101)]})
        employee = pd.DataFrame({'id': np.arange(1, 1001), 'name': [f'Employee {i}' for i in range(1, 1001)], 'salary': np.random.randint(10000, 100000, 1000), 'departmentId': np.random.choice(np.arange(1, 101), 1000)})
        return employee, department
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

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge employee and department dataframes
    merged_df = employee.merge(department, left_on="departmentId", right_on="id", suffixes=("", "_department"))

    # Find the maximum salary for each department
    max_salaries = merged_df.groupby("departmentId")["salary"].max().reset_index()

    # Merge the max_salaries dataframe with the merged_df to filter out the employees with the highest salary in each department
    result = merged_df.merge(max_salaries, on=["departmentId", "salary"])

    # Select the required columns and rename them
    result = result[["name_department", "name", "salary"]].rename(
        columns={"name_department": "Department", "name": "Employee", "salary": "Salary"}
    )

    return result
