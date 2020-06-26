import paho.mqtt.publish as publish
import time
MQTT_SERVER = "192.168.0.11"  #Write Server IP Address
MQTT_PATH = "Image"

f=open("image1.jpg", "rb") #3.7kiB in same folder
fileContent = f.read()
byteArr = bytearray(fileContent)
time.sleep(2)
print("Sending data")


publish.single(MQTT_PATH, byteArr, hostname=MQTT_SERVER)
print("Sent data")
import os
os.system("python sub3.py")
