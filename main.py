import config
from gateway.mqtt import connect_mqtt, subscribe_mqtt
from gateway.utils import on_connect, on_message


def run():
    mqtt_client = connect_mqtt(on_connect)
    subscribe_mqtt(mqtt_client, topic=config.MQTT_TOPIC, on_message=on_message)
    mqtt_client.loop_forever()


if __name__ == '__main__':
    run()
