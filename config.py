import logging

from decouple import config


logging.basicConfig(level=logging.INFO)


MQTT_HOST = config('MQTT_HOST')
MQTT_PORT = config('MQTT_PORT', cast=int, default=1883)
MQTT_USERNAME = config('MQTT_USERNAME')
MQTT_PASSWD = config('MQTT_PASSWD')
MQTT_TOPIC = config('MQTT_TOPIC', default='esp/weather')
MQTT_CLIENT_ID = config('MQTT_CLIENT_ID', default='gateway-esp')

WS_HOST = config('WS_HOST', default='localhost')
WS_API_KEY = config('WS_API_KEY', default='123')

WS_PAYLOAD_ENDPOINT = 'iot/cw/big-data-service/api/measurements'

FAKE_SENSORS_COUNT = config('FAKE_SENSORS_COUNT', cast=int, default=20)
