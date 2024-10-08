import requests
import json

webhook = "https://hook.eu2.make.com/sfa0uqnrm98tj5w4sg7xoomef3cno26y"
api = "98adbfad6b4b220565d13e94b5769fd7"

def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&appid={api}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = {
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "weather_main": data["weather"][0]["main"],
            "weather_description": data["weather"][0]["description"],
        }
        return weather
    else:
        print("Chyba pri ziskavani udajov o pocasi")
        return None

def update_dashboard(value):
    value = json.dumps(value)
    url = f"{webhook}?value={value}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Uspesna aktualizacia dat")
    else:
        print(f"Chyba pri aktualizacii")

if __name__ == "__main__":
    lat = input("Zadajte zemepisnu sirku: ")
    lon = input("Zadajte zemepisnu dlzku: ")

    weather = get_weather(lat, lon)

    if weather:
        update_dashboard(weather)