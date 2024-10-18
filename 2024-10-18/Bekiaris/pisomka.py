import requests
import json
import time
import matplotlib.pyplot as plt
from datetime import datetime


apiKey = "1442625978e85c9f4d85a14aa9ecbfbc"

#Zadanie nazvu mesta od uzivatela
city_name = input("Zadajte nazov mesta: ")
city = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={5}&appid={apiKey}"

response = requests.get(city)
data = response.json()

if response.status_code == 200:
    lon = data[0]["lon"]
    lat = data[0]["lat"]

else:
    print("Chyba komunikacie")
    


urlWeather = f"http://api.openweathermap.org/data/2.5/forecast?units=Metric&lat={lat}&lon={lon}&appid={apiKey}"
response = requests.get(urlWeather)
data = response.json()

if response.status_code == 200:
    date = []
    temp = []
    for i in range(len(data["list"])):
        date.append(datetime.utcfromtimestamp(data["list"][i]["dt"]))
        temp.append(data["list"][i]["main"]["temp"])
    weather = {
        "date": date,
        "temp": temp
    }
    
    
else:
    print("Comunication ERROR")
    

x = weather["date"]
y = weather["temp"]

plt.plot(x, y)

plt.xlabel('DATE')
plt.ylabel('TEMP ℃')
plt.title('WEATHER FORECAST FOR 5 DAYS')

plt.show()


