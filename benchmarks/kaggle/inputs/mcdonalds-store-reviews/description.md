### Dataset name ###

McDonald's Store Reviews

### Dataset description ###

# Description: 

&gt;This dataset contains over 33,000 anonymized reviews of McDonald's stores in the United States, scraped from Google reviews. It provides valuable insights into customer experiences and opinions about various McDonald's locations across the country. The dataset includes information such as store names, categories, addresses, geographic coordinates, review ratings, review texts, and timestamps.

# Key Features:

&gt;- **reviewer_id**: *Unique identifier for each reviewer (anonymized)*
- **store_name**: *Name of the McDonald's store*
- **category**: *Category or type of the store*
- **store_address**: *Address of the store*
- **latitude**: *Latitude coordinate of the store's location*
- **longitude**: *Longitude coordinate of the store's location*
- **rating_count**: *Number of ratings/reviews for the store*
- **review_time**: *Timestamp of the review*
- **review**: *Textual content of the review*
- **rating**: *Rating provided by the reviewer*


# Potential Use Cases:


&gt;- **Sentiment analysis:** Analyze the sentiment of reviews to understand overall customer satisfaction and identify areas for improvement.
- **Location-based analysis:** Explore geographical patterns in reviews and ratings to identify high-performing or underperforming regions.
- **Category analysis:** Investigate how different categories of McDonald's stores (e.g., drive-thru, McCafé) are perceived by customers.
- **Time-based analysis:** Examine temporal trends in reviews to identify any shifts in customer opinions or preferences over time.


Data Source: *The dataset was obtained by scraping Google reviews of McDonald's stores in the United States. The data does not contain any personally identifiable information (PII) to ensure privacy and comply with ethical guidelines.*<br>
If this was helpful, a vote is appreciated ❤️

### Dataset files ###

- McDonald_s_Reviews.csv

    pandas.DataFrame(shape=(33396, 10), columns=["reviewer_id", "store_name", "category", "store_address", "latitude ", "longitude", "rating_count", "review_time", "review", "rating"])
               reviewer_id  store_name             category        store_address  latitude   longitude rating_count   review_time               review   rating
        0                1  McDonald's  Fast food restau...  13749 US-183 Hwy...  30.460718 -97.792874        1,240  3 months ago  Why does it look...   1 star
        1                2  McDonald's  Fast food restau...  13749 US-183 Hwy...  30.460718 -97.792874        1,240    5 days ago  It'd McDonalds. ...  4 stars
        2                3  McDonald's  Fast food restau...  13749 US-183 Hwy...  30.460718 -97.792874        1,240    5 days ago  Made a mobile or...   1 star
        3                4  McDonald's  Fast food restau...  13749 US-183 Hwy...  30.460718 -97.792874        1,240   a month ago  My mc. Crispy ch...  5 stars
        4                5  McDonald's  Fast food restau...  13749 US-183 Hwy...  30.460718 -97.792874        1,240  2 months ago  I repeat my orde...   1 star
        ...            ...         ...                  ...                  ...        ...        ...          ...           ...                  ...      ...
        33391        33392  McDonald's  Fast food restau...  3501 Biscayne Bl...  25.810000 -80.189098        2,810   4 years ago  They treated me ...   1 star
        33392        33393  McDonald's  Fast food restau...  3501 Biscayne Bl...  25.810000 -80.189098        2,810    a year ago  The service is v...  5 stars
        33393        33394  McDonald's  Fast food restau...  3501 Biscayne Bl...  25.810000 -80.189098        2,810    a year ago  To remove hunger...  4 stars
        33394        33395  McDonald's  Fast food restau...  3501 Biscayne Bl...  25.810000 -80.189098        2,810   5 years ago  It's good, but l...  5 stars
        33395        33396  McDonald's  Fast food restau...  3501 Biscayne Bl...  25.810000 -80.189098        2,810   2 years ago  they took good c...  5 stars

