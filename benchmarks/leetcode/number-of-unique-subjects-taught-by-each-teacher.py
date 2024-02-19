'''
### Description ###

Table: `Teacher`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.
```

Write a solution to calculatethe number of unique subjects each teacher teaches in the university.

Return the result table in **any order**.

Theresult format is shown in the following example.

**Example 1:**

```
**Input:** 
Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
**Output:**  
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
**Explanation:** 
Teacher 1:
  - They teach subject 2 in departments 3 and 4.
  - They teach subject 3 in department 3.
Teacher 2:
  - They teach subject 1 in department 1.
  - They teach subject 2 in department 1.
  - They teach subject 3 in department 1.
  - They teach subject 4 in department 1.
```

### Schema ###

data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
Teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})

### Code snippet ###

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame`.

  `teacher` is a DataFrame with the following columns:
  - teacher_id: int
  - subject_id: int
  - dept_id: int
  Each row in this table indicates that the teacher with `teacher_id` teaches the subject `subject_id` in the department `dept_id`.

  The function should calculate the number of unique subjects each teacher teaches in the university. Return the result table in **any order**.

  The result format is shown in the following example.

  Example input:
  ```
  teacher:
  +------------+------------+---------+
  | teacher_id | subject_id | dept_id |
  +------------+------------+---------+
  | 1          | 2          | 3       |
  | 1          | 2          | 4       |
  | 1          | 3          | 3       |
  | 2          | 1          | 1       |
  | 2          | 2          | 1       |
  | 2          | 3          | 1       |
  | 2          | 4          | 1       |
  +------------+------------+---------+
  ```

  Example output:
  ```
  +------------+-----+
  | teacher_id | cnt |
  +------------+-----+
  | 1          | 2   |
  | 2          | 4   |
  +------------+-----+
  ```

  Example explanation:
  - Teacher 1:
    - They teach subject 2 in departments 3 and 4.
    - They teach subject 3 in department 3.
  - Teacher 2:
    - They teach subject 1 in department 1.
    - They teach subject 2 in department 1.
    - They teach subject 3 in department 1.
    - They teach subject 4 in department 1.

validator:
  table_test:
    function_name: count_unique_subjects
    input_validator: |
      def _validate(teacher):
        assert teacher.shape[0] > 0
        assert teacher.dtypes.equals(pd.Series({'teacher_id': 'int64', 'subject_id': 'int64', 'dept_id': 'int64'}))
        assert teacher.teacher_id.between(1, 1000).all()
        assert teacher.subject_id.between(1, 1000).all()
        assert teacher.dept_id.between(1, 1000).all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'teacher_id': [1, 1, 1, 2, 2, 2, 2], 'subject_id': [2, 2, 3, 1, 2, 3, 4], 'dept_id': [3, 4, 3, 1, 1, 1, 1]})`"
    - # corner case: only one teacher
      - "`pd.DataFrame({'teacher_id': [1, 1, 1, 1], 'subject_id': [1, 2, 3, 4], 'dept_id': [1, 1, 1, 1]})`"
    - # corner case: only one subject
      - "`pd.DataFrame({'teacher_id': [1, 1, 1, 1], 'subject_id': [1, 1, 1, 1], 'dept_id': [1, 2, 3, 4]})`"
    - # corner case: only one department
      - "`pd.DataFrame({'teacher_id': [1, 1, 1, 1], 'subject_id': [1, 2, 3, 4], 'dept_id': [1, 1, 1, 1]})`"
    - | # random cases
      ```
      def _generate():
        teacher = pd.DataFrame({'teacher_id': np.random.choice(np.arange(1, 1001), 1000), 'subject_id': np.random.choice(np.arange(1, 1001), 1000), 'dept_id': np.random.choice(np.arange(1, 1001), 1000)})
        return teacher,
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

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # Group by teacher_id and subject_id, then count the number of unique subjects for each teacher
    result = teacher.groupby("teacher_id")["subject_id"].nunique().reset_index()

    # Rename the columns for clarity
    result.columns = ["teacher_id", "cnt"]

    return result
