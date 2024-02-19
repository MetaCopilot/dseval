'''
### Description ###

Table: `Products`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
```

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**
```

**Input:** 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
**Output:** 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
**Explanation:** Only products 1 and 3 are both low fat and recyclable.

```

### Schema ###

data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
Products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})

### Code snippet ###

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def find_products(products: pd.DataFrame) -> pd.DataFrame`.

  `products` is a DataFrame with the following columns:
  - product_id: int
  - low_fats: str
  - recyclable: str
  `products` holds all products. Each product has a unique `product_id`. `low_fats` must be either 'Y' or 'N', where 'Y' means this product is low fat and 'N' means it is not. `recyclable` must be either 'Y' or 'N', where 'Y' means this product is recyclable and 'N' means it is not.

  The function should return the ids of products that are both low fat and recyclable. Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  products:
  +-------------+----------+------------+
  | product_id  | low_fats | recyclable |
  +-------------+----------+------------+
  | 0           | Y        | N          |
  | 1           | Y        | Y          |
  | 2           | N        | Y          |
  | 3           | Y        | Y          |
  | 4           | N        | N          |
  +-------------+----------+------------+
  ```

  Example output:
  ```
  +-------------+
  | product_id  |
  +-------------+
  | 1           |
  | 3           |
  +-------------+
  ```

  Example explanation: Only products 1 and 3 are both low fat and recyclable.

validator:
  table_test:
    function_name: find_products
    input_validator: |
      def _validate(products):
        assert products.shape[0] > 0
        assert products.dtypes.equals(pd.Series({'product_id': 'int64', 'low_fats': 'object', 'recyclable': 'object'}))
        assert products.product_id.is_unique
        assert products.low_fats.isin(['Y', 'N']).all()
        assert products.recyclable.isin(['Y', 'N']).all()

    output_checker:
      ignore_order: true
        
    test_cases:
    - # example
      - "`pd.DataFrame({'product_id': [0, 1, 2, 3, 4], 'low_fats': ['Y', 'Y', 'N', 'Y', 'N'], 'recyclable': ['N', 'Y', 'Y', 'Y', 'N']})`"
    - # corner case: no products are both low fat and recyclable
      - "`pd.DataFrame({'product_id': [0, 1, 2, 3, 4], 'low_fats': ['Y', 'Y', 'N', 'Y', 'N'], 'recyclable': ['N', 'N', 'Y', 'N', 'N']})`"
    - # corner case: all products are both low fat and recyclable
      - "`pd.DataFrame({'product_id': [0, 1, 2, 3, 4], 'low_fats': ['Y', 'Y', 'Y', 'Y', 'Y'], 'recyclable': ['Y', 'Y', 'Y', 'Y', 'Y']})`"
    - # corner case: only one product
      - "`pd.DataFrame({'product_id': [0], 'low_fats': ['Y'], 'recyclable': ['Y']})`"
    - # corner case: product_id is not ordered
      - "`pd.DataFrame({'product_id': [4, 2, 3, 1, 0], 'low_fats': ['Y', 'Y', 'N', 'Y', 'N'], 'recyclable': ['N', 'Y', 'Y', 'Y', 'N']})`"
"""

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # Filter products that are both low fat and recyclable
    result = products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")]

    # Return only the product_id column
    return result[["product_id"]]
