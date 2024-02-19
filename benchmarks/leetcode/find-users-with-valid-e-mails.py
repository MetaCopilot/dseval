'''
### Description ###

Table: `Users`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains information of the users signed up in a website. Some e-mails are invalid.
```

Write a solution to find the users who have **valid emails**.

A valid e-mail has a prefix name and a domain where:

* **The prefix name** is a string that may contain letters (upper or lower case), digits, underscore `'_'`, period `'.'`, and/or dash `'-'`. The prefix name **must** start with a letter.
* **The domain** is `'@leetcode.com'`.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Users table:
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 2       | Jonathan  | jonathanisgreat         |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
| 5       | Marwan    | quarz#2020@leetcode.com |
| 6       | David     | david69@gmail.com       |
| 7       | Shapiro   | .shapo@leetcode.com     |
+---------+-----------+-------------------------+
**Output:** 
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
+---------+-----------+-------------------------+
**Explanation:** 
The mail of user 2 does not have a domain.
The mail of user 5 has the # sign which is not allowed.
The mail of user 6 does not have the leetcode domain.
The mail of user 7 starts with a period.
```

### Schema ###

data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'], [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'], [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'], [7, 'Shapiro', '.shapo@leetcode.com']]
Users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})

### Code snippet ###

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def valid_emails(users: pd.DataFrame) -> pd.DataFrame`.

  `users` is a DataFrame with the following columns:
  - user_id: int
  - name: str
  - mail: str
  `users` contains information of the users signed up in a website. Some e-mails are invalid.

  The function should return the users who have **valid emails**.

  A valid e-mail has a prefix name and a domain where:

  * **The prefix name** is a string that may contain letters (upper or lower case), digits, underscore `'_'`, period `'.'`, and/or dash `'-'`. The prefix name **must** start with a letter.
  * **The domain** is `'@leetcode.com'`.

  Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  users:
  +---------+-----------+-------------------------+
  | user_id | name      | mail                    |
  +---------+-----------+-------------------------+
  | 1       | Winston   | winston@leetcode.com    |
  | 2       | Jonathan  | jonathanisgreat         |
  | 3       | Annabelle | bella-@leetcode.com     |
  | 4       | Sally     | sally.come@leetcode.com |
  | 5       | Marwan    | quarz#2020@leetcode.com |
  | 6       | David     | david69@gmail.com       |
  | 7       | Shapiro   | .shapo@leetcode.com     |
  +---------+-----------+-------------------------+
  ```

  Example output:
  ```
  +---------+-----------+-------------------------+
  | user_id | name      | mail                    |
  +---------+-----------+-------------------------+
  | 1       | Winston   | winston@leetcode.com    |
  | 3       | Annabelle | bella-@leetcode.com     |
  | 4       | Sally     | sally.come@leetcode.com |
  +---------+-----------+-------------------------+
  ```

  Example explanation:
  - The mail of user 2 does not have a domain.
  - The mail of user 5 has the # sign which is not allowed.
  - The mail of user 6 does not have the leetcode domain.
  - The mail of user 7 starts with a period.

validator:
  table_test:
    function_name: valid_emails
    input_validator: |
      def _validate(users):
        assert users.shape[0] > 0
        assert users.dtypes.equals(pd.Series({'user_id': 'int64', 'name': 'object', 'mail': 'object'}))
        assert users.user_id.is_unique
        assert users.name.str.match(r'^\w+$').all()
        assert users.mail.str.match(r'^.+$').all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'user_id': [1, 2, 3, 4, 5, 6, 7], 'name': ['Winston', 'Jonathan', 'Annabelle', 'Sally', 'Marwan', 'David', 'Shapiro'], 'mail': ['winston@leetcode.com', 'jonathanisgreat', 'bella-@leetcode.com', 'sally.come@leetcode.com', 'quarz#2020@leetcode.com', 'david69@gmail.com', '.shapo@leetcode.com']})`"
    - # corner case: only one user
      - "`pd.DataFrame({'user_id': [1], 'name': ['Winston'], 'mail': ['winston@leetcode.com']})`"
    - # corner case: all users have invalid emails
      - "`pd.DataFrame({'user_id': [1, 2, 3], 'name': ['Winston', 'Jonathan', 'Annabelle'], 'mail': ['winston@leetcode', 'jonathanisgreat', 'bella-@leetcode']})`"
    - # corner case: all users have valid emails
      - "`pd.DataFrame({'user_id': [1, 2, 3], 'name': ['Winston', 'Jonathan', 'Annabelle'], 'mail': ['winston@leetcode.com', 'jonathan@leetcode.com', 'bella-@leetcode.com']})`"
    - # corner case: all users have the same email
      - "`pd.DataFrame({'user_id': [1, 2, 3], 'name': ['Winston', 'Jonathan', 'Annabelle'], 'mail': ['winston@leetcode.com', 'winston@leetcode.com', 'winston@leetcode.com']})`"
    - # corner case: from leetcode
      - "`pd.DataFrame({'user_id': [1], 'name': 'Winston', 'mail': ['winston@leetcode?com']})`"
    - # corner case: multiple @
      - "`pd.DataFrame({'user_id': [1], 'name': 'Winston', 'mail': ['winston@@leetcode.com']})`"
    - # corner case: only leetcode
      - "`pd.DataFrame({'user_id': [1], 'name': 'Winston', 'mail': ['@leetcode.com']})`"
    - | # random case
      ```
      import string
      def _generate():
        import random
        emails = []
        for i in range(10000):
          val = np.random.uniform(0, 1)
          if val < 0.5:
            ending = "@leetcode.com"
          else:
            ending = random.choice(["", "@gmail.com", "@leetcodecom", "@", "@leetcode", "leetcode.com", "com", "@leetcode.com.com"])
            prefix_choosing_from = string.ascii_letters + string.digits + "_-."
            if val > 0.8:
              prefix_choosing_from += string.punctuation
            prefix = "".join(random.choices(prefix_choosing_from, k=random.randint(1, 15)))
          emails.append(f"{prefix}{ending}")
        return pd.DataFrame({"user_id": range(1, 10001), "name": ["".join(random.choices(string.ascii_letters, k=random.randint(1, 15))) for _ in range(10000)], "mail": emails}),
      ```
"""

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Use regex to filter valid emails
    valid_email_pattern = r"^[a-zA-Z][\w\.-]*@leetcode\.com$"
    valid_users = users[users["mail"].str.match(valid_email_pattern)]
    return valid_users
