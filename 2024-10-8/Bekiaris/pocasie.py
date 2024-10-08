import requests
import json
import time

apiKey = "1442625978e85c9f4d85a14aa9ecbfbc"


urlWebHook = "https://hook.eu2.make.com/j588e53vi7cab8jnbfru23q8df4dtt05"



def get_weather(lat,lon):
    urlWeather = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&appid={apiKey}"
    response = requests.get(urlWeather)
    data = response.json()

    if response.status_code == 200:
        weather = {
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure":  data["main"]["pressure"],
            "weather_main": data["weather"][0]["main"],
            "weather_description": data["weather"][0]["description"]
        }
        return weather
    else:
        print("Comunication ERROR")
        return None

def update_dash(value):
    value = json.dumps(value)
    url = f"{urlWebHook}?value={value}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Update succesfull")
    else:
        print("Update failed")

lat = input("Zadajte zemepisnu sirku: ")
lon = input("Zadajte zemepisnu dlzku: ")

weather = get_weather(lat,lon)

if weather:
    update_dash(weather)





