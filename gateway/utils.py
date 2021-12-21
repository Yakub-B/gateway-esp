import logging
import random
from datetime import timedelta, datetime

import config

logger = logging.getLogger(__name__)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info('Connected to broker')
        logger.info(f'{userdata=}')
        logger.info(f'{flags=}')
    else:
        logger.error(f'Failed to connect, return code - {rc}')


def random_times_from_range(original_datetime: datetime, delta_seconds: int, count: int):
    """
    Returns generator yielding random unix timestamps in range of +-delta_seconds between original_datetime
    """
    for _ in range(count):
        random_second = random.randrange(delta_seconds) * 2
        fake_dt = original_datetime - timedelta(seconds=delta_seconds) + timedelta(seconds=random_second)
        yield fake_dt.strftime(config.DT_FORMAT)


def random_mac_address():
    return ':'.join([f'{random.randint(0, 255):02x}' for _ in range(6)])


def random_temp(orig_temp: float) -> str:
    delta = 1.5
    random_degree = random.uniform(0, delta) * 2
    return '{:.2f}'.format(orig_temp - delta + random_degree)


def random_humidity(orig_humidity: float) -> str:
    delta = 5
    random_degree = random.uniform(0, delta) * 2
    return '{:.2f}'.format(orig_humidity - delta + random_degree)
