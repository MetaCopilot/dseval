### Dataset name ###

Happiness Index 2018-2019

### Dataset description ###

**About data:** This study analyzes the association between the Happiness Index Score in 2018 and 2019, and a set of independent variables such as 'Overall rank', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity' and 'Perceptions of corruption'. The objective of this study is to investigate the impact of these independent variables on the level of happiness of individuals during these two years. In addition, a country-wise analysis was conducted to examine variations in variables between the top-ranking happiest country and India. Multiple visualizations were employed to identify and illustrate these differences in a clear and concise manner.

**Dependent &amp; Independent variables:** The first independent variable is GDP per capita, which represents the economic well-being of a country's residents. The second variable, freedom to make life choices, represents the level of autonomy and control individuals have over their lives. The third variable, health life expectancy, indicates the length of time individuals can expect to live in good health. The fourth variable, perception of corruption, reflects the extent to which corruption is perceived to be prevalent in a society. Finally, the fifth variable, social support, measures the extent to which individuals have access to support from family, friends, and other social networks.

By examining the relationship between these independent variables and the Happiness Index Score, the study aims to contribute to the understanding of the factors that impact individuals' happiness levels. The results of this study could be useful for policymakers and other stakeholders in identifying areas for intervention and improvement to enhance the overall well-being of the population.

**Overview of the Data (2018 &amp; 2019)**
- Overall rank: List of ranks of different countries from 1 to 156
- Country or region: List of the names of different countries.
- Score: List of happiness scores of different countries.
- GDP per capita: The GDP per capita score of different countries.
- Social support: The social support of different countries.
- Healthy life expectancy: The healthy life expectancy of different countries.
- Freedom to make life choices: The score of perception of freedom of different countries.
- Generosity: Generosity (the quality of being kind and generous) score of different countries.
- Perceptions of corruption: The score of the perception of corruption in different countries.

**Abstract**

This study aims to investigate the relationship between the Happiness Index Score and several independent variables, namely GDP per capita, social support, healthy life expectancy, freedom to make life choices, and perceptions of corruption, in the years 2018 and 2019. By analyzing these variables, we sought to identify the factors that significantly influence individuals' happiness levels and contribute to a better understanding of the factors that impact overall well-being. The study used regression analysis to examine the statistical significance of these variables and their impact on the dependent variable, the Happiness Index Score. The results indicate that all independent variables significantly influence the Happiness Index Score and can explain up to 98.6% and 98.1% of the variance in the dependent variable in 2018 and 2019, respectively. Moreover, the analysis suggests that social support and GDP per capita are the main parameters that differentiate Finland from India in terms of happiness levels. The findings of this study could be useful for policymakers and stakeholders in identifying areas for intervention and improvement to enhance the overall well-being of the population.

**Keywords:** Happiness Index Score, GDP per capita, social support, healthy life expectancy, freedom to make life choices, perceptions of corruption, regression analysis, Finland, India.

**Introduction:**

The pursuit of happiness has been a central theme in human societies throughout history. The Happiness Index Score is a measure of well-being that has gained considerable attention in recent years as an indicator of a country's overall prosperity and quality of life. The Happiness Index Score is calculated based on several variables, including GDP per capita, social support, healthy life expectancy, freedom to make life choices, perceptions of corruption, and generosity.

The purpose of this study is to investigate the impact of these variables on the Happiness Index Score in 2018 and 2019 and to identify the factors that significantly influence individuals' happiness levels. The study aims to contribute to the understanding of the factors that impact overall well-being and to provide insights for policymakers and stakeholders in identifying areas for intervention and improvement.

**Methodology:**

The study used regression analysis to examine the relationship between the Happiness Index Score and independent variables, namely GDP per capita, social support, healthy life expectancy, freedom to make life choices, and perceptions of corruption. The data for this study was obtained from the World Happiness Report for the years 2018 and 2019. The analysis was conducted using Python programming and all the visualizations were created using the same.

**Results:**

The regression analysis revealed that all independent variables significantly influence the Happiness Index Score in both 2018 and 2019. The adjusted R squared values of 0.986 and 0.981 in 2018 and 2019, respectively, indicate a robust model capable of explaining a large proportion of the variance in the dependent variable. Moreover, the p-values associated with the F statistics were less than 0.05, indicating that the model is statistically significant and reliable.

Firstly, a regression analysis was conducted for dataset "Happiness Index 2018". Here, The regression model indicates that the independent variables, namely GDP per capita, social support, freedom to make life choices, generosity, and perceptions of corruption, significantly influence the dependent variable, which is the Happiness Index Score. This finding suggests that variations in the aforementioned independent variables can considerably affect positively the level of happiness in a given population. It is worth noting that all the independent variables have p-values less than 0.05, indicating that they are statistically significant in the model. Additionally, the adjusted R squared value of 0.986 is indicative of a robust model, which can explain 98.6% of the variance in the dependent variable. Moreover, the p-value associated with the F statistics is also less than 0.05, further strengthening the evidence that the model is significant and capable of producing reliable results. Overall, these findings suggest that the regression model is valid and can be used to make accurate predictions about the Happiness Index Score based on the selected independent variables.

Thereafter, another regression analysis was conducted for dataset "Happiness Index 2019" to investigate the influence of social support, freedom to make life choices, generosity, and perceptions of corruption on the happiness index score. The analysis revealed that all independent variables significantly influenced the dependent variable, indicating that the happiness index score varied greatly based on these factors. The statistical significance of these variables was confirmed by a p-value of less than 0.05. The robustness of the model was also demonstrated by an adjusted R squared value of 0.981. Moreover, the p-value associated with F statistics was less than 0.05, suggesting that the model was good. These findings suggest that policymakers and organizations could target these independent variables to enhance overall happiness levels.

Furthermore, the country-wise analysis showed that Finland had significantly higher levels of GDP per capita and social support compared to India, which were the two main factors contributing to the difference in happiness levels between the two countries.

**Conclusion:**
The study concludes that the independent variables, namely GDP per capita, social support, healthy life expectancy, freedom to make life choices, and perceptions of corruption, significantly influence the Happiness Index Score in both 2018 and 2019. The findings suggest that policymakers and stakeholders could target these variables to enhance overall well-being and happiness levels. The analysis also highlights the importance of GDP per capita and social support in determining the Happiness Index Score and differentiating countries' happiness levels, as demonstrated by the comparison of Finland and India.

The study contributes to the understanding of the factors that impact individuals' happiness levels and provides insights for policymakers and stakeholders in identifying areas for intervention and improvement.


**Code link:** https://www.kaggle.com/code/sougatapramanick/soug009

### Dataset files ###

- report_2018-2019.csv

    pandas.DataFrame(shape=(312, 10), columns=["Overall rank", "Country or region", "Year", "Score", "GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"])
             Overall rank Country or region  Year  Score  GDP per capita  Social support  Healthy life expectancy  Freedom to make life choices  Generosity  Perceptions of corruption
        0             154       Afghanistan  2019  3.203           0.350           0.517                0.361                    0.000                0.158                0.025      
        1             145       Afghanistan  2018  3.632           0.332           0.537                0.255                    0.085                0.191                0.036      
        2             107           Albania  2019  4.719           0.947           0.848                0.874                    0.383                0.178                0.027      
        3             112           Albania  2018  4.586           0.916           0.817                0.790                    0.419                0.149                0.032      
        4              88           Algeria  2019  5.211           1.002           1.160                0.785                    0.086                0.073                0.114      
        ..            ...               ...   ...    ...             ...             ...                  ...                      ...                  ...                  ...      
        307           152             Yemen  2018  3.355           0.442           1.073                0.343                    0.244                0.083                0.064      
        308           138            Zambia  2019  4.107           0.578           1.058                0.426                    0.431                0.247                0.087      
        309           125            Zambia  2018  4.377           0.562           1.047                0.295                    0.503                0.221                0.082      
        310           146          Zimbabwe  2019  3.663           0.366           1.114                0.433                    0.361                0.151                0.089      
        311           144          Zimbabwe  2018  3.692           0.357           1.094                0.248                    0.406                0.132                0.099

- 2018.csv

    pandas.DataFrame(shape=(156, 9), columns=["Overall rank", "Country or region", "Score", "GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"])
             Overall rank    Country or region  Score  GDP per capita  Social support  Healthy life expectancy  Freedom to make life choices  Generosity  Perceptions of corruption
        0               1              Finland  7.632           1.305           1.592                0.874                    0.681                0.202                0.393      
        1               2               Norway  7.594           1.456           1.582                0.861                    0.686                0.286                0.340      
        2               3              Denmark  7.555           1.351           1.590                0.868                    0.683                0.284                0.408      
        3               4              Iceland  7.495           1.343           1.644                0.914                    0.677                0.353                0.138      
        4               5          Switzerland  7.487           1.420           1.549                0.927                    0.660                0.256                0.357      
        ..            ...                  ...    ...             ...             ...                  ...                      ...                  ...                  ...      
        151           152                Yemen  3.355           0.442           1.073                0.343                    0.244                0.083                0.064      
        152           153             Tanzania  3.303           0.455           0.991                0.381                    0.481                0.270                0.097      
        153           154          South Sudan  3.254           0.337           0.608                0.177                    0.112                0.224                0.106      
        154           155  Central African ...  3.083           0.024           0.000                0.010                    0.305                0.218                0.038      
        155           156              Burundi  2.905           0.091           0.627                0.145                    0.065                0.149                0.076

- 2019.csv

    pandas.DataFrame(shape=(156, 9), columns=["Overall rank", "Country or region", "Score", "GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"])
             Overall rank    Country or region  Score  GDP per capita  Social support  Healthy life expectancy  Freedom to make life choices  Generosity  Perceptions of corruption
        0               1              Finland  7.769           1.340           1.587                0.986                    0.596                0.153                0.393      
        1               2              Denmark  7.600           1.383           1.573                0.996                    0.592                0.252                0.410      
        2               3               Norway  7.554           1.488           1.582                1.028                    0.603                0.271                0.341      
        3               4              Iceland  7.494           1.380           1.624                1.026                    0.591                0.354                0.118      
        4               5          Netherlands  7.488           1.396           1.522                0.999                    0.557                0.322                0.298      
        ..            ...                  ...    ...             ...             ...                  ...                      ...                  ...                  ...      
        151           152               Rwanda  3.334           0.359           0.711                0.614                    0.555                0.217                0.411      
        152           153             Tanzania  3.231           0.476           0.885                0.499                    0.417                0.276                0.147      
        153           154          Afghanistan  3.203           0.350           0.517                0.361                    0.000                0.158                0.025      
        154           155  Central African ...  3.083           0.026           0.000                0.105                    0.225                0.235                0.035      
        155           156          South Sudan  2.853           0.306           0.575                0.295                    0.010                0.202                0.091

