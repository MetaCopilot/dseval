'''
### Description ###

Table: `Users`

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) of this table.
This table has the info of the users of an online shopping website where users can sell and buy items.
```

Table: `Orders`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the primary key (column with unique values) of this table.
item_id is a foreign key (reference column) to the Items table.
buyer_id and seller_id are foreign keys to the Users table.
```

Table: `Items`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
item_id is the primary key (column with unique values) of this table.
```

Write a solutionto find for each user, the join date and the number of orders they made as a buyer in `2019`.

Return the result table in **any order**.

Theresult format is in the following example.

**Example 1:**

```
**Input:** 
Users table:
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2018-01-01 | Lenovo         |
| 2       | 2018-02-09 | Samsung        |
| 3       | 2018-01-19 | LG             |
| 4       | 2018-05-21 | HP             |
+---------+------------+----------------+
Orders table:
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2018-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2018-08-04 | 1       | 4        | 2         |
| 5        | 2018-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+
Items table:
+---------+------------+
| item_id | item_brand |
+---------+------------+
| 1       | Samsung    |
| 2       | Lenovo     |
| 3       | LG         |
| 4       | HP         |
+---------+------------+
**Output:** 
+-----------+------------+----------------+
| buyer_id  | join_date  | orders_in_2019 |
+-----------+------------+----------------+
| 1         | 2018-01-01 | 1              |
| 2         | 2018-02-09 | 2              |
| 3         | 2018-01-19 | 0              |
| 4         | 2018-05-21 | 0              |
+-----------+------------+----------------+
```

### Schema ###

data = [[1, '2018-01-01', 'Lenovo'], [2, '2018-02-09', 'Samsung'], [3, '2018-01-19', 'LG'], [4, '2018-05-21', 'HP']]
Users = pd.DataFrame(data, columns=['user_id', 'join_date', 'favorite_brand']).astype({'user_id':'Int64', 'join_date':'datetime64[ns]', 'favorite_brand':'object'})
data = [[1, '2019-08-01', 4, 1, 2], [2, '2018-08-02', 2, 1, 3], [3, '2019-08-03', 3, 2, 3], [4, '2018-08-04', 1, 4, 2], [5, '2018-08-04', 1, 3, 4], [6, '2019-08-05', 2, 2, 4]]
Orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'item_id', 'buyer_id', 'seller_id']).astype({'order_id':'Int64', 'order_date':'datetime64[ns]', 'item_id':'Int64', 'buyer_id':'Int64', 'seller_id':'Int64'})
data = [[1, 'Samsung'], [2, 'Lenovo'], [3, 'LG'], [4, 'HP']]
Items = pd.DataFrame(data, columns=['item_id', 'item_brand']).astype({'item_id':'Int64', 'item_brand':'object'})

### Code snippet ###

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

r"""
question: |
  Write a function `def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame`.

  `users` is a DataFrame with the following columns:
  - user_id: int
  - join_date: datetime
  - favorite_brand: str
  It contains the info of the users of an online shopping website where users can sell and buy items.

  `orders` is a DataFrame with the following columns:
  - order_id: int
  - order_date: datetime
  - item_id: int
  - buyer_id: int
  - seller_id: int
  Each `item_id` can be found in `items` DataFrame. Each `buyer_id` and `seller_id` can be found in the `user_id` column of `users` DataFrame.

  `items` is a DataFrame with the following columns:
  - item_id: int
  - item_brand: str

  The function should return: for each user, the join date and the number of orders they made as a buyer in `2019`. The format of the result is in the following example.

  Example input:
  ```
  users:
  +---------+------------+----------------+
  | user_id | join_date  | favorite_brand |
  +---------+------------+----------------+
  | 1       | 2018-01-01 | Lenovo         |
  | 2       | 2018-02-09 | Samsung        |
  | 3       | 2018-01-19 | LG             |
  | 4       | 2018-05-21 | HP             |
  +---------+------------+----------------+
  orders:
  +----------+------------+---------+----------+-----------+
  | order_id | order_date | item_id | buyer_id | seller_id |
  +----------+------------+---------+----------+-----------+
  | 1        | 2019-08-01 | 4       | 1        | 2         |
  | 2        | 2018-08-02 | 2       | 1        | 3         |
  | 3        | 2019-08-03 | 3       | 2        | 3         |
  | 4        | 2018-08-04 | 1       | 4        | 2         |
  | 5        | 2018-08-04 | 1       | 3        | 4         |
  | 6        | 2019-08-05 | 2       | 2        | 4         |
  +----------+------------+---------+----------+-----------+
  items:
  +---------+------------+
  | item_id | item_brand |
  +---------+------------+
  | 1       | Samsung    |
  | 2       | Lenovo     |
  | 3       | LG         |
  | 4       | HP         |
  +---------+------------+
  ```

  Example output:
  ```
  +-----------+------------+----------------+
  | buyer_id  | join_date  | orders_in_2019 |
  +-----------+------------+----------------+
  | 1         | 2018-01-01 | 1              |
  | 2         | 2018-02-09 | 2              |
  | 3         | 2018-01-19 | 0              |
  | 4         | 2018-05-21 | 0              |
  +-----------+------------+----------------+
  ```

validator:
  table_test:
    function_name: market_analysis
    input_validator: |
      def _validate(users, orders, items):
        assert users.shape[0] > 0 and orders.shape[0] > 0 and items.shape[0] > 0
        assert users.dtypes.equals(pd.Series({'user_id': 'int64', 'join_date': 'datetime64[ns]', 'favorite_brand': 'object'}))
        assert orders.dtypes.equals(pd.Series({'order_id': 'int64', 'order_date': 'datetime64[ns]', 'item_id': 'int64', 'buyer_id': 'int64', 'seller_id': 'int64'}))
        assert items.dtypes.equals(pd.Series({'item_id': 'int64', 'item_brand': 'object'}))
        assert users.user_id.is_unique
        assert users.join_date.between('2000-01-01', '2099-12-31').all()
        assert users.favorite_brand.isin(items.item_brand).all()
        assert orders.order_id.is_unique
        assert orders.order_date.between('2000-01-01', '2099-12-31').all()
        assert orders.item_id.isin(items.item_id).all()
        assert orders.buyer_id.isin(users.user_id).all()
        assert orders.seller_id.isin(users.user_id).all()
        assert items.item_id.is_unique
        assert items.item_brand.str.match(r'^\w+$').all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'user_id': [1, 2, 3, 4], 'join_date': pd.to_datetime(['2018-01-01', '2018-02-09', '2018-01-19', '2018-05-21']), 'favorite_brand': ['Lenovo', 'Samsung', 'LG', 'HP']})`"
      - "`pd.DataFrame({'order_id': [1, 2, 3, 4, 5, 6], 'order_date': pd.to_datetime(['2019-08-01', '2018-08-02', '2019-08-03', '2018-08-04', '2018-08-04', '2019-08-05']), 'item_id': [4, 2, 3, 1, 1, 2], 'buyer_id': [1, 1, 2, 4, 3, 2], 'seller_id': [2, 3, 3, 2, 4, 4]})`"
      - "`pd.DataFrame({'item_id': [1, 2, 3, 4], 'item_brand': ['Samsung', 'Lenovo', 'LG', 'HP']})`"
    - # corner case: only one user
      - "`pd.DataFrame({'user_id': [1], 'join_date': pd.to_datetime(['2018-01-01']), 'favorite_brand': ['Lenovo']})`"
      - "`pd.DataFrame({'order_id': [1, 2, 3, 4, 5, 6], 'order_date': pd.to_datetime(['2019-08-01', '2018-08-02', '2019-08-03', '2018-08-04', '2018-08-04', '2019-08-05']), 'item_id': [1, 1, 1, 1, 1, 1], 'buyer_id': [1, 1, 1, 1, 1, 1], 'seller_id': [1, 1, 1, 1, 1, 1]})`"
      - "`pd.DataFrame({'item_id': [1], 'item_brand': ['Lenovo']})`"
    - # corner case: no orders in 2019
      - "`pd.DataFrame({'user_id': [1, 2, 3, 4], 'join_date': pd.to_datetime(['2018-01-01', '2018-02-09', '2018-01-19', '2018-05-21']), 'favorite_brand': ['Lenovo', 'Samsung', 'LG', 'HP']})`"
      - "`pd.DataFrame({'order_id': [1, 2, 3, 4, 5, 6], 'order_date': pd.to_datetime(['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-04', '2018-08-05']), 'item_id': [4, 2, 3, 1, 1, 2], 'buyer_id': [1, 1, 2, 4, 3, 2], 'seller_id': [2, 3, 3, 2, 4, 4]})`"
      - "`pd.DataFrame({'item_id': [1, 2, 3, 4], 'item_brand': ['Samsung', 'Lenovo', 'LG', 'HP']})`"
    - # corner case: id is not ordered
      - "`pd.DataFrame({'user_id': [4, 2, 3, 1], 'join_date': pd.to_datetime(['2018-01-01', '2018-02-09', '2018-01-19', '2018-05-21']), 'favorite_brand': ['Lenovo', 'Samsung', 'LG', 'HP']})`"
      - "`pd.DataFrame({'order_id': [5, 3, 1, 2, 4, 6], 'order_date': pd.to_datetime(['2019-08-01', '2018-08-02', '2019-08-03', '2018-08-04', '2018-08-04', '2019-08-05']), 'item_id': [4, 2, 3, 1, 1, 2], 'buyer_id': [1, 1, 2, 4, 3, 2], 'seller_id': [2, 3, 3, 2, 4, 4]})`"
      - "`pd.DataFrame({'item_id': [2, 3, 1, 4], 'item_brand': ['Samsung', 'Lenovo', 'LG', 'HP']})`"
    - | # random cases
      ```
      def _generate():
        users = pd.DataFrame({
          'user_id': np.arange(1, 1001),
          'join_date': pd.Series(np.random.choice(pd.date_range('2018-07-01', '2020-06-30'), 1000)),
          'favorite_brand': np.random.choice(['Lenovo', 'Samsung', 'LG', 'HP'], size=1000),
        })
        orders = pd.DataFrame({
          'order_id': np.arange(1, 1001),
          'order_date': pd.Series(np.random.choice(pd.date_range('2018-07-01', '2020-06-30'), 1000)),
          'item_id': np.random.choice(np.arange(1, 5), size=1000),
          'buyer_id': np.random.choice(np.arange(1, 1001), size=1000),
          'seller_id': np.random.choice(np.arange(1, 1001), size=1000),
        })
        items = pd.DataFrame({
          'item_id': [2, 3, 1, 4],
          'item_brand': ['Samsung', 'Lenovo', 'LG', 'HP']
        })
        return users, orders, items
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

def market_analysis(
    users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame
) -> pd.DataFrame:

    # Step 1: Filter the orders dataframe to only include orders from the year 2019.
    df = orders.query("order_date.dt.year==2019").merge(
        # Step 2: Merge the filtered orders with the users dataframe on buyer_id and user_id.
        users,
        left_on="buyer_id",
        right_on="user_id",
        how="right",
    )

    # Step 3: Group the merged dataframe by user_id and join_date, then count the number of items (orders) for each user.
    result = df.groupby(["user_id", "join_date"]).item_id.count()

    # Step 4: Format the output by resetting the index and renaming the columns for clarity.
    return result.reset_index().rename(
        columns={"user_id": "buyer_id", "item_id": "orders_in_2019"}
    )