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

Write a solution to report all the duplicate emails. Note that it's guaranteed that the emailfield is not NULL.

Return the result table in **any order**.

Theresult format is in the following example.

**Example 1:**

```
**Input:** 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
**Output:** 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
**Explanation:** a@b.com is repeated two times.
```

### Schema ###

data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
Person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})

### Code snippet ###

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame`.

  `person` is a DataFrame with the following columns:
  - id: int
  - email: str
  `person` contains an email for each record. The emails will not contain uppercase letters.

  The function should return all the duplicate emails. Note that it's guaranteed that the email field is not NULL. Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  person:
  +----+---------+
  | id | email   |
  +----+---------+
  | 1  | a@b.com |
  | 2  | c@d.com |
  | 3  | a@b.com |
  +----+---------+
  ```

  Example output:
  ```
  +---------+
  | email   |
  +---------+
  | a@b.com |
  +---------+
  ```

  Example explanation: a@b.com is repeated two times.

validator:
  table_test:
    function_name: duplicate_emails
    input_validator: |
      def _validate(person):
        assert person.shape[0] > 0
        assert person.dtypes.equals(pd.Series({'id': 'int64', 'email': 'object'}))
        assert person.id.is_unique
        assert person.email.str.match(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$').all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'id': [1, 2, 3], 'email': ['a@b.com', 'c@d.com', 'a@b.com']})`"
    - # corner case: only one email
      - "`pd.DataFrame({'id': [1], 'email': ['a@b.com']})`"
    - # corner case: all emails are the same
      - "`pd.DataFrame({'id': [1, 2, 3], 'email': ['a@b.com', 'a@b.com', 'a@b.com']})`"
    - # corner case: all emails are different
      - "`pd.DataFrame({'id': [1, 2, 3], 'email': ['a@b.com', 'c@d.com', 'e@f.com']})`"
    - # corner case: some emails are the same
      - "`pd.DataFrame({'id': [1, 2, 3, 4], 'email': ['a@b.com', 'c@d.com', 'a@b.com', 'c@d.com']})`"
    - # corner case: some emails are the same, but not all
      - "`pd.DataFrame({'id': [1, 2, 3, 4, 5], 'email': ['a@b.com', 'c@d.com', 'a@b.com', 'c@d.com', 'e@f.com']})`"
"""

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # Group by email and count the occurrences
    email_counts = person.groupby("email").size().reset_index(name="count")

    # Filter the emails with count greater than 1 (duplicates)
    duplicates = email_counts[email_counts["count"] > 1]

    # Return the duplicate emails as a DataFrame
    return duplicates[["email"]]
