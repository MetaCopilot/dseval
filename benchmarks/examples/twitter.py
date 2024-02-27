# %%

"""
question: |
  Load the data from `inputs/twc-sample.csv`. Save it as `twc`.

validator:
  namespace_check:
    twc:
"""

import pandas as pd
twc = pd.read_csv("inputs/twc-sample.csv")

# %%

"""
question: |
  Connvert text column to lowercase and remove all punctuation. Save the result in a new column `text_wo_punct`.

validator:
  namespace_check:
    twc:
"""

import string

def remove_punctuation(text: str):
    return text.lower().translate(str.maketrans("", "", string.punctuation))

twc["text_wo_punct"] = twc["text"].apply(remove_punctuation)

# %%

from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))

# %%

"""
question: |
  Remove stopwords from the `text_wo_punct` column. Save the result in a new column `text_wo_stopwords`.

validator:
  namespace_check:
    twc:
"""

twc["text_wo_stopwords"] = twc["text_wo_punct"].apply(
    lambda text: " ".join([word for word in str(text).split() if word not in STOPWORDS])
)
