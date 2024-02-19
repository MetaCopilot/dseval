'''
### Description ###

Table: `Students`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.
```

Table: `Subjects`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.
```

Table: `Examinations`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
```

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by `student_id` and `subject_name`.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Students table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |
+------------+--------------+
Subjects table:
+--------------+
| subject_name |
+--------------+
| Math         |
| Physics      |
| Programming  |
+--------------+
Examinations table:
+------------+--------------+
| student_id | subject_name |
+------------+--------------+
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
| 13         | Math         |
| 13         | Programming  |
| 13         | Physics      |
| 2          | Math         |
| 1          | Math         |
+------------+--------------+
**Output:** 
+------------+--------------+--------------+----------------+
| student_id | student_name | subject_name | attended_exams |
+------------+--------------+--------------+----------------+
| 1          | Alice        | Math         | 3              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 1              |
| 2          | Bob          | Physics      | 0              |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | 0              |
| 6          | Alex         | Physics      | 0              |
| 6          | Alex         | Programming  | 0              |
| 13         | John         | Math         | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Programming  | 1              |
+------------+--------------+--------------+----------------+
**Explanation:** 
The result table should contain all students and all subjects.
Alice attended the Math exam 3 times, the Physics exam 2 times, and the Programming exam 1 time.
Bob attended the Math exam 1 time, the Programming exam 1 time, and did not attend the Physics exam.
Alex did not attend any exams.
John attended the Math exam 1 time, the Physics exam 1 time, and the Programming exam 1 time.
```

### Schema ###

data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
Students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
data = [['Math'], ['Physics'], ['Programming']]
Subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
Examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})

### Code snippet ###

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame`.

  `students` is a DataFrame with the following columns:
  - student_id: int
  - student_name: str
  Each row of this table contains the ID and the name of one student in the school.

  `subjects` is a DataFrame with the following columns:
  - subject_name: str
  Each row of this table contains the name of one subject in the school.

  `examinations` is a DataFrame with the following columns:
  - student_id: int
  - subject_name: str
  Each student from the Students table takes every course from the Subjects table. Each row of this table indicates that a student with ID student_id attended the exam of subject_name.

  The function should return the number of times each student attended each exam. Return the result table ordered by `student_id` and `subject_name`.

  The result format is in the following example.

  Example input:
  ```
  students:
  +------------+--------------+
  | student_id | student_name |
  +------------+--------------+
  | 1          | Alice        |
  | 2          | Bob          |
  | 13         | John         |
  | 6          | Alex         |
  +------------+--------------+
  subjects:
  +--------------+
  | subject_name |
  +--------------+
  | Math         |
  | Physics      |
  | Programming  |
  +--------------+
  examinations:
  +------------+--------------+
  | student_id | subject_name |
  +------------+--------------+
  | 1          | Math         |
  | 1          | Physics      |
  | 1          | Programming  |
  | 2          | Programming  |
  | 1          | Physics      |
  | 1          | Math         |
  | 13         | Math         |
  | 13         | Programming  |
  | 13         | Physics      |
  | 2          | Math         |
  | 1          | Math         |
  +------------+--------------+
  ```

  Example output:
  ```
  +------------+--------------+--------------+----------------+
  | student_id | student_name | subject_name | attended_exams |
  +------------+--------------+--------------+----------------+
  | 1          | Alice        | Math         | 3              |
  | 1          | Alice        | Physics      | 2              |
  | 1          | Alice        | Programming  | 1              |
  | 2          | Bob          | Math         | 1              |
  | 2          | Bob          | Physics      | 0              |
  | 2          | Bob          | Programming  | 1              |
  | 6          | Alex         | Math         | 0              |
  | 6          | Alex         | Physics      | 0              |
  | 6          | Alex         | Programming  | 0              |
  | 13         | John         | Math         | 1              |
  | 13         | John         | Physics      | 1              |
  | 13         | John         | Programming  | 1              |
  +------------+--------------+--------------+----------------+
  ```

validator:
  table_test:
    function_name: students_and_examinations
    input_validator: |
      def _validate(students, subjects, examinations):
        assert students.shape[0] > 0 and subjects.shape[0] > 0 and examinations.shape[0] > 0
        assert students.dtypes.equals(pd.Series({'student_id': 'int64', 'student_name': 'object'}))
        assert subjects.dtypes.equals(pd.Series({'subject_name': 'object'}))
        assert examinations.dtypes.equals(pd.Series({'student_id': 'int64', 'subject_name': 'object'}))
        assert students.student_id.is_unique
        assert subjects.subject_name.is_unique
        assert examinations.student_id.isin(students.student_id).all()
        assert examinations.subject_name.isin(subjects.subject_name).all()

    output_checker:
      ignore_index: true

    test_cases:
    - # example
      - "`pd.DataFrame({'student_id': [1, 2, 13, 6], 'student_name': ['Alice', 'Bob', 'John', 'Alex']})`"
      - "`pd.DataFrame({'subject_name': ['Math', 'Physics', 'Programming']})`"
      - "`pd.DataFrame({'student_id': [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1], 'subject_name': ['Math', 'Physics', 'Programming', 'Programming', 'Physics', 'Math', 'Math', 'Programming', 'Physics', 'Math', 'Math']})`"
    - # corner case: only one student, one subject, one examination
      - "`pd.DataFrame({'student_id': [1], 'student_name': ['Alice']})`"
      - "`pd.DataFrame({'subject_name': ['Math']})`"
      - "`pd.DataFrame({'student_id': [1], 'subject_name': ['Math']})`"
    - # corner case: all students attended all exams
      - "`pd.DataFrame({'student_id': [1, 2], 'student_name': ['Alice', 'Bob']})`"
      - "`pd.DataFrame({'subject_name': ['Math', 'Physics']})`"
      - "`pd.DataFrame({'student_id': [1, 1, 2, 2], 'subject_name': ['Math', 'Physics', 'Math', 'Physics']})`"
    - | # generate random cases
      ```
      def _generate():
        students = pd.DataFrame({'student_id': np.arange(1, 1001), 'student_name': [f'student_{i}' for i in range(1, 1001)]})
        subjects = pd.DataFrame({'subject_name': [f'subject_{i}' for i in range(1, 11)]})
        examinations = pd.DataFrame({'student_id': np.random.choice(students.student_id, 1000), 'subject_name': np.random.choice(subjects.subject_name, 1000)})
        return students, subjects, examinations
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

def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    cross = students.merge(subjects, how="cross")

    counts = (
        examinations.groupby(["student_id", "subject_name"]).agg(attended_exams=("subject_name", "count")).reset_index()
    )

    result = cross.merge(counts, on=["student_id", "subject_name"], how="left").sort_values(
        by=["student_id", "subject_name"]
    )

    return result.fillna(0)[["student_id", "student_name", "subject_name", "attended_exams"]]
