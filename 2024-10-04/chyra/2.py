import urequests
import json
import network
import dht
import machine
import time

dht_pin = machine.Pin(15)

dht_sensor = dht.DHT11(dht_pin)

webhook_url = 'https://hook.eu2.make.com/2v2grxj8p4zcfwbyk4f9ybdot823ovgp'

ssid = 'Ucebna13'
passw = 'jablko987'

def connectToWifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(ssid, passw)

    while not wifi.isconnected():
        pass

    print("Pripojene k Wi-Fi: ", wifi.ifconfig())
    
def sendData(temp, hum):
    try:
        url = f"{webhook_url}?temperature={temp}&humidity={hum}"
        response = urequests.get(url)
        print(response.text)
    except Exception as e:
        print("[Error]: ", e)
        
connectToWifi()

while True:
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
        
        print(f"Teplota: {temp} C  Vlhkost: {hum}%")
        
        sendData(temp, hum)
        
    except OSError as e:
        print("Failed to read sensor.")
        
    time.sleep(2)


