# %%
import pandas as pd
import numpy as np

# %%
"""
question: Import the dataset from this `inputs/CVD_cleaned.csv`. Assign it to a variable called cvd.

validator:
  namespace_check:
    cvd:

execution:
  max_time: 2
"""

cvd = pd.read_csv('inputs/CVD_cleaned.csv')

# %%
"""
question: |
  Categorize the BMI (Body Mass Index) of each individual into one of four categories: "Underweight", "Normal weight", "Overweight", and "Obesity". This is based on the following ranges: underweight is a BMI less than 18.5, normal weight is a BMI from 18.5 to 24.9, overweight is a BMI from 25 to 29.9, and obesity is a BMI of 30 or higher. Create a new column called "BMI_Category" in the dataset to store the BMI category of each individual. Use category dtype for this column.

validator:
  namespace_check:
    cvd:
"""

cvd['BMI_Category'] = pd.cut(cvd['BMI'], bins=[0, 18.5, 25, 30, np.inf], right=False, labels=['Underweight', 'Normal weight', 'Overweight', 'Obesity'])

# %%
"""
question: |
  Add `Checkup_Frequency` to `cvd`.
  Firstly, measure the last checkup time by years. For example, if the last checkup time is "Within the past 2 years", it should be mapped to 2. Assume the last checkup time to be 10 for 5 or more years, and 20 if the person has never had a checkup.
  The `Checkup_Frequency` is the reciprocal of the last checkup time. For example, if the last checkup time is 2, the `Checkup_Frequency` is 1/2 = 0.5.

validator:
  namespace_check:
    cvd:
"""

cvd['Checkup_Frequency'] = 1 / cvd['Checkup'].map({'Within the past year': 1, 'Within the past 2 years': 2, 'Within the past 5 years': 5, '5 or more years ago': 10, 'Never': 20})

# %%
"""
question: |
  Compute `Lifestyle_Score`, which is a composite score based on various lifestyle factors including exercise, smoking, fruit consumption, green vegetable consumption, and alcohol consumption. Each lifestyle factor is assigned a certain weight, with positive activities like exercise (weight 1) and fruit eating (weight 0.1), green vegetables (weight 0.1) contributing positively to the score, and negative activities like smoking (weight -1) and alcohol consumption (weight -0.1) subtracting from the score.

validator:
  namespace_check:
    cvd:
"""

exercise_mapping = {'Yes': 1, 'No': 0}
smoking_mapping = {'Yes': -1, 'No': 0}
cvd['Lifestyle_Score'] = cvd['Exercise'].replace(exercise_mapping) - cvd['Smoking_History'].replace(smoking_mapping) + cvd['Fruit_Consumption'] / 10 + cvd['Green_Vegetables_Consumption'] / 10 - cvd['Alcohol_Consumption'] / 10

# %%
"""
question: |
  Add the following columns to `cvd`:
  - `Healthy_Diet_Score`: This variable calculates a score based on the individual's diet. It considers the consumption of fruits, green vegetables, and fried potatoes. More consumption of fruits and green vegetables adds positively to the score, while consumption of fried potatoes subtracts from the score. All weights are 1.
  - `Smoking_Alcohol`: This interaction term represents the combination of smoking and alcohol consumption. It multiplies the mapped values of smoking history and alcohol consumption.
  - `Checkup_Exercise`: This interaction term represents the combination of health check-up frequency and exercise habits. It multiplies the mapped values of health check-up frequency and exercise habits.
  - `Height_to_Weight`: This variable calculates the ratio of an individual's height to their weight.
  - `Fruit_Vegetables`: This interaction term represents the combined consumption of fruits and green vegetables. It multiplies the values of fruit consumption and green vegetable consumption.
  - `HealthyDiet_Lifestyle`: This interaction term represents the combination of the Healthy Diet Score and the Lifestyle Score. It multiplies the values of these two scores.
  - `Alcohol_FriedPotato`: This interaction term represents the combined consumption of alcohol and fried potatoes. It multiplies the values of alcohol consumption and fried potato consumption.

validator:
  namespace_check:
    cvd:
"""

cvd['Healthy_Diet_Score'] = cvd['Fruit_Consumption'] + cvd['Green_Vegetables_Consumption'] - cvd['FriedPotato_Consumption']
cvd['Smoking_Alcohol'] = cvd['Smoking_History'].replace(smoking_mapping) * cvd['Alcohol_Consumption']
cvd['Checkup_Exercise'] = cvd['Checkup_Frequency'] * cvd['Exercise'].replace(exercise_mapping)
cvd['Height_to_Weight'] = cvd['Height_(cm)'] / cvd['Weight_(kg)']
cvd['Fruit_Vegetables'] = cvd['Fruit_Consumption'] * cvd['Green_Vegetables_Consumption']
cvd['Fruit_Vegetables'] = cvd['Fruit_Consumption'] * cvd['Green_Vegetables_Consumption']
cvd['HealthyDiet_Lifestyle'] = cvd['Healthy_Diet_Score'] * cvd['Lifestyle_Score']
cvd['Alcohol_FriedPotato'] = cvd['Alcohol_Consumption'] * cvd['FriedPotato_Consumption']

# %%
"""
question: |
  Convert the "Diabetes" column to 0 and 1 through the following rules:
  - "No" and "No, pre-diabetes or borderline diabetes" are represented as 0.
  - "Yes" and "Yes, but female told only during pregnancy" are represented as 1.

validator:
  namespace_check:
    cvd:
"""

cvd['Diabetes'] = cvd['Diabetes'].map({
    'No': 0, 
    'No, pre-diabetes or borderline diabetes': 0, 
    'Yes, but female told only during pregnancy': 1,
    'Yes': 1
})

# %%
"""
question: |
  Split the "Sex" column into split into two separate binary variables: Sex_Male and Sex_Female, where a 1 indicates the presence of the category and a 0 indicates the absence.
  Remove the original "Sex" column.

validator:
  namespace_check:
    cvd:
"""

cvd = pd.get_dummies(cvd, columns=['Sex'])

# %%
"""
question: |
  Convert remaining categorical variables with "Yes" and "No" values to binary format.

validator:
  namespace_check:
    cvd:
"""

binary_columns = ['Heart_Disease', 'Skin_Cancer', 'Other_Cancer', 'Depression', 'Arthritis', 'Smoking_History','Exercise']
for column in binary_columns:
    cvd[column] = cvd[column].map({'Yes': 1, 'No': 0})

# %%
"""
question: |
  Drop all rows with missing values from the dataset. And then drop the duplicates. Save the cleaned dataset inplace.

validator:
  namespace_check:
    cvd:
"""

# Drop rows with missing values
cvd = cvd.dropna()

# Drop duplicates
cvd = cvd.drop_duplicates()

# %%
"""
question: |
  Calculate the mean, median, and standard deviation for each numerical variable in the dataset. Show three columns: mean, median, and std. Sort the variables alphabetically.
"""

cvd.describe().loc[['mean', '50%', 'std']].rename(index={'50%': 'median'}).transpose().sort_index()

# %%
"""
question: |
  Find the number of individuals for each combination of general health status and last checkup time.
  Generate a contingency table with "General Health" as the index and "Last Checkup" as the columns.
  The health status should be sorted from the worst to best, and the last checkup time should be sorted from the most recent to the least recent.
"""

pd.crosstab(cvd['General_Health'], cvd['Checkup'], rownames=['General Health'], colnames=['Last Checkup']).sort_index(ascending=False, key=lambda x: x.map({'Excellent': 5, 'Very Good': 4, 'Good': 3, 'Fair': 2, 'Poor': 1}))[['Within the past year', 'Within the past 2 years', 'Within the past 5 years', '5 or more years ago', 'Never']]

# %%
"""
question: |
  Show the pearson correlation between general health status and last checkup time. Return the correlation coefficient.
  The general health status should be mapped to numerical values as follows: "Excellent" = 5, "Very Good" = 4, "Good" = 3, "Fair" = 2, "Poor" = 1.
  The last checkup time is measured by years. For example, if the last checkup time is "Within the past 2 years", it should be mapped to 2.
  Assume the last checkup time to be 10 for 5 or more years, and 20 if the person has never had a checkup.
"""

from scipy.stats import pearsonr

# Map health status to scores
general_health_scores = cvd['General_Health'].map({'Excellent': 5, 'Very Good': 4, 'Good': 3, 'Fair': 2, 'Poor': 1})
# Map last checkup time to scores
last_checkup_scores = cvd['Checkup'].map({'Within the past year': 1, 'Within the past 2 years': 2, 'Within the past 5 years': 5, '5 or more years ago': 10, 'Never': 20})
pearsonr(general_health_scores, last_checkup_scores)[0]

# %%
"""
question: |
  Convert the following columns to ordinal:
  - General_Health: "Poor" is represented as 0 and "Excellent" is represented as 4, with intermediate categories assigned consecutive numbers. 
  - BMI_Category: "Underweight" is represented as 0 and "Obesity" is represented as 3, with intermediate categories assigned consecutive numbers.
  - Age_Category: It is mapped from age ranges into an ordinal format, where "18-24" is represented as 0 and "80+" is represented as 12, with intermediate categories assigned consecutive numbers.
  Then drop the checkup column.

validator:
  namespace_check:
    cvd:
"""

general_health_mapping = {
    'Poor': 0,
    'Fair': 1,
    'Good': 2,
    'Very Good': 3,
    'Excellent': 4
}
cvd['General_Health'] = cvd['General_Health'].map(general_health_mapping)

bmi_mapping = {
    'Underweight': 0,
    'Normal weight': 1,
    'Overweight': 2,
    'Obesity': 3
}

cvd['BMI_Category'] = cvd['BMI_Category'].map(bmi_mapping).astype(int)

age_category_mapping = {
    '18-24': 0,
    '25-29': 1,
    '30-34': 2,
    '35-39': 3,
    '40-44': 4,
    '45-49': 5,
    '50-54': 6,
    '55-59': 7,
    '60-64': 8,
    '65-69': 9,
    '70-74': 10,
    '75-79': 11,
    '80+': 12
}
cvd['Age_Category'] = cvd['Age_Category'].map(age_category_mapping)    

cvd = cvd.drop(columns=['Checkup'])

# %%
"""
question: Conduct a chi-squared test to examine the relationship between exercise habits and heart disease. Show the chi-squared statistic and p-value.
"""

from scipy.stats import chi2_contingency

# Create contingency table
contingency = pd.crosstab(cvd['Exercise'], cvd['Heart_Disease'])

# Conduct chi-squared test
chi2, p, dof, expected = chi2_contingency(contingency)

chi2, p

# %%
"""
question: Conduct a t-test to compare the mean BMI of individuals with and without heart disease. Show p-value.

validator:
  result:
    atol: 0
"""

from scipy.stats import ttest_ind

# Separate the groups
group1 = cvd.loc[cvd['Heart_Disease'].astype(bool), 'BMI']
group2 = cvd.loc[~cvd['Heart_Disease'].astype(bool), 'BMI']

# Conduct t-test
t_stat, p_val = ttest_ind(group1, group2)

p_val

# %%
"""
question: |
  Try to predict heart disease based on all other variables. Split the dataset into training and testing sets with a test size of 0.2.
  Use random state 42 for reproducibility. Save the training set as `X_train`, `y_train`, and the testing set as `X_test`, `y_test`.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

from sklearn.model_selection import train_test_split
X = cvd.drop('Heart_Disease', axis=1)
y = cvd['Heart_Disease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Construct a model using XGBClassifier to predict heart disease. Save it in a variable called `model`.
  Fit the model on the training set.

validator:
  template: intact
  namespace_check:
    model:
      type_only: true
  model:
    model_name: model
    inputs_name: X_test
    labels_name: y_test
    metric_type: roc_auc
    tolerance: 0.99

execution:
  forbid_names:
    - X_test
    - y_test
  max_time: 15
"""

from xgboost import XGBClassifier

model = XGBClassifier(scale_pos_weight=sum(y==0)/sum(y==1), # adjust class weights due to class imbalance
                      eval_metric='logloss', # use logloss to evaluate performance
                      use_label_encoder=False, # to avoid warning message
                      random_state=42)
model.fit(X_train, y_train)

# %%
"""
question: |
  Make predictions on the test set. Compute area under ROC curve.

execution:
  max_time: 2
"""

from sklearn.metrics import roc_curve, auc
y_pred = model.predict(X_test)
y_score = model.predict_proba(X_test)[:,1]

fpr_optimized, tpr_optimized, _ = roc_curve(y_test, y_pred)
roc_auc_optimized = auc(fpr_optimized, tpr_optimized)
roc_auc_optimized
