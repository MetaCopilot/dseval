'''
### Description ###

Table: `Customers`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.
```

Table: `Orders`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
```

Write a solution to find all customers who never order anything.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
**Output:** 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

### Schema ###

data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
Customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
Orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

### Code snippet ###

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame`.

  `customers` is a DataFrame with the following columns:
  - id: int
  - name: str
  Each row of this table indicates the ID and name of a customer.

  `orders` is a DataFrame with the following columns:
  - id: int
  - customerId: int
  Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

  The function should return all customers who never order anything. Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  customers:
  +----+-------+
  | id | name  |
  +----+-------+
  | 1  | Joe   |
  | 2  | Henry |
  | 3  | Sam   |
  | 4  | Max   |
  +----+-------+
  orders:
  +----+------------+
  | id | customerId |
  +----+------------+
  | 1  | 3          |
  | 2  | 1          |
  +----+------------+
  ```

  Example output:
  ```
  +-----------+
  | Customers |
  +-----------+
  | Henry     |
  | Max       |
  +-----------+
  ```

validator:
  table_test:
    function_name: find_customers
    input_validator: |
      def _validate(customers, orders):
        assert customers.shape[0] > 0 and orders.shape[0] > 0
        assert customers.dtypes.equals(pd.Series({'id': 'int64', 'name': 'object'}))
        assert orders.dtypes.equals(pd.Series({'id': 'int64', 'customerId': 'int64'}))
        assert customers.id.is_unique
        assert orders.id.is_unique
        assert orders.customerId.isin(customers.id).all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['Joe', 'Henry', 'Sam', 'Max']})`"
      - "`pd.DataFrame({'id': [1, 2], 'customerId': [3, 1]})`"
    - # corner case: only one customer
      - "`pd.DataFrame({'id': [1], 'name': ['Joe']})`"
      - "`pd.DataFrame({'id': [1], 'customerId': [1]})`"
    - # corner case: all customers never order anything
      - "`pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['Joe', 'Henry', 'Sam', 'Max']})`"
      - "`pd.DataFrame({'id': [1, 2], 'customerId': [3, 1]})`"
    - # corner case: all customers order something
      - "`pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['Joe', 'Henry', 'Sam', 'Max']})`"
      - "`pd.DataFrame({'id': [1, 2, 3, 4], 'customerId': [1, 2, 3, 4]})`"
    - | # random cases
      ```
      def _generate():
        customers = pd.DataFrame({'id': np.arange(1, 1001), 'name': [f'Customer {i}' for i in range(1, 1001)]})
        orders = pd.DataFrame({'id': np.arange(1, 1001), 'customerId': np.random.choice(customers.id, 1000)})
        return customers, orders
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

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge customers and orders dataframes on customerId and id
    merged_df = customers.merge(orders, left_on="id", right_on="customerId", how="left")

    # Find customers who never order anything by checking for NaN values in the orders id column
    no_orders = merged_df[merged_df["id_y"].isna()]

    # Return the result table with only the customer names
    return no_orders[["name"]].rename(columns={"name": "Customers"})
