import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import os
from dotenv import load_dotenv
import json
import datetime

load_dotenv()
mqttBroker = os.getenv('HIVEMQ_RYAN_BROKER')
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "CO2")
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set(os.getenv('HIVEMQ_RYAN_USERNAME'), os.getenv('HIVEMQ_RYAN_PASSWORD'))
client.connect(mqttBroker,int( os.getenv('HIVEMQ_RYAN_PORT')), 60)
while True:
    randNumber = uniform(20.0, 21.0)
    timestamp = datetime.datetime.now()
    data = json.dumps({
        "Sensor": "Sensor 001",
        "Timestamp": str(timestamp),
        "CH4":randNumber,
        "CH2":randNumber
    })
    client.publish("GreenHouseGas", data)
    print("Published CH4 : " + data + " to Topic GreenHouseGas")
    time.sleep(1)