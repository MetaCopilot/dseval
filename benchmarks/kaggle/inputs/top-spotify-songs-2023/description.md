### Dataset name ###

Most Streamed Spotify Songs 2023

### Dataset description ###

# Description :

&gt; This dataset contains a comprehensive list of the most famous songs of 2023 as listed on Spotify. The dataset offers a wealth of features beyond what is typically available in similar datasets. It provides insights into each song's attributes, popularity, and presence on various music platforms. The dataset includes information such as **track name, artist(s) name, release date, Spotify playlists and charts, streaming statistics, Apple Music presence, Deezer presence, Shazam charts, and various audio features**.


# Key Features:


&gt;- **track_name**: *Name of the song*
- **artist(s)_name**: *Name of the artist(s) of the song*
- **artist_count**: *Number of artists contributing to the song*
- **released_year**: *Year when the song was released*
- **released_month**: *Month when the song was released*
- **released_day**: *Day of the month when the song was released*
- **in_spotify_playlists**: *Number of Spotify playlists the song is included in*
- **in_spotify_charts**: *Presence and rank of the song on Spotify charts*
- **streams**: *Total number of streams on Spotify*
- **in_apple_playlists**: *Number of Apple Music playlists the song is included in*
- **in_apple_charts**: *Presence and rank of the song on Apple Music charts*
- **in_deezer_playlists**: *Number of Deezer playlists the song is included in*
- **in_deezer_charts**: *Presence and rank of the song on Deezer charts*
- **in_shazam_charts**: *Presence and rank of the song on Shazam charts*
- **bpm**: *Beats per minute, a measure of song tempo*
- **key**: *Key of the song*
- **mode**: *Mode of the song (major or minor)*
- **danceability_%**: *Percentage indicating how suitable the song is for dancing*
- **valence_%**: *Positivity of the song's musical content*
- **energy_%**: *Perceived energy level of the song*
- **acousticness_%**: *Amount of acoustic sound in the song*
- **instrumentalness_%**: *Amount of instrumental content in the song*
- **liveness_%**: *Presence of live performance elements*
- **speechiness_%**: *Amount of spoken words in the song*

# Potential Use Cases:

&gt;- **Music analysis:** Explore patterns in audio features to understand trends and preferences in popular songs.
- **Platform comparison:** Compare the song's popularity across different music platforms.
- **Artist impact:** Analyze how artist involvement and attributes relate to a song's success.
- **Temporal trends:** Identify any shifts in music attributes and preferences over time.
- **Cross-platform presence:** Investigate how songs perform across different streaming services.

If you find this dataset useful, your support through an upvote would be greatly appreciated ❤️🙂 <br>
Thank you

### Dataset files ###

- spotify-2023.csv

    pandas.DataFrame(shape=(953, 24), columns=["track_name", "artist(s)_name", "artist_count", "released_year", "released_month", "released_day", "in_spotify_playlists", "in_spotify_charts", "streams", "in_apple_playlists", "in_apple_charts", "in_deezer_playlists", "in_deezer_charts", "in_shazam_charts", "bpm", "key", "mode", "danceability_%", "valence_%", "energy_%", "acousticness_%", "instrumentalness_%", "liveness_%", "speechiness_%"])
                      track_name      artist(s)_name  artist_count  released_year  released_month  released_day  in_spotify_playlists  ...  danceability_% valence_%  energy_%  acousticness_% instrumentalness_%  liveness_% speechiness_%
        0    Seven (feat. Lat...    Latto, Jung Kook             2           2023               7            14                  553   ...              80        89        83              31                  0           8             4
        1                   LALA         Myke Towers             1           2023               3            23                 1474   ...              71        61        74               7                  0          10             4
        2                vampire      Olivia Rodrigo             1           2023               6            30                 1397   ...              51        32        53              17                  0          31             6
        3           Cruel Summer        Taylor Swift             1           2019               8            23                 7858   ...              55        58        72              11                  0          11            15
        4         WHERE SHE GOES           Bad Bunny             1           2023               5            18                 3133   ...              65        23        80              14                 63          11             6
        ..                   ...                 ...           ...            ...             ...           ...                  ...   ...             ...       ...       ...             ...                ...         ...           ...
        948         My Mind & Me        Selena Gomez             1           2022              11             3                  953   ...              60        24        39              57                  0           8             3
        949  Bigger Than The ...        Taylor Swift             1           2022              10            21                 1180   ...              42         7        24              83                  1          12             6
        950  A Veces (feat. F...  Feid, Paulo Londra             2           2022              11             3                  573   ...              80        81        67               4                  0           8             6
        951        En La De Ella  Feid, Sech, Jhayco             3           2022              10            20                 1320   ...              82        67        77               8                  0          12             5
        952                Alone           Burna Boy             1           2022              11             4                  782   ...              61        32        67              15                  0          11             5

