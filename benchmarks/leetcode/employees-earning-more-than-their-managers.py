'''
### Description ###

Table: `Employee`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
```

Write a solutionto find the employees who earn more than their managers.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
**Output:** 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
**Explanation:** Joe is the only employee who earns more than his manager.
```

### Schema ###

data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
Employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})

### Code snippet ###

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def find_employees(employee: pd.DataFrame) -> pd.DataFrame`.

  `employee` is a DataFrame with the following columns:
  - id: int
  - name: str
  - salary: int
  - managerId: int
  Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

  The function should return the employees who earn more than their managers. Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  Employee table:
  +----+-------+--------+-----------+
  | id | name  | salary | managerId |
  +----+-------+--------+-----------+
  | 1  | Joe   | 70000  | 3         |
  | 2  | Henry | 80000  | 4         |
  | 3  | Sam   | 60000  | Null      |
  | 4  | Max   | 90000  | Null      |
  +----+-------+--------+-----------+
  ```

  Example output:
  ```
  +----------+
  | Employee |
  +----------+
  | Joe      |
  +----------+
  ```

  Example explanation: Joe is the only employee who earns more than his manager.

validator:
  table_test:
    function_name: find_employees
    input_validator: |
      def _validate(employee):
        assert employee.shape[0] > 0
        assert employee.dtypes.equals(pd.Series({'id': 'Int64', 'name': 'object', 'salary': 'int64', 'managerId': 'Int64'}))
        assert employee.id.is_unique
        assert employee.salary.between(0, 10**6).all()
        assert (employee.managerId.isin(employee.id) | employee.managerId.isnull()).all()
        assert (employee.managerId == employee.id).sum() == 0

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'id': pd.array([1, 2, 3, 4], dtype='Int64'), 'name': ['Joe', 'Henry', 'Sam', 'Max'], 'salary': [70000, 80000, 60000, 90000], 'managerId': pd.array([3, 4, None, None], dtype='Int64')})`"
    - # corner case: only one employee
      - "`pd.DataFrame({'id': pd.array([1], dtype='Int64'), 'name': ['Joe'], 'salary': [70000], 'managerId': pd.array([None], dtype='Int64')})`"
    - # corner case: all employees have the same salary
      - "`pd.DataFrame({'id': pd.array([1, 2, 3, 4], dtype='Int64'), 'name': ['Joe', 'Henry', 'Sam', 'Max'], 'salary': [70000, 70000, 70000, 70000], 'managerId': pd.array([3, 4, None, None], dtype='Int64')})`"
    - # corner case: all employees have different salaries
      - "`pd.DataFrame({'id': pd.array([1, 2, 3, 4], dtype='Int64'), 'name': ['Joe', 'Henry', 'Sam', 'Max'], 'salary': [70000, 80000, 60000, 90000], 'managerId': pd.array([3, 4, 1, 2], dtype='Int64')})`"
    - | # generate random cases
      ```
      def _generate():
        none_probability = np.random.uniform(0, 1)
        manager_ids = pd.array([np.random.choice(np.concatenate([np.arange(1, i), np.arange(i + 1, 1001)])) for i in range(1, 1001)], dtype='Int64')
        manager_ids[np.random.uniform(0, 1, 1000) < none_probability] = None
        employee = pd.DataFrame({'id': pd.array(np.arange(1, 1001), dtype='Int64'), 'name': [f'Employee {i}' for i in range(1, 1001)], 'salary': np.random.randint(0, 1000, 1000), 'managerId': pd.array(manager_ids, dtype='Int64')})
        return employee,
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

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Merge the employee DataFrame with itself on managerId and id
    merged_df = employee.merge(employee, left_on="managerId", right_on="id", suffixes=("", "_manager"))

    # Filter the merged DataFrame to only include employees with a higher salary than their manager
    higher_salary = merged_df[merged_df["salary"] > merged_df["salary_manager"]]

    # Return the names of the employees with a higher salary than their manager
    return higher_salary[["name"]].rename(columns={"name": "Employee"})
