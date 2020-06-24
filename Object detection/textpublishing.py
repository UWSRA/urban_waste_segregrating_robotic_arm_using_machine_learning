import paho.mqtt.publish as publish
MQTT_SERVER = "localhost"  #Write Server IP Address
MQTT_PATH = "text"
def text_pub(message):
     print("message to be published")
     publish.single(MQTT_PATH, message, hostname=MQTT_SERVER)
