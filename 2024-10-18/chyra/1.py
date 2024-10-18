import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime

api = "98adbfad6b4b220565d13e94b5769fd7"
make = "https://hook.eu2.make.com/2qe94j871yg04swi8zrwi1tonbv2fk6q"

def get_weather():
    lat = "48.7172272"
    lon = "21.2496774"
    url = f"http://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt=2&appid={api}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        if data['list'][0]['weather'][0]['main'] == "Rain":
            hehe = "Budete potrebovat dazdnik."
        else:
            hehe = "Nebudete potrebovat dazdnik."

        weather = {
            "desc": data['list'][0]['weather'][0]['description'],
            "minTemp": data['list'][0]['temp']['min'],
            "maxTemp": data['list'][0]['temp']['max'],
            "hehe": hehe
        }

        return weather
    else:
        print("Chyba pri ziskavani udajov o pocasi")
        return None

def update_dashboard(value):
    value = json.dumps(value)
    url = f"{make}?value={value}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Uspesna aktualizacia dat")
    else:
        print(f"Chyba pri aktualizacii")


if __name__ == "__main__":
    weather = get_weather()

    if weather:
        update_dashboard(weather)