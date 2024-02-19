# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/Billionaires Statistics Dataset.csv` into a variable `billionaires`.

validator:
  namespace_check:
    billionaires:
"""

billionaires = pd.read_csv('inputs/Billionaires Statistics Dataset.csv')

# %%
"""
question: |
  Identify the top 10 billionaires with the highest net worth as of right now. Return a DataFrame containing their "rank", "personName", and "finalWorth".
"""

billionaires[['rank', 'personName', 'finalWorth']].sort_values(by='finalWorth', ascending=False).head(10)

# %%
"""
question: |
  Identify the top 10 countries with the most billionaires. Return a Series with "Country" as the index and the "Number of Billionaires" as the values.
"""

billionaires['country'].value_counts().head(10).rename('Number of Billionaires').rename_axis('Country')

# %%
"""
question: |
  Calculate the average age of billionaires for each country. The result should be put into a Series with "Country" as the index and "Average Age" as the values.
"""

billionaires.groupby('country')['age'].mean().rename('Average Age').rename_axis('Country')

# %%
"""
question: |
  Compare the population as well as average net worth of male and female billionaires. Show a DataFrame with "Gender" as the index and "Population" and "Average Net Worth" as the columns.
"""

billionaires.groupby('gender').agg({'personName': 'count', 'finalWorth': 'mean'}).rename(columns={'personName': 'Population', 'finalWorth': 'Average Net Worth'}).rename_axis('Gender')

# %%
"""
question: |
  List the names of the top 10 industries that have produced the most billionaires.
"""

billionaires['industries'].value_counts().head(10).index.tolist()

# %%
"""
question: |
  Calculate the pearson correlation between the final worth and age of billionaires.
"""

billionaires['finalWorth'].corr(billionaires['age'])

# %%
"""
question: |
  Create a new feature named "wealthLevel" that classifies billionaires into different wealth levels based on their final worth. The wealth levels are defined as follows:
  - "Ultra High Net Worth": Final worth > $50 billion
  - "Very High Net Worth": $10 billion < Final worth <= $50 billion
  - "High Net Worth": $5 billion < Final worth <= $10 billion
  - "Affluent": Final worth <= $5 billion
  Use category data type for the new feature.

validator:
  namespace_check:
    billionaires:
"""

billionaires['wealthLevel'] = pd.cut(billionaires['finalWorth'], bins=[0, 5000, 10000, 50000, np.inf], labels=['Affluent', 'High Net Worth', 'Very High Net Worth', 'Ultra High Net Worth'])

# %%
"""
question: |
  Clean and tokenize the 'source' column. Convert all characters to lowercase, remove punctuation, and split the text into individual words. Present the results in a dict with the most common 20 words as the keys and their counts as the values.
"""

from collections import Counter

# Clean and tokenize the 'source' column
words = billionaires['source'].str.lower().str.replace(r'[,.;@#?!&$/]+\ *', ' ', regex=True).str.split().explode()

# Count the occurrences of each word
word_counts = Counter(words)

# Get the 20 most common words
dict(word_counts.most_common(20))

# %%
"""
question: |
  Calculate the proportion of self-made billionaires to the total number of billionaires.
"""

billionaires['selfMade'].value_counts(normalize=True).loc[True]

# %%
"""
question: |
  Identify the countries with the highest and lowest GDP. Put the results in a dict with the country names as the keys and the GDP as the values. If a country has multiple GDP values, use the average of the presented GDP values.
"""

gdp_country = billionaires[['country', 'gdp_country']].dropna()
gdp_country['gdp_country'] = gdp_country['gdp_country'].map(lambda x: float(x.split('$')[1].replace(',', '')))
{
    gdp_country.groupby('country')['gdp_country'].mean().idxmax(): gdp_country.groupby('country')['gdp_country'].mean().max(),
    gdp_country.groupby('country')['gdp_country'].mean().idxmin(): gdp_country.groupby('country')['gdp_country'].mean().min()
}
