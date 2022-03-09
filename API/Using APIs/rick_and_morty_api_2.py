from numpy import character
import requests, json

character_name = requests.get("https://rickandmortyapi.com/api/character")
character_name = character_name.json()

for x in character_name['results']:
    print(x['name'])