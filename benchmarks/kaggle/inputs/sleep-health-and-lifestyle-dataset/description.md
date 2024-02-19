### Dataset name ###

Sleep Health and Lifestyle Dataset

### Dataset description ###

Note: Don't forget to upvote when you find this useful.

**Dataset Overview:**
The Sleep Health and Lifestyle Dataset comprises 400 rows and 13 columns, covering a wide range of variables related to sleep and daily habits. It includes details such as gender, age, occupation, sleep duration, quality of sleep, physical activity level, stress levels, BMI category, blood pressure, heart rate, daily steps, and the presence or absence of sleep disorders.

**Key Features of the Dataset:**
Comprehensive Sleep Metrics: Explore sleep duration, quality, and factors influencing sleep patterns.
Lifestyle Factors: Analyze physical activity levels, stress levels, and BMI categories.
Cardiovascular Health: Examine blood pressure and heart rate measurements.
Sleep Disorder Analysis: Identify the occurrence of sleep disorders such as Insomnia and Sleep Apnea.

**Dataset Columns:**<br>
Person ID: An identifier for each individual.<br>
Gender: The gender of the person (Male/Female).<br>
Age: The age of the person in years.<br>
Occupation: The occupation or profession of the person.<br>
Sleep Duration (hours): The number of hours the person sleeps per day.<br>
Quality of Sleep (scale: 1-10): A subjective rating of the quality of sleep, ranging from 1 to 10.<br>
Physical Activity Level (minutes/day): The number of minutes the person engages in physical activity daily.<br>
Stress Level (scale: 1-10): A subjective rating of the stress level experienced by the person, ranging from 1 to 10.<br>
BMI Category: The BMI category of the person (e.g., Underweight, Normal, Overweight).<br>
Blood Pressure (systolic/diastolic): The blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure.<br>
Heart Rate (bpm): The resting heart rate of the person in beats per minute.<br>
Daily Steps: The number of steps the person takes per day.<br>
Sleep Disorder: The presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea).<br>

**Details about Sleep Disorder Column:**
- None: The individual does not exhibit any specific sleep disorder.
- Insomnia: The individual experiences difficulty falling asleep or staying asleep, leading to inadequate or poor-quality sleep.
- Sleep Apnea: The individual suffers from pauses in breathing during sleep, resulting in disrupted sleep patterns and potential health risks.


**Acknowledgement:**
- I would like to clarify that the data I am presenting is synthetic and created by me for illustrative purposes.

### Dataset files ###

- Sleep_health_and_lifestyle_dataset.csv

    pandas.DataFrame(shape=(374, 13), columns=["Person ID", "Gender", "Age", "Occupation", "Sleep Duration", "Quality of Sleep", "Physical Activity Level", "Stress Level", "BMI Category", "Blood Pressure", "Heart Rate", "Daily Steps", "Sleep Disorder"])
             Person ID  Gender  Age           Occupation  Sleep Duration  Quality of Sleep  Physical Activity Level  Stress Level BMI Category Blood Pressure  Heart Rate  Daily Steps Sleep Disorder
        0            1    Male   27    Software Engineer             6.1                 6                   42                 6   Overweight         126/83          77         4200            NaN
        1            2    Male   28               Doctor             6.2                 6                   60                 8       Normal         125/80          75        10000            NaN
        2            3    Male   28               Doctor             6.2                 6                   60                 8       Normal         125/80          75        10000            NaN
        3            4    Male   28  Sales Representa...             5.9                 4                   30                 8        Obese         140/90          85         3000    Sleep Apnea
        4            5    Male   28  Sales Representa...             5.9                 4                   30                 8        Obese         140/90          85         3000    Sleep Apnea
        ..         ...     ...  ...                  ...             ...               ...                  ...               ...          ...            ...         ...          ...            ...
        369        370  Female   59                Nurse             8.1                 9                   75                 3   Overweight         140/95          68         7000    Sleep Apnea
        370        371  Female   59                Nurse             8.0                 9                   75                 3   Overweight         140/95          68         7000    Sleep Apnea
        371        372  Female   59                Nurse             8.1                 9                   75                 3   Overweight         140/95          68         7000    Sleep Apnea
        372        373  Female   59                Nurse             8.1                 9                   75                 3   Overweight         140/95          68         7000    Sleep Apnea
        373        374  Female   59                Nurse             8.1                 9                   75                 3   Overweight         140/95          68         7000    Sleep Apnea

