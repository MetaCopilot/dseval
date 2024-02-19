'''
### Description ###

Table: `Orders`

```
+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.
```

Write a solution to find the `customer_number` for the customer who has placed **the largest number of orders**.

The test cases are generated so that **exactly one customer** will have placed more orders than any other customer.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+
**Output:** 
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+
**Explanation:** 
The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
So the result is customer_number 3.
```

**Follow up:** What if more than one customer has the largest number of orders, can you find all the `customer_number` in this case?

### Schema ###

data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})

### Code snippet ###

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def largest_orders(orders: pd.DataFrame) -> pd.DataFrame`.

  `orders` is a DataFrame with the following columns:
  - order_number: int
  - customer_number: int
  `orders` contains information about the order ID and the customer ID.

  The function should find the `customer_number` for the customer who has placed **the largest number of orders**. The test cases are generated so that **exactly one customer** will have placed more orders than any other customer.

  The result format is in the following example.

  Example input:
  ```
  orders:
  +--------------+-----------------+
  | order_number | customer_number |
  +--------------+-----------------+
  | 1            | 1               |
  | 2            | 2               |
  | 3            | 3               |
  | 4            | 3               |
  +--------------+-----------------+
  ```

  Example output:
  ```
  +-----------------+
  | customer_number |
  +-----------------+
  | 3               |
  +-----------------+
  ```

  Example explanation:
  The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. So the result is customer_number 3.

validator:
  table_test:
    function_name: largest_orders
    input_validator: |
      def _validate(orders):
        assert orders.shape[0] > 0
        assert orders.dtypes.equals(pd.Series({'order_number': 'int64', 'customer_number': 'int64'}))
        assert orders.order_number.is_unique
        assert orders.customer_number.between(1, 1000).all()
        order_numbers = orders.groupby('customer_number').size()
        assert order_numbers[order_numbers == order_numbers.max()].count() == 1

    output_checker:
      ignore_index: true

    test_cases:
    - # example
      - "`pd.DataFrame({'order_number': [1, 2, 3, 4], 'customer_number': [1, 2, 3, 3]})`"
    - # corner case: only one order
      - "`pd.DataFrame({'order_number': [1], 'customer_number': [1]})`"
    - # corner case: only one customer
      - "`pd.DataFrame({'order_number': [1, 2, 3, 4], 'customer_number': [1, 1, 1, 1]})`"
    - # corner case: id is not ordered
      - "`pd.DataFrame({'order_number': [4, 3, 2, 1], 'customer_number': [1, 2, 3, 3]})`"
    - | # random cases
      ```
      def _generate():
        counts = np.random.choice(np.arange(51, 101), size=np.random.randint(1, 51), replace=False)
        orders = np.arange(1, counts.sum() + 1)
        np.random.shuffle(orders)
        return pd.DataFrame({'order_number': orders, 'customer_number': np.repeat(np.arange(1, counts.size + 1), counts)}),
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

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Count the number of orders for each customer
    customer_counts = orders.groupby("customer_number").size().reset_index(name="count")

    # Find the customer with the largest number of orders
    max_count = customer_counts["count"].max()

    # Filter the customers with the largest number of orders
    result = customer_counts[customer_counts["count"] == max_count]

    # Return the result as a DataFrame with only the customer_number column
    return result[["customer_number"]]
