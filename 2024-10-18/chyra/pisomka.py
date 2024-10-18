import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime

api = "98adbfad6b4b220565d13e94b5769fd7"

def get_weather(city):
    cityUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api}"
    responseCity = requests.get(cityUrl)
    dataCity = responseCity.json()
    lat = 0
    lon = 0

    if responseCity.status_code == 200:
        lat = dataCity[0]["lat"]
        lon = dataCity[0]["lon"]
    else:
        print("Chyba pri ziskavani mesta")
        return None

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = []
        dt = []
        for i in range(len(data["list"])):
            temp.append(data["list"][i]["main"]["temp"])
            dt.append(datetime.utcfromtimestamp(data["list"][i]["dt"]))
        weather = {
            "dt": dt,
            "temp": temp
        }
        return weather
    else:
        print("Chyba pri ziskavani udajov o pocasi")
        return None

if __name__ == "__main__":
    city = input("Zadajte mesto: ")

    weather = get_weather(city)

    if weather:
        plt.plot(weather["dt"], weather["temp"])
        plt.xlabel('Cas')  
        plt.ylabel('Teplota')
        plt.title('Pocasie')
        plt.show()
