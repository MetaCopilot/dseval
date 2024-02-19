'''
### Description ###

Table: `Activity`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
```

Write a solution to find the **first login date** for each player.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
**Output:** 
+-----------+-------------+
| player_id | first_login |
+-----------+-------------+
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
+-----------+-------------+
```

### Schema ###

data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
Activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})

### Code snippet ###

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def game_analysis(activity: pd.DataFrame) -> pd.DataFrame`.

  `activity` is a DataFrame with the following columns:
  - player_id: int
  - device_id: int
  - event_date: datetime
  - games_played: int
  Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device. The combination of `player_id` and `event_date` is unique.

  The function should return the **first login date** for each player. Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  activity:
  +-----------+-----------+------------+--------------+
  | player_id | device_id | event_date | games_played |
  +-----------+-----------+------------+--------------+
  | 1         | 2         | 2016-03-01 | 5            |
  | 1         | 2         | 2016-05-02 | 6            |
  | 2         | 3         | 2017-06-25 | 1            |
  | 3         | 1         | 2016-03-02 | 0            |
  | 3         | 4         | 2018-07-03 | 5            |
  +-----------+-----------+------------+--------------+
  ```

  Example output:
  ```
  +-----------+-------------+
  | player_id | first_login |
  +-----------+-------------+
  | 1         | 2016-03-01  |
  | 2         | 2017-06-25  |
  | 3         | 2016-03-02  |
  +-----------+-------------+
  ```

validator:
  table_test:
    function_name: game_analysis
    input_validator: |
      def _validate(activity):
        assert activity.shape[0] > 0
        assert activity.dtypes.equals(pd.Series({'player_id': 'int64', 'device_id': 'int64', 'event_date': 'datetime64[ns]', 'games_played': 'int64'}))
        assert activity.event_date.between('2000-01-01', '2099-12-31').all()
        assert activity.games_played.between(0, 100).all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'player_id': [1, 1, 2, 3, 3], 'device_id': [2, 2, 3, 1, 4], 'event_date': pd.to_datetime(['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03']), 'games_played': [5, 6, 1, 0, 5]})`"
    - # corner case: only one player
      - "`pd.DataFrame({'player_id': [1, 1], 'device_id': [2, 2], 'event_date': pd.to_datetime(['2016-03-01', '2016-05-02']), 'games_played': [5, 6]})`"
    - # corner case: no games played
      - "`pd.DataFrame({'player_id': [1, 1, 2, 3, 3], 'device_id': [2, 2, 3, 1, 4], 'event_date': pd.to_datetime(['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03']), 'games_played': [0, 0, 0, 0, 0]})`"
    - # corner case: all games played
      - "`pd.DataFrame({'player_id': [1, 1, 2, 3, 3], 'device_id': [2, 2, 3, 1, 4], 'event_date': pd.to_datetime(['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03']), 'games_played': [100, 100, 100, 100, 100]})`"
    - | # generate random cases
      ```
      def _generate():
        dates = pd.date_range('2016-01-01', '2018-12-31')
        activity = pd.DataFrame({'player_id': np.repeat(np.arange(1, 1001), 10), 'device_id': np.random.choice(np.arange(1, 1001), 10000), 'event_date': np.random.choice(dates, 10000), 'games_played': np.random.choice(np.arange(0, 101), 10000)})
        return activity,
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

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Group by player_id and find the minimum event_date for each player
    result = activity.groupby("player_id")["event_date"].min().reset_index()

    # Rename the columns for clarity
    result.columns = ["player_id", "first_login"]

    return result
