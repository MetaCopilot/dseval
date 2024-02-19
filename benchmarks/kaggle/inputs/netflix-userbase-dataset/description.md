### Dataset name ###

Netflix Userbase Dataset

### Dataset description ###

The dataset provides a snapshot of a sample Netflix userbase, showcasing various aspects of user subscriptions, revenue, account details, and activity. Each row represents a unique user, identified by their User ID. The dataset includes information such as the user's subscription type (Basic, Standard, or Premium), the monthly revenue generated from their subscription, the date they joined Netflix (Join Date), the date of their last payment (Last Payment Date), and the country in which they are located.

Additional columns have been included to provide insights into user behavior and preferences. These columns include Device Type (e.g., Smart TV, Mobile, Desktop, Tablet) and Account Status (whether the account is active or not). The dataset serves as a synthetic representation and does not reflect actual Netflix user data. It can be used for analysis and modeling to understand user trends, preferences, and revenue generation within a hypothetical Netflix userbase.

### Dataset files ###

- Netflix Userbase.csv

    pandas.DataFrame(shape=(2500, 10), columns=["User ID", "Subscription Type", "Monthly Revenue", "Join Date", "Last Payment Date", "Country", "Age", "Gender", "Device", "Plan Duration"])
              User ID Subscription Type  Monthly Revenue Join Date Last Payment Date         Country  Age  Gender      Device Plan Duration
        0           1             Basic               10  15-01-22          10-06-23   United States   28    Male  Smartphone       1 Month
        1           2           Premium               15  05-09-21          22-06-23          Canada   35  Female      Tablet       1 Month
        2           3          Standard               12  28-02-23          27-06-23  United Kingdom   42    Male    Smart TV       1 Month
        3           4          Standard               12  10-07-22          26-06-23       Australia   51  Female      Laptop       1 Month
        4           5             Basic               10  01-05-23          28-06-23         Germany   33    Male  Smartphone       1 Month
        ...       ...               ...              ...       ...               ...             ...  ...     ...         ...           ...
        2495     2496           Premium               14  25-07-22          12-07-23           Spain   28  Female    Smart TV       1 Month
        2496     2497             Basic               15  04-08-22          14-07-23           Spain   33  Female    Smart TV       1 Month
        2497     2498          Standard               12  09-08-22          15-07-23   United States   38    Male      Laptop       1 Month
        2498     2499          Standard               13  12-08-22          12-07-23          Canada   48  Female      Tablet       1 Month
        2499     2500             Basic               15  13-08-22          12-07-23   United States   35  Female    Smart TV       1 Month

