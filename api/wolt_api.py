import logging

import requests as requests


class WoltApiHook:

    def __init__(self, url: str, venue_id: str, token: str) -> None:
        self._url = url
        self._venue_id = venue_id
        self._token = token

    def patch_data(self, endpoint, payload) -> bool:
        url = f'{self._url}/venues/{self._venue_id}/{endpoint}'

        logging.info(f'Processing url: {url}')

        headers = {
            'Content-Type': "application/json;charset=utf-8",
            'Authorization': f"Basic {self._token}",
            'cache-control': "no-cache"
        }

        r = requests.patch(url, headers=headers, data=payload)

        success_code = 202

        result_is_success = r.status_code == success_code

        if not result_is_success:
            logging.error(f"Status code: {r.status_code} - {r.reason}. Response text: {r.text}")

        return result_is_success