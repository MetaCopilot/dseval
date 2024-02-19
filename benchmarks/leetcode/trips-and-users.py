'''
### Description ###

Table: `Trips`

```
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| client_id   | int      |
| driver_id   | int      |
| city_id     | int      |
| status      | enum     |
| request_at  | date     |     
+-------------+----------+
id is the primary key (column with unique values) for this table.
The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
Status is an ENUM (category) type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').
```

Table: `Users`

```
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| users_id    | int      |
| banned      | enum     |
| role        | enum     |
+-------------+----------+
users_id is the primary key (column with unique values) for this table.
The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
banned is an ENUM (category) type of ('Yes', 'No').
```

The **cancellation rate** is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Write a solution to find the **cancellation rate** of requests with unbanned users (**both client and driver must not be banned**) each day between `"2013-10-01"` and `"2013-10-03"`. Round `Cancellation Rate` to **two decimal** points.

Return the result table in **any order**.

Theresult format is in the following example.

**Example 1:**

```
**Input:** 
Trips table:
+----+-----------+-----------+---------+---------------------+------------+
| id | client_id | driver_id | city_id | status              | request_at |
+----+-----------+-----------+---------+---------------------+------------+
| 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
+----+-----------+-----------+---------+---------------------+------------+
Users table:
+----------+--------+--------+
| users_id | banned | role   |
+----------+--------+--------+
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |
+----------+--------+--------+
**Output:** 
+------------+-------------------+
| Day        | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |
+------------+-------------------+
**Explanation:** 
On 2013-10-01:
  - There were 4 requests in total, 2 of which were canceled.
  - However, the request with Id=2 was made by a banned client (User_Id=2), so it is ignored in the calculation.
  - Hence there are 3 unbanned requests in total, 1 of which was canceled.
  - The Cancellation Rate is (1 / 3) = 0.33
On 2013-10-02:
  - There were 3 requests in total, 0 of which were canceled.
  - The request with Id=6 was made by a banned client, so it is ignored.
  - Hence there are 2 unbanned requests in total, 0 of which were canceled.
  - The Cancellation Rate is (0 / 2) = 0.00
On 2013-10-03:
  - There were 3 requests in total, 1 of which was canceled.
  - The request with Id=8 was made by a banned client, so it is ignored.
  - Hence there are 2 unbanned request in total, 1 of which were canceled.
  - The Cancellation Rate is (1 / 2) = 0.50
```

### Schema ###

data = [['1', '1', '10', '1', 'completed', '2013-10-01'], ['2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01'], ['3', '3', '12', '6', 'completed', '2013-10-01'], ['4', '4', '13', '6', 'cancelled_by_client', '2013-10-01'], ['5', '1', '10', '1', 'completed', '2013-10-02'], ['6', '2', '11', '6', 'completed', '2013-10-02'], ['7', '3', '12', '6', 'completed', '2013-10-02'], ['8', '2', '12', '12', 'completed', '2013-10-03'], ['9', '3', '10', '12', 'completed', '2013-10-03'], ['10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03']]
Trips = pd.DataFrame(data, columns=['id', 'client_id', 'driver_id', 'city_id', 'status']).astype({'id':'Int64', 'client_id':'Int64', 'driver_id':'Int64', 'city_id':'Int64', 'status':'object'})
data = [['1', 'No', 'client'], ['2', 'Yes', 'client'], ['3', 'No', 'client'], ['4', 'No', 'client'], ['10', 'No', 'driver'], ['11', 'No', 'driver'], ['12', 'No', 'driver'], ['13', 'No', 'driver']]
Users = pd.DataFrame(data, columns=['users_id', 'banned', 'role']).astype({'users_id':'Int64', 'banned':'object', 'role':'object'})

### Code snippet ###

import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame`.

  `trips` is a DataFrame with the following columns:
  - id: int
  - client_id: int
  - driver_id: int
  - city_id: int
  - status: str
  - request_at: datetime
  `trips` holds all taxi trips. Each record has a unique `id`, while `client_id` and `driver_id` can be found in `users_id` in the users DataFrame. Status must be one of `completed`, `cancelled_by_driver`, `cancelled_by_client`.

  `users` is a DataFrame with the following columns:
  - users_id: int
  - banned: str
  - role: str
  `users` holds all users. Each user has a unique `users_id`, and `role` must be one of `client`, `driver`, `partner`. `banned` must be either `Yes` or `No`.

  The **cancellation rate** is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

  The function should return the **cancellation rate** of requests with unbanned users (**both client and driver must not be banned**) each day between `"2013-10-01"` and `"2013-10-03"`. Round `Cancellation Rate` to **two decimal** points. Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  trips:
  +----+-----------+-----------+---------+---------------------+------------+
  | id | client_id | driver_id | city_id | status              | request_at |
  +----+-----------+-----------+---------+---------------------+------------+
  | 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
  | 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
  | 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
  | 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
  | 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
  | 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
  | 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
  | 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
  | 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
  | 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
  +----+-----------+-----------+---------+---------------------+------------+
  users:
  +----------+--------+--------+
  | users_id | banned | role   |
  +----------+--------+--------+
  | 1        | No     | client |
  | 2        | Yes    | client |
  | 3        | No     | client |
  | 4        | No     | client |
  | 10       | No     | driver |
  | 11       | No     | driver |
  | 12       | No     | driver |
  | 13       | No     | driver |
  +----------+--------+--------+
  ```

  Example output:
  ```
  +------------+-------------------+
  | Day        | Cancellation Rate |
  +------------+-------------------+
  | 2013-10-01 | 0.33              |
  | 2013-10-02 | 0.00              |
  | 2013-10-03 | 0.50              |
  +------------+-------------------+
  ```

  Example explanation:
  - On 2013-10-01:
    - There were 4 requests in total, 2 of which were canceled.
    - However, the request with Id=2 was made by a banned client (User_Id=2), so it is ignored in the calculation.
    - Hence there are 3 unbanned requests in total, 1 of which was canceled.
    - The Cancellation Rate is (1 / 3) = 0.33
  - On 2013-10-02:
    - There were 3 requests in total, 0 of which were canceled.
    - The request with Id=6 was made by a banned client, so it is ignored.
    - Hence there are 2 unbanned requests in total, 0 of which were canceled.
    - The Cancellation Rate is (0 / 2) = 0.00
  - On 2013-10-03:
    - There were 3 requests in total, 1 of which was canceled.
    - The request with Id=8 was made by a banned client, so it is ignored.
    - Hence there are 2 unbanned request in total, 1 of which were canceled.
    - The Cancellation Rate is (1 / 2) = 0.50

validator:
  table_test:
    function_name: trips_and_users
    input_validator: |
      def _validate(trips, users):
        assert trips.shape[0] > 0 and users.shape[0] > 0
        assert trips.dtypes.equals(pd.Series({'id': 'int64', 'client_id': 'int64', 'driver_id': 'int64', 'city_id': 'int64', 'status': 'object', 'request_at': 'datetime64[ns]'}))
        assert users.dtypes.equals(pd.Series({'users_id': 'int64', 'banned': 'object', 'role': 'object'}))
        assert trips.id.is_unique
        assert trips.status.isin(['completed', 'cancelled_by_driver', 'cancelled_by_client']).all()
        assert trips.request_at.between('2013-01-01', '2013-12-31').all()
        assert trips.client_id.isin(users[users.role == 'client'].users_id).all()
        assert trips.driver_id.isin(users[users.role == 'driver'].users_id).all()
        assert users.users_id.is_unique
        assert users.banned.isin(['Yes', 'No']).all()
        assert users.role.isin(['client', 'driver', 'partner']).all()

    output_checker: |
      def compare_fn(expected, output):
        if not np.issubdtype(output['Cancellation Rate'], np.number):
          output['Cancellation Rate'] = pd.to_numeric(output['Cancellation Rate'])
        return {
          'match': expected.sort_values(by=['Day', 'Cancellation Rate']).reset_index(drop=True).equals(output.sort_values(by=['Day', 'Cancellation Rate']).reset_index(drop=True)),
          'reason': ''
        }

    test_cases:
    - # example
      - "`pd.DataFrame({'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'client_id': [1, 2, 3, 4, 1, 2, 3, 2, 3, 4], 'driver_id': [10, 11, 12, 13, 10, 11, 12, 12, 10, 13], 'city_id': [1, 1, 6, 6, 1, 6, 6, 12, 12, 12], 'status': ['completed', 'cancelled_by_driver', 'completed', 'cancelled_by_client', 'completed', 'completed', 'completed', 'completed', 'completed', 'cancelled_by_driver'], 'request_at': pd.to_datetime(['2013-10-01', '2013-10-01', '2013-10-01', '2013-10-01', '2013-10-02', '2013-10-02', '2013-10-02', '2013-10-03', '2013-10-03', '2013-10-03'])})`"
      - "`pd.DataFrame({'users_id': [1, 2, 3, 4, 10, 11, 12, 13], 'banned': ['No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No'], 'role': ['client', 'client', 'client', 'client', 'driver', 'driver', 'driver', 'driver']})`"
    - # corner case where none of the trips are in the date range
      - "`pd.DataFrame({'id': [1], 'client_id': [1], 'driver_id': [10], 'city_id': [1], 'status': ['completed'], 'request_at': pd.to_datetime(['2013-10-04'])})`"
      - "`pd.DataFrame({'users_id': [1, 10], 'banned': ['No', 'No'], 'role': ['client', 'driver']})`"
    - # corner case where all the trips are cancelled
      - "`pd.DataFrame({'id': [1, 2], 'client_id': [1, 1], 'driver_id': [10, 10], 'city_id': [1, 2], 'status': ['cancelled_by_driver', 'cancelled_by_client'], 'request_at': pd.to_datetime(['2013-10-01', '2013-10-03'])})`"
      - "`pd.DataFrame({'users_id': [1, 10], 'banned': ['No', 'No'], 'role': ['client', 'driver']})`"
    - # corner case where all the users are banned
      - "`pd.DataFrame({'id': [1, 2], 'client_id': [1, 1], 'driver_id': [10, 10], 'city_id': [1, 10], 'status': ['cancelled_by_driver', 'completed'], 'request_at': pd.to_datetime(['2013-10-01', '2013-10-03'])})`"
      - "`pd.DataFrame({'users_id': [1, 10], 'banned': ['Yes', 'Yes'], 'role': ['client', 'driver']})`"
    - | # generate random cases
      ```
      def _generate():
        dates = pd.date_range('2013-09-30', '2013-10-04')
        users = pd.DataFrame({'users_id': np.arange(1, 1001), 'banned': np.random.choice(['Yes', 'No'], 1000), 'role': np.random.choice(['client', 'driver', 'partner'], 1000)})
        trips = pd.DataFrame({'id': np.arange(1, 1001), 'client_id': np.random.choice(users[users.role == 'client'].users_id, 1000), 'driver_id': np.random.choice(users[users.role == 'driver'].users_id, 1000), 'city_id': np.random.choice(np.arange(1, 101), 1000), 'status': np.random.choice(['completed', 'cancelled_by_driver', 'cancelled_by_client'], 1000), 'request_at': np.random.choice(dates, 1000)})
        return trips, users
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

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # 1) temporal filtering
    df = trips[trips['request_at'].between("2013-10-01","2013-10-03")].rename(columns={'request_at':'Day'})

    # 2) filtering based not banned
    banned_set =  set(users[users['banned']=='Yes']['users_id'].tolist())
    df = df[(~df['client_id'].isin(banned_set)) & (~df['driver_id'].isin(banned_set))]

    # 3) counting the cancelled and total trips per day
    df['status_cancelled'] = df['status'].str.contains('cancelled')
    
    # 4) calculating the ratio
    df = df.groupby('Day', as_index=False).agg({'status_cancelled': 'mean'}).rename(columns={'status_cancelled': 'Cancellation Rate'})
    df['Cancellation Rate'] = (df['Cancellation Rate']).round(2)
    return df
