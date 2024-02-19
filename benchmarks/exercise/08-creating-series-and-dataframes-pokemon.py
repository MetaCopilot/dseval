# %%
import pandas as pd

# %%
"""
question: |

  Create a Dataframe called pokemon with the following contents:

      evolution  hp        name pokedex   type
  0     Ivysaur  45   Bulbasaur     yes  grass
  1  Charmeleon  39  Charmander      no   fire
  2   Wartortle  44    Squirtle     yes  water
  3     Metapod  45    Caterpie      no    bug

validator:
  namespace_check:
    pokemon:
"""

pokemon = pd.DataFrame({
    'evolution': ['Ivysaur', 'Charmeleon', 'Wartortle', 'Metapod'],
    'hp': [45, 39, 44, 45],
    'name': ['Bulbasaur', 'Charmander', 'Squirtle', 'Caterpie'],
    'pokedex': ['yes', 'no', 'yes', 'no'],
    'type': ['grass', 'fire', 'water', 'bug']
})

# %%
"""
question: Ops...it seems the DataFrame columns are in alphabetical order. Place  the order of the columns as name, type, hp, evolution, pokedex. Save it to a variable called pokemon_col.

validator:
  namespace_check:
    pokemon_col:
"""

pokemon_col = pokemon[['name', 'type', 'hp', 'evolution', 'pokedex']]

# %%
"""
question: |
  Add another column called place. The values of place are as follows:
  - Bulbasaur is in park
  - Caterpie is in forest
  - Squirtle is in lake
  - Charmander is in street

validator:
  namespace_check:
    pokemon_col:
"""

pokemon_place = pd.DataFrame({
    'name': ['Bulbasaur', 'Charmander', 'Squirtle', 'Caterpie'],
    'place': ['park', 'street', 'lake', 'forest']
})
pokemon_col = pokemon_col.merge(pokemon_place, on='name')

# %%
"""
question: Present the type of each column
"""

pokemon_col.dtypes
