import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b1a4016aba4500c5c4f9c406a5945b08'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Rabbit",
    "photo_id": 35
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)


body_changename = {
    "pokemon_id": "74531",
    "name": "New rabbit",
    "photo_id": 35
}

response_changname = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changename, )
print(response_changname.json()['message'])

body_catch = {
    "pokemon_id": "74531"
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.json()['message'])