from decouple import config


MQTT_HOST = config('MQTT_HOST')
MQTT_PORT = config('MQTT_PORT', cast=int, default=1883)
MQTT_USERNAME = config('MQTT_USERNAME')
MQTT_PASSWD = config('MQTT_PASSWD')
MQTT_TOPIC = config('MQTT_TOPIC', default='esp/weather')

WS_HOST = config('WS_HOST')
WS_API_KEY = config('WS_API_KEY')

WS_PAYLOAD_ENDPOINT = '/iot/cw/big-data-service/api/measurements'
