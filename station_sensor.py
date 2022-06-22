"""
Station Sensor - Reads from Ambient weather observerIP 3.0
on LAN and publishes to MQTT Endpoint
"""

from lxml import html
import requests
import time
import paho.mqtt.client as mqtt
from faker import Faker
from datetime import datetime

# let's connect to the MQTT broker
MQTT_BROKER_URL    = "mqtt.eclipseprojects.io"
MQTT_PUBLISH_TOPIC = "biot-temperature"

mqttc = mqtt.Client()
mqttc.connect(MQTT_BROKER_URL)

# Init faker our fake data provider
fake = Faker()

station_url = 'http://192.168.1.126/livedata.htm'

# Infinite loop of fake data sent to the Broker
while True:
    page = requests.get(station_url)
    tree = html.fromstring(page.content)
    curr_time = (tree.xpath('//input[@name="CurrTime"]')[0].value)
    curr_time_dt = datetime.strptime(curr_time, "%H:%M %m/%d/%Y")
    out_temp = float(tree.xpath('//input[@name="outTemp"]')[0].value)

    mqttc.publish(MQTT_PUBLISH_TOPIC, out_temp)
    print(f"Published Outside Temp: {curr_time_dt.strftime('%Y-%m-%d %H:%M')} | {out_temp}")
    time.sleep(60)
