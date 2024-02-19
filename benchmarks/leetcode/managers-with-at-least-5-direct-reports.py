'''
### Description ###

Table: `Employee`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
```

Write a solution to find managers with at least **five direct reports**.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | None      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
**Output:** 
+------+
| name |
+------+
| John |
+------+
```

### Schema ###

data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
Employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})

### Code snippet ###

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def find_managers(employee: pd.DataFrame) -> pd.DataFrame`.

  `employee` is a DataFrame with the following columns:
  - id: int
  - name: str
  - department: str
  - managerId: int
  `employee` contains the information of employees. Each row of this table indicates the name of an employee, their department, and the id of their manager. If managerId is null, then the employee does not have a manager. No employee will be the manager of themself.

  The function should return managers with at least **five direct reports**. Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  Employee table:
  +-----+-------+------------+-----------+
  | id  | name  | department | managerId |
  +-----+-------+------------+-----------+
  | 101 | John  | A          | None      |
  | 102 | Dan   | A          | 101       |
  | 103 | James | A          | 101       |
  | 104 | Amy   | A          | 101       |
  | 105 | Anne  | A          | 101       |
  | 106 | Ron   | B          | 101       |
  +-----+-------+------------+-----------+
  ```

  Example output:
  ```
  +------+
  | name |
  +------+
  | John |
  +------+
  ```

validator:
  table_test:
    function_name: find_managers
    input_validator: |
      def _validate(employee):
        assert employee.shape[0] > 0
        assert employee.dtypes.equals(pd.Series({'id': 'Int64', 'name': 'object', 'department': 'object', 'managerId': 'Int64'}))
        assert employee.id.is_unique
        assert (employee.managerId.isin(employee.id) | employee.managerId.isnull()).all()
        assert (employee.managerId == employee.id).sum() == 0

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'id': pd.array([101, 102, 103, 104, 105, 106], dtype='Int64'), 'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'], 'department': ['A', 'A', 'A', 'A', 'A', 'B'], 'managerId': pd.array([None, 101, 101, 101, 101, 101], dtype='Int64')})`"
    - # corner case: only one manager
      - "`pd.DataFrame({'id': pd.array([1, 2, 3, 4, 5, 6], dtype='Int64'), 'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'], 'department': ['A', 'A', 'A', 'A', 'A', 'B'], 'managerId': pd.array([None, 1, 1, 1, 1, 1], dtype='Int64')})`"
    - # corner case: no manager has at least five direct reports
      - "`pd.DataFrame({'id': pd.array([1, 2, 3, 4, 5, 6], dtype='Int64'), 'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'], 'department': ['A', 'A', 'A', 'A', 'A', 'B'], 'managerId': pd.array([None, 1, 1, 1, 1, 2], dtype='Int64')})`"
    - # corner case: all managers have at least five direct reports
      - "`pd.DataFrame({'id': pd.array([1, 2, 3, 4, 5, 6], dtype='Int64'), 'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'], 'department': ['A', 'A', 'A', 'A', 'A', 'B'], 'managerId': pd.array([None, 1, 1, 1, 1, 1], dtype='Int64')})`"
    - # corner case: all employees are managers
      - "`pd.DataFrame({'id': pd.array([1, 2, 3, 4, 5, 6], dtype='Int64'), 'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'], 'department': ['A', 'A', 'A', 'A', 'A', 'B'], 'managerId': pd.array([None, 1, 2, 3, 4, 5], dtype='Int64')})`"
    - |  # generation
      ```
      import string
      def _generate():
        N = 3000
        permutation = np.random.permutation(N)
        manager_ids = pd.array([np.random.choice(permutation[:i].tolist() + [None]) for i in range(N)], dtype='Int64')
        shuffle_permutation = np.random.permutation(N)
        employee = pd.DataFrame({
          'id': pd.array(permutation[shuffle_permutation], dtype='Int64'),
          'name': [''.join(random.choices(string.ascii_letters, k=8)) for i in range(1, N + 1)],
          'department': [''.join(random.choices(string.ascii_letters, k=2)) for i in range(1, N + 1)],
          'managerId': pd.array(manager_ids[shuffle_permutation], dtype='Int64')
        })
        return employee,
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

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Count the number of direct reports for each manager
    direct_reports = employee.groupby("managerId").size().reset_index(name="num_direct_reports")

    # Filter managers with at least five direct reports
    managers = direct_reports[direct_reports["num_direct_reports"] >= 5]

    # Merge the managers with the employee table to get their names
    result = managers.merge(employee, left_on="managerId", right_on="id", how="inner")

    # Return the result with only the name column
    return result[["name"]]
