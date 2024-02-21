### Dataset name ###

Super Market Sales

### Dataset description ###

Here's a brief description of each of the attributes or labels in the dataset:

1. **Invoice ID**: A unique identifier for each invoice or transaction.
2. **Branch**: The branch or location where the transaction occurred.
3. **City**: The city where the branch is located.
4. **Customer Type**: Indicates whether the customer is a regular or new customer.
5. **Gender**: The gender of the customer.
6. **Product Line**: The category or type of product purchased.
7. **Unit Price**: The price of a single unit of the product.
8. **Quantity**: The number of units of the product purchased.
9. **Tax 5%**: The amount of tax (5% of the total cost) applied to the transaction.
10. **Total**: The total cost of the transaction, including tax.
11. **Date**: The date when the transaction took place.
12. **Time**: The time of day when the transaction occurred.
13. **Payment**: The payment method used (e.g., credit card, cash).
14. **COGS (Cost of Goods Sold)**: The direct costs associated with producing or purchasing the products sold.
15. **Gross Margin Percentage**: The profit margin percentage for the transaction.
16. **Gross Income**: The total profit earned from the transaction.
17. **Rating**: Customer satisfaction rating or feedback on the transaction.

 For instance, if you were interested in predicting customer satisfaction, **Rating** might be a suitable label. If you were trying to predict sales or revenue, **Total** or **Gross Income** could be a potential label.

### Dataset files ###

- supermarket_sales.csv

    pandas.DataFrame(shape=(1000, 17), columns=["Invoice ID", "Branch", "City", "Customer type", "Gender", "Product line", "Unit price", "Quantity", "Tax 5%", "Total", "Date", "Time", "Payment", "cogs", "gross margin percentage", "gross income", "Rating"])
              Invoice ID Branch       City Customer type  Gender         Product line  Unit price  ...       Date   Time      Payment    cogs gross margin percentage gross income  Rating
        0    750-67-8428      A     Yangon        Member  Female    Health and beauty       74.69  ...   1/5/2019  13:08      Ewallet  522.83             4.761905         26.1415     9.1
        1    226-31-3081      C  Naypyitaw        Normal  Female  Electronic acces...       15.28  ...   3/8/2019  10:29         Cash   76.40             4.761905          3.8200     9.6
        2    631-41-3108      A     Yangon        Normal    Male   Home and lifestyle       46.33  ...   3/3/2019  13:23  Credit card  324.31             4.761905         16.2155     7.4
        3    123-19-1176      A     Yangon        Member    Male    Health and beauty       58.22  ...  1/27/2019  20:33      Ewallet  465.76             4.761905         23.2880     8.4
        4    373-73-7910      A     Yangon        Normal    Male    Sports and travel       86.31  ...   2/8/2019  10:37      Ewallet  604.17             4.761905         30.2085     5.3
        ..           ...    ...        ...           ...     ...                  ...         ...  ...        ...    ...          ...     ...                  ...             ...     ...
        995  233-67-5758      C  Naypyitaw        Normal    Male    Health and beauty       40.35  ...  1/29/2019  13:46      Ewallet   40.35             4.761905          2.0175     6.2
        996  303-96-2227      B   Mandalay        Normal  Female   Home and lifestyle       97.38  ...   3/2/2019  17:16      Ewallet  973.80             4.761905         48.6900     4.4
        997  727-02-1313      A     Yangon        Member    Male   Food and beverages       31.84  ...   2/9/2019  13:22         Cash   31.84             4.761905          1.5920     7.7
        998  347-56-2442      A     Yangon        Normal    Male   Home and lifestyle       65.82  ...  2/22/2019  15:33         Cash   65.82             4.761905          3.2910     4.1
        999  849-09-3807      A     Yangon        Member  Female  Fashion accessories       88.34  ...  2/18/2019  13:28         Cash  618.38             4.761905         30.9190     6.6

