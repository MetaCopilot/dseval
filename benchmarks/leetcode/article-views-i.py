'''
### Description ###

Table: `Views`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
```

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by `id` in ascending order.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
**Output:** 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
```

### Schema ###

data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
Views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})

### Code snippet ###

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def article_views(views: pd.DataFrame) -> pd.DataFrame`.

  `views` is a DataFrame with the following columns:
  - article_id: int
  - author_id: int
  - viewer_id: int
  - view_date: datetime
  Each row of this table indicates that some viewer viewed an article (written by some author) on some date. Note that equal author_id and viewer_id indicate the same person.

  The function should find all the authors that viewed at least one of their own articles. Return the result table sorted by `id` in ascending order.

  The result format is in the following example.

  Example input:
  ```
  views:
  +------------+-----------+-----------+------------+
  | article_id | author_id | viewer_id | view_date  |
  +------------+-----------+-----------+------------+
  | 1          | 3         | 5         | 2019-08-01 |
  | 1          | 3         | 6         | 2019-08-02 |
  | 2          | 7         | 7         | 2019-08-01 |
  | 2          | 7         | 6         | 2019-08-02 |
  | 4          | 7         | 1         | 2019-07-22 |
  | 3          | 4         | 4         | 2019-07-21 |
  | 3          | 4         | 4         | 2019-07-21 |
  +------------+-----------+-----------+------------+
  ```

  Example output:
  ```
  +------+
  | id   |
  +------+
  | 4    |
  | 7    |
  +------+
  ```

validator:
  table_test:
    function_name: article_views
    input_validator: |
      def _validate(views):
        assert views.shape[0] > 0
        assert views.dtypes.equals(pd.Series({'article_id': 'int64', 'author_id': 'int64', 'viewer_id': 'int64', 'view_date': 'datetime64[ns]'}))
        assert views.view_date.between('2000-01-01', '2099-12-31').all()

    output_checker:
      ignore_index: true

    test_cases:
    - # example
      - "`pd.DataFrame({'article_id': [1, 1, 2, 2, 4, 3, 3], 'author_id': [3, 3, 7, 7, 7, 4, 4], 'viewer_id': [5, 6, 7, 6, 1, 4, 4], 'view_date': pd.to_datetime(['2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02', '2019-07-22', '2019-07-21', '2019-07-21'])})`"
    - # corner case: only one view
      - "`pd.DataFrame({'article_id': [1], 'author_id': [1], 'viewer_id': [1], 'view_date': pd.to_datetime(['2019-08-01'])})`"
    - # corner case: no self-views
      - "`pd.DataFrame({'article_id': [1, 2, 3], 'author_id': [1, 2, 3], 'viewer_id': [2, 3, 1], 'view_date': pd.to_datetime(['2019-08-01', '2019-08-02', '2019-08-03'])})`"
    - # corner case: all self-views
      - "`pd.DataFrame({'article_id': [1, 2, 3], 'author_id': [1, 2, 3], 'viewer_id': [1, 2, 3], 'view_date': pd.to_datetime(['2019-08-01', '2019-08-02', '2019-08-03'])})`"
    - | # generate random cases
      ```
      def _generate():
        views = pd.DataFrame({'article_id': np.arange(1, 1001), 'author_id': np.random.choice(np.arange(1, 1001), 1000), 'viewer_id': np.random.choice(np.arange(1, 1001), 1000), 'view_date': np.random.choice(pd.date_range('2019-01-01', '2019-12-31'), 1000)})
        return views,
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

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter the rows where the author viewed their own article
    self_views = views[views["author_id"] == views["viewer_id"]]

    # Get the unique author ids
    unique_authors = self_views["author_id"].unique()

    # Create the result dataframe and sort by id
    result = pd.DataFrame({"id": unique_authors}).sort_values(by="id").reset_index(drop=True)

    return result
