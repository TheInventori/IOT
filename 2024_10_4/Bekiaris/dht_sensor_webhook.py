import dht
import machine
import time
import requests
import network

dht_pin = machine.Pin(15)

dht_sensor = dht.DHT11(dht_pin)

ssid = "Ucebna13"
password = "jablko987"


def connect_wifi():
	wlan = network.WLAN(network.STA_IF)
	wlan.active(True)
	wlan.connect(ssid, password)
	
	while not wlan.isconnected():
		time.sleep(1)
	print("WiFi pripojene")
	print("IP adress: ", wlan.ifconfig()[0])
	
connect_wifi()
	
while True:
	try:
		dht_sensor.measure()
		temp = dht_sensor.temperature()
		hum = dht_sensor.humidity()
		
		print("Teplota: {}°C	Vlhkost: {}%".format(temp,hum))
		
		obj = {'temp': temp,
			   'hum': hum,}
		requests.post("https://hook.eu2.make.com/eklgtpauuxqs8wgexvg2ykead5o76tii", json = obj)
		
	except OSError as e:
		print("Failed to read sensor")
		
	time.sleep(1)