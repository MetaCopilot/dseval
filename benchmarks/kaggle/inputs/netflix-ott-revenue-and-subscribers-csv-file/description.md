### Dataset name ###

Netflix OTT Revenue and Subscribers (CSV File)

### Dataset description ###

Netflix OTT Revenue and Number of Paid Subscribers dataset contains the revenue of Netflix  in dollars and number of paid subscribers region wise. 

**Note** : Netflix's financial year is from Jan 1st to 31st Dec.

**Data Dictionary (column description)**

Date : Month-Year of Quarter .

Global Revenue: Revenue collected Worldwide (Streaming Revenue + United States Domestic DVD Revenue).
UCAN : United States and Canada
EMEA : Europe, Middle East and Africa
APAC : Asia-Pacific
LATM : Latin America

ARPU is average revenue per member and it is calculated as streaming revenue divided by number of month in period, i.e. , for quarter is 3 months (here).
All revenue is in US Dollars.  

For older versions :
From 2019 till today, Netflix released data region wise, before that It released as Domestic market
(UACN) and International Market.
Before 2019, global users are higher in number because it in lost his subscribers drastically. [Read Here](https://www.cnbc.com/2019/07/18/why-netflix-says-it-had-a-rare-subscriber-loss-in-q2-2019.html)
[Read Here](https://www.forbes.com/sites/stephenmcbride1/2019/11/11/in-24-hours-netflix-could-lose-25-of-its-subscribers/?sh=20e217341b39)

**Note #1.  In 2019, difference in global and all region sum revenue is 297217000 USD . In 2020 is 239381000 USD. In 2021 is 182348000 USD. In 2022 is 145698000 USD. In Q1, 2023 is 31502000 USD. Excludes DVD revenues of $182 million, $146 million and $32 million for the years ended December 31, 2021, 2022, and the three months ended March 31, 2023, respectively. Q1, 2023 Financial Statement Excludes DVD revenues of $0.2 billion, $0.2 billion and $0.1 billion for the years ended December 31, 2020, 2021 and 2022, respectively. Total US revenues for the years ended December 31, 2020, 2021 and 2022 were $10.8 billion, $12.1 billion and $13.0 billion, respectively. Q4, 2022 Financial Statement**

### Dataset files ###

- netflix_revenue_updated.csv

    pandas.DataFrame(shape=(17, 15), columns=["Date", "Global Revenue", "UCAN Streaming Revenue", "EMEA Streaming Revenue", "LATM Streaming Revenue", "APAC Streaming Revenue", "UCAN Members", "EMEA  Members", "LATM Members", "APAC Members", "UCAN ARPU", "EMEA ARPU", "LATM  ARPU", "APAC  ARPU", "Netflix Streaming Memberships "])
                  Date  Global Revenue  UCAN Streaming Revenue  EMEA Streaming Revenue  LATM Streaming Revenue  APAC Streaming Revenue  UCAN Members  EMEA  Members  LATM Members  APAC Members  UCAN ARPU  EMEA ARPU  LATM  ARPU  APAC  ARPU  Netflix Streaming Memberships 
        0   31-03-2019      4520992000           2256851000              1233379000               630472000               319602000         66633000       42542000      27547000      12141000      11.45      10.23        7.84        9.37            148863000           
        1   30-06-2019      4923116000           2501199000              1319087000               677136000               349494000         66501000       44229000      27890000      12942000      12.52      10.13        8.14        9.29            151562000           
        2   30-09-2019      5244905000           2621250000              1428040000               741434000               382304000         67114000       47355000      29380000      14485000      13.08      10.40        8.63        9.29            158334000           
        3   31-12-2019      5467434000           2671908000              1562561000               746392000               418121000         67662000       51778000      31417000      16233000      13.22      10.51        8.18        9.07            167090000           
        4   31-03-2020      5767691000           2702776000              1723474000               793453000               483660000         69969000       58734000      34318000      19835000      13.09      10.40        8.05        8.94            182856000           
        ..         ...             ...                  ...                     ...                     ...                     ...              ...            ...           ...           ...        ...        ...         ...         ...                  ...           
        12  31-03-2022      7867767000           3350424000              2561831000               998948000               916754000         74579000       73733000      39610000      33719000      14.91      11.56        8.37        9.21            221641000           
        13  30-06-2022      7970141000           3537863000              2457235000              1030234000               907719000         73283000       72966000      39624000      34799000      15.95      11.17        8.67        8.83            220672000           
        14  30-09-2022      7925589000           3601565000              2375814000              1023945000               889037000         73387000       73534000      39936000      36228000      16.37      10.81        8.58        8.34            223085000           
        15  31-12-2022      7852053000           3594791000              2350135000              1016846000               856711000         74296000       76729000      41699000      38023000      16.23      10.43        8.30        7.69            230747000           
        16  31-03-2023      8161503000           3608645000              2517641000              1070192000               933523000         74398000       77373000      41249000      39478000      16.18      10.89        8.60        8.03            232498000

