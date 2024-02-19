'''
### Description ###

Table: `Users`

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
```

Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by `user_id`.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
**Output:** 
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
```

### Schema ###

data = [[1, 'aLice'], [2, 'bOB']]
Users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})

### Code snippet ###

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def fix_names(users: pd.DataFrame) -> pd.DataFrame`.

  `users` is a DataFrame with the following columns:
  - user_id: int
  - name: str
  `users` contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.

  The function should fix the names so that only the first character is uppercase and the rest are lowercase.

  Return the result table ordered by `user_id`.

  The result format is in the following example.

  Example input:
  ```
  Users table:
  +---------+-------+
  | user_id | name  |
  +---------+-------+
  | 1       | aLice |
  | 2       | bOB   |
  +---------+-------+
  ```

  Example output:
  ```
  +---------+-------+
  | user_id | name  |
  +---------+-------+
  | 1       | Alice |
  | 2       | Bob   |
  +---------+-------+
  ```

validator:
  table_test:
    function_name: fix_names
    input_validator: |
      def _validate(users):
        assert users.shape[0] > 0
        assert users.dtypes.equals(pd.Series({'user_id': 'int64', 'name': 'object'}))
        assert users.user_id.is_unique
        assert users.name.str.match(r'^[a-zA-Z]+$').all()

    output_checker:
      ignore_index: true

    test_cases:
    - # example
      - "`pd.DataFrame({'user_id': [1, 2], 'name': ['aLice', 'bOB']})`"
    - # corner case: only one user
      - "`pd.DataFrame({'user_id': [1], 'name': ['aLice']})`"
    - # corner case: all names are already fixed
      - "`pd.DataFrame({'user_id': [1, 2], 'name': ['Alice', 'Bob']})`"
    - # corner case: all names are lowercase
      - "`pd.DataFrame({'user_id': [1, 2], 'name': ['alice', 'bob']})`"
    - # corner case: all names are uppercase
      - "`pd.DataFrame({'user_id': [1, 2], 'name': ['ALICE', 'BOB']})`"
    - | # generate random cases
      ```
      def _generate():
        import string
        import random
        names = [''.join(random.choices(string.ascii_letters, k=5)) for _ in range(1000)]
        users = pd.DataFrame({'user_id': np.arange(1, 1001), 'name': names})
        return users,
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

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    return users.sort_values(by="user_id").reset_index(drop=True)
