'''
### Description ###

Table: `Products`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.
```

Write a solution to rearrange the `Products` table so that each row has `(product_id, store, price)`. If a product is not available in a store, do **not** include a row with that `product_id` and `store` combination in the result table.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
**Output:** 
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+
**Explanation:** 
Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.
```

### Schema ###

data = [[0, 95, 100, 105], [1, 70, None, 80]]
Products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype({'product_id':'int64', 'store1':'int64', 'store2':'int64', 'store3':'int64'})

### Code snippet ###

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame`.

  `products` is a DataFrame with the following columns:
  - product_id: int
  - store1: int or None
  - store2: int or None
  - store3: int or None
  `products` contains the product's price in 3 different stores: store1, store2, and store3. If the product is not available in a store, the price will be None in that store's column.

  The function should rearrange the `Products` table so that each row has `(product_id, store, price)`. If a product is not available in a store, do **not** include a row with that `product_id` and `store` combination in the result table.

  Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  Products table:
  +------------+--------+--------+--------+
  | product_id | store1 | store2 | store3 |
  +------------+--------+--------+--------+
  | 0          | 95     | 100    | 105    |
  | 1          | 70     | null   | 80     |
  +------------+--------+--------+--------+
  ```

  Example output:
  ```
  +------------+--------+-------+
  | product_id | store  | price |
  +------------+--------+-------+
  | 0          | store1 | 95    |
  | 0          | store2 | 100   |
  | 0          | store3 | 105   |
  | 1          | store1 | 70    |
  | 1          | store3 | 80    |
  +------------+--------+-------+
  ```

  Example explanation:
  - Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
  - Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.

validator:
  table_test:
    function_name: rearrange_products_table
    input_validator: |
      def _validate(products):
        assert products.shape[0] > 0
        assert products.dtypes.equals(pd.Series({'product_id': 'int64', 'store1': 'Int64', 'store2': 'Int64', 'store3': 'Int64'}))
        assert products.product_id.is_unique
        assert ((products.store1 >= 0) | products.store1.isnull()).all()
        assert ((products.store2 >= 0) | products.store2.isnull()).all()
        assert ((products.store3 >= 0) | products.store3.isnull()).all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'product_id': [0, 1], 'store1': pd.array([95, 70], dtype='Int64'), 'store2': pd.array([100, None], dtype='Int64'), 'store3': pd.array([105, 80], dtype='Int64')})`"
    - # corner case: only one product
      - "`pd.DataFrame({'product_id': [0], 'store1': pd.array([95], dtype='Int64'), 'store2': pd.array([100], dtype='Int64'), 'store3': pd.array([105], dtype='Int64')})`"
    - # corner case: only one store has the product
      - "`pd.DataFrame({'product_id': [0], 'store1': pd.array([95], dtype='Int64'), 'store2': pd.array([None], dtype='Int64'), 'store3': pd.array([None], dtype='Int64')})`"
    - # corner case: all stores have the product
      - "`pd.DataFrame({'product_id': [0], 'store1': pd.array([95], dtype='Int64'), 'store2': pd.array([100], dtype='Int64'), 'store3': pd.array([105], dtype='Int64')})`"
    - # corner case: no store has the product
      - "`pd.DataFrame({'product_id': [0], 'store1': pd.array([None], dtype='Int64'), 'store2': pd.array([None], dtype='Int64'), 'store3': pd.array([None], dtype='Int64')})`"
    - | # generate random cases
      ```
      def _generate():
        products = pd.DataFrame({'product_id': np.arange(1, 1001), 'store1': pd.array(np.random.choice([None] + list(range(1, 101)), 1000), dtype='Int64'), 'store2': pd.array(np.random.choice([None] + list(range(1, 101)), 1000), dtype='Int64'), 'store3': pd.array(np.random.choice([None] + list(range(1, 101)), 1000), dtype='Int64')})
        return products,
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

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Melt the products DataFrame to have product_id, store, and price columns
    melted_products = products.melt(
        id_vars="product_id", var_name="store", value_name="price"
    )

    # Remove rows with None price (product not available in the store)
    melted_products = melted_products[melted_products["price"].notna()]

    return melted_products
