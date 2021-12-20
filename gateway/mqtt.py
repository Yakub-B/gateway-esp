import typing
import logging

import config
from paho.mqtt import client as mqtt_client


logger = logging.getLogger(__name__)


def connect_mqtt(on_connect: typing.Callable = None) -> mqtt_client.Client:
    logger.info(f'Trying to connect to broker: {config.MQTT_HOST}:{config.MQTT_PORT}')
    logger.info(f'Credentials: {config.MQTT_USERNAME}, {config.MQTT_PASSWD}')

    client = mqtt_client.Client('is_this_relevant?')
    client.username_pw_set(config.MQTT_USERNAME, config.MQTT_PASSWD)
    if on_connect:
        client.on_connect = on_connect
    client.connect(host=config.MQTT_HOST, port=config.MQTT_PORT)
    return client


def subscribe_mqtt(client: mqtt_client.Client, topic: str, on_message: typing.Callable):
    client.subscribe(topic)
    client.on_message = on_message
