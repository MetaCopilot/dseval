'''
### Description ###

Table `Activities`:

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each row of this table contains the product name and the date it was sold in a market.
```

Write a solution to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by `sell_date`.

Theresult format is in the following example.

**Example 1:**

```
**Input:** 
Activities table:
+------------+------------+
| sell_date  | product     |
+------------+------------+
| 2020-05-30 | Headphone  |
| 2020-06-01 | Pencil     |
| 2020-06-02 | Mask       |
| 2020-05-30 | Basketball |
| 2020-06-01 | Bible      |
| 2020-06-02 | Mask       |
| 2020-05-30 | T-Shirt    |
+------------+------------+
**Output:** 
+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
+------------+----------+------------------------------+
**Explanation:** 
For 2020-05-30, Sold items were (Headphone, Basketball, T-shirt), we sort them lexicographically and separate them by a comma.
For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
For 2020-06-02, the Sold item is (Mask), we just return it.
```

### Schema ###

data = [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], ['2020-06-02', 'Mask'], ['2020-05-30', 'Basketball'], ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], ['2020-05-30', 'T-Shirt']]
Activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype({'sell_date':'datetime64[ns]', 'product':'object'})

### Code snippet ###

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def categorize_products(activities: pd.DataFrame) -> pd.DataFrame`.

  `activities` is a DataFrame with the following columns:
  - sell_date: datetime
  - product: str
  Each row of this table contains the product name and the date it was sold in a market.

  The function should return: for each date the number of different products sold and their names. The sold products names for each date should be sorted lexicographically. Return the result table ordered by `sell_date`.

  The result format is in the following example.

  Example input:
  ```
  activities:
  +------------+------------+
  | sell_date  | product     |
  +------------+------------+
  | 2020-05-30 | Headphone  |
  | 2020-06-01 | Pencil     |
  | 2020-06-02 | Mask       |
  | 2020-05-30 | Basketball |
  | 2020-06-01 | Bible      |
  | 2020-06-02 | Mask       |
  | 2020-05-30 | T-Shirt    |
  +------------+------------+
  ```

  Example output:
  ```
  +------------+----------+------------------------------+
  | sell_date  | num_sold | products                     |
  +------------+----------+------------------------------+
  | 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
  | 2020-06-01 | 2        | Bible,Pencil                 |
  | 2020-06-02 | 1        | Mask                         |
  +------------+----------+------------------------------+
  ```

  Example explanation:
  - For 2020-05-30, Sold items were (Headphone, Basketball, T-shirt), we sort them lexicographically and separate them by a comma.
  - For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
  - For 2020-06-02, the Sold item is (Mask), we just return it.

validator:
  table_test:
    function_name: categorize_products
    input_validator: |
      def _validate(activities):
        assert activities.shape[0] > 0
        assert activities.dtypes.equals(pd.Series({'sell_date': 'datetime64[ns]', 'product': 'object'}))
        assert activities.sell_date.between('2000-01-01', '2099-12-31').all()
        assert activities['product'].str.match(r'^[\w\-]+$').all()

    output_checker:
      ignore_index: true

    test_cases:
    - # example
      - "`pd.DataFrame({'sell_date': pd.to_datetime(['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30']), 'product': ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-Shirt']})`"
    - # corner case: only one product
      - "`pd.DataFrame({'sell_date': pd.to_datetime(['2020-05-30']), 'product': ['Headphone']})`"
    - # corner case: all products are the same
      - "`pd.DataFrame({'sell_date': pd.to_datetime(['2020-05-30', '2020-05-30', '2020-05-30']), 'product': ['Headphone', 'Headphone', 'Headphone']})`"
    - # corner case: all products are different
      - "`pd.DataFrame({'sell_date': pd.to_datetime(['2020-05-30', '2020-05-30', '2020-05-30']), 'product': ['Headphone', 'Pencil', 'Mask']})`"
    - # corner case: all dates are different
      - "`pd.DataFrame({'sell_date': pd.to_datetime(['2020-05-30', '2020-05-31', '2020-06-01']), 'product': ['Headphone', 'Headphone', 'Headphone']})`"
    - | # generate random cases
      ```
      def _generate():
        dates = pd.date_range('2020-05-30', '2020-06-02')
        products = ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'T-Shirt']
        activities = pd.DataFrame({'sell_date': np.random.choice(dates, 1000), 'product': np.random.choice(products, 1000)})
        return activities,
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

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby(
        'sell_date'
    )['product'].agg([  # type: ignore
        ('num_sold', 'nunique'),
        ('products', lambda x: ','.join(sorted(x.unique())))
    ]).reset_index()
