'''
### Description ###

Table: `Patients`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
patient_id is the primary key (column with unique values) for this table.
'conditions' contains 0 or more code separated by spaces. 
This table contains information of the patients in the hospital.
```

Write a solution to find the patient\_id, patient\_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with `DIAB1` prefix.

Return the result table in **any order**.

Theresult format is in the following example.

**Example 1:**

```
**Input:** 
Patients table:
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |
+------------+--------------+--------------+
**Output:** 
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 | 
+------------+--------------+--------------+
**Explanation:** Bob and George both have a condition that starts with DIAB1.
```

### Schema ###

data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]
Patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'})

### Code snippet ###

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def find_patients(patients: pd.DataFrame) -> pd.DataFrame`.

  `patients` is a DataFrame with the following columns:
  - patient_id: int
  - patient_name: str
  - conditions: str
  `patients` contains information of the patients in the hospital. 'conditions' contains 0 or more code separated by spaces.

  The function should return the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with `DIAB1` prefix.

  Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  Patients table:
  +------------+--------------+--------------+
  | patient_id | patient_name | conditions   |
  +------------+--------------+--------------+
  | 1          | Daniel       | YFEV COUGH   |
  | 2          | Alice        |              |
  | 3          | Bob          | DIAB100 MYOP |
  | 4          | George       | ACNE DIAB100 |
  | 5          | Alain        | DIAB201      |
  +------------+--------------+--------------+
  ```

  Example output:
  ```
  +------------+--------------+--------------+
  | patient_id | patient_name | conditions   |
  +------------+--------------+--------------+
  | 3          | Bob          | DIAB100 MYOP |
  | 4          | George       | ACNE DIAB100 | 
  +------------+--------------+--------------+
  ```

  Example explanation: Bob and George both have a condition that starts with DIAB1.

validator:
  table_test:
    function_name: find_patients
    input_validator: |
      def _validate(patients):
        assert patients.shape[0] > 0
        assert patients.dtypes.equals(pd.Series({'patient_id': 'int64', 'patient_name': 'object', 'conditions': 'object'}))
        assert patients.patient_id.is_unique
        assert patients.patient_name.str.match(r'^\w+$').all()
        assert patients.conditions.str.match(r'^(\w+ )*\w*$').all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'patient_id': [1, 2, 3, 4, 5], 'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'], 'conditions': ['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201']})`"
    - # corner case: only one patient
      - "`pd.DataFrame({'patient_id': [1], 'patient_name': ['Daniel'], 'conditions': ['YFEV COUGH']})`"
    - # corner case: no conditions
      - "`pd.DataFrame({'patient_id': [1, 2, 3, 4, 5], 'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'], 'conditions': ['', '', '', '', '']})`"
    - # corner case: all conditions are Type I Diabetes
      - "`pd.DataFrame({'patient_id': [1, 2, 3, 4, 5], 'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'], 'conditions': ['DIAB100', 'DIAB101', 'DIAB102', 'DIAB103', 'DIAB104']})`"
    - # corner case: conditions are not ordered
      - "`pd.DataFrame({'patient_id': [1, 2, 3, 4, 5], 'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'], 'conditions': ['DIAB100 YFEV COUGH', 'DIAB101', 'DIAB102 MYOP', 'DIAB103 ACNE', 'DIAB104']})`"
    - # corner case from leetcode
      - "`pd.DataFrame({'patient_id': [1], 'patient_name': ['Daniel'], 'conditions': ['SADIAB100']})`"
    - | # random cases
      ```
      def _generate():
        patients = pd.DataFrame({
          'patient_id': np.arange(1, 1001),
          'patient_name': [''.join(np.random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 5)) for _ in range(1000)],
          'conditions': [' '.join(np.random.choice(['DIAB1', 'DIAB2', 'YFEV', 'COUGH', 'MYOP', 'ACNE', 'DIAB2DIAB1'], np.random.randint(0, 4), replace=False)) for _ in range(1000)],
        })
        return patients,
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

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Filter the patients DataFrame to only include patients with Type I Diabetes
    type1_diabetes_patients = patients[patients["conditions"].str.match(r"(^DIAB1)|(.*\sDIAB1)")]

    return type1_diabetes_patients[["patient_id", "patient_name", "conditions"]]
