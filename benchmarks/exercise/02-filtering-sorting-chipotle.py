# %%
import pandas as pd

# %%
"""
question: |
  Import the dataset from this `inputs/chipotle.tsv`.
  Assign it to a variable called chipo.

validator:
  namespace_check:
    chipo:

data:
  chipotle.tsv: https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv
"""

chipo = pd.read_csv('inputs/chipotle.tsv', sep = '\t')

# %%
"""
question: How many products have a unit cost more than $10.00?
"""

# clean the item_price column and transform it in a float
prices = [float(value[1 : -1]) for value in chipo.item_price]

# reassign the column with the cleaned prices
chipo.item_price = prices

# delete the duplicates in item_name and quantity
chipo_filtered = chipo.drop_duplicates(['item_name','quantity','choice_description'])

# calculate the price per item and query the ones that are greater than $10.00
chipo['price_per_item'] = chipo.item_price / chipo.quantity
chipo.query('price_per_item > 10').item_name.nunique()

# %%
"""
question: |
  What is the price of each item? 
  Return a data frame with only two columns item_name and item_price, sorted from the most to less expensive
"""

# delete the duplicates in item_name and quantity
chipo_filtered = chipo.drop_duplicates(['item_name','quantity'])

# select only the products with quantity equals to 1
chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]

# select only the item_name and item_price columns
chipo_one_prod[['item_name', 'item_price']].sort_values(by = "item_price", ascending = False)

# %%
"""
question: Sort chipo by the name of the item
"""

chipo.sort_values(by = "item_name")

# %%
"""
question: What was the quantity of the most expensive item ordered?
"""

chipo.sort_values(by = "item_price", ascending = False).iloc[0].quantity

# %%
"""
question: How many times was a Veggie Salad Bowl ordered?
"""

chipo_salad = chipo[chipo.item_name == "Veggie Salad Bowl"]

len(chipo_salad)

# %%
"""
question: How many times did someone order more than one Canned Soda?
"""

chipo_drink_steak_bowl = chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]
len(chipo_drink_steak_bowl)
