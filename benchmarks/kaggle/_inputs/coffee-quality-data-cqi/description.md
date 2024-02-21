### Dataset name ###

Coffee Quality Data (CQI May-2023)

### Dataset description ###

# Coffee Quality Institute 
The Coffee Quality Institute (CQI) is a non-profit organization that works to improve the quality and value of coffee worldwide. It was founded in 1996 and has its headquarters in California, USA.

CQI's mission is to promote coffee quality through a range of activities that include research, training, and certification programs. The organization works with coffee growers, processors, roasters, and other stakeholders to improve coffee quality standards, promote sustainability, and support the development of the specialty coffee industry.

# Data
CQI maintains a web database that serves as a resource for coffee professionals and enthusiasts who are interested in learning about coffee quality and sustainability. The database includes a range of information on coffee production, processing, and sensory evaluation. It also contains data on coffee genetics, soil types, and other factors that can affect coffee quality.

## Sensory evaluations (coffee quality scores)
* *Aroma:* Refers to the scent or fragrance of the coffee.
* *Flavor:* The flavor of coffee is evaluated based on the taste, including any sweetness, bitterness, acidity, and other flavor notes.
* *Aftertaste:* Refers to the lingering taste that remains in the mouth after swallowing the coffee.
* *Acidity:* Acidity in coffee refers to the brightness or liveliness of the taste.
* *Body:* The body of coffee refers to the thickness or viscosity of the coffee in the mouth.
* *Balance:* Balance refers to how well the different flavor components of the coffee work together.
* *Uniformity:* Uniformity refers to the consistency of the coffee from cup to cup.
* *Clean Cup:* A clean cup refers to a coffee that is free of any off-flavors or defects, such as sourness, mustiness, or staleness.
* *Sweetness:* It can be described as caramel-like, fruity, or floral, and is a desirable quality in coffee.

**PLEASE NOTE: 'Total Cup Points' is literally the total of 10 features given above. There were some notebooks trying to predict the total cup points given these features. We know the exact function underlying the total cup points.**

## Defects
Defects are undesirable qualities that can occur in coffee beans during processing or storage. Defects can be categorized into two categories: Category One and Category Two defects.

Category One defects are primary defects that can be perceived through visual inspection of the coffee beans. These defects include Black beans, sour beans, insect-damaged beans, fungus-damaged beans, etc.

Category Two defects are secondary defects that are more subtle and can only be detected through tasting. These defects include Over-fermentation, staleness, rancidness, chemical taste, etc.

## Data Scraping
On this part, great thanks to [James LeDoux](https://github.com/jldbc). His repo [coffee-quality-database](https://github.com/jldbc/coffee-quality-database) from 2018 is efficiently written and well documented. To scrape the data, I used most of his code, but due to some changes on the website, I modified some of the lines. Also, some practices on modules were deprecated and deleted so I updated those codes also. Therefore, in May-2023 we can use this updated Python program to scrape data from this database. You can find my repo at https://github.com/fatih-boyar/coffee-quality-data-CQI/tree/main 


Only data was collected for the arabica type. With a few modifications in [scraper_bot.py](https://github.com/fatih-boyar/coffee-quality-data-CQI/blob/main/scraper_bot.py), scraping can be easily replicated for robusta types also.

### Dataset files ###

- df_arabica_clean.csv

    pandas.DataFrame(shape=(207, 41), columns=["Unnamed: 0", "ID", "Country of Origin", "Farm Name", "Lot Number", "Mill", "ICO Number", "Company", "Altitude", "Region", "Producer", "Number of Bags", "Bag Weight", "In-Country Partner", "Harvest Year", "Grading Date", "Owner", "Variety", "Status", "Processing Method", "Aroma", "Flavor", "Aftertaste", "Acidity", "Body", "Balance", "Uniformity", "Clean Cup", "Sweetness", "Overall", "Defects", "Total Cup Points", "Moisture Percentage", "Category One Defects", "Quakers", "Color", "Category Two Defects", "Expiration", "Certification Body", "Certification Address", "Certification Contact"])
             Unnamed: 0   ID Country of Origin            Farm Name           Lot Number                 Mill        ICO Number  ... Quakers         Color Category Two Defects           Expiration   Certification Body Certification Address Certification Contact
        0             0    0          Colombia     Finca El Paraiso           CQU2022015     Finca El Paraiso               NaN  ...       0         green                    3  September 21st, ...  Japan Coffee Exc...  〒413-0002 静岡県熱海市...   松澤　宏樹　Koju Matsu... 
        1             1    1            Taiwan  Royal Bean Geish...  The 2022 Pacific...  Royal Bean Geish...               NaN  ...       0    blue-green                    0  November 15th, 2023  Taiwan Coffee La...  QAHWAH CO., LTD ...   Lin, Jen-An Neil... 
        2             2    2              Laos   OKLAO coffee farms  The 2022 Pacific...  oklao coffee pro...               NaN  ...       0     yellowish                    2  November 15th, 2023  Taiwan Coffee La...  QAHWAH CO., LTD ...   Lin, Jen-An Neil... 
        3             3    3        Costa Rica            La Cumbre           CQU2022017  La Montana Tarra...               NaN  ...       0         green                    0  September 21st, ...  Japan Coffee Exc...  〒413-0002 静岡県熱海市...   松澤　宏樹　Koju Matsu... 
        4             4    4          Colombia      Finca Santuario           CQU2023002      Finca Santuario               NaN  ...       2  yellow-green                    2      March 5th, 2024  Japan Coffee Exc...  〒413-0002 静岡県熱海市...   松澤　宏樹　Koju Matsu... 
        ..          ...  ...               ...                  ...                  ...                  ...               ...  ...     ...           ...                  ...                  ...                  ...                  ...                   ... 
        202         202  202            Brazil    Fazenda Conquista               019/22             Dry Mill               NaN  ...       0         green                    4   February 2nd, 2024  Brazil Specialty...  Rua Gaspar Batis...   Chris Allen - 55... 
        203         203  203         Nicaragua     Finca San Felipe         017-053-0155  Beneficio Atlant...      017-053-0155  ...       2         green                   12      March 2nd, 2024  Asociación de Ca...  Del Hotel Semino...   Maria Ines Benav... 
        204         204  204              Laos                    -     105/3/VL7285-005             DRY MILL  105/3/VL7285-005  ...       9         green                   11  November 11th, 2023  Japan Coffee Exc...  〒413-0002 静岡県熱海市...   松澤　宏樹　Koju Matsu... 
        205         205  205       El Salvador  Rosario de Maria...              0423A01  Optimum Coffee, ...               NaN  ...      12  bluish-green                   13      March 7th, 2024  Salvadoran Coffe...  Final 1a. Av. No...   Tomas Bonilla - ... 
        206         206  206            Brazil        Walter Matter          1058 y 1059  Beneficio humedo...     002/1208/1016  ...       0         green                    1  November 18th, 2023  Centro Agroecoló...  Instituto de Eco...   Stephany Escamil...

