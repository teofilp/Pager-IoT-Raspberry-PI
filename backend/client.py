import paho.mqtt.client as mqtt
from notification import NotificationService

service = NotificationService()

def on_message(client, userdata, msg):
    service.add_notification(msg.payload.decode('utf-8'))
    
client = mqtt.Client()
client.connect("192.168.1.6", 1883, 60)

client.subscribe("test")
client.on_message = on_message

try:
    client.loop_forever()
except KeyboardInterrupt:
    service.cleanup()