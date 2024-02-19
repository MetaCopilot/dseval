### Dataset name ###

Health &amp; Development Indicators: Global Insights

### Dataset description ###

Labels: "Status" (Development Status: Developing or Developed)

Features:
1. Country: The name of the country.
2. Year: The year of data recording.
3. Life Expectancy: The average number of years a newborn, person at different age ranges, or the entire population is expected to live
4. Adult Mortality: Probability of dying between 15 and 60 years per 1000 population.
5. Infant Deaths: Number of infant deaths per 1000 live births.
6. Alcohol: Alcohol consumption per capita (in liters of pure alcohol).
7. Percentage Expenditure: Expenditure on health as a percentage of total government spending or GDP.
8. Hepatitis B: Hepatitis B immunization coverage among 1-year-olds (percentage).
9. Measles: Measles immunization coverage among 1-year-olds (percentage).

### Dataset files ###

- Life_Expectancy_Data.csv

    pandas.DataFrame(shape=(1649, 22), columns=["Country", "Year", "Status", "Life expectancy ", "Adult Mortality", "infant deaths", "Alcohol", "percentage expenditure", "Hepatitis B", "Measles ", " BMI ", "under-five deaths ", "Polio", "Total expenditure", "Diphtheria ", " HIV/AIDS", "GDP", "Population", " thinness  1-19 years", " thinness 5-9 years", "Income composition of resources", "Schooling"])
                  Country  Year      Status  Life expectancy   Adult Mortality  infant deaths  Alcohol  ...   HIV/AIDS         GDP  Population   thinness  1-19 years   thinness 5-9 years  Income composition of resources  Schooling
        0     Afghanistan  2015  Developing              65.0              263             62     0.01  ...        0.1  584.259210  33736494.0                 17.2                   17.3                0.479                   10.1
        1     Afghanistan  2014  Developing              59.9              271             64     0.01  ...        0.1  612.696514    327582.0                 17.5                   17.5                0.476                   10.0
        2     Afghanistan  2013  Developing              59.9              268             66     0.01  ...        0.1  631.744976  31731688.0                 17.7                   17.7                0.470                    9.9
        3     Afghanistan  2012  Developing              59.5              272             69     0.01  ...        0.1  669.959000   3696958.0                 17.9                   18.0                0.463                    9.8
        4     Afghanistan  2011  Developing              59.2              275             71     0.01  ...        0.1   63.537231   2978599.0                 18.2                   18.2                0.454                    9.5
        ...           ...   ...         ...               ...              ...            ...      ...  ...        ...         ...         ...                  ...                    ...                  ...                    ...
        1644     Zimbabwe  2004  Developing              44.3              723             27     4.36  ...       33.6  454.366654  12777511.0                  9.4                    9.4                0.407                    9.2
        1645     Zimbabwe  2003  Developing              44.5              715             26     4.06  ...       36.7  453.351155  12633897.0                  9.8                    9.9                0.418                    9.5
        1646     Zimbabwe  2002  Developing              44.8               73             25     4.43  ...       39.8   57.348340    125525.0                  1.2                    1.3                0.427                   10.0
        1647     Zimbabwe  2001  Developing              45.3              686             25     1.72  ...       42.1  548.587312  12366165.0                  1.6                    1.7                0.427                    9.8
        1648     Zimbabwe  2000  Developing              46.0              665             24     1.68  ...       43.5  547.358878  12222251.0                 11.0                   11.2                0.434                    9.8

