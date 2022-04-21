from unicodedata import name
import requests
def get_pokemon_info(name):
    """
    Gets a dictionary of information from the PokeaAPi from a pokemon
    :param name : Pokemons name
    :return : dictionary of pokemon if succesfull, none if its not 
    """
    print("Getting pokemon information...", end="")
    if name is None:
        return

    name = name.lower().strip()
    if name == '':
        return
    
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(name))

    if response.status_code == 200:
        print("Success")
        return  response.json()
    else:
        print('Failed. Response code:',response.status_code)
        return

def get_pokemon_list(limit=200, offset=0):
    """
    Gets a dictionary of information from the PokeaAPi from a pokemon
    :param limit : Pokemons limit for the list
    :param offset : 
    """
    print("Getting list of Pokemon...", end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    params = {
        'offset': offset,
        'limit': limit
    }
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        print('success')
        poke_dict = response.json()
        return [p['name'] for p in poke_dict['results']]
    else:
        print('failed. Response code:', response.status_code)

def get_pokemon_image_url(name):
    poke_dict = get_pokemon_info(name)
    if poke_dict:
        poke_url = poke_dict['sprites']['other']['official-artwork']['front_default']
        return poke_url