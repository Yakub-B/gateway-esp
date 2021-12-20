import logging
import json

logger = logging.getLogger(__name__)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info('Connected to broker')
        logger.info(f'{userdata=}')
        logger.info(f'{flags=}')
    else:
        logger.error(f'Failed to connect, return code - {rc}')


def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    logger.info(f'Received message - {data}')
