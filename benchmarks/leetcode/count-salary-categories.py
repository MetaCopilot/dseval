'''
### Description ###

Table: `Accounts`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.
```

Write a solutionto calculate the number of bank accounts for each salary category. The salary categories are:

* `"Low Salary"`: All the salaries **strictly less** than `$20000`.
* `"Average Salary"`: All the salaries in the **inclusive** range `[$20000, $50000]`.
* `"High Salary"`: All the salaries **strictly greater** than `$50000`.

The result table **must** contain all three categories. If there are no accounts in a category,return`0`.

Return the result table in **any order**.

Theresult format is in the following example.

**Example 1:**

```
**Input:** 
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
**Output:** 
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
**Explanation:** 
Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.
```

### Schema ###

data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
Accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})

### Code snippet ###

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame`.

  `accounts` is a DataFrame with the following columns:
  - account_id: int
  - income: int
  Each row contains information about the monthly income for one bank account.

  The function should calculate the number of bank accounts for each salary category. The salary categories are:
  - "Low Salary": All the salaries **strictly less** than $20000.
  - "Average Salary": All the salaries in the **inclusive** range [$20000, $50000].
  - "High Salary": All the salaries **strictly greater** than $50000.

  The result table **must** contain all three categories. If there are no accounts in a category, return `0`.

  Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  Accounts table:
  +------------+--------+
  | account_id | income |
  +------------+--------+
  | 3          | 108939 |
  | 2          | 12747  |
  | 8          | 87709  |
  | 6          | 91796  |
  +------------+--------+
  ```

  Example output:
  ```
  +----------------+----------------+
  | category       | accounts_count |
  +----------------+----------------+
  | Low Salary     | 1              |
  | Average Salary | 0              |
  | High Salary    | 3              |
  +----------------+----------------+
  ```

  Example explanation:
  - Low Salary: Account 2.
  - Average Salary: No accounts.
  - High Salary: Accounts 3, 6, and 8.

validator:
  table_test:
    function_name: count_salary_categories
    input_validator: |
      def _validate(accounts):
        assert accounts.shape[0] > 0
        assert accounts.dtypes.equals(pd.Series({'account_id': 'int64', 'income': 'int64'}))
        assert accounts.account_id.is_unique
        assert accounts.income.between(0, 1000000).all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'account_id': [3, 2, 8, 6], 'income': [108939, 12747, 87709, 91796]})`"
    - # corner case: only one account
      - "`pd.DataFrame({'account_id': [1], 'income': [1000000]})`"
    - # corner case: all accounts have the same income
      - "`pd.DataFrame({'account_id': [1, 2, 3], 'income': [50000, 50000, 50000]})`"
    - # corner case: all accounts have different categories
      - "`pd.DataFrame({'account_id': [1, 2, 3], 'income': [19999, 20000, 50001]})`"
    - # corner case: all accounts have the same category
      - "`pd.DataFrame({'account_id': [1, 2, 3], 'income': [20000, 30000, 50000]})`"
    - | # generate random cases
      ```
      def _generate():
        accounts = pd.DataFrame({'account_id': np.arange(1, 1001), 'income': np.random.randint(0, 1000001, 1000)})
        return accounts,
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

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [
            accounts[accounts.income < 20000].shape[0],
            accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[0],
            accounts[accounts.income > 50000].shape[0],
        ],
    })
