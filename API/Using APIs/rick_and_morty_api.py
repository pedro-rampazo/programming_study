import requests
import json

rm_characters = requests.get("https://rickandmortyapi.com/api/character")
rm_characters = rm_characters.json()
print(rm_characters)