# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/McDonald_s_Reviews.csv` into a variable `reviews`.

validator:
  namespace_check:
    reviews:
"""

reviews = pd.read_csv('inputs/McDonald_s_Reviews.csv', encoding='latin-1')

# %%
"""
question: |
  List out the top 10 most frequent words in the reviews with 2 stars.
  Assume the reviews are written in English.
  The result should be a list of lower-cased words.

validator:
  result:
    ignore_order: true

execution:
  max_time: 10
"""

from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Filter 2-star reviews
two_star_reviews = reviews[reviews['rating'] == '2 stars']

# Tokenize and remove stopwords
words = word_tokenize(' '.join(two_star_reviews['review'].str.lower()))
words = [word for word in words if word.isalpha() and word not in stopwords.words('english')]

# Count word frequencies
word_freq = Counter(words)

# Get top 10 words
list(dict(word_freq.most_common(10)).keys())

# %%
"""
question: |
  Count the number of unique values for latitude and longitude. Return a tuple.
"""

reviews['latitude '].nunique(), reviews['longitude'].nunique()

# %%
"""
question: |
  Show the `store_address` for rows with missing entries of latitudes and longitudes.

validator:
  result:
    value_only: true
"""

reviews.loc[reviews['latitude '].isna() | reviews['longitude'].isna(), 'store_address']

# %%
"""
question: |
  Show the average rating for every unique latitude and longitude. The result should be a DataFrame with "Latitude", "Longitude", and "Average Rating" as the columns.

validator:
  result:
    ignore_order: true
"""

# Convert ratings to numerical values
reviews['rating_numerical'] = reviews['rating'].str.extract('(\d+)').astype(int)

# Calculate average rating for each location
reviews.groupby(['latitude ', 'longitude'])['rating_numerical'].mean().reset_index().rename(columns={'latitude ': 'Latitude', 'longitude': 'Longitude', 'rating_numerical': 'Average Rating'})

# %%
"""
question: |
  Use the Sentiment Intensity Analyzer in NLTK's Vader module to calculate sentiment scores for each review. Add a new column "sentiment_score" to the DataFrame to store the compound sentiment scores.

validator:
  namespace_check:
    reviews:

execution:
  max_time: 15
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()

# Calculate sentiment scores
reviews['sentiment_score'] = reviews['review'].apply(lambda review: sia.polarity_scores(review)['compound'])

# %%
"""
question: |
  Compute the average sentiment for each rating. Sort the result by rating in ascending order. The result should be a DataFrame with "Rating" and "Average Sentiment" as the columns.

validator:
  result:
    ignore_order: false
"""

average_sentiments = reviews.groupby('rating')['sentiment_score'].mean().reset_index().rename(columns={'rating': 'Rating', 'sentiment_score': 'Average Sentiment'}).sort_values('Rating')

average_sentiments

# %%
"""
question: |
  Classify the reviews into Positive, Negative and Neutral based on the sentiment scores. The rules are as follows:
  - If the sentiment score is greater than 0.05, the sentiment is Positive.
  - If the sentiment score is less than -0.05, the sentiment is Negative.
  - Otherwise, the sentiment is Neutral.
  Add the sentiment labels to the DataFrame in a new categorical column named "sentiment".

validator:
  namespace_check:
    reviews:
"""

reviews['sentiment'] = pd.cut(reviews['sentiment_score'], bins=[-np.inf, -0.05 - 1e-12, 0.05, np.inf], labels=['Negative', 'Neutral', 'Positive'])

# %%
"""
question: |
  Use the review to predict the sentiment. Split the dataset into training and testing sets with a test size of 0.2.
  Use random state 42 for reproducibility. Save the training set as `X_train`, `y_train`, and the testing set as `X_test`, `y_test`.

validator:
  namespace_check:
    X_train:
    y_train:
    X_test:
    y_test:
"""

from sklearn.model_selection import train_test_split

X = reviews['review']
y = reviews['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
"""
question: |
  Use TF-IDF vectorizer to convert the textual data into a numerical representation suitable for machine learning algorithms. Save the vectorizer as `vectorizer` and the transformed data as `X_train_transformed` and `X_test_transformed`.

validator:
  namespace_check:
    vectorizer:
      type_only: true
    X_train_transformed:
    X_test_transformed:

execution:
  max_time: 2
"""

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X_train_transformed = vectorizer.fit_transform(X_train)
X_test_transformed = vectorizer.transform(X_test)

# %%
"""
question: |
  Use Linear Support Vector Machine to predict sentiment intensity. Save the classifier as `model`.
  Fit the model on the training set.

validator:
  template: intact
  namespace_check:
    model:
      type_only: true
  model:
    model_name: model
    inputs_name: X_test_transformed
    labels_name: y_test
    metric_type: accuracy
    tolerance: 0.99

execution:
  forbid_names:
    - X_test
    - X_test_transformed
    - y_test
    - X
    - y
"""

# from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

model = LinearSVC()
model.fit(X_train_transformed, y_train)

# %%
"""
question: |
  Show the classification report of the classifier in a dict.
"""

from sklearn.metrics import classification_report

y_pred = model.predict(X_test_transformed)

classification_report(y_test, y_pred, output_dict=True)

# %%
"""
question: |
  Write a sentiment prediction function called `predict_sentiment`. The function should take a review as input and return the predicted sentiment ("Positive", "Negative", or "Neutral") as output.

validator:
  table_test:
    function_name: predict_sentiment

    test_cases:
    - ["This restaurant has excellent service and delicious food."]
    - ["This restaurant sucks."]
    - ["This is fine"]
    - ["This is dull"]
    - ["its bad"]
"""

def predict_sentiment(review):
    review_transformed = vectorizer.transform([review])
    return model.predict(review_transformed)[0]
