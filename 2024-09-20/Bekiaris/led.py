from machine import TouchPad, Pin
import time

led = Pin(2,Pin.OUT)

touch1 = TouchPad(Pin(32))
touch2 = TouchPad(Pin(33))
touch3 = TouchPad(Pin(27))

while True:
	touch_value1 = touch1.read()
	touch_value2 = touch2.read()
	touch_value3 = touch3.read()
	print("Touch Value:", touch_value1, "\t", touch_value2, "\t", touch_value3)
	time.sleep(0.1)
	
	if touch_value1 < 200:
		led.value(1)
		time.sleep(0.4)
		led.value(0)
		time.sleep(0.4)
	elif touch_value2 < 200:
		for i in range(2):
			led.value(1)
			time.sleep(0.4)
			led.value(0)
			time.sleep(0.4)
	elif touch_value3 < 200:
		for i in range(3):
			led.value(1)
			time.sleep(0.4)
			led.value(0)
			time.sleep(0.4)