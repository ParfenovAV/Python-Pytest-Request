import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '22e465133abff771c451311117703012'
HEADER = {  'Content-type': 'application/json',  'trainer_token': TOKEN}
body_pokemon ={    "name": "generate",     "photo_id": 1 }


response = requests.post(url = f'{URL}pokemons', headers=HEADER, json= body_pokemon)
print(response, response.text)

pok_id = response.json()['id']
body_rename= { "pokemon_id": pok_id,  "name": "New" }
body_pokeball= { "pokemon_id": pok_id }

response_rename = requests.patch(url = f'{URL}pokemons', headers=HEADER, json= body_rename)
print(response_rename, response_rename.text)

response_pokeball = requests.post(url = f'{URL}trainers/add_pokeball', headers=HEADER, json= body_pokeball)
print(response_pokeball, response_pokeball.text)