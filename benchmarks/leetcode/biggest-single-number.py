'''
### Description ###

Table: `MyNumbers`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.
```

A **single number** is a number that appeared only once in the `MyNumbers` table.

Find the largest **single number**. If there is no **single number**, report `null`.

The result format is in the following example.

 

**Example 1:**

```
**Input:** 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+
**Output:** 
+-----+
| num |
+-----+
| 6   |
+-----+
**Explanation:** The single numbers are 1, 4, 5, and 6.
Since 6 is the largest single number, we return it.
```

**Example 2:**

```
**Input:** 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+
**Output:** 
+------+
| num  |
+------+
| null |
+------+
**Explanation:** There are no single numbers in the input table so we return null.
```

### Schema ###

data = [[8], [8], [3], [3], [1], [4], [5], [6]]
MyNumbers = pd.DataFrame(data, columns=['num']).astype({'num':'Int64'})

### Code snippet ###

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame`.

  `my_numbers` is a DataFrame with the following columns:
  - num: int
  Each row of this table contains an integer. This table may contain duplicates.

  A **single number** is a number that appeared only once in the `my_numbers` table.

  The function should find the largest **single number**. If there is no **single number**, report `null`.

  The result format is in the following example.

  Example input:
  ```
  my_numbers:
  +-----+
  | num |
  +-----+
  | 8   |
  | 8   |
  | 3   |
  | 3   |
  | 1   |
  | 4   |
  | 5   |
  | 6   |
  +-----+
  ```

  Example output:
  ```
  +-----+
  | num |
  +-----+
  | 6   |
  +-----+
  ```

  Example explanation: The single numbers are 1, 4, 5, and 6. Since 6 is the largest single number, we return it.

validator:
  table_test:
    function_name: biggest_single_number
    input_validator: |
      def _validate(my_numbers):
        assert my_numbers.shape[0] > 0
        assert my_numbers.dtypes.equals(pd.Series({'num': 'int64'}))

    test_cases:
    - # example 1
      - "`pd.DataFrame({'num': [8, 8, 3, 3, 1, 4, 5, 6]})`"
    - # example 2
      - "`pd.DataFrame({'num': [8, 8, 7, 7, 3, 3, 3]})`"
    - # corner case: only one number
      - "`pd.DataFrame({'num': [1]})`"
    - # corner case: all numbers are the same
      - "`pd.DataFrame({'num': [1, 1, 1, 1, 1, 1, 1, 1]})`"
    - # corner case: all numbers are different
      - "`pd.DataFrame({'num': [1, 2, 3, 4, 5, 6, 7, 8]})`"
    - # corner case: all numbers are single numbers except one
      - "`pd.DataFrame({'num': [1, 2, 3, 4, 5, 6, 7, 8, 8]})`"
    - # corner case: all numbers are single numbers except two
      - "`pd.DataFrame({'num': [1, 2, 3, 4, 5, 6, 7, 8, 8, 7]})`"
"""

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # Count the occurrences of each number
    counts = my_numbers["num"].value_counts()

    # Filter the single numbers
    single_numbers = counts[counts == 1].index

    # Find the largest single number or return null if there are no single numbers
    largest_single_number = single_numbers.max() if len(single_numbers) > 0 else None

    return pd.DataFrame({"num": [largest_single_number]})
