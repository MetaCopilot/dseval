### Dataset name ###

Heart Attack Risk Prediction Dataset

### Dataset description ###

### Context

The Heart Attack Risk Prediction Dataset serves as a valuable resource for delving into the intricate dynamics of heart health and its predictors. Heart attacks, or myocardial infarctions, continue to be a significant global health issue, necessitating a deeper comprehension of their precursors and potential mitigating factors. This dataset encapsulates a diverse range of attributes including age, cholesterol levels, blood pressure, smoking habits, exercise patterns, dietary preferences, and more, aiming to elucidate the complex interplay of these variables in determining the likelihood of a heart attack. By employing predictive analytics and machine learning on this dataset, researchers and healthcare professionals can work towards proactive strategies for heart disease prevention and management. The dataset stands as a testament to collective efforts to enhance our understanding of cardiovascular health and pave the way for a healthier future.

### Content

This dataset provides a comprehensive array of features relevant to heart health and lifestyle choices, encompassing patient-specific details such as age, gender, cholesterol levels, blood pressure, heart rate, and indicators like diabetes, family history, smoking habits, obesity, and alcohol consumption. Additionally, lifestyle factors like exercise hours, dietary habits, stress levels, and sedentary hours are included. Medical aspects comprising previous heart problems, medication usage, and triglyceride levels are considered. Socioeconomic aspects such as income and geographical attributes like country, continent, and hemisphere are incorporated. The dataset, consisting of 8763 records from patients around the globe, culminates in a crucial binary classification feature denoting the presence or absence of a heart attack risk, providing a comprehensive resource for predictive analysis and research in cardiovascular health.

### Dataset Glossary (Column-wise)

* <b>Patient ID</b> - Unique identifier for each patient
* <b>Age</b> - Age of the patient
* <b>Sex</b> - Gender of the patient (Male/Female)
* <b>Cholesterol</b> - Cholesterol levels of the patient
* <b>Blood Pressure</b> - Blood pressure of the patient (systolic/diastolic)
* <b>Heart Rate</b> - Heart rate of the patient
* <b>Diabetes</b> - Whether the patient has diabetes (Yes/No)
* <b>Family History</b> - Family history of heart-related problems (1: Yes, 0: No)
* <b>Smoking</b> - Smoking status of the patient (1: Smoker, 0: Non-smoker)
* <b>Obesity</b> - Obesity status of the patient (1: Obese, 0: Not obese)
* <b>Alcohol Consumption</b> - Level of alcohol consumption by the patient (None/Light/Moderate/Heavy)
* <b>Exercise Hours Per Week</b> - Number of exercise hours per week
* <b>Diet</b> - Dietary habits of the patient (Healthy/Average/Unhealthy)
* <b>Previous Heart Problems</b> - Previous heart problems of the patient (1: Yes, 0: No)
* <b>Medication Use</b> - Medication usage by the patient (1: Yes, 0: No)
* <b>Stress Level</b> - Stress level reported by the patient (1-10)
* <b>Sedentary Hours Per Day</b> - Hours of sedentary activity per day
* <b>Income</b> - Income level of the patient
* <b>BMI</b> - Body Mass Index (BMI) of the patient
* <b>Triglycerides</b> - Triglyceride levels of the patient
* <b>Physical Activity Days Per Week</b> - Days of physical activity per week
* <b>Sleep Hours Per Day</b> - Hours of sleep per day
* <b>Country</b> - Country of the patient
* <b>Continent</b> - Continent where the patient resides
* <b>Hemisphere</b> - Hemisphere where the patient resides
* <b>Heart Attack Risk</b> - Presence of heart attack risk (1: Yes, 0: No)

### Structure of the Dataset

![](https://i.imgur.com/5cTusqA.png)

### Acknowledgement

This dataset is a synthetic creation generated using ChatGPT to simulate a realistic experience. Its purpose is to provide a platform for beginners and data enthusiasts, allowing them to create, enjoy, practice, and learn from a dataset that mirrors real-world scenarios. The aim is to foster learning and experimentation in a simulated environment, encouraging a deeper understanding of data analysis and interpretation.

Cover Photo by: <b><a href="https://www.freepik.com/free-vector/human-internal-organ-with-heart_27289238.htm#query=heart%20organ&amp;position=14&amp;from_view=keyword&amp;track=ais">brgfx</a> on Freepik</b>

Thumbnail by: <b><a href="https://www.freepik.com/free-vector/cardiology-clinic-hospital-department-healthy-heart-cardiovascular-prevention-healthcare-industry-idea-design-element-electrocardiogram-ekg-vector-isolated-concept-metaphor-illustration_12468752.htm#query=human%20heart&amp;position=17&amp;from_view=keyword&amp;track=ais">vectorjuice</a> on Freepik</b>

### Dataset files ###

- heart_attack_prediction_dataset.csv

    pandas.DataFrame(shape=(8763, 26), columns=["Patient ID", "Age", "Sex", "Cholesterol", "Blood Pressure", "Heart Rate", "Diabetes", "Family History", "Smoking", "Obesity", "Alcohol Consumption", "Exercise Hours Per Week", "Diet", "Previous Heart Problems", "Medication Use", "Stress Level", "Sedentary Hours Per Day", "Income", "BMI", "Triglycerides", "Physical Activity Days Per Week", "Sleep Hours Per Day", "Country", "Continent", "Hemisphere", "Heart Attack Risk"])
             Patient ID  Age     Sex  Cholesterol Blood Pressure  Heart Rate  Diabetes  ...  Triglycerides  Physical Activity Days Per Week  Sleep Hours Per Day         Country      Continent           Hemisphere  Heart Attack Risk
        0       BMW7812   67    Male          208         158/88          72         0  ...            286                    0                                6       Argentina  South America  Southern Hemisphere                  0
        1       CZE1114   21    Male          389         165/93          98         1  ...            235                    1                                7          Canada  North America  Northern Hemisphere                  0
        2       BNI9906   21  Female          324         174/99          72         1  ...            587                    4                                4          France         Europe  Northern Hemisphere                  0
        3       JLN3497   84    Male          383        163/100          73         1  ...            378                    3                                4          Canada  North America  Northern Hemisphere                  0
        4       GFO8847   66    Male          318          91/88          93         1  ...            231                    1                                5        Thailand           Asia  Northern Hemisphere                  0
        ...         ...  ...     ...          ...            ...         ...       ...  ...            ...                  ...                              ...             ...            ...                  ...                ...
        8758    MSV9918   60    Male          121          94/76          61         1  ...             67                    7                                7        Thailand           Asia  Northern Hemisphere                  0
        8759    QSV6764   28  Female          120        157/102          73         1  ...            617                    4                                9          Canada  North America  Northern Hemisphere                  0
        8760    XKA5925   47    Male          250         161/75         105         0  ...            527                    4                                4          Brazil  South America  Southern Hemisphere                  1
        8761    EPE6801   36    Male          178         119/67          60         1  ...            114                    2                                8          Brazil  South America  Southern Hemisphere                  0
        8762    ZWN9666   25  Female          356         138/67          75         1  ...            180                    7                                4  United Kingdom         Europe  Northern Hemisphere                  1

