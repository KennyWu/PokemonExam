import requests
import json

url = ""
data = None
with open("type_pokemon.json", "r") as f:
    data = json.load(f)

for i in range(1, 1297):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(i) + "/"
    print(url)
