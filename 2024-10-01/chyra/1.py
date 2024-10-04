import network

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("Ucebna13", "jablko987")

while not wifi.isconnected():
    pass

print("Pripojene k Wi-Fi: ", wifi.ifconfig())