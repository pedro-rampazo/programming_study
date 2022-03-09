import requests, json

pokemons = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=100").json()
counter = 1

for name in pokemons['results']:
    print(f"{counter} - {name['name'].upper()}")
    counter += 1

