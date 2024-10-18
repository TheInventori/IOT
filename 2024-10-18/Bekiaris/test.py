import requests
apiKey = "1442625978e85c9f4d85a14aa9ecbfbc"

city_name = input("Zadajte nazov mesta")

city = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={5}&appid={apiKey}"

response = requests.get(city)
data = response.json()

lon = data[0]["lon"]

print(lon)