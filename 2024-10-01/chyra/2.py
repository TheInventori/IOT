import requests

request = requests.get("https://api.le-systeme-solaire.net/rest/bodies/uranus")

request = request.json()

for i in range(len(request["moons"])):
    print(request["moons"][i]["moon"])