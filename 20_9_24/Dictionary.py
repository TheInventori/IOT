import requests;

pokedex = requests.get("https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json")

pokemondata = pokedex.json()

numberOfPokemon =   len(pokemondata["pokemon"])

for i in range (numberOfPokemon):
    #if pokemon has 2 types they get joined into one string
    if (len(pokemondata["pokemon"][i]["type"])) == 2:
        pokemontype = pokemondata["pokemon"][i]["type"][0] + " and " + pokemondata["pokemon"][i]["type"][1]
    else:
        pokemontype = pokemondata["pokemon"][i]["type"][0]
    #printing of the pokemon info
    print("Pokemon " + pokemondata["pokemon"][i]["name"] +
    " of " + 
    pokemontype +
    " type is " + pokemondata["pokemon"][i]["height"] +
    " high with weight of " + pokemondata["pokemon"][i]["weight"])

print("Pocet pokemonov v pokedexe: ", numberOfPokemon)



print(len(pokemondata["pokemon"][0]["next_evolution"]))

print(len(pokemondata["pokemon"][18]["next_evolution"]))


z = 3

for i in range (0, numberOfPokemon,  z):
    if z == 2:
        print(pokemondata["pokemon"][i]["name"] + 
        "->" + 
        pokemondata["pokemon"][i]["next_evolution"][0]["name"])

    elif z == 3:
        print(pokemondata["pokemon"][i]["name"] + "->" + 
        pokemondata["pokemon"][i]["next_evolution"][0]["name"] +
        "->" + 
        pokemondata["pokemon"][i]["next_evolution"][1]["name"])

    else:
        print(pokemondata["pokemon"][i]["name"])

    if (len(pokemondata["pokemon"][i]["next_evolution"])) == 1:
        z = 2
    elif (len(pokemondata["pokemon"][i]["next_evolution"])) == 2:
        z = 3
    else:
        z = 1

