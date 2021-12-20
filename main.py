import config
from gateway.mqtt import connect_mqtt, subscribe_mqtt
from gateway.services import process_message
from gateway.utils import on_connect


def run():
    mqtt_client = connect_mqtt(on_connect)
    subscribe_mqtt(mqtt_client, topic=config.MQTT_TOPIC, on_message=process_message)
    mqtt_client.loop_forever()


if __name__ == '__main__':
    run()
