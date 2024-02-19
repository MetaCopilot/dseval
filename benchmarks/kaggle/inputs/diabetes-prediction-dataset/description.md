### Dataset name ###

Diabetes prediction dataset

### Dataset description ###

The **Diabetes prediction dataset** is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. This dataset can be used to build machine learning models to predict diabetes in patients based on their medical history and demographic information. This can be useful for healthcare professionals in identifying patients who may be at risk of developing diabetes and in developing personalized treatment plans. Additionally, the dataset can be used by researchers to explore the relationships between various medical and demographic factors and the likelihood of developing diabetes.

### Dataset files ###

- diabetes_prediction_dataset.csv

    pandas.DataFrame(shape=(100000, 9), columns=["gender", "age", "hypertension", "heart_disease", "smoking_history", "bmi", "HbA1c_level", "blood_glucose_level", "diabetes"])
               gender   age  hypertension  heart_disease smoking_history    bmi  HbA1c_level  blood_glucose_level  diabetes
        0      Female  80.0             0              1           never  25.19          6.6                  140         0
        1      Female  54.0             0              0         No Info  27.32          6.6                   80         0
        2        Male  28.0             0              0           never  27.32          5.7                  158         0
        3      Female  36.0             0              0         current  23.45          5.0                  155         0
        4        Male  76.0             1              1         current  20.14          4.8                  155         0
        ...       ...   ...           ...            ...             ...    ...          ...                  ...       ...
        99995  Female  80.0             0              0         No Info  27.32          6.2                   90         0
        99996  Female   2.0             0              0         No Info  17.37          6.5                  100         0
        99997    Male  66.0             0              0          former  27.83          5.7                  155         0
        99998  Female  24.0             0              0           never  35.42          4.0                  100         0
        99999  Female  57.0             0              0         current  22.43          6.6                   90         0

