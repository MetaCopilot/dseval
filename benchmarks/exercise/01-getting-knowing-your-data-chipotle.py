# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Import the dataset from `inputs/chipotle.tsv`.
  Assign it to a variable called chipo.

validator:
  namespace_check:
    chipo:

data:
  chipotle.tsv: https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv
"""

url = 'inputs/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')

# %%
"""
question: See the first 10 entries
"""

chipo.head(10)

# %%
"""
question: What is the number of observations in the dataset?
"""

chipo.shape[0]  # entries <= 4622 observations

# %%
"""
question: What is the number of columns in the dataset?
"""

chipo.shape[1]

# %%
"""
question: The name of all the columns.

validator:
  result:
    compare_fn:
      value_only: true
"""

chipo.columns

# %%
"""
question: How is the dataset indexed?
"""

chipo.index

# %%
"""
question: What is the name of the most-ordered item?
"""

c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1).index[0]

# %%
"""
question: For the most-ordered item, how many items were ordered?
"""

c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)['quantity'][0]

# %%
"""
question: How much quantity was ordered for the most ordered item in the choice_description column?
"""

c = chipo.groupby('choice_description').sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)['quantity'][0]

# %%
"""
question: How many items were ordered in total?
"""

total_items_orders = chipo.quantity.sum()
total_items_orders

# %%
"""
question: Turn the item price into a float. The change should happen in-place.

validator:
  namespace_check:
    chipo:
"""

dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)

# %%
"""
question: How much was the revenue for the period in the dataset? Round to two decimal places.
"""

revenue = (chipo['quantity']* chipo['item_price']).sum()

np.round(revenue,2)

# %%
"""
question: How many orders were made in the period?
"""

orders = chipo.order_id.value_counts().count()
orders

# %%
"""
question: What is the average revenue amount per order?
"""

chipo['revenue'] = chipo['quantity'] * chipo['item_price']
chipo.groupby(by=['order_id']).sum(numeric_only=True).mean()['revenue']

# %%
"""
question: How many different items are sold?
"""

chipo.item_name.value_counts().count()
