'''
### Description ###

Table: `ActorDirector`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
timestamp is the primary key (column with unique values) for this table.
```

Write a solution to find all the pairs `(actor_id, director_id)` where the actor has cooperated with the director at least three times.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
ActorDirector table:
+-------------+-------------+-------------+
| actor_id    | director_id | timestamp   |
+-------------+-------------+-------------+
| 1           | 1           | 0           |
| 1           | 1           | 1           |
| 1           | 1           | 2           |
| 1           | 2           | 3           |
| 1           | 2           | 4           |
| 2           | 1           | 5           |
| 2           | 1           | 6           |
+-------------+-------------+-------------+
**Output:** 
+-------------+-------------+
| actor_id    | director_id |
+-------------+-------------+
| 1           | 1           |
+-------------+-------------+
**Explanation:** The only pair is (1, 1) where they cooperated exactly 3 times.
```

### Schema ###

data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
ActorDirector = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype({'actor_id':'int64', 'director_id':'int64', 'timestamp':'int64'})

### Code snippet ###

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame`.

  `actor_director` is a DataFrame with the following columns:
  - actor_id: int
  - director_id: int
  - timestamp: int
  `timestamp` is the primary key (column with unique values) for this table.

  The function should find all the pairs `(actor_id, director_id)` where the actor has cooperated with the director at least three times.

  Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  ActorDirector table:
  +-------------+-------------+-------------+
  | actor_id    | director_id | timestamp   |
  +-------------+-------------+-------------+
  | 1           | 1           | 0           |
  | 1           | 1           | 1           |
  | 1           | 1           | 2           |
  | 1           | 2           | 3           |
  | 1           | 2           | 4           |
  | 2           | 1           | 5           |
  | 2           | 1           | 6           |
  +-------------+-------------+-------------+
  ```

  Example output:
  ```
  +-------------+-------------+
  | actor_id    | director_id |
  +-------------+-------------+
  | 1           | 1           |
  +-------------+-------------+
  ```
  Example explanation: The only pair is (1, 1) where they cooperated exactly 3 times.

validator:
  table_test:
    function_name: actors_and_directors
    input_validator: |
      def _validate(actor_director):
        assert actor_director.shape[0] > 0
        assert actor_director.dtypes.equals(pd.Series({'actor_id': 'int64', 'director_id': 'int64', 'timestamp': 'int64'}))
        assert actor_director.timestamp.is_unique
        assert actor_director.actor_id.between(1, 1000).all()
        assert actor_director.director_id.between(1, 1000).all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'actor_id': [1, 1, 1, 1, 1, 2, 2], 'director_id': [1, 1, 1, 2, 2, 1, 1], 'timestamp': [0, 1, 2, 3, 4, 5, 6]})`"
    - # corner case: only one pair
      - "`pd.DataFrame({'actor_id': [1, 1, 1], 'director_id': [1, 1, 1], 'timestamp': [0, 1, 2]})`"
    - # corner case: no pair
      - "`pd.DataFrame({'actor_id': [1, 1, 1, 1, 1, 2, 2], 'director_id': [1, 1, 1, 2, 2, 1, 1], 'timestamp': [0, 1, 2, 3, 4, 5, 6]})`"
    - # corner case: all pairs
      - "`pd.DataFrame({'actor_id': [1, 1, 1, 1, 1, 2, 2], 'director_id': [1, 1, 1, 2, 2, 1, 1], 'timestamp': [0, 1, 2, 3, 4, 5, 6]})`"
    - | # random cases
      ```
      def _generate():
        actor_director = pd.DataFrame({'actor_id': np.random.randint(1, 1001, 1000), 'director_id': np.random.randint(1, 1001, 1000), 'timestamp': np.arange(1000)})
        return actor_director,
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

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Group by actor_id and director_id, and count the number of collaborations
    collaboration_count = actor_director.groupby(["actor_id", "director_id"]).size().reset_index(name="count")

    # Filter the pairs with at least 3 collaborations
    result = collaboration_count[collaboration_count["count"] >= 3]

    # Return the result without the count column
    return result[["actor_id", "director_id"]]
