### Dataset name ###

Cardiovascular Diseases Risk Prediction Dataset

### Dataset description ###

# CVDs Risk Prediction Using Personal Lifestyle Factors

### - Check my notebook [here!](https://www.kaggle.com/alphiree/cvds-risk-prediction-notebook-full) 😄
### - Access the web application I created [here!](https://cvd-risk-prediction.streamlit.app/) 🔗

## BRFSS Dataset
The Behavioral Risk Factor Surveillance System (BRFSS) is the nation’s premier system of health-related telephone surveys that collect state data about U.S. residents regarding their health-related risk behaviors, chronic health conditions, and use of preventive services. 

## Preprocessing of BRFSS Dataset
I preprocessed and cleaned the BRFSS Dataset. From 304 unique variables, I hand-picked 19 variables that relates to lifestyle factors of a person that can be contributed to being at risk with any form of Cardiovascular Diseases.


## Research Article
You can also read the research article that was published that made use of this dataset.
[Read Here!](https://eajournals.org/ejcsit/vol11-issue-3-2023/integrated-machine-learning-model-for-comprehensive-heart-disease-risk-assessment-based-on-multi-dimensional-health-factors/)

### Dataset files ###

- CVD_cleaned.csv

    pandas.DataFrame(shape=(308854, 19), columns=["General_Health", "Checkup", "Exercise", "Heart_Disease", "Skin_Cancer", "Other_Cancer", "Depression", "Diabetes", "Arthritis", "Sex", "Age_Category", "Height_(cm)", "Weight_(kg)", "BMI", "Smoking_History", "Alcohol_Consumption", "Fruit_Consumption", "Green_Vegetables_Consumption", "FriedPotato_Consumption"])
               General_Health              Checkup Exercise Heart_Disease Skin_Cancer Other_Cancer Depression  ... Weight_(kg)    BMI Smoking_History Alcohol_Consumption  Fruit_Consumption  Green_Vegetables_Consumption  FriedPotato_Consumption
        0                Poor  Within the past ...       No            No          No           No         No  ...       32.66  14.54             Yes                 0.0               30.0                 16.0                          12.0    
        1           Very Good  Within the past ...       No           Yes          No           No         No  ...       77.11  28.29              No                 0.0               30.0                  0.0                           4.0    
        2           Very Good  Within the past ...      Yes            No          No           No         No  ...       88.45  33.47              No                 4.0               12.0                  3.0                          16.0    
        3                Poor  Within the past ...      Yes           Yes          No           No         No  ...       93.44  28.73              No                 0.0               30.0                 30.0                           8.0    
        4                Good  Within the past ...       No            No          No           No         No  ...       88.45  24.37             Yes                 0.0                8.0                  4.0                           0.0    
        ...               ...                  ...      ...           ...         ...          ...        ...  ...         ...    ...             ...                 ...                ...                  ...                           ...    
        308849      Very Good  Within the past ...      Yes            No          No           No         No  ...       81.65  29.05              No                 4.0               30.0                  8.0                           0.0    
        308850           Fair  Within the past ...      Yes            No          No           No         No  ...       69.85  21.48              No                 8.0               15.0                 60.0                           4.0    
        308851      Very Good  5 or more years ago      Yes            No          No           No        Yes  ...       61.23  24.69             Yes                 4.0               40.0                  8.0                           4.0    
        308852      Very Good  Within the past ...      Yes            No          No           No         No  ...       79.38  23.73              No                 3.0               30.0                 12.0                           0.0    
        308853      Excellent  Within the past ...      Yes            No          No           No         No  ...       81.19  31.71              No                 1.0                5.0                 12.0                           1.0

