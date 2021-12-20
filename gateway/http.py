import logging

import requests

import config
from gateway.types import Payload


logger = logging.getLogger(__name__)


def send_data_to_ws(payload: Payload):
    url = f'{config.WS_HOST}/{config.WS_PAYLOAD_ENDPOINT}'
    with requests.session() as client:
        client.headers['Content-Type'] = 'application/json'
        logger.info(f'Sending data to - {url}')
        try:
            response = client.post(url, json=payload)
        except requests.HTTPError as e:
            logger.error(f"Data to {url} doesn't sent", exc_info=e)
        else:
            if response.status_code != 200:
                logger.error(f'Data sending not successful, ws respond with status code {response.status_code}')
                return
            logger.info(f'Data to {url} sent successfully')
