'''
### Description ###

Table: `Store`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| bill_id     | int  |
| customer_id | int  |
| amount      | int  |
+-------------+------+
bill_id is the primary key (column with unique values) for this table.
Each row contains information about the amount of one bill and the customer associated with it.
```

Write a solution to report the number of customers who had **at least one** bill with an amount **strictly greater** than `500`.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Store table:
+---------+-------------+--------+
| bill_id | customer_id | amount |
+---------+-------------+--------+
| 6       | 1           | 549    |
| 8       | 1           | 834    |
| 4       | 2           | 394    |
| 11      | 3           | 657    |
| 13      | 3           | 257    |
+---------+-------------+--------+
**Output:** 
+------------+
| rich_count |
+------------+
| 2          |
+------------+
**Explanation:** 
Customer 1 has two bills with amounts strictly greater than 500.
Customer 2 does not have any bills with an amount strictly greater than 500.
Customer 3 has one bill with an amount strictly greater than 500.
```

### Schema ###

data = [[6, 1, 549], [8, 1, 834], [4, 2, 394], [11, 3, 657], [13, 3, 257]]
Store = pd.DataFrame(data, columns=['bill_id', 'customer_id', 'amount']).astype({'bill_id':'int64', 'customer_id':'int64', 'amount':'int64'})

### Code snippet ###

import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame`.

  `store` is a DataFrame with the following columns:
  - bill_id: int
  - customer_id: int
  - amount: int
  Each row contains information about the amount of one bill and the customer associated with it.

  The function should report the number of customers who had **at least one** bill with an amount **strictly greater** than `500`.

  The result format is in the following example.

  Example input:
  ```
  store:
  +---------+-------------+--------+
  | bill_id | customer_id | amount |
  +---------+-------------+--------+
  | 6       | 1           | 549    |
  | 8       | 1           | 834    |
  | 4       | 2           | 394    |
  | 11      | 3           | 657    |
  | 13      | 3           | 257    |
  +---------+-------------+--------+
  ```

  Example output:
  ```
  +------------+
  | rich_count |
  +------------+
  | 2          |
  +------------+
  ```

  Example explanation:
  - Customer 1 has two bills with amounts strictly greater than 500.
  - Customer 2 does not have any bills with an amount strictly greater than 500.
  - Customer 3 has one bill with an amount strictly greater than 500.

validator:
  table_test:
    function_name: count_rich_customers
    input_validator: |
      def _validate(store):
        assert store.shape[0] > 0
        assert store.dtypes.equals(pd.Series({'bill_id': 'int64', 'customer_id': 'int64', 'amount': 'int64'}))
        assert store.bill_id.is_unique
        assert store.customer_id.between(1, 1000).all()
        assert store.amount.between(1, 1000).all()

    test_cases:
    - # example
      - "`pd.DataFrame({'bill_id': [6, 8, 4, 11, 13], 'customer_id': [1, 1, 2, 3, 3], 'amount': [549, 834, 394, 657, 257]})`"
    - # corner case: only one customer
      - "`pd.DataFrame({'bill_id': [1, 2, 3], 'customer_id': [1, 1, 1], 'amount': [100, 200, 300]})`"
    - # corner case: all customers have bills with amount > 500
      - "`pd.DataFrame({'bill_id': [1, 2, 3], 'customer_id': [1, 2, 3], 'amount': [600, 700, 800]})`"
    - # corner case: no customers have bills with amount > 500
      - "`pd.DataFrame({'bill_id': [1, 2, 3], 'customer_id': [1, 2, 3], 'amount': [100, 200, 300]})`"
    - # corner case: strictly greater than 500
      - "`pd.DataFrame({'bill_id': [1, 2, 3, 4, 5, 6], 'customer_id': [1, 1, 2, 2, 3, 3], 'amount': [499, 500, 500, 501, 501, 502]})`"
    - | # random cases
      ```
      def _generate():
        store = pd.DataFrame({'bill_id': np.arange(1, 1001), 'customer_id': np.random.choice(np.arange(1, 101), 1000), 'amount': np.random.choice(np.arange(1, 1001), 1000)})
        return store,
      ```
    # 10 more random cases
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

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    # Filter the store DataFrame to only include bills with an amount greater than 500
    rich_bills = store[store["amount"] > 500]

    # Count the number of unique customer_ids in the filtered DataFrame
    rich_count = rich_bills["customer_id"].nunique()

    # Return the result as a DataFrame with a single row and column
    return pd.DataFrame({"rich_count": [rich_count]})
