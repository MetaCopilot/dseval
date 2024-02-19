'''
### Description ###

Table: `Scores`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
```

Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

* The scores should be ranked from the highest to the lowest.
* If there is a tie between two scores, both should have the same ranking.
* After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.

Return the result table ordered by `score` in descending order.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
**Output:** 
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
```

### Schema ###

data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
Scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})

### Code snippet ###

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def order_scores(scores: pd.DataFrame) -> pd.DataFrame`.

  `scores` is a DataFrame with the following columns:
  - id: int
  - score: float
  Each row of this table contains the score of a game. Score is a floating point value with two decimal places.

  The function should return the rank of the scores. The ranking should be calculated according to the following rules:
  - The scores should be ranked from the highest to the lowest.
  - If there is a tie between two scores, both should have the same ranking.
  - After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.

  Return the result table ordered by `score` in descending order.

  The result format is in the following example.

  Example input:
  ```
  Scores table:
  +----+-------+
  | id | score |
  +----+-------+
  | 1  | 3.50  |
  | 2  | 3.65  |
  | 3  | 4.00  |
  | 4  | 3.85  |
  | 5  | 4.00  |
  | 6  | 3.65  |
  +----+-------+
  ```

  Example output:
  ```
  +-------+------+
  | score | rank |
  +-------+------+
  | 4.00  | 1    |
  | 4.00  | 1    |
  | 3.85  | 2    |
  | 3.65  | 3    |
  | 3.65  | 3    |
  | 3.50  | 4    |
  +-------+------+
  ```

validator:
  table_test:
    function_name: order_scores
    input_validator: |
      def _validate(scores):
        assert scores.shape[0] > 0
        assert scores.dtypes.equals(pd.Series({'id': 'int64', 'score': 'float64'}))
        assert scores.id.is_unique
        assert scores.score.between(0, 5).all()

    output_checker:
      ignore_index: true

    test_cases:
    - # example
      - "`pd.DataFrame({'id': [1, 2, 3, 4, 5, 6], 'score': [3.5, 3.65, 4.0, 3.85, 4.0, 3.65]})`"
    - # corner case: only one score
      - "`pd.DataFrame({'id': [1], 'score': [3.5]})`"
    - # corner case: all scores are the same
      - "`pd.DataFrame({'id': [1, 2, 3, 4, 5, 6], 'score': [3.5, 3.5, 3.5, 3.5, 3.5, 3.5]})`"
    - # corner case: all scores are different
      - "`pd.DataFrame({'id': [1, 2, 3, 4, 5, 6], 'score': [3.5, 3.6, 3.7, 3.8, 3.9, 4.0]})`"
    - # corner case: scores are not ordered
      - "`pd.DataFrame({'id': [1, 2, 3, 4, 5, 6], 'score': [4.0, 3.5, 3.65, 3.85, 4.0, 3.65]})`"
    - # corner case from leetcode
      - "`pd.DataFrame({'id': [1, 2, 3, 4, 5, 6], 'score': [3.5, 3.65, 4.0, 3.85, 4.0, 3.65]})`"
    - | # generate random cases
      ```
      def _generate():
        scores = pd.DataFrame({'id': np.arange(1, 1001), 'score': np.random.uniform(0, 5, 1000).round(2)})
        return scores,
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

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Sort the scores in descending order
    sorted_scores = scores.sort_values(by="score", ascending=False)

    # Calculate the rank for each score
    sorted_scores["rank"] = sorted_scores["score"].rank(method="dense", ascending=False)

    # Return the result with only score and rank columns
    return sorted_scores[["score", "rank"]]
