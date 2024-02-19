'''
### Description ###

Table: `DailySales`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| date_id     | date    |
| make_name   | varchar |
| lead_id     | int     |
| partner_id  | int     |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
The name consists of only lowercase English letters.
```

For each `date_id` and `make_name`, find the number of **distinct** `lead_id`'s and **distinct** `partner_id`'s.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
DailySales table:
+-----------+-----------+---------+------------+
| date_id   | make_name | lead_id | partner_id |
+-----------+-----------+---------+------------+
| 2020-12-8 | toyota    | 0       | 1          |
| 2020-12-8 | toyota    | 1       | 0          |
| 2020-12-8 | toyota    | 1       | 2          |
| 2020-12-7 | toyota    | 0       | 2          |
| 2020-12-7 | toyota    | 0       | 1          |
| 2020-12-8 | honda     | 1       | 2          |
| 2020-12-8 | honda     | 2       | 1          |
| 2020-12-7 | honda     | 0       | 1          |
| 2020-12-7 | honda     | 1       | 2          |
| 2020-12-7 | honda     | 2       | 1          |
+-----------+-----------+---------+------------+
**Output:** 
+-----------+-----------+--------------+-----------------+
| date_id   | make_name | unique_leads | unique_partners |
+-----------+-----------+--------------+-----------------+
| 2020-12-8 | toyota    | 2            | 3               |
| 2020-12-7 | toyota    | 1            | 2               |
| 2020-12-8 | honda     | 2            | 2               |
| 2020-12-7 | honda     | 3            | 2               |
+-----------+-----------+--------------+-----------------+
**Explanation:** 
For 2020-12-8, toyota gets leads = [0, 1] and partners = [0, 1, 2] while honda gets leads = [1, 2] and partners = [1, 2].
For 2020-12-7, toyota gets leads = [0] and partners = [1, 2] while honda gets leads = [0, 1, 2] and partners = [1, 2].
```

### Schema ###

data = [['2020-12-8', 'toyota', 0, 1], ['2020-12-8', 'toyota', 1, 0], ['2020-12-8', 'toyota', 1, 2], ['2020-12-7', 'toyota', 0, 2], ['2020-12-7', 'toyota', 0, 1], ['2020-12-8', 'honda', 1, 2], ['2020-12-8', 'honda', 2, 1], ['2020-12-7', 'honda', 0, 1], ['2020-12-7', 'honda', 1, 2], ['2020-12-7', 'honda', 2, 1]]
DailySales = pd.DataFrame(data, columns=['date_id', 'make_name', 'lead_id', 'partner_id']).astype({'date_id':'datetime64[ns]', 'make_name':'object', 'lead_id':'Int64', 'partner_id':'Int64'})

### Code snippet ###

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame`.

  `daily_sales` is a DataFrame with the following columns:
  - date_id: datetime
  - make_name: str
  - lead_id: int
  - partner_id: int
  `daily_sales` contains the date and the name of the product sold and the IDs of the lead and partner it was sold to. The name consists of only lowercase English letters.

  For each `date_id` and `make_name`, find the number of **distinct** `lead_id`'s and **distinct** `partner_id`'s.

  Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  DailySales table:
  +-----------+-----------+---------+------------+
  | date_id   | make_name | lead_id | partner_id |
  +-----------+-----------+---------+------------+
  | 2020-12-8 | toyota    | 0       | 1          |
  | 2020-12-8 | toyota    | 1       | 0          |
  | 2020-12-8 | toyota    | 1       | 2          |
  | 2020-12-7 | toyota    | 0       | 2          |
  | 2020-12-7 | toyota    | 0       | 1          |
  | 2020-12-8 | honda     | 1       | 2          |
  | 2020-12-8 | honda     | 2       | 1          |
  | 2020-12-7 | honda     | 0       | 1          |
  | 2020-12-7 | honda     | 1       | 2          |
  | 2020-12-7 | honda     | 2       | 1          |
  +-----------+-----------+---------+------------+
  ```

  Example output:
  ```
  +-----------+-----------+--------------+-----------------+
  | date_id   | make_name | unique_leads | unique_partners |
  +-----------+-----------+--------------+-----------------+
  | 2020-12-8 | toyota    | 2            | 3               |
  | 2020-12-7 | toyota    | 1            | 2               |
  | 2020-12-8 | honda     | 2            | 2               |
  | 2020-12-7 | honda     | 3            | 2               |
  +-----------+-----------+--------------+-----------------+
  ```

  Example explanation:
  - For 2020-12-8, toyota gets leads = [0, 1] and partners = [0, 1, 2] while honda gets leads = [1, 2] and partners = [1, 2].
  - For 2020-12-7, toyota gets leads = [0] and partners = [1, 2] while honda gets leads = [0, 1, 2] and partners = [1, 2].

validator:
  table_test:
    function_name: daily_leads_and_partners
    input_validator: |
      def _validate(daily_sales):
        assert daily_sales.shape[0] > 0
        assert daily_sales.dtypes.equals(pd.Series({'date_id': 'datetime64[ns]', 'make_name': 'object', 'lead_id': 'int64', 'partner_id': 'int64'}))
        assert daily_sales.date_id.between('2000-01-01', '2099-12-31').all()
        assert daily_sales.make_name.str.match(r'^[a-z]+$').all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'date_id': pd.to_datetime(['2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7']), 'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota', 'honda', 'honda', 'honda', 'honda', 'honda'], 'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2], 'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]})`"
    - # corner case where all the trips are in the date range
      - "`pd.DataFrame({'date_id': pd.to_datetime(['2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7']), 'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota', 'honda', 'honda', 'honda', 'honda', 'honda'], 'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2], 'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]})`"
    - # corner case where all the trips are in the date range
      - "`pd.DataFrame({'date_id': pd.to_datetime(['2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7']), 'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota', 'honda', 'honda', 'honda', 'honda', 'honda'], 'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2], 'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]})`"
    - | # generate random cases
      ```
      def _generate():
        dates = pd.date_range('2020-12-01', '2020-12-31')
        makes = ['toyota', 'honda', 'ford', 'chevrolet', 'nissan', 'bmw', 'mercedes', 'audi', 'volkswagen', 'porsche']
        daily_sales = pd.DataFrame({'date_id': np.random.choice(dates, 1000), 'make_name': np.random.choice(makes, 1000), 'lead_id': np.random.randint(0, 1000, 1000), 'partner_id': np.random.randint(0, 1000, 1000)})
        return daily_sales,
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

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # Group by date_id and make_name, then count the distinct lead_id's and partner_id's
    result = (
        daily_sales.groupby(["date_id", "make_name"])
        .agg({"lead_id": "nunique", "partner_id": "nunique"})
        .reset_index()
    )

    # Rename the columns for clarity
    result.columns = ["date_id", "make_name", "unique_leads", "unique_partners"]

    return result
