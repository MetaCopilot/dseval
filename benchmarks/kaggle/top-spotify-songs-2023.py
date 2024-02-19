# %%
import pandas as pd
import numpy as np

# %%
"""
question: |
  Read the file `inputs/spotify-2023.csv` into a variable `spotify`.

validator:
  namespace_check:
    spotify:
"""

spotify = pd.read_csv('inputs/spotify-2023.csv', encoding='latin-1')

# %%
"""
question: |
  Count the number of missing values for each column.
"""

spotify.isnull().sum()

# %%
"""
question: |
  Parse the 'streams' column as numeric. If there is any error during the parsing, set the value to NaN.

validator:
  namespace_check:
    spotify:
"""

spotify['streams'] = pd.to_numeric(spotify['streams'], errors='coerce')

# %%
"""
question: |
  Group the songs by artist(s) and sum up their streams.
"""

spotify.groupby('artist(s)_name')['streams'].sum()

# %%
"""
question: |
  Encode the 'track_name' column with numbers. Each unique track name should be assigned a unique number. Save the encoded column as 'track_id'.

validator:
  # We don't care about the exact values.
  namespace_check:
    spotify: |
      def compare_fn(ref, sub):
        if type(ref) != type(sub) or ref.columns.tolist() != sub.columns.tolist():
          return {"match": False, "reason": "The dataframe is not of the right type or does not have expected columns."}
        from collections import Counter
        if sorted(Counter(ref['track_id']).values()) != sorted(Counter(sub['track_id']).values()):
          return {"match": False, "reason": "The track_id column is not encoded correctly."}
        return {"match": True, "reason": ""}
"""

spotify['track_id'] = spotify['track_name'].astype('category').cat.codes

# %%
"""
question: |
  Use one-hot encoding to encode the 'key' and 'mode' columns. Convert the binary columns 'in_spotify_charts', 'in_apple_charts', 'in_deezer_charts', and 'in_shazam_charts' to int. Modify the dataset in-place.

validator:
  namespace_check:
    spotify:
"""

spotify = pd.get_dummies(spotify, columns=['key', 'mode'])
binary_columns = ['in_spotify_charts', 'in_apple_charts', 'in_deezer_charts', 'in_shazam_charts']
for column in binary_columns:
    spotify[column] = spotify[column].map({'Yes': 1, 'No': 0})

# %%
"""
question: |
  Rename the columns to remove the "_%" suffix. Save the renamed dataset in-place.

validator:
  namespace_check:
    spotify:
"""

spotify.columns = spotify.columns.str.replace(r'_%$', '', regex=True)

# %%
"""
question: |
  Conduct a T-test to examine the difference in 'streams' between different modes. Show the p-value.
"""

from scipy.stats import ttest_ind

group1 = spotify.loc[spotify['mode_Major'] == 1, 'streams'].dropna()
group2 = spotify.loc[spotify['mode_Minor'] == 1, 'streams'].dropna()

t_stat, p_val = ttest_ind(group1, group2)

p_val

# %%
"""
question: |
  Conduct an ANOVA test to examine the difference in 'streams' across different 'key' levels. Return the p-value.

validator:
  result:
    atol: 0
"""

from scipy.stats import f_oneway

groups = [spotify.loc[spotify[column] == 1, 'streams'].dropna() for column in spotify.columns if column.startswith('key_')]

f_stat, p_val = f_oneway(*groups)

p_val

# %%
"""
question: |
  Create a new feature 'is_top_artist' that indicates whether the artist(s) is(are) among the top 15 artists with the most number of popular songs. Save the new feature as boolean in-place.

validator:
  namespace_check:
    spotify:
"""

top_artists = spotify['artist(s)_name'].value_counts().nlargest(15).index
spotify['is_top_artist'] = spotify['artist(s)_name'].map(lambda x: x in top_artists)

# %%
"""
question: |
  Compute the number of pouplar songs releases for each year from 1900 to 2023. Return a DataFrame with "Year" as the index and "Count" as the values.
"""

pd.DataFrame({'Year': range(1900, 2024)}).merge(spotify['released_year'].value_counts().sort_index().rename_axis('Year').rename('Count').to_frame().reset_index(), how='left').fillna(0).astype(int).set_index('Year')

# %%
"""
question: |
  Calculate the total count of tracks present in playlists/charts for Spotify and Apple Music. The resulting DataFrame should have "Platform" (i.e., Spotify and Apple Music) as the index and "Count" as the values.
"""

pd.DataFrame({
    'Platform': ['Spotify', 'Apple Music'],
    'Count': [spotify['in_spotify_playlists'].sum(), spotify['in_apple_playlists'].sum()]
}).set_index('Platform')

# %%
"""
question: |
  List the top 10 song names for Spotify based on their presence in playlists.

validator:
  result:
    ignore_order: true
    value_only: true
"""

spotify[['track_name', 'in_spotify_playlists']].set_index('track_name').nlargest(10, 'in_spotify_playlists').index.tolist()

# %%
"""
question: |
  Identify collaborations by splitting the 'artist(s)_name' column, and filtering out songs (rows) that have only one artist to get collaborative tracks. Assuming the multiple artists are separated by comma(s).
"""

spotify[spotify['artist(s)_name'].str.contains(', ', regex=False)]

# %%
"""
question: |
  Find out the top 10 frequent collaborator pairs. Return a dict with the pairs as keys and the frequencies as values. For each pair, the artists should be sorted in lexicographical order.
"""

from collections import Counter
from itertools import combinations

# Split the artist(s) names
artists = spotify[spotify['artist(s)_name'].str.contains(', ')]['artist(s)_name'].str.split(', ', regex=False)

# Get all pairs of artists
pairs = artists.apply(lambda x: [tuple(sorted(t)) for t in combinations(x, 2)])

# Count the occurrences of each pair
pair_counts = Counter(pairs.explode())
dict(pair_counts.most_common())
