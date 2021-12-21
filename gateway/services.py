import json
import logging
import typing
from datetime import datetime

import config
from gateway.http import send_data_to_ws
from gateway.types import DataEntry, Payload
from gateway.utils import random_times_from_range, random_mac_address, random_temp, random_humidity


logger = logging.getLogger(__name__)


def generate_payload(real_data: DataEntry) -> typing.Optional[Payload]:
    # try:
    #     real_dt = datetime.fromtimestamp(real_data['time'])
    # except TypeError:
    #     logger.warning(f'Got invalid time: {real_data["time"]}')
    #     return

    real_dt = datetime.now()

    fake_data = []

    with open('gateway/fixtures/macs.json') as f:
        macs = json.load(f)

    for idx, timestamp in enumerate(random_times_from_range(real_dt, 15, config.FAKE_SENSORS_COUNT)):
        fake_data.append(
            [
                macs[idx],
                random_temp(real_data['temperature']),
                random_humidity(real_data['humidity']),
                timestamp,
            ]
        )
    return Payload(values=fake_data)


def process_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    logger.info(f'Received message - {data}')
    payload = generate_payload(data)
    if payload is None:
        logger.warning('Empty payload skipped')
        return

    send_data_to_ws(payload)
