'''
### Description ###

Table: `Employees`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| emp_id      | int  |
| event_day   | date |
| in_time     | int  |
| out_time    | int  |
+-------------+------+
(emp_id, event_day, in_time) is the primary key (combinations of columns with unique values) of this table.
The table shows the employees' entries and exits in an office.
event_day is the day at which this event happened, in_time is the minute at which the employee entered the office, and out_time is the minute at which they left the office.
in_time and out_time are between 1 and 1440.
It is guaranteed that no two events on the same day intersect in time, and in_time < out_time.
```

Write a solution to calculate the total time **in minutes** spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is `out_time - in_time`.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Employees table:
+--------+------------+---------+----------+
| emp_id | event_day  | in_time | out_time |
+--------+------------+---------+----------+
| 1      | 2020-11-28 | 4       | 32       |
| 1      | 2020-11-28 | 55      | 200      |
| 1      | 2020-12-03 | 1       | 42       |
| 2      | 2020-11-28 | 3       | 33       |
| 2      | 2020-12-09 | 47      | 74       |
+--------+------------+---------+----------+
**Output:** 
+------------+--------+------------+
| day        | emp_id | total_time |
+------------+--------+------------+
| 2020-11-28 | 1      | 173        |
| 2020-11-28 | 2      | 30         |
| 2020-12-03 | 1      | 41         |
| 2020-12-09 | 2      | 27         |
+------------+--------+------------+
**Explanation:** 
Employee 1 has three events: two on day 2020-11-28 with a total of (32 - 4) + (200 - 55) = 173, and one on day 2020-12-03 with a total of (42 - 1) = 41.
Employee 2 has two events: one on day 2020-11-28 with a total of (33 - 3) = 30, and one on day 2020-12-09 with a total of (74 - 47) = 27.
```

### Schema ###

data = [['1', '2020-11-28', '4', '32'], ['1', '2020-11-28', '55', '200'], ['1', '2020-12-3', '1', '42'], ['2', '2020-11-28', '3', '33'], ['2', '2020-12-9', '47', '74']]
Employees = pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time']).astype({'emp_id':'Int64', 'event_day':'datetime64[ns]', 'in_time':'Int64', 'out_time':'Int64'})

### Code snippet ###

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def total_time(employees: pd.DataFrame) -> pd.DataFrame`.

  `employees` is a DataFrame with the following columns:
  - emp_id: int
  - event_day: datetime
  - in_time: int
  - out_time: int
  `employees` shows the employees' entries and exits in an office. `event_day` is the day at which this event happened, `in_time` is the minute at which the employee entered the office, and `out_time` is the minute at which they left the office. `in_time` and `out_time` are between 1 and 1440. It is guaranteed that no two events on the same day intersect in time, and `in_time` < `out_time`.

  The function should calculate the total time **in minutes** spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is `out_time - in_time`.

  Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  employees:
  +--------+------------+---------+----------+
  | emp_id | event_day  | in_time | out_time |
  +--------+------------+---------+----------+
  | 1      | 2020-11-28 | 4       | 32       |
  | 1      | 2020-11-28 | 55      | 200      |
  | 1      | 2020-12-03 | 1       | 42       |
  | 2      | 2020-11-28 | 3       | 33       |
  | 2      | 2020-12-09 | 47      | 74       |
  +--------+------------+---------+----------+
  ```

  Example output:
  ```
  +------------+--------+------------+
  | day        | emp_id | total_time |
  +------------+--------+------------+
  | 2020-11-28 | 1      | 173        |
  | 2020-11-28 | 2      | 30         |
  | 2020-12-03 | 1      | 41         |
  | 2020-12-09 | 2      | 27         |
  +------------+--------+------------+
  ```

  Example explanation:
  - Employee 1 has three events: two on day 2020-11-28 with a total of (32 - 4) + (200 - 55) = 173, and one on day 2020-12-03 with a total of (42 - 1) = 41.
  - Employee 2 has two events: one on day 2020-11-28 with a total of (33 - 3) = 30, and one on day 2020-12-09 with a total of (74 - 47) = 27.

validator:
  table_test:
    function_name: total_time
    input_validator: |
      def _validate(employees):
        assert employees.shape[0] > 0
        assert employees.dtypes.equals(pd.Series({'emp_id': 'int64', 'event_day': 'datetime64[ns]', 'in_time': 'int64', 'out_time': 'int64'}))
        assert employees.in_time.between(1, 1440).all()
        assert employees.out_time.between(1, 1440).all()
        assert (employees.in_time < employees.out_time).all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'emp_id': [1, 1, 1, 2, 2], 'event_day': pd.to_datetime(['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09']), 'in_time': [4, 55, 1, 3, 47], 'out_time': [32, 200, 42, 33, 74]})`"
    - # corner case: only one employee
      - "`pd.DataFrame({'emp_id': [1], 'event_day': pd.to_datetime(['2020-11-28']), 'in_time': [4], 'out_time': [32]})`"
    - # corner case: only one day
      - "`pd.DataFrame({'emp_id': [1, 1, 2, 2], 'event_day': pd.to_datetime(['2020-11-28', '2020-11-28', '2020-11-28', '2020-11-28']), 'in_time': [4, 55, 3, 47], 'out_time': [32, 200, 33, 74]})`"
    - # corner case: only one entry per day
      - "`pd.DataFrame({'emp_id': [1, 1, 2, 2], 'event_day': pd.to_datetime(['2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09']), 'in_time': [4, 1, 3, 47], 'out_time': [32, 42, 33, 74]})`"
    - | # generate random cases
      ```
      def _generate():
        dates = pd.date_range('2020-11-01', '2020-11-30')
        employees = pd.DataFrame({'emp_id': np.random.choice(np.arange(1, 101), 1000), 'event_day': np.random.choice(dates, 1000), 'in_time': np.random.randint(1, 1440, 1000), 'out_time': np.random.randint(1, 1440, 1000)})
        employees = employees[employees.in_time < employees.out_time]
        return employees,
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

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate the time spent in the office for each entry
    employees["time_spent"] = employees["out_time"] - employees["in_time"]

    # Group by employee and day, summing the time spent
    result = employees.groupby(['emp_id', 'event_day'])['time_spent'].sum().reset_index()

    # Rename columns for clarity
    result = result.rename(columns={"emp_id": "emp_id", "event_day": "day", "time_spent": "total_time"})

    return result
