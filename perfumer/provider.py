from requests import get
import json

BASE_PERFUMER_URL = 'https://front-app-pub.perfumist.net/api'
AUTH_ID = 'EBfAYDzS6hjizqytkAgx'


def load(path: str) -> json:
    headers = {"x-perfumist-token": AUTH_ID}

    response = get(f'{BASE_PERFUMER_URL}/{path}', headers=headers, verify=False)
    return response.json()
