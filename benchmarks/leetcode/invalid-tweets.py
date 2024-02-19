'''
### Description ###

Table: `Tweets`

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
This table contains all the tweets in a social media app.
```

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is **strictly greater** than `15`.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Tweets table:
+----------+----------------------------------+
| tweet_id | content                          |
+----------+----------------------------------+
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
+----------+----------------------------------+
**Output:** 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
**Explanation:** 
Tweet 1 has length = 14. It is a valid tweet.
Tweet 2 has length = 32. It is an invalid tweet.
```

### Schema ###

data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
Tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})

### Code snippet ###

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame`.

  `tweets` is a DataFrame with the following columns:
  - tweet_id: int
  - content: str
  `tweets` contains all the tweets in a social media app.

  The function should find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is **strictly greater** than `15`.

  Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  tweets:
  +----------+----------------------------------+
  | tweet_id | content                          |
  +----------+----------------------------------+
  | 1        | Vote for Biden                   |
  | 2        | Let us make America great again! |
  +----------+----------------------------------+
  ```

  Example output:
  ```
  +----------+
  | tweet_id |
  +----------+
  | 2        |
  +----------+
  ```

  Example explanation:
  - Tweet 1 has length = 14. It is a valid tweet.
  - Tweet 2 has length = 32. It is an invalid tweet.

validator:
  table_test:
    function_name: invalid_tweets
    input_validator: |
      def _validate(tweets):
        assert tweets.shape[0] > 0
        assert tweets.dtypes.equals(pd.Series({'tweet_id': 'int64', 'content': 'object'}))
        assert tweets.tweet_id.is_unique
        assert tweets.content.str.len().between(1, 100).all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'tweet_id': [1, 2], 'content': ['Vote for Biden', 'Let us make America great again!']})`"
    - # corner case: only one tweet
      - "`pd.DataFrame({'tweet_id': [1], 'content': ['Vote for Biden']})`"
    - # corner case: all tweets are valid
      - "`pd.DataFrame({'tweet_id': [1, 2], 'content': ['Vote for Biden', 'Make America great']})`"
    - # corner case: all tweets are invalid
      - "`pd.DataFrame({'tweet_id': [1, 2], 'content': ['Vote for Biden in 2020', 'Let us make America great again!']})`"
    - | # random cases
      ```
      def _generate():
        tweets = pd.DataFrame({'tweet_id': np.arange(1, 1001), 'content': [''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'), np.random.randint(1, 101))) for _ in range(1000)]})
        return tweets,
      ```
    # 10 more random cases
    - //
    - //
    - //
    - //
    - //
    - //
    - //
    - //
    - //
    - //
"""

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter the tweets DataFrame to only include tweets with content length greater than 15
    invalid = tweets[tweets["content"].str.len() > 15]

    # Return the tweet_id column of the filtered DataFrame
    return invalid[["tweet_id"]]
