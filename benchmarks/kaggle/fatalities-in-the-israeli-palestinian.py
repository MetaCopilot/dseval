# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/fatalities_isr_pse_conflict_2000_to_2023.csv` into a variable `fatalities`.

validator:
  namespace_check:
    fatalities:
"""

fatalities = pd.read_csv('inputs/fatalities_isr_pse_conflict_2000_to_2023.csv')

# %%
"""
question: |
  Fill missing values in the dataset as follows:
  - For numerical columns, fill with the mean of the column.
  - For the "place_of_residence" column, fill with "Unknown".
  - For the "type_of_injury" and "ammunition" columns, fill with "Not Specified".
  - For the "gender" column, fill with the mode of the column.
  - For the "took_part_in_the_hostilities" column, drop the rows with missing values.
  Save the cleaned dataset in-place.

validator:
  namespace_check:
    fatalities:
"""

# Fill missing values
fatalities['age'] = fatalities['age'].fillna(fatalities['age'].mean())
fatalities['place_of_residence'] = fatalities['place_of_residence'].fillna('Unknown')
fatalities['type_of_injury'] = fatalities['type_of_injury'].fillna('Not Specified')
fatalities['ammunition'] = fatalities['ammunition'].fillna('Not Specified')
fatalities['gender'] = fatalities['gender'].fillna(fatalities['gender'].mode()[0])

# Drop rows with missing values
fatalities = fatalities.dropna(subset=['took_part_in_the_hostilities'])

# %%
"""
question: |
  Convert the `date_of_event` and `date_of_death` columns to datetime format.

validator:
  namespace_check:
    fatalities:
"""

fatalities['date_of_event'] = pd.to_datetime(fatalities['date_of_event'])
fatalities['date_of_death'] = pd.to_datetime(fatalities['date_of_death'])

# %%
"""
question: |
  Show the fatality trends from 2000 to 2023. Count the number of fatalities for each year. Return a Series with "Year" as the index and "Number of Fatalities" as the values.
"""

fatalities['date_of_event'].dt.year.value_counts().sort_index().rename('Number of Fatalities').rename_axis('Year')

# %%
"""
question: |
  Analyze the difference of brutal occupation between men and women, and between young and old.
  Count the number of fatalities for each gender and age group. The age groups are "Under 18" (including 18), "18-40" (40 included), "40-60" (60 included), and "60+".
  Return a dict with "Men", "Women", "Under 18", "18-40", "40-60", and "60+" as the keys, and the number of fatalities as the values.
"""

{
    'Men': fatalities[fatalities['gender'] == 'M']['gender'].count(),
    'Women': fatalities[fatalities['gender'] == 'F']['gender'].count(),
    'Under 18': fatalities[fatalities['age'] <= 18]['age'].count(),
    '18-40': fatalities[(fatalities['age'] > 18) & (fatalities['age'] <= 40)]['age'].count(),
    '40-60': fatalities[(fatalities['age'] > 40) & (fatalities['age'] <= 60)]['age'].count(),
    '60+': fatalities[fatalities['age'] > 60]['age'].count()
}

# %%
"""
question: |
  Analyze the distribution of fatalities by district where the event took place. Show the counts of top 10 districts and the rest as "Others".
  Return a Series with "District" as the index and "Number of Fatalities" as the values.
"""

district_counts = fatalities['event_location_district'].value_counts()
pd.concat([district_counts[:10], pd.Series(district_counts[10:].sum(), index=['Others'])]).rename('Number of Fatalities').rename_axis('District')

# %%
"""
question: |
  Analyze the distribution of place of residence. Show the counts of top 10 places and the rest as "Others".
  Return a Series with "Place of Residence" as the index and "Number of Fatalities" as the values.
"""

residence_counts = fatalities['place_of_residence'].value_counts()
pd.concat([residence_counts[:10], pd.Series(residence_counts[10:].sum(), index=['Others'])]).rename('Number of Fatalities').rename_axis('Place of Residence')

# %%
"""
question: |
  Count the occurrences of each type of injury.

validator:
  result:
    value_only: true
    ignore_order: true
"""

fatalities['type_of_injury'].value_counts()

# %%
"""
question: |
  Identify the most common characteristics of victims. For each of the following characteristics: "age", "gender", "citizenship", "place_of_residence", "type_of_injury", "ammunition", "killed_by", calculate its mode (most common value). Show the result in a Series with "Characteristic" as the index and "Mode" as the values.
"""

characteristics = ['age', 'gender', 'citizenship', 'place_of_residence', 'type_of_injury', 'ammunition', 'killed_by']
pd.Series({characteristic: fatalities[characteristic].mode()[0] for characteristic in characteristics}, name='Mode').rename_axis('Characteristic')

# %%
"""
question: |
  Create a new feature that represents the time elapsed between the date of event and date of death. The time should be measured by days. Save the new feature in a new column named "days_until_death".

validator:
  namespace_check:
    fatalities:
"""

fatalities['days_until_death'] = (fatalities['date_of_death'] - fatalities['date_of_event']).dt.days

# %%
"""
question: |
  Compare the trend of fatalities with respect to time, between Palestinian and Israeli.
  Count the number of fatalities for each year for each citizenship. Return a DataFrame with "Year", "Palestinian Fatalities", and "Israeli Fatalities" as the columns.

validator:
  result:
    ignore_index: true
"""

fatalities.groupby([fatalities['date_of_event'].dt.year, 'citizenship']).size().unstack(fill_value=0).rename(columns={'Palestinian': 'Palestinian Fatalities', 'Israeli': 'Israeli Fatalities'}).reset_index().rename(columns={'date_of_event': 'Year'})[['Year', 'Palestinian Fatalities', 'Israeli Fatalities']]
