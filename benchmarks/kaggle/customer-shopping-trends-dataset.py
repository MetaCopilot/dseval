# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/shopping_trends_updated.csv` into a variable `shopping`.

validator:
  namespace_check:
    shopping:
"""

shopping = pd.read_csv('inputs/shopping_trends_updated.csv')

# %%
"""
question: |
  What is the most common item purchased? Return the item name.
"""

shopping['Item Purchased'].mode().iloc[0]

# %%
"""
question: |
  What is the average purchase amount for customers with a subscription status of 'Yes' and 'No'?
"""

shopping.groupby('Subscription Status')['Purchase Amount (USD)'].mean()

# %%
"""
question: |
  How many customers used a promo code for their purchase?
"""

(shopping['Promo Code Used'] == 'Yes').sum()

# %%
"""
question: |
  What is the most common category of items purchased by female customers with a review rating below 3?
"""

shopping.loc[(shopping['Gender'] == 'Female') & (shopping['Review Rating'] < 3), 'Category'].mode().iloc[0]

# %%
"""
question: |
  What is the average purchase amount for customers who used Venmo as the payment method, but had no subscription and did not use a promo code? Return the average purchase amount.
"""

shopping.loc[(shopping['Subscription Status'] == 'No') & (shopping['Payment Method'] == 'Venmo') & (shopping['Promo Code Used'] == 'No'), 'Purchase Amount (USD)'].mean()

# %%
"""
question: |
  Conduct a chi-squared test to examine the relationship between 'Gender' and 'Discount Applied'. Show the chi-squared statistic.
"""

from scipy.stats import chi2_contingency

# Create contingency table
contingency = pd.crosstab(shopping['Gender'], shopping['Discount Applied'])

# Conduct chi-squared test
chi2, p, dof, expected = chi2_contingency(contingency)

chi2

# %%
"""
question: |
  Create a pivot table that shows the average purchase amount for each combination of 'Gender' and 'Category'.
"""

shopping.pivot_table(values='Purchase Amount (USD)', index='Gender', columns='Category')

# %%
"""
question: |
  Create a pivot table that shows the total purchase amount for each combination of 'Location' and 'Season'.
"""

shopping.pivot_table(values='Purchase Amount (USD)', index='Location', columns='Season', aggfunc='sum')

# %%
"""
question: |
  Create a new feature "Seasonal Shopping" which indicates if the customers in a certain location make most of their purchases in a particular season. If the customers make more than 35% of their purchases in a single season, the location is considered "Seasonal Shopping". Otherwise, they are not considered as "Seasonal Shopping". Save the new feature in-place as boolean.

validator:
  namespace_check:
    shopping:
"""

seasonal_shopper = shopping.groupby(['Location', 'Season']).size().groupby(level=0).apply(lambda x: x.max() / x.sum() > 0.35)
shopping['Seasonal Shopping'] = shopping['Location'].map(seasonal_shopper)

# %%
"""
question: |
  Identify anomalies in the 'Previous Purchases' column using the Z-score method.
"""

from scipy.stats import zscore

# Calculate Z-scores
z_scores = zscore(shopping['Previous Purchases'])

# Identify anomalies
shopping[np.abs(z_scores) > 3]

# %%
"""
question: |
  Create a new feature 'Review Group' which categorizes customers into groups based on their review ratings. The groups are defined as follows:
  - "Excellent": Review rating >= 4.5
  - "Good": 3.5 <= Review rating < 4.5
  - "Fair": 2.8 <= Review rating < 3.5
  - "Poor": Review rating < 2.8
  Save the new feature in-place.

validator:
  namespace_check:
    shopping:
"""

shopping['Review Group'] = pd.cut(shopping['Review Rating'], bins=[0, 2.8, 3.5, 4.5, 5 + 1e-12], labels=['Poor', 'Fair', 'Good', 'Excellent'], right=False)

# %%
"""
question: |
  Conduct a chi-squared test to examine the relationship between 'Review Group' and 'Subscription Status'. Show the chi-squared statistic and p-value.
"""

# Create contingency table
contingency = pd.crosstab(shopping['Review Group'], shopping['Subscription Status'])

# Conduct chi-squared test
chi2, p, dof, expected = chi2_contingency(contingency)

chi2, p
