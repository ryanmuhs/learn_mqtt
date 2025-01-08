import paho.mqtt.client as mqtt
import time
import os
from dotenv import load_dotenv
import json

load_dotenv()

sensor_data = {}
def on_message(client, userdata, message):
    global sensor_data
    try:
        data = json.loads(str(message.payload.decode("utf-8")))
        sensor_data.update(data)
        print("Update Sensor Data :", sensor_data)
    except json.JSONEncoder:
        print("Received invalid JSON:", message.payload.decode("utf-8"))

mqttBroker = os.getenv('HIVEMQ_RYAN_BROKER')
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Greenhouse Gas")
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set(os.getenv('HIVEMQ_RYAN_USERNAME'), os.getenv('HIVEMQ_RYAN_PASSWORD'))
client.connect(mqttBroker, int(os.getenv('HIVEMQ_RYAN_PORT')), 60)

client.loop_start()
client.subscribe("GreenHouseGas")
client.on_message = on_message
time.sleep(30)
client.loop_read()