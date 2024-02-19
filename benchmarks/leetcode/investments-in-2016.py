'''
### Description ###

Table: `Insurance`

```
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |
+-------------+-------+
pid is the primary key (column with unique values) for this table.
Each row of this table contains information about one policy where:
pid is the policyholder's policy ID.
tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
lat is the latitude of the policy holder's city. It's guaranteed that lat is not NULL.
lon is the longitude of the policy holder's city. It's guaranteed that lon is not NULL.
```

Write a solution to report the sum of all total investment values in 2016 `tiv_2016`, for all policyholders who:

* have the same `tiv_2015` value as one or more other policyholders, and
* are not located in the same city as any other policyholder (i.e., the (`lat, lon`) attribute pairs must be unique).

Round `tiv_2016` to **two decimal places**.

Theresult format is in the following example.

**Example 1:**

```
**Input:** 
Insurance table:
+-----+----------+----------+-----+-----+
| pid | tiv_2015 | tiv_2016 | lat | lon |
+-----+----------+----------+-----+-----+
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |
+-----+----------+----------+-----+-----+
**Output:** 
+----------+
| tiv_2016 |
+----------+
| 45.00    |
+----------+
**Explanation:** 
The first record in the table, like the last record, meets both of the two criteria.
The tiv_2015 value 10 is the same as the third and fourth records, and its location is unique.

The second record does not meet any of the two criteria. Its tiv_2015 is not like any other policyholders and its location is the same as the third record, which makes the third record fail, too.
So, the result is the sum of tiv_2016 of the first and last record, which is 45.
```

### Schema ###

data = [[1, 10, 5, 10, 10], [2, 20, 20, 20, 20], [3, 10, 30, 20, 20], [4, 10, 40, 40, 40]]
Insurance = pd.DataFrame(data, columns=['pid', 'tiv_2015', 'tiv_2016', 'lat', 'lon']).astype({'pid':'Int64', 'tiv_2015':'Float64', 'tiv_2016':'Float64', 'lat':'Float64', 'lon':'Float64'})

### Code snippet ###

import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def find_investments(insurance: pd.DataFrame) -> pd.DataFrame`.

  `insurance` is a DataFrame with the following columns:
  - pid: int
  - tiv_2015: float
  - tiv_2016: float
  - lat: float
  - lon: float
  `insurance` contains information about one policy where:
  - pid is the policyholder's policy ID.
  - tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
  - lat is the latitude of the policy holder's city. It's guaranteed that lat is not NULL.
  - lon is the longitude of the policy holder's city. It's guaranteed that lon is not NULL.

  The function should report the sum of all total investment values in 2016 `tiv_2016`, for all policyholders who:
  - have the same `tiv_2015` value as one or more other policyholders, and
  - are not located in the same city as any other policyholder (i.e., the (`lat, lon`) attribute pairs must be unique).

  Round `tiv_2016` to **two decimal places**.

  The result format is in the following example.

  Example input:
  ```
  insurance:
  +-----+----------+----------+-----+-----+
  | pid | tiv_2015 | tiv_2016 | lat | lon |
  +-----+----------+----------+-----+-----+
  | 1   | 10       | 5        | 10  | 10  |
  | 2   | 20       | 20       | 20  | 20  |
  | 3   | 10       | 30       | 20  | 20  |
  | 4   | 10       | 40       | 40  | 40  |
  +-----+----------+----------+-----+-----+
  ```

  Example output:
  ```
  +----------+
  | tiv_2016 |
  +----------+
  | 45.00    |
  +----------+
  ```

  Example explanation:
  - The first record in the table, like the last record, meets both of the two criteria.
    The tiv_2015 value 10 is the same as the third and fourth records, and its location is unique.
  - The second record does not meet any of the two criteria. Its tiv_2015 is not like any other policyholders and its location is the same as the third record, which makes the third record fail, too.
  - So, the result is the sum of tiv_2016 of the first and last record, which is 45.

validator:
  table_test:
    function_name: find_investments
    input_validator: |
      def _validate(insurance):
        assert insurance.shape[0] > 0
        assert insurance.dtypes.equals(pd.Series({'pid': 'int64', 'tiv_2015': 'float64', 'tiv_2016': 'float64', 'lat': 'float64', 'lon': 'float64'}))
        assert insurance.pid.is_unique
        assert insurance.tiv_2015.between(0, 1e6).all()
        assert insurance.tiv_2016.between(0, 1e6).all()
        assert insurance.lat.between(-90, 90).all()
        assert insurance.lon.between(-180, 180).all()

    output_checker: |
      def compare_fn(expected, output):
        if not np.issubdtype(output['tiv_2016'], np.number):
          output['tiv_2016'] = pd.to_numeric(output['tiv_2016'])
        return {
          'match': expected.equals(output),
          'reason': ''
        }

    test_cases:
    - # example
      - "`pd.DataFrame({'pid': [1, 2, 3, 4], 'tiv_2015': [10., 20., 10., 10.], 'tiv_2016': [5., 20., 30., 40.], 'lat': [10., 20., 20., 40.], 'lon': [10., 20., 20., 40.]})`"
    - # corner case: only one record
      - "`pd.DataFrame({'pid': [1], 'tiv_2015': [10.], 'tiv_2016': [5.], 'lat': [10.], 'lon': [10.]})`"
    - # corner case: all records have the same tiv_2015
      - "`pd.DataFrame({'pid': [1, 2, 3, 4], 'tiv_2015': [10., 10., 10., 10.], 'tiv_2016': [5, 20., 30., 40.], 'lat': [10., 20., 30., 40.], 'lon': [10., 20., 30., 40.]})`"
    - # corner case: all records have the same location
      - "`pd.DataFrame({'pid': [1, 2, 3, 4], 'tiv_2015': [10., 20., 30., 40.], 'tiv_2016': [5, 20., 30., 40.], 'lat': [10., 10., 10., 10.], 'lon': [10., 10., 10., 10.]})`"
    - | # generate random cases
      ```
      def _generate():
        insurance = pd.DataFrame({'pid': np.arange(1, 1001), 'tiv_2015': np.round(np.random.uniform(0, 1e6, 1000) / 1e5) * 1e5, 'tiv_2016': np.round(np.random.uniform(0, 1e6, 1000) / 1e5) * 1e5, 'lat': np.round(np.random.uniform(-90, 90, 1000) / 45) * 45, 'lon': np.round(np.random.uniform(-180, 180, 1000) / 45) * 45})
        return insurance,
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

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    # 1) filtering based on tiv_2015, and unique lat and lon
    df = insurance[(insurance['tiv_2015'].duplicated(keep=False)) & (~insurance[['lat', 'lon']].duplicated(keep=False))]

    # 2) summing the tiv_2016
    result = df['tiv_2016'].sum()

    # 3) formatting the output
    return pd.DataFrame({"tiv_2016": [round(result, 2)]})
