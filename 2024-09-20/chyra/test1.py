import requests

test = requests.get("https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/refs/heads/master/pokedex.json")

test = test.json()

print(len(test["pokemon"]))

len2 = len(test["pokemon"])

for i in range(len2):
    print(test["pokemon"][i]["name"], end="")
    try:
        len1 = len(test["pokemon"][i]["next_evolution"])
        for j in range(len(test["pokemon"][i]["next_evolution"])):
            print(" -> " + test["pokemon"][i]["next_evolution"][j]["name"], end="")
        i += len1
    except:
        print(end="")
    
    print()
