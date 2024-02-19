### Dataset name ###

Housing Price Prediction

### Dataset description ###

This dataset provides comprehensive information for house price prediction, with 13 column names:

1. **Price:** The price of the house.
2. **Area:** The total area of the house in square feet.
3. **Bedrooms:** The number of bedrooms in the house.
4. **Bathrooms:** The number of bathrooms in the house.
5. **Stories:** The number of stories in the house.
6. **Mainroad:** Whether the house is connected to the main road (Yes/No).
7. **Guestroom:** Whether the house has a guest room (Yes/No).
8. **Basement:** Whether the house has a basement (Yes/No).
9. **Hot water heating:** Whether the house has a hot water heating system (Yes/No).
10. **Airconditioning:** Whether the house has an air conditioning system (Yes/No).
11. **Parking:** The number of parking spaces available within the house.
12. **Prefarea:** Whether the house is located in a preferred area (Yes/No).
13. **Furnishing status:** The furnishing status of the house (Fully Furnished, Semi-Furnished, Unfurnished).

Kindly, upvote if you find the dataset interesting.

### Dataset files ###

- Housing.csv

    pandas.DataFrame(shape=(545, 13), columns=["price", "area", "bedrooms", "bathrooms", "stories", "mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "parking", "prefarea", "furnishingstatus"])
                price  area  bedrooms  bathrooms  stories mainroad guestroom basement hotwaterheating airconditioning  parking prefarea furnishingstatus
        0    13300000  7420         4          2        3      yes        no       no              no             yes        2      yes        furnished
        1    12250000  8960         4          4        4      yes        no       no              no             yes        3       no        furnished
        2    12250000  9960         3          2        2      yes        no      yes              no              no        2      yes   semi-furnished
        3    12215000  7500         4          2        2      yes        no      yes              no             yes        3      yes        furnished
        4    11410000  7420         4          1        2      yes       yes      yes              no             yes        2       no        furnished
        ..        ...   ...       ...        ...      ...      ...       ...      ...             ...             ...      ...      ...              ...
        540   1820000  3000         2          1        1      yes        no      yes              no              no        2       no      unfurnished
        541   1767150  2400         3          1        1       no        no       no              no              no        0       no   semi-furnished
        542   1750000  3620         2          1        1      yes        no       no              no              no        0       no      unfurnished
        543   1750000  2910         3          1        1       no        no       no              no              no        0       no        furnished
        544   1750000  3850         3          1        2      yes        no       no              no              no        0       no      unfurnished

