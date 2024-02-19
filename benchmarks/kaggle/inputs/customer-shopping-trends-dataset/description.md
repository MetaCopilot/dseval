### Dataset name ###

Customer Shopping Trends Dataset

### Dataset description ###

### Context

The Customer Shopping Preferences Dataset offers valuable insights into consumer behavior and purchasing patterns. Understanding customer preferences and trends is critical for businesses to tailor their products, marketing strategies, and overall customer experience. This dataset captures a wide range of customer attributes including age, gender, purchase history, preferred payment methods, frequency of purchases, and more. Analyzing this data can help businesses make informed decisions, optimize product offerings, and enhance customer satisfaction. The dataset stands as a valuable resource for businesses aiming to align their strategies with customer needs and preferences. It's important to note that this dataset is a Synthetic Dataset Created for Beginners to learn more about Data Analysis and Machine Learning.

### Content

This dataset encompasses various features related to customer shopping preferences, gathering essential information for businesses seeking to enhance their understanding of their customer base. The features include customer age, gender, purchase amount, preferred payment methods, frequency of purchases, and feedback ratings. Additionally, data on the type of items purchased, shopping frequency, preferred shopping seasons, and interactions with promotional offers is included. With a collection of 3900 records, this dataset serves as a foundation for businesses looking to apply data-driven insights for better decision-making and customer-centric strategies.

### Dataset Glossary (Column-wise)

* <b>Customer ID</b> - Unique identifier for each customer
* <b>Age</b> - Age of the customer
* <b>Gender</b> - Gender of the customer (Male/Female)
* <b>Item Purchased</b> - The item purchased by the customer
* <b>Category</b> - Category of the item purchased
* <b>Purchase Amount (USD)</b> - The amount of the purchase in USD
* <b>Location</b> - Location where the purchase was made
* <b>Size</b> - Size of the purchased item
* <b>Color</b> - Color of the purchased item
* <b>Season</b> - Season during which the purchase was made
* <b>Review Rating</b> - Rating given by the customer for the purchased item
* <b>Subscription Status</b> - Indicates if the customer has a subscription (Yes/No)
* <b>Shipping Type</b> - Type of shipping chosen by the customer
* <b>Discount Applied</b> - Indicates if a discount was applied to the purchase (Yes/No)
* <b>Promo Code Used</b> - Indicates if a promo code was used for the purchase (Yes/No)
* <b>Previous Purchases</b> - The total count of transactions concluded by the customer at the store, excluding the ongoing transaction
* <b>Payment Method</b> - Customer's most preferred payment method
* <b>Frequency of Purchases</b> - Frequency at which the customer makes purchases (e.g., Weekly, Fortnightly, Monthly)

### Structure of the Dataset

![](https://i.imgur.com/6UEqejq.png)

### Acknowledgement

This dataset is a synthetic creation generated using ChatGPT to simulate a realistic customer shopping experience. Its purpose is to provide a platform for beginners and data enthusiasts, allowing them to create, enjoy, practice, and learn from a dataset that mirrors real-world customer shopping behavior. The aim is to foster learning and experimentation in a simulated environment, encouraging a deeper understanding of data analysis and interpretation in the context of consumer preferences and retail scenarios.

Cover Photo by: <b><a href="https://www.freepik.com/free-vector/hand-drawn-people-shopping-sale_12063508.htm#query=shopping%20cartoon&amp;position=7&amp;from_view=keyword&amp;track=ais">Freepik</a></b>

Thumbnail by: <b><a href="https://www.flaticon.com/free-icons/clothing">Clothing icons created by Flat Icons - Flaticon</a></b>

### Dataset files ###

- shopping_trends.csv

    pandas.DataFrame(shape=(3900, 19), columns=["Customer ID", "Age", "Gender", "Item Purchased", "Category", "Purchase Amount (USD)", "Location", "Size", "Color", "Season", "Review Rating", "Subscription Status", "Payment Method", "Shipping Type", "Discount Applied", "Promo Code Used", "Previous Purchases", "Preferred Payment Method", "Frequency of Purchases"])
              Customer ID  Age  Gender Item Purchased     Category  Purchase Amount (USD)       Location  ... Payment Method   Shipping Type Discount Applied  Promo Code Used Previous Purchases Preferred Payment Method Frequency of Purchases
        0               1   55    Male         Blouse     Clothing                   53         Kentucky  ...    Credit Card         Express              Yes              Yes                 14                Venmo              Fortnightly  
        1               2   19    Male        Sweater     Clothing                   64            Maine  ...  Bank Transfer         Express              Yes              Yes                  2                 Cash              Fortnightly  
        2               3   50    Male          Jeans     Clothing                   73    Massachusetts  ...           Cash   Free Shipping              Yes              Yes                 23          Credit Card                   Weekly  
        3               4   21    Male        Sandals     Footwear                   90     Rhode Island  ...         PayPal    Next Day Air              Yes              Yes                 49               PayPal                   Weekly  
        4               5   45    Male         Blouse     Clothing                   49           Oregon  ...           Cash   Free Shipping              Yes              Yes                 31               PayPal                 Annually  
        ...           ...  ...     ...            ...          ...                  ...              ...  ...            ...             ...              ...              ...                ...                  ...                      ...  
        3895         3896   40  Female         Hoodie     Clothing                   28         Virginia  ...           Cash  2-Day Shipping               No               No                 32                Venmo                   Weekly  
        3896         3897   52  Female       Backpack  Accessories                   49             Iowa  ...         PayPal    Store Pickup               No               No                 41        Bank Transfer                Bi-Weekly  
        3897         3898   46  Female           Belt  Accessories                   33       New Jersey  ...    Credit Card        Standard               No               No                 24                Venmo                Quarterly  
        3898         3899   44  Female          Shoes     Footwear                   77        Minnesota  ...         PayPal         Express               No               No                 24                Venmo                   Weekly  
        3899         3900   52  Female        Handbag  Accessories                   81       California  ...  Bank Transfer    Store Pickup               No               No                 33                Venmo                Quarterly

- shopping_trends_updated.csv

    pandas.DataFrame(shape=(3900, 18), columns=["Customer ID", "Age", "Gender", "Item Purchased", "Category", "Purchase Amount (USD)", "Location", "Size", "Color", "Season", "Review Rating", "Subscription Status", "Shipping Type", "Discount Applied", "Promo Code Used", "Previous Purchases", "Payment Method", "Frequency of Purchases"])
              Customer ID  Age  Gender Item Purchased     Category  Purchase Amount (USD)       Location  ... Subscription Status   Shipping Type Discount Applied  Promo Code Used Previous Purchases Payment Method Frequency of Purchases
        0               1   55    Male         Blouse     Clothing                   53         Kentucky  ...                 Yes         Express              Yes              Yes                 14          Venmo          Fortnightly  
        1               2   19    Male        Sweater     Clothing                   64            Maine  ...                 Yes         Express              Yes              Yes                  2           Cash          Fortnightly  
        2               3   50    Male          Jeans     Clothing                   73    Massachusetts  ...                 Yes   Free Shipping              Yes              Yes                 23    Credit Card               Weekly  
        3               4   21    Male        Sandals     Footwear                   90     Rhode Island  ...                 Yes    Next Day Air              Yes              Yes                 49         PayPal               Weekly  
        4               5   45    Male         Blouse     Clothing                   49           Oregon  ...                 Yes   Free Shipping              Yes              Yes                 31         PayPal             Annually  
        ...           ...  ...     ...            ...          ...                  ...              ...  ...                 ...             ...              ...              ...                ...            ...                  ...  
        3895         3896   40  Female         Hoodie     Clothing                   28         Virginia  ...                  No  2-Day Shipping               No               No                 32          Venmo               Weekly  
        3896         3897   52  Female       Backpack  Accessories                   49             Iowa  ...                  No    Store Pickup               No               No                 41  Bank Transfer            Bi-Weekly  
        3897         3898   46  Female           Belt  Accessories                   33       New Jersey  ...                  No        Standard               No               No                 24          Venmo            Quarterly  
        3898         3899   44  Female          Shoes     Footwear                   77        Minnesota  ...                  No         Express               No               No                 24          Venmo               Weekly  
        3899         3900   52  Female        Handbag  Accessories                   81       California  ...                  No    Store Pickup               No               No                 33          Venmo            Quarterly

