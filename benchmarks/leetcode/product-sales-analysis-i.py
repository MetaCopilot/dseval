'''
### Description ###

Table: `Sales`

```
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.
```

Table: `Product`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.
```

Write a solution to report the `product_name`, `year`, and `price` for each `sale_id` in the `Sales` table.

Return the resulting table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
**Output:** 
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+
**Explanation:** 
From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.
From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.
From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.
```

### Schema ###

data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
Sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype({'sale_id':'Int64', 'product_id':'Int64', 'year':'Int64', 'quantity':'Int64', 'price':'Int64'})
data = [[100, 'Nokia'], [200, 'Apple'], [300, 'Samsung']]
Product = pd.DataFrame(data, columns=['product_id', 'product_name']).astype({'product_id':'Int64', 'product_name':'object'})

### Code snippet ###

import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame`.

  `sales` is a DataFrame with the following columns:
  - sale_id: int
  - product_id: int
  - year: int
  - quantity: int
  - price: int
  Each row of this table shows a sale on the product `product_id` in a certain year. Note that the price is per unit.

  `product` is a DataFrame with the following columns:
  - product_id: int
  - product_name: str
  Each row of this table indicates the product name of each product.

  The function should return the `product_name`, `year`, and `price` for each `sale_id` in the `Sales` table. Return the resulting table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  sales:
  +---------+------------+------+----------+-------+
  | sale_id | product_id | year | quantity | price |
  +---------+------------+------+----------+-------+ 
  | 1       | 100        | 2008 | 10       | 5000  |
  | 2       | 100        | 2009 | 12       | 5000  |
  | 7       | 200        | 2011 | 15       | 9000  |
  +---------+------------+------+----------+-------+
  product:
  +------------+--------------+
  | product_id | product_name |
  +------------+--------------+
  | 100        | Nokia        |
  | 200        | Apple        |
  | 300        | Samsung      |
  +------------+--------------+
  ```

  Example output:
  ```
  +--------------+-------+-------+
  | product_name | year  | price |
  +--------------+-------+-------+
  | Nokia        | 2008  | 5000  |
  | Nokia        | 2009  | 5000  |
  | Apple        | 2011  | 9000  |
  +--------------+-------+-------+
  ```

  Example explanation:
  - From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.
  - From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.
  - From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.

validator:
  table_test:
    function_name: sales_analysis
    input_validator: |
      def _validate(sales, product):
        assert sales.shape[0] > 0 and product.shape[0] > 0
        assert sales.dtypes.equals(pd.Series({'sale_id': 'int64', 'product_id': 'int64', 'year': 'int64', 'quantity': 'int64', 'price': 'int64'}))
        assert product.dtypes.equals(pd.Series({'product_id': 'int64', 'product_name': 'object'}))
        assert sales.sale_id.is_unique
        assert sales.product_id.isin(product.product_id).all()
        assert sales.year.between(2000, 2099).all()
        assert sales.quantity.between(1, 100).all()
        assert sales.price.between(1, 10000).all()
        assert product.product_id.is_unique
        assert product.product_name.str.match(r'^\w+$').all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'sale_id': [1, 2, 7], 'product_id': [100, 100, 200], 'year': [2008, 2009, 2011], 'quantity': [10, 12, 15], 'price': [5000, 5000, 9000]})`"
      - "`pd.DataFrame({'product_id': [100, 200, 300], 'product_name': ['Nokia', 'Apple', 'Samsung']})`"
    - # corner case: only one sale
      - "`pd.DataFrame({'sale_id': [1], 'product_id': [100], 'year': [2008], 'quantity': [10], 'price': [5000]})`"
      - "`pd.DataFrame({'product_id': [100], 'product_name': ['Nokia']})`"
    - # corner case: only one product
      - "`pd.DataFrame({'sale_id': [1, 2, 7], 'product_id': [100, 100, 100], 'year': [2008, 2009, 2011], 'quantity': [10, 12, 15], 'price': [5000, 5000, 9000]})`"
      - "`pd.DataFrame({'product_id': [100], 'product_name': ['Nokia']})`"
    - # corner case: id is not ordered
      - "`pd.DataFrame({'sale_id': [7, 2, 1], 'product_id': [200, 100, 100], 'year': [2011, 2009, 2008], 'quantity': [15, 12, 10], 'price': [9000, 5000, 5000]})`"
      - "`pd.DataFrame({'product_id': [300, 200, 100], 'product_name': ['Samsung', 'Apple', 'Nokia']})`"
    - | # random cases
      ```
      def _generate():
        sales = pd.DataFrame({
          'sale_id': np.arange(1, 1001),
          'product_id': np.random.choice(np.arange(1, 101), 1000),
          'year': np.random.choice(np.arange(2000, 2100), 1000),
          'quantity': np.random.randint(1, 101, 1000),
          'price': np.random.randint(1, 10001, 1000),
        })
        product = pd.DataFrame({
          'product_id': np.arange(1, 101),
          'product_name': [f'Product{i}' for i in range(1, 101)],
        })
        return sales, product
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

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Merge the sales and product dataframes on product_id
    result = sales.merge(product, on="product_id")

    # Select the required columns and rename them for clarity
    result = result[["product_name", "year", "price"]]

    return result
