### Dataset name ###

Bank Customer Churn

### Dataset description ###

RowNumber—corresponds to the record (row) number and has no effect on the output.
CustomerId—contains random values and has no effect on customer leaving the bank.
Surname—the surname of a customer has no impact on their decision to leave the bank.
CreditScore—can have an effect on customer churn, since a customer with a higher credit score is less likely to leave the bank.
Geography—a customer’s location can affect their decision to leave the bank.
Gender—it’s interesting to explore whether gender plays a role in a customer leaving the bank.
Age—this is certainly relevant, since older customers are less likely to leave their bank than younger ones.
Tenure—refers to the number of years that the customer has been a client of the bank. Normally, older clients are more loyal and less likely to leave a bank.
Balance—also a very good indicator of customer churn, as people with a higher balance in their accounts are less likely to leave the bank compared to those with lower balances.
NumOfProducts—refers to the number of products that a customer has purchased through the bank.
HasCrCard—denotes whether or not a customer has a credit card. This column is also relevant, since people with a credit card are less likely to leave the bank.
IsActiveMember—active customers are less likely to leave the bank.
EstimatedSalary—as with balance, people with lower salaries are more likely to leave the bank compared to those with higher salaries.
Exited—whether or not the customer left the bank.
Complain—customer has complaint or not.
Satisfaction Score—Score provided by the customer for their complaint resolution.
Card Type—type of card hold by the customer.
Points Earned—the points earned by the customer for using credit card.

Acknowledgements

As we know, it is much more expensive to sign in a new client than keeping an existing one.

It is advantageous for banks to know what leads a client towards the decision to leave the company.

Churn prevention allows companies to develop loyalty programs and retention campaigns to keep as many customers as possible.

### Dataset files ###

- Customer-Churn-Records.csv

    pandas.DataFrame(shape=(10000, 18), columns=["RowNumber", "CustomerId", "Surname", "CreditScore", "Geography", "Gender", "Age", "Tenure", "Balance", "NumOfProducts", "HasCrCard", "IsActiveMember", "EstimatedSalary", "Exited", "Complain", "Satisfaction Score", "Card Type", "Point Earned"])
              RowNumber  CustomerId    Surname  CreditScore Geography  Gender  Age  ...  IsActiveMember  EstimatedSalary  Exited  Complain  Satisfaction Score  Card Type  Point Earned
        0             1    15634602   Hargrave          619    France  Female   42  ...               1        101348.88       1         1                   2    DIAMOND           464
        1             2    15647311       Hill          608     Spain  Female   41  ...               1        112542.58       0         1                   3    DIAMOND           456
        2             3    15619304       Onio          502    France  Female   42  ...               0        113931.57       1         1                   3    DIAMOND           377
        3             4    15701354       Boni          699    France  Female   39  ...               0         93826.63       0         0                   5       GOLD           350
        4             5    15737888   Mitchell          850     Spain  Female   43  ...               1         79084.10       0         0                   5       GOLD           425
        ...         ...         ...        ...          ...       ...     ...  ...  ...             ...              ...     ...       ...                 ...        ...           ...
        9995       9996    15606229   Obijiaku          771    France    Male   39  ...               0         96270.64       0         0                   1    DIAMOND           300
        9996       9997    15569892  Johnstone          516    France    Male   35  ...               1        101699.77       0         0                   5   PLATINUM           771
        9997       9998    15584532        Liu          709    France  Female   36  ...               1         42085.58       1         1                   3     SILVER           564
        9998       9999    15682355  Sabbatini          772   Germany    Male   42  ...               0         92888.52       1         1                   2       GOLD           339
        9999      10000    15628319     Walker          792    France  Female   28  ...               0         38190.78       0         0                   3    DIAMOND           911

