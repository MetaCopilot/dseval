'''
### Description ###

Table: `Delivery`

```
+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the primary key (column with unique values) of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
```

If the customer's preferred delivery date is the same as the order date, then the order is called **immediate;** otherwise, it is called **scheduled**.

Write a solution to find the percentage of immediate orders in the table, **rounded to 2 decimal places**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 5           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-11                  |
| 4           | 3           | 2019-08-24 | 2019-08-26                  |
| 5           | 4           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
+-------------+-------------+------------+-----------------------------+
**Output:** 
+----------------------+
| immediate_percentage |
+----------------------+
| 33.33                |
+----------------------+
**Explanation:** The orders with delivery id 2 and 3 are immediate while the others are scheduled.
```

### Schema ###

data = [[1, 1, '2019-08-01', '2019-08-02'], [2, 5, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-11'], [4, 3, '2019-08-24', '2019-08-26'], [5, 4, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13']]
Delivery = pd.DataFrame(data, columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype({'delivery_id':'Int64', 'customer_id':'Int64', 'order_date':'datetime64[ns]', 'customer_pref_delivery_date':'datetime64[ns]'})

### Code snippet ###

import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame`.

  `delivery` is a DataFrame with the following columns:
  - delivery_id: int
  - customer_id: int
  - order_date: datetime
  - customer_pref_delivery_date: datetime
  `delivery` holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).

  If the customer's preferred delivery date is the same as the order date, then the order is called **immediate;** otherwise, it is called **scheduled**.

  The function should return the percentage of immediate orders in the table, **rounded to 2 decimal places**.

  The result format is in the following example.

  Example input:
  ```
  Delivery table:
  +-------------+-------------+------------+-----------------------------+
  | delivery_id | customer_id | order_date | customer_pref_delivery_date |
  +-------------+-------------+------------+-----------------------------+
  | 1           | 1           | 2019-08-01 | 2019-08-02                  |
  | 2           | 5           | 2019-08-02 | 2019-08-02                  |
  | 3           | 1           | 2019-08-11 | 2019-08-11                  |
  | 4           | 3           | 2019-08-24 | 2019-08-26                  |
  | 5           | 4           | 2019-08-21 | 2019-08-22                  |
  | 6           | 2           | 2019-08-11 | 2019-08-13                  |
  +-------------+-------------+------------+-----------------------------+
  ```

  Example output:
  ```
  +----------------------+
  | immediate_percentage |
  +----------------------+
  | 33.33                |
  +----------------------+
  ```

  Example explanation: The orders with delivery id 2 and 3 are immediate while the others are scheduled.

validator:
  table_test:
    function_name: food_delivery
    input_validator: |
      def _validate(delivery):
        assert delivery.shape[0] > 0
        assert delivery.dtypes.equals(pd.Series({'delivery_id': 'int64', 'customer_id': 'int64', 'order_date': 'datetime64[ns]', 'customer_pref_delivery_date': 'datetime64[ns]'}))
        assert delivery.delivery_id.is_unique
        assert delivery.customer_id.between(1, 1000).all()
        assert delivery.order_date.between('2000-01-01', '2099-12-31').all()
        assert delivery.customer_pref_delivery_date.between('2000-01-01', '2099-12-31').all()

    output_checker: |
      def compare_fn(expected, output):
        if not np.issubdtype(output['immediate_percentage'], np.number):
          output['immediate_percentage'] = pd.to_numeric(output['immediate_percentage'])
        return {
          'match': expected.sort_values(by=['immediate_percentage']).reset_index(drop=True).equals(output.sort_values(by=['immediate_percentage']).reset_index(drop=True)),
          'reason': ''
        }

    test_cases:
    - # example
      - "`pd.DataFrame({'delivery_id': [1, 2, 3, 4, 5, 6], 'customer_id': [1, 5, 1, 3, 4, 2], 'order_date': pd.to_datetime(['2019-08-01', '2019-08-02', '2019-08-11', '2019-08-24', '2019-08-21', '2019-08-11']), 'customer_pref_delivery_date': pd.to_datetime(['2019-08-02', '2019-08-02', '2019-08-11', '2019-08-26', '2019-08-22', '2019-08-13'])})`"
    - # corner case: only one delivery
      - "`pd.DataFrame({'delivery_id': [1], 'customer_id': [1], 'order_date': pd.to_datetime(['2019-08-01']), 'customer_pref_delivery_date': pd.to_datetime(['2019-08-01'])})`"
    - # corner case: all deliveries are immediate
      - "`pd.DataFrame({'delivery_id': [1, 2, 3], 'customer_id': [1, 2, 3], 'order_date': pd.to_datetime(['2019-08-01', '2019-08-02', '2019-08-03']), 'customer_pref_delivery_date': pd.to_datetime(['2019-08-01', '2019-08-02', '2019-08-03'])})`"
    - # corner case: all deliveries are scheduled
      - "`pd.DataFrame({'delivery_id': [1, 2, 3], 'customer_id': [1, 2, 3], 'order_date': pd.to_datetime(['2019-08-01', '2019-08-02', '2019-08-03']), 'customer_pref_delivery_date': pd.to_datetime(['2019-08-02', '2019-08-03', '2019-08-04'])})`"
    - | # generate random cases
      ```
      def _generate():
        dates = pd.date_range('2019-08-01', '2019-08-31')
        delivery = pd.DataFrame({'delivery_id': np.arange(1, 1001), 'customer_id': np.random.choice(np.arange(1, 1001), 1000), 'order_date': np.random.choice(dates, 1000), 'customer_pref_delivery_date': np.random.choice(dates, 1000)})
        return delivery,
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

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # Calculate the number of immediate orders
    immediate_orders = delivery[delivery["order_date"] == delivery["customer_pref_delivery_date"]].shape[0]

    # Calculate the total number of orders
    total_orders = delivery.shape[0]

    # Calculate the percentage of immediate orders
    immediate_percentage = round((immediate_orders / total_orders) * 100, 2)

    # Return the result as a DataFrame
    return pd.DataFrame({"immediate_percentage": [immediate_percentage]})
