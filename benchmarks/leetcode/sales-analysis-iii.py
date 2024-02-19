'''
### Description ###

Table: `Product`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the name and the price of each product.
```

Table: `Sales`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |
+-------------+---------+
This table can have duplicate rows.
product_id is a foreign key (reference column) to the Product table.
Each row of this table contains some information about one sale.
```

Write a solution toreportthe **products** that were **only** sold in the first quarter of `2019`. That is, between `2019-01-01` and `2019-03-31` inclusive.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Product table:
+------------+--------------+------------+
| product_id | product_name | unit_price |
+------------+--------------+------------+
| 1          | S8           | 1000       |
| 2          | G4           | 800        |
| 3          | iPhone       | 1400       |
+------------+--------------+------------+
Sales table:
+-----------+------------+----------+------------+----------+-------+
| seller_id | product_id | buyer_id | sale_date  | quantity | price |
+-----------+------------+----------+------------+----------+-------+
| 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
| 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
| 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
+-----------+------------+----------+------------+----------+-------+
**Output:** 
+-------------+--------------+
| product_id  | product_name |
+-------------+--------------+
| 1           | S8           |
+-------------+--------------+
**Explanation:** 
The product with id 1 was only sold in the spring of 2019.
The product with id 2 was sold in the spring of 2019 but was also sold after the spring of 2019.
The product with id 3 was sold after spring 2019.
We return only product 1 as it is the product that was only sold in the spring of 2019.
```

### Schema ###

data = [[1, 'S8', 1000], [2, 'G4', 800], [3, 'iPhone', 1400]]
Product = pd.DataFrame(data, columns=['product_id', 'product_name', 'unit_price']).astype({'product_id':'Int64', 'product_name':'object', 'unit_price':'Int64'})
data = [[1, 1, 1, '2019-01-21', 2, 2000], [1, 2, 2, '2019-02-17', 1, 800], [2, 2, 3, '2019-06-02', 1, 800], [3, 3, 4, '2019-05-13', 2, 2800]]
Sales = pd.DataFrame(data, columns=['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price']).astype({'seller_id':'Int64', 'product_id':'Int64', 'buyer_id':'Int64', 'sale_date':'datetime64[ns]', 'quantity':'Int64', 'price':'Int64'})

### Code snippet ###

import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame`.

  `product` is a DataFrame with the following columns:
  - product_id: int
  - product_name: str
  - unit_price: int
  Each row of this table indicates the name and the price of each product.

  `sales` is a DataFrame with the following columns:
  - seller_id: int
  - product_id: int
  - buyer_id: int
  - sale_date: datetime
  - quantity: int
  - price: int
  Each row of this table contains some information about one sale.

  The function should report the **products** that were **only** sold in the first quarter of `2019`. That is, between `2019-01-01` and `2019-03-31` inclusive.

  Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  product:
  +------------+--------------+------------+
  | product_id | product_name | unit_price |
  +------------+--------------+------------+
  | 1          | S8           | 1000       |
  | 2          | G4           | 800        |
  | 3          | iPhone       | 1400       |
  +------------+--------------+------------+
  sales:
  +-----------+------------+----------+------------+----------+-------+
  | seller_id | product_id | buyer_id | sale_date  | quantity | price |
  +-----------+------------+----------+------------+----------+-------+
  | 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
  | 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
  | 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
  | 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
  +-----------+------------+----------+------------+----------+-------+
  ```

  Example output:
  ```
  +-------------+--------------+
  | product_id  | product_name |
  +-------------+--------------+
  | 1           | S8           |
  +-------------+--------------+
  ```

  Example explanation:
  - The product with id 1 was only sold in the spring of 2019.
  - The product with id 2 was sold in the spring of 2019 but was also sold after the spring of 2019.
  - The product with id 3 was sold after spring 2019.
  - We return only product 1 as it is the product that was only sold in the spring of 2019.

validator:
  table_test:
    function_name: sales_analysis
    input_validator: |
      def _validate(product, sales):
        assert product.shape[0] > 0 and sales.shape[0] > 0
        assert product.dtypes.equals(pd.Series({'product_id': 'int64', 'product_name': 'object', 'unit_price': 'int64'}))
        assert sales.dtypes.equals(pd.Series({'seller_id': 'int64', 'product_id': 'int64', 'buyer_id': 'int64', 'sale_date': 'datetime64[ns]', 'quantity': 'int64', 'price': 'int64'}))
        assert product.product_id.is_unique
        assert sales.product_id.isin(product.product_id).all()
        assert sales.sale_date.between('2018-01-01', '2020-12-31').all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'product_id': [1, 2, 3], 'product_name': ['S8', 'G4', 'iPhone'], 'unit_price': [1000, 800, 1400]})`"
      - "`pd.DataFrame({'seller_id': [1, 1, 2, 3], 'product_id': [1, 2, 2, 3], 'buyer_id': [1, 2, 3, 4], 'sale_date': pd.to_datetime(['2019-01-21', '2019-02-17', '2019-06-02', '2019-05-13']), 'quantity': [2, 1, 1, 2], 'price': [2000, 800, 800, 2800]})`"
    - # corner case: no products sold in the first quarter of 2019
      - "`pd.DataFrame({'product_id': [1, 2, 3], 'product_name': ['S8', 'G4', 'iPhone'], 'unit_price': [1000, 800, 1400]})`"
      - "`pd.DataFrame({'seller_id': [1, 1, 2, 3], 'product_id': [1, 2, 2, 3], 'buyer_id': [1, 2, 3, 4], 'sale_date': pd.to_datetime(['2019-04-21', '2019-04-17', '2019-06-02', '2019-05-13']), 'quantity': [2, 1, 1, 2], 'price': [2000, 800, 800, 2800]})`"
    - # corner case: all products sold in the first quarter of 2019
      - "`pd.DataFrame({'product_id': [1, 2, 3], 'product_name': ['S8', 'G4', 'iPhone'], 'unit_price': [1000, 800, 1400]})`"
      - "`pd.DataFrame({'seller_id': [1, 1, 2, 3], 'product_id': [1, 2, 2, 3], 'buyer_id': [1, 2, 3, 4], 'sale_date': pd.to_datetime(['2019-01-21', '2019-02-17', '2019-03-02', '2019-03-13']), 'quantity': [2, 1, 1, 2], 'price': [2000, 800, 800, 2800]})`"
    - | # generate random cases
      ```
      def _generate():
        product = pd.DataFrame({'product_id': np.arange(1, 1001), 'product_name': [f'Product {i}' for i in range(1, 1001)], 'unit_price': np.random.randint(100, 10000, 1000)})
        sales = pd.DataFrame({'seller_id': np.random.randint(1, 1001, 1000), 'product_id': np.random.choice(product.product_id, 1000), 'buyer_id': np.random.randint(1, 1001, 1000), 'sale_date': pd.Series(np.random.choice(pd.date_range('2018-12-31', '2020-01-31'), 1000)), 'quantity': np.random.randint(1, 11, 1000), 'price': np.random.randint(100, 10000, 1000)})
        return product, sales
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

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # Filter sales to only include those in the first quarter of 2019
    sales_q1 = sales[sales["sale_date"].between("2019-01-01", "2019-03-31")]

    # Find the unique product_ids sold in the first quarter
    q1_products = set(sales_q1["product_id"].unique())

    # Filter sales to only include those outside the first quarter of 2019
    sales_not_q1 = sales[~sales["sale_date"].between("2019-01-01", "2019-03-31")]

    # Find the unique product_ids sold outside the first quarter
    not_q1_products = set(sales_not_q1["product_id"].unique())

    # Find the products that were only sold in the first quarter
    only_q1_products = q1_products - not_q1_products

    # Filter the product DataFrame to only include the products that were only sold in the first quarter
    result = product[product["product_id"].isin(only_q1_products)]

    return result[["product_id", "product_name"]]
