import dht
import machine
import time

dht_pin = machine.Pin(15)

dht_sensor = dht.DHT11(dht_pin)


while True:
	try:
		dht_sensor.measure()
		temp = dht_sensor.temperature()
		hum = dht_sensor.humidity()
		
		print("Teplota: {}°C	Vlhkost: {}%".format(temp,hum))
		
		
	except OSError as e:
		print("Failed to read sensor")
		
	time.sleep(1)