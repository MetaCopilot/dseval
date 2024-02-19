'''
### Description ###

Table: `Courses`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.
```

Write a solution to find all the classes that have **at least five students**.

Return the result table in **any order**.

Theresult format is in the following example.

**Example 1:**

```
**Input:** 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
**Output:** 
+---------+
| class   |
+---------+
| Math    |
+---------+
**Explanation:** 
- Math has 6 students, so we include it.
- English has 1 student, so we do not include it.
- Biology has 1 student, so we do not include it.
- Computer has 1 student, so we do not include it.
```

### Schema ###

data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
Courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})

### Code snippet ###

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def find_classes(courses: pd.DataFrame) -> pd.DataFrame`.

  `courses` is a DataFrame with the following columns:
  - student: str
  - class: str
  Each row of this table indicates the name of a student and the class in which they are enrolled.

  The function should return all the classes that have **at least five students**. Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  courses:
  +---------+----------+
  | student | class    |
  +---------+----------+
  | A       | Math     |
  | B       | English  |
  | C       | Math     |
  | D       | Biology  |
  | E       | Math     |
  | F       | Computer |
  | G       | Math     |
  | H       | Math     |
  | I       | Math     |
  +---------+----------+
  ```

  Example output:
  ```
  +---------+
  | class   |
  +---------+
  | Math    |
  +---------+
  ```

  Example explanation:
  - Math has 6 students, so we include it.
  - English has 1 student, so we do not include it.
  - Biology has 1 student, so we do not include it.
  - Computer has 1 student, so we do not include it.

validator:
  table_test:
    function_name: find_classes
    input_validator: |
      def _validate(courses):
        assert courses.shape[0] > 0
        assert courses.dtypes.equals(pd.Series({'student': 'object', 'class': 'object'}))
        assert courses.student.str.match(r'^\w+$').all()
        assert courses['class'].str.match(r'^\w+$').all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']})`"
    - # corner case: only one class
      - "`pd.DataFrame({'student': ['A', 'B', 'C', 'D', 'E'], 'class': ['Math', 'Math', 'Math', 'Math', 'Math']})`"
    - # corner case: no class has at least five students
      - "`pd.DataFrame({'student': ['A', 'B', 'C', 'D', 'E'], 'class': ['Math', 'English', 'Math', 'Biology', 'Math']})`"
    - # corner case: all classes have at least five students
      - "`pd.DataFrame({'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 'class': ['Math', 'Math', 'Math', 'Math', 'Math', 'English', 'English', 'English', 'English']})`"
    - | # random cases
      ```
      def _generate():
        classes = ['Math', 'English', 'Biology', 'Computer']
        students = [f'{chr(ord("A") + i)}' for i in range(26)]
        courses = pd.DataFrame({'student': np.random.choice(students, 1000), 'class': np.random.choice(classes, 1000)})
        return courses,
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

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Group by class and count the number of students in each class
    class_counts = courses.groupby("class").size().reset_index(name="count")

    # Filter the classes with at least 5 students
    result = class_counts[class_counts["count"] >= 5]

    # Return the result with only the class column
    return result[["class"]]
