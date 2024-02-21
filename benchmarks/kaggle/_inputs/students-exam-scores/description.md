### Dataset name ###

Students Exam Scores: Extended Dataset

### Dataset description ###

This dataset includes scores from three test scores of students at a (fictional) public school and a variety of personal and socio-economic factors that may have interaction effects upon them. 

**Remark/warning/disclaimer:** 
- This datasets are **fictional** and should be used for **educational purposes only**. 
- The original dataset generator creator is Mr. [Royce Kimmons](http://roycekimmons.com/tools/generated_data/exams)
- There are *similar datasets* on kaggle already but this one is **different** and **arguably better** in two ways. 
    -&gt; 1) has **more data** (**&gt;30k** instead of just the 1k the other datasets have),
    -&gt; 2) has extended datasets with **more features** (15 instead of 9) and has **missing values** which makes it ideal for data cleaning and data preprocessing.

### Data Dictionary (column description)

1. **Gender**: Gender of the student (male/female)
2. **EthnicGroup**: Ethnic group of the student (group A to E)
3. **ParentEduc**: Parent(s) education background (from some_highschool to master's degree)
4. **LunchType**: School lunch type (standard or free/reduced)
5. **TestPrep**: Test preparation course followed (completed or none)
6. **ParentMaritalStatus**: Parent(s) marital status (married/single/widowed/divorced)
7. **PracticeSport**: How often the student parctice sport (never/sometimes/regularly))
8. **IsFirstChild**: If the child is first child in the family or not (yes/no)
9. **NrSiblings**: Number of siblings the student has (0 to 7)
10. **TransportMeans**: Means of transport to school (schoolbus/private)
11. **WklyStudyHours**: Weekly self-study hours(less that 5hrs; between 5 and 10hrs; more than 10hrs)
12. **MathScore**: math test score(0-100)
13. **ReadingScore**: reading test score(0-100)
14. **WritingScore**: writing test score(0-100)

### Analytics questions:

1. What factors (features) affect test scores most?
2. Are there interacting features which affect test scores?

### Dataset files ###

- Expanded_data_with_more_features.csv

    pandas.DataFrame(shape=(30641, 15), columns=["Unnamed: 0", "Gender", "EthnicGroup", "ParentEduc", "LunchType", "TestPrep", "ParentMaritalStatus", "PracticeSport", "IsFirstChild", "NrSiblings", "TransportMeans", "WklyStudyHours", "MathScore", "ReadingScore", "WritingScore"])
               Unnamed: 0  Gender EthnicGroup          ParentEduc     LunchType   TestPrep ParentMaritalStatus PracticeSport IsFirstChild  NrSiblings TransportMeans WklyStudyHours  MathScore  ReadingScore  WritingScore
        0               0  female         NaN   bachelor's degree      standard       none             married     regularly          yes         3.0     school_bus            < 5         71            71            74
        1               1  female     group C        some college      standard        NaN             married     sometimes          yes         0.0            NaN         5 - 10         69            90            88
        2               2  female     group B     master's degree      standard       none              single     sometimes          yes         4.0     school_bus            < 5         87            93            91
        3               3    male     group A  associate's degree  free/reduced       none             married         never           no         1.0            NaN         5 - 10         45            56            42
        4               4    male     group C        some college      standard       none             married     sometimes          yes         0.0     school_bus         5 - 10         76            78            75
        ...           ...     ...         ...                 ...           ...        ...                 ...           ...          ...         ...            ...            ...        ...           ...           ...
        30636         816  female     group D         high school      standard       none              single     sometimes           no         2.0     school_bus         5 - 10         59            61            65
        30637         890    male     group E         high school      standard       none              single     regularly           no         1.0        private         5 - 10         58            53            51
        30638         911  female         NaN         high school  free/reduced  completed             married     sometimes           no         1.0        private         5 - 10         61            70            67
        30639         934  female     group D  associate's degree      standard  completed             married     regularly           no         3.0     school_bus         5 - 10         82            90            93
        30640         960    male     group B        some college      standard       none             married         never           no         1.0     school_bus         5 - 10         64            60            58

- Original_data_with_more_rows.csv

    pandas.DataFrame(shape=(30641, 9), columns=["Unnamed: 0", "Gender", "EthnicGroup", "ParentEduc", "LunchType", "TestPrep", "MathScore", "ReadingScore", "WritingScore"])
               Unnamed: 0  Gender EthnicGroup          ParentEduc     LunchType   TestPrep  MathScore  ReadingScore  WritingScore
        0               0  female     group B   bachelor's degree      standard       none         72            72            74
        1               1  female     group C        some college      standard  completed         69            90            88
        2               2  female     group B     master's degree      standard       none         90            95            93
        3               3    male     group A  associate's degree  free/reduced       none         47            57            44
        4               4    male     group C        some college      standard       none         76            78            75
        ...           ...     ...         ...                 ...           ...        ...        ...           ...           ...
        30636         995    male     group C    some high school      standard       none         56            47            51
        30637         996    male     group E  associate's degree  free/reduced       none         74            75            72
        30638         997    male     group C        some college      standard       none         36            29            27
        30639         998    male     group A    some high school  free/reduced  completed         43            34            39
        30640         999  female     group D  associate's degree      standard       none         52            68            66

