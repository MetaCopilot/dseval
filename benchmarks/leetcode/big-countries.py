'''
### Description ###

Table: `World`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.
```

A country is **big** if:

* it has an area of at leastthree million (i.e., `3000000 km2`), or
* it has a population of at leasttwenty-five million (i.e., `25000000`).

Write a solution to find the name, population, and area of the **big countries**.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
**Output:** 
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
```

### Schema ###

data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000], ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000], ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
World = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype({'name':'object', 'continent':'object', 'area':'Int64', 'population':'Int64', 'gdp':'Int64'})

### Code snippet ###

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def big_countries(world: pd.DataFrame) -> pd.DataFrame`.

  `world` is a DataFrame with the following columns:
  - name: str
  - continent: str
  - area: int
  - population: int
  - gdp: int
  Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.

  A country is **big** if:
  - it has an area of at least three million (i.e., `3000000 km2`), or
  - it has a population of at least twenty-five million (i.e., `25000000`).

  The function should return the name, population, and area of the **big countries**. Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  World table:
  +-------------+-----------+---------+------------+--------------+
  | name        | continent | area    | population | gdp          |
  +-------------+-----------+---------+------------+--------------+
  | Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
  | Albania     | Europe    | 28748   | 2831741    | 12960000000  |
  | Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
  | Andorra     | Europe    | 468     | 78115      | 3712000000   |
  | Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
  +-------------+-----------+---------+------------+--------------+
  ```

  Example output:
  ```
  +-------------+------------+---------+
  | name        | population | area    |
  +-------------+------------+---------+
  | Afghanistan | 25500100   | 652230  |
  | Algeria     | 37100000   | 2381741 |
  +-------------+------------+---------+
  ```

validator:
  table_test:
    function_name: big_countries
    input_validator: |
      def _validate(world):
        assert world.shape[0] > 0
        assert world.dtypes.equals(pd.Series({'name': 'object', 'continent': 'object', 'area': 'int64', 'population': 'int64', 'gdp': 'int64'}))
        assert world.name.is_unique
        assert world.area.between(0, 1e7).all()
        assert world.population.between(0, 1e9).all()
        assert world.gdp.between(0, 1e12).all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'name': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'], 'continent': ['Asia', 'Europe', 'Africa', 'Europe', 'Africa'], 'area': [652230, 28748, 2381741, 468, 1246700], 'population': [25500100, 2831741, 37100000, 78115, 20609294], 'gdp': [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]})`"
    - # corner case: only one country
      - "`pd.DataFrame({'name': ['Afghanistan'], 'continent': ['Asia'], 'area': [652230], 'population': [25500100], 'gdp': [20343000000]})`"
    - # corner case: no big countries
      - "`pd.DataFrame({'name': ['Albania', 'Andorra'], 'continent': ['Europe', 'Europe'], 'area': [28748, 468], 'population': [2831741, 78115], 'gdp': [12960000000, 3712000000]})`"
    - # corner case: all countries are big
      - "`pd.DataFrame({'name': ['Afghanistan', 'Algeria'], 'continent': ['Asia', 'Africa'], 'area': [652230, 2381741], 'population': [25500100, 37100000], 'gdp': [20343000000, 188681000000]})`"
    - | # generate random cases
      ```
      def _generate():
        names = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola']
        world = pd.DataFrame({'name': names, 'continent': np.random.choice(['Asia', 'Europe', 'Africa'], 5), 'area': np.random.randint(0, 1e7, 5), 'population': np.random.randint(0, 1e9, 5), 'gdp': np.random.randint(0, 1e12, 5)})
        return world,
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

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Filter the big countries
    big_countries = world[(world["area"] >= 3000000) | (world["population"] >= 25000000)]

    # Select the required columns
    result = big_countries[["name", "population", "area"]]

    return result
