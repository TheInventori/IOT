import requests

test = requests.get("https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/refs/heads/master/pokedex.json")

pok1 = input("Meno prveho pokemona: ")
pok2 = input("Meno druheho pokemona: ")



test = test.json()

print(len(test["pokemon"]))

for i in range(len(test["pokemon"])):
    print("Pokemon " + test["pokemon"][i]["name"] + " of " + " and ".join(test["pokemon"][i]["type"]) + " type is " + test["pokemon"][i]["height"] + " high with weight of " + test["pokemon"][i]["weight"])
