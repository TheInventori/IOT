import requests

dictionary = requests.get("https://api.le-systeme-solaire.net/rest/bodies/uranus")

data = dictionary.json()

numberOfMoons = len(data["moons"])

for i in range (numberOfMoons):
    print(data["moons"][i]["moon"])