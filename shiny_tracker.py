import pip._vendor.requests 
import json

# This is going to be a PokeDex/Shiny tracker I can use during my eventual shiny hunts across all pokemon games.
# The app will have a search bar for the user to search for a specific pokemon, and a display area for the information about the selected pokemon.

def get_pokemon_data():
    """
    This function retrieves data about a specific Pokémon from the PokéAPI.

    Parameters:
    None

    Returns:
    object Pokemon: A pokemon object containing the Pokémon's data. 
    """

    url = "https://pokeapi.co/api/v2/pokemon/1"
    response = pip._vendor.requests.get(url);

  

class Pokemon:
    def __init__(self, name, id, sprite, status):
        self.name = name
        self.id = id
        self.sprite = sprite
        self.status = status