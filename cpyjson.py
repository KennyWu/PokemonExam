import requests
import json

url = 'https://pokeapi.co/api/v2/type'
response = requests.get(url)
data = None
json_files = []
type_chart = {}


def retrieve(url=""):
    data = None
    poke_w = []
    poke_r = []
    poke_i = []
    type_info = {}
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    for poke_type in data["damage_relations"]["double_damage_from"]:
        poke_w.append(poke_type["name"])

    for poke_type in data["damage_relations"]["half_damage_from"]:
        poke_r.append(poke_type["name"])

    for poke_type in data["damage_relations"]["no_damage_from"]:
        poke_i.append(poke_type["name"])
    poke_r = poke_r + poke_i
    type_info["effective"] = poke_w
    type_info["neutral"] = poke_r

    return type_info


def main():
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error")

    with open('./Types/types.json', 'w') as f:
        json.dump(data, f, indent=4)

    type_src = []
    type_chart["result"] = {}
    for item in data["results"]:
        type_s = {}
        url = item["url"]
        type_s = retrieve(url)
        type_chart["result"][item["name"]] = type_s

    with open("type_pokemon.json", "w") as f:
        json.dump(type_chart, f, indent=4)


main()
