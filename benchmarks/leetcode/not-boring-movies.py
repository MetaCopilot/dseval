'''
### Description ###

Table: `Cinema`

```
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+
id is the primary key (column with unique values) for this table.
Each row contains information about the name of a movie, its genre, and its rating.
rating is a 2 decimal places float in the range [0, 10]
```

Write a solution to report the movies with an odd-numbered ID and a description that is not `"boring"`.

Return the result table ordered by `rating` **in descending order**.

Theresult format is in the following example.

**Example 1:**

```
**Input:** 
Cinema table:
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |
+----+------------+-------------+--------+
**Output:** 
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |
+----+------------+-------------+--------+
**Explanation:** 
We have three movies with odd-numbered IDs: 1, 3, and 5. The movie with ID = 3 is boring so we do not include it in the answer.
```

### Schema ###

data = [[1, 'War', 'great 3D', 8.9], [2, 'Science', 'fiction', 8.5], [3, 'irish', 'boring', 6.2], [4, 'Ice song', 'Fantacy', 8.6], [5, 'House card', 'Interesting', 9.1]]
cinema = pd.DataFrame(data, columns=['id', 'movie', 'description', 'rating']).astype({'id':'Int64', 'movie':'object', 'description':'object', 'rating':'Float64'})

### Code snippet ###

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame`.

  `cinema` is a DataFrame with the following columns:
  - id: int
  - movie: str
  - description: str
  - rating: float
  `cinema` contains information about the name of a movie, its genre, and its rating. `rating` is a 2 decimal places float in the range [0, 10].

  The function should report the movies with an odd-numbered ID and a description that is not `"boring"`.

  Return the result table ordered by `rating` **in descending order**.

  The result format is in the following example.

  Example input:
  ```
  cinema:
  +----+------------+-------------+--------+
  | id | movie      | description | rating |
  +----+------------+-------------+--------+
  | 1  | War        | great 3D    | 8.9    |
  | 2  | Science    | fiction     | 8.5    |
  | 3  | irish      | boring      | 6.2    |
  | 4  | Ice song   | Fantacy     | 8.6    |
  | 5  | House card | Interesting | 9.1    |
  +----+------------+-------------+--------+
  ```

  Example output:
  ```
  +----+------------+-------------+--------+
  | id | movie      | description | rating |
  +----+------------+-------------+--------+
  | 5  | House card | Interesting | 9.1    |
  | 1  | War        | great 3D    | 8.9    |
  +----+------------+-------------+--------+
  ```

  Example explanation:
  - We have three movies with odd-numbered IDs: 1, 3, and 5. The movie with ID = 3 is boring so we do not include it in the answer.

validator:
  table_test:
    function_name: not_boring_movies
    input_validator: |
      def _validate(cinema):
        assert cinema.shape[0] > 0
        assert cinema.dtypes.equals(pd.Series({'id': 'int64', 'movie': 'object', 'description': 'object', 'rating': 'float64'}))
        assert cinema.id.is_unique
        assert cinema.rating.between(0, 10).all()
        assert cinema.description.str.match(r'^[\w\s]+$').all()

    output_checker:
      ignore_index: true

    test_cases:
    - # example
      - "`pd.DataFrame({'id': [1, 2, 3, 4, 5], 'movie': ['War', 'Science', 'irish', 'Ice song', 'House card'], 'description': ['great 3D', 'fiction', 'boring', 'Fantacy', 'Interesting'], 'rating': [8.9, 8.5, 6.2, 8.6, 9.1]})`"
    - # corner case: only one movie
      - "`pd.DataFrame({'id': [1], 'movie': ['War'], 'description': ['great 3D'], 'rating': [8.9]})`"
    - # corner case: all movies are boring
      - "`pd.DataFrame({'id': [1, 2, 3, 4, 5], 'movie': ['War', 'Science', 'irish', 'Ice song', 'House card'], 'description': ['boring', 'boring', 'boring', 'boring', 'boring'], 'rating': [8.9, 8.5, 6.2, 8.6, 9.1]})`"
    - # corner case: all movies have even-numbered IDs
      - "`pd.DataFrame({'id': [2, 4, 6, 8, 10], 'movie': ['War', 'Science', 'irish', 'Ice song', 'House card'], 'description': ['great 3D', 'fiction', 'boring', 'Fantacy', 'Interesting'], 'rating': [8.9, 8.5, 6.2, 8.6, 9.1]})`"
    - | # generate random cases
      ```
      def _generate():
        import numpy as np
        import pandas as pd
        n = np.random.randint(1, 1001)
        cinema = pd.DataFrame({
          'id': np.arange(1, n + 1),
          'movie': [f"Movie {i}" for i in range(1, n + 1)],
          'description': np.random.choice(['boring', 'great 3D', 'fiction', 'Fantacy', 'Interesting'], n),
          'rating': np.round(np.random.uniform(0, 10, n), 2),
        })
        return cinema,
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

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    # Filter the movies with odd-numbered ID and a description that is not "boring"
    filtered_movies = cinema[(cinema["id"] % 2 == 1) & (cinema["description"] != "boring")]

    # Sort the result by rating in descending order
    return filtered_movies.sort_values(by="rating", ascending=False)
