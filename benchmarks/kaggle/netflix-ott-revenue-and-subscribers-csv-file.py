# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/netflix_revenue_updated.csv` into a variable `netflix`.

validator:
  namespace_check:
    netflix:
"""

netflix = pd.read_csv('inputs/netflix_revenue_updated.csv')

# %%
"""
question: |
  Convert the `Date` column to datetime format. Remove excessive spaces from the column names. Save the cleaned dataset in-place.

validator:
  namespace_check:
    netflix:
"""

# Convert Date to datetime
netflix['Date'] = pd.to_datetime(netflix['Date'], dayfirst=True)

# Canonicalize column names
netflix.columns = [' '.join(col.strip().split()) for col in netflix.columns]

# %%
"""
question: |
  Calculate the mean, median, and standard deviation of revenue and subscribers for each region.
  Return a DataFrame with "Region" as the index and "Mean Revenue", "Median Revenue", "Std Revenue", "Mean Subscribers", "Median Subscribers", "Std Subscribers" as the columns.

validator:
  result:
    ignore_order: true
"""

regions = ['UCAN', 'EMEA', 'LATM', 'APAC']
pd.concat([
    netflix[[f'{region} Streaming Revenue' for region in regions]].agg(['mean', 'median', 'std']).rename(index={'mean': 'Mean Revenue', 'median': 'Median Revenue', 'std': 'Std Revenue'}).rename(columns=lambda col: col.split()[0]),
    netflix[[f'{region} Members' for region in regions]].agg(['mean', 'median', 'std']).rename(index={'mean': 'Mean Subscribers', 'median': 'Median Subscribers', 'std': 'Std Subscribers'}).rename(columns=lambda col: col.split()[0])
]).transpose()

# %%
"""
question: |
  Calculate the average quarterly revenue growth rate, ARPU growth rate, and subscriber growth rate for each region throughout the entire period. The result should be a DataFrame with "Region" as the index and "Revenue Growth Rate", "ARPU Growth Rate", "Subscriber Growth Rate" as the columns.

validator:
  result:
    ignore_order: true
"""

growth_rates = []
for region in regions:
    revenue = netflix[f'{region} Streaming Revenue']
    arpu = netflix[f'{region} ARPU']
    subscribers = netflix[f'{region} Members']
    growth_rates.append({
        'Region': region,
        'Revenue Growth Rate': ((revenue - revenue.shift(1)) / revenue.shift(1)).mean(),
        'ARPU Growth Rate': ((arpu - arpu.shift(1)) / arpu.shift(1)).mean(),
        'Subscriber Growth Rate': ((subscribers - subscribers.shift(1)) / subscribers.shift(1)).mean(),
    })
growth_rates = pd.DataFrame.from_records(growth_rates).set_index('Region')

growth_rates

# %%
"""
question: Which region has the highest average revenue growth rate?
"""

growth_rates['Revenue Growth Rate'].idxmax()

# %%
"""
question: |
  Analyze the seasonality in the revenue and subscribers for each region.
  For each region, calculate the average revenue and subscribers for each month of the year.
  The result should have "Region" and "Month" as the index and "Average Revenue" and "Average Subscribers" as the columns.

validator:
  result:
    ignore_order: true  
"""

seasonality = []
for region in regions:
    monthly_avg = netflix.groupby(netflix['Date'].dt.month)[[f'{region} Streaming Revenue', f'{region} Members']].mean().reset_index().rename(columns={f'{region} Streaming Revenue': 'Average Revenue', f'{region} Members': 'Average Subscribers', 'Date': 'Month'})
    monthly_avg['Region'] = region
    seasonality.append(monthly_avg)
seasonality = pd.concat(seasonality, axis=0).set_index(['Region', 'Month'])
seasonality

# %%
"""
question: |
  Identify the season (among Q1 to Q4) with the highest and lowest average revenue for each region.
  The result DataFrame should have "Region", "Highest Revenue Season", "Lowest Revenue Season", "Highest Revenue", and "Lowest Revenue" as its columns.

validator:
  result:
    ignore_order: true
"""

highest_lowest_revenue = pd.DataFrame(index=regions, columns=['Highest Revenue Season', 'Lowest Revenue Season', 'Highest Revenue', 'Lowest Revenue'])
for region in regions:
    region_seasonality = seasonality.loc[region]
    highest_lowest_revenue.loc[region, 'Highest Revenue Season'] = 'Q' + str(region_seasonality['Average Revenue'].idxmax() // 3)
    highest_lowest_revenue.loc[region, 'Lowest Revenue Season'] = 'Q' + str(region_seasonality['Average Revenue'].idxmin() // 3)
    highest_lowest_revenue.loc[region, 'Highest Revenue'] = region_seasonality['Average Revenue'].max()
    highest_lowest_revenue.loc[region, 'Lowest Revenue'] = region_seasonality['Average Revenue'].min()
highest_lowest_revenue

# %%
"""
question: |
  Calculate the correlation between revenue and subscribers for each region.
  Return a DataFrame with "Region" and "Correlation" as the columns.

validator:
  result:
    ignore_order: true
"""

correlations = pd.DataFrame.from_records([
    {'Region': region, 'Correlation': netflix[[f'{region} Streaming Revenue', f'{region} Members']].corr().iloc[0, 1]}
    for region in regions
])

correlations

# %%
"""
question: |
  Calculate the rolling 12-month average and standard deviation for revenue and subscribers for each region.
  Return a DataFrame with "Region", "Date", "Rolling Average Revenue", "Rolling Std Revenue", "Rolling Average Subscribers", and "Rolling Std Subscribers" as the columns. Drop rows with missing values.

validator:
  result:
    ignore_order: true
"""

rolling_stats = []
for region in regions:
    region_stats = netflix[[f'{region} Streaming Revenue', f'{region} Members']].rolling(4).agg(['mean', 'std'])
    region_stats.columns = ['Rolling Average Revenue', 'Rolling Std Revenue', 'Rolling Average Subscribers', 'Rolling Std Subscribers']
    region_stats['Region'] = region
    region_stats['Date'] = netflix['Date']
    rolling_stats.append(region_stats)
rolling_stats = pd.concat(rolling_stats).dropna().set_index(['Region', 'Date']).reset_index()

rolling_stats

# %%
"""
question: |
  For each region, identify the periods of highest and lowest volatility in revenue and subscribers.
  Volatility is measured by the standard deviation.
  Return a DataFrame with "Region", "Highest Volatility Period", "Lowest Volatility Period", "Highest Volatility", and "Lowest Volatility" as the columns. The periods should be in the format of "YYYY-MM to YYYY-MM".

validator:
  result:
    ignore_order: true
"""

volatility_periods = []
for region in regions:
    region_stats = rolling_stats.loc[rolling_stats['Region'] == region]
    volatility_periods.append({
        'Region': region,
        'Highest Volatility Period': region_stats.loc[region_stats['Rolling Std Revenue'].idxmax(), 'Date'],
        'Lowest Volatility Period': region_stats.loc[region_stats['Rolling Std Revenue'].idxmin(), 'Date'],
        'Highest Volatility': region_stats['Rolling Std Revenue'].max(),
        'Lowest Volatility': region_stats['Rolling Std Revenue'].min(),
    })

volatility_periods = pd.DataFrame.from_records(volatility_periods)
volatility_periods['Highest Volatility Period'] = volatility_periods['Highest Volatility Period'].apply(lambda dt: (dt - pd.DateOffset(years=1) + pd.DateOffset(days=1)).strftime('%Y-%m') + ' to ' + dt.strftime('%Y-%m'))
volatility_periods['Lowest Volatility Period'] = volatility_periods['Lowest Volatility Period'].apply(lambda dt: (dt - pd.DateOffset(years=1) + pd.DateOffset(days=1)).strftime('%Y-%m') + ' to ' + dt.strftime('%Y-%m'))

volatility_periods
