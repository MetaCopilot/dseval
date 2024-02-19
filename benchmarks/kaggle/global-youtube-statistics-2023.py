# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/Global YouTube Statistics.csv` into a variable `youtube`.

validator:
  namespace_check:
    youtube:
"""

youtube = pd.read_csv('inputs/Global YouTube Statistics.csv', encoding='latin-1')

# %%
"""
question: |
  Create a "created" column by assembling the "created_year", "created_month", and "created_date" columns. The "created" column should be of type `datetime64[ns]`.

validator:
  namespace_check:
    youtube:
"""

youtube['created'] = youtube.apply(lambda row: str(row['created_month']) + ' ' + str(int(row['created_date'])) + ', ' + str(int(row['created_year'])) if isinstance(row['created_month'], str) else float('nan'), axis=1)
youtube['created'] = pd.to_datetime(youtube['created'])

# %%
"""
question: |
  Compute the average yearly earnings for every YouTuber. The average yearly earnings is the average of the lowest and highest yearly earnings. Save the result in a new column named "average_yearly_earnings".

validator:
  namespace_check:
    youtube:
"""

youtube['average_yearly_earnings'] = (youtube['lowest_yearly_earnings'] + youtube['highest_yearly_earnings']) / 2

# %%
"""
question: |
  Compute the ratio of missing values for each column.
"""

youtube.isnull().mean()

# %%
"""
question: |
  Identify the names of top 10 YouTubers with the highest average yearly earnings.

validator:
  result:
    ignore_order: true
    value_only: true
"""

youtube.set_index('Youtuber')['average_yearly_earnings'].sort_values(ascending=False).head(10).index.tolist()

# %%
"""
question: |
  Identify the top 10 countries with the most YouTubers. Return a Series with "Country" as the index and the "Number of YouTubers" as the values.
"""

youtube['Country'].value_counts().head(10).rename('Number of YouTubers').rename_axis('Country')

# %%
"""
question: |
  Calculate the number of YouTubers that was created in each year (sorted by year).

validator:
  result:
    ignore_index: true
"""

youtube['created'].dt.year.value_counts().sort_index()

# %%
"""
question: |
  Count the percentage of top-trending channel types. The top-trending channel types are the top 10 most common channel types. Categorize the non-top-10 types as "Others". Return a dict with the channel types as the keys and the percentages as the values.
"""

top_10_channel_types = youtube['channel_type'].value_counts().head(10).index
(youtube['channel_type'].where(youtube['channel_type'].isin(top_10_channel_types), 'Others').value_counts(normalize=True) * 100).to_dict()

# %%
"""
question: |
  Identify the top 3 earners among YouTube channels based on their creation years. Return a DataFrame with "Year", "Youtuber" as index, and "Average Yearly Earnings" as the columns.
"""

top_earners = []
for year in sorted(youtube['created'].dt.year.unique()):
    top_earners_year = youtube.loc[youtube['created'].dt.year == year, ['Youtuber', 'average_yearly_earnings']].sort_values(by='average_yearly_earnings', ascending=False).head(3)
    top_earners_year['Year'] = year
    top_earners.append(top_earners_year)
top_earners = pd.concat(top_earners)

top_earners.set_index(['Year', 'Youtuber']).rename(columns={'average_yearly_earnings': 'Average Yearly Earnings'})

# %%
"""
question: |
  Compute the correlation of uploads and average yearly earnings.
"""

youtube['uploads'].corr(youtube['average_yearly_earnings'])

# %%
"""
question: |
  List out the names of the top 10 YouTubers with the biggest increase in subscribers in the last 30 days.

validator:
  result:
    ignore_order: true
"""

youtube[['Youtuber', 'subscribers_for_last_30_days']].sort_values(by='subscribers_for_last_30_days', ascending=False).head(10)['Youtuber'].tolist()
