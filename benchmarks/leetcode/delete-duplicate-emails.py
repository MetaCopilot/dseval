'''
### Description ###

Table: `Person`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
```

Write a solution to **delete** all duplicate emails, keeping only one unique email with the smallest `id`.

For SQL users, please note that you are supposed to write a `DELETE` statement and not a `SELECT` one.

For Pandas users, please note that you are supposed to modify `Person` in place.

After running your script, the answer shown is the `Person` table. The driver will first compile and run your piece of code and then show the `Person` table. The final order of the `Person` table **does not matter**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
**Output:** 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
**Explanation:** john@example.com is repeated two times. We keep the row with the smallest Id = 1.
```

### Schema ###

data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
Person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'int64', 'email':'object'})

### Code snippet ###

import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def delete_duplicate_emails(person: pd.DataFrame) -> None`.

  `person` is a DataFrame with the following columns:
  - id: int
  - email: str
  `person` contains an email for each record. The emails will not contain uppercase letters.

  The function should **delete** all duplicate emails, keeping only one unique email with the smallest `id`. Modify `person` in place.

  The result format is in the following example.

  Example input:
  ```
  person:
  +----+------------------+
  | id | email            |
  +----+------------------+
  | 1  | john@example.com |
  | 2  | bob@example.com  |
  | 3  | john@example.com |
  +----+------------------+
  ```

  Example output:
  ```
  +----+------------------+
  | id | email            |
  +----+------------------+
  | 1  | john@example.com |
  | 2  | bob@example.com  |
  +----+------------------+
  ```
  Example explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.

validator:
  table_test:
    function_name: delete_duplicate_emails
    input_validator: |
      def _validate(person):
        assert person.shape[0] > 0
        assert person.dtypes.equals(pd.Series({'id': 'int64', 'email': 'object'}))
        assert person.id.is_unique
        assert person.email.str.match(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$').all()

    input_checker: true

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'id': [1, 2, 3], 'email': ['john@example.com', 'bob@example.com', 'john@example.com']})`"
    - # corner case: only one email
      - "`pd.DataFrame({'id': [1], 'email': ['john@example.com']})`"
    - # corner case: all emails are the same
      - "`pd.DataFrame({'id': [1, 2, 3], 'email': ['john@example.com', 'john@example.com', 'john@example.com']})`"
    - # corner case: all emails are different
      - "`pd.DataFrame({'id': [1, 2, 3], 'email': ['john@example.com', 'bob@example.com', 'alice@example.com']})`"
"""

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Group by email and find the minimum id for each email
    min_ids = person.groupby("email")["id"].min().values

    # Keep only the rows with id in min_ids
    person.drop(person[~person["id"].isin(min_ids)].index, inplace=True)
