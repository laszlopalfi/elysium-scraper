from requests import get, Response
import json

BASE_PERFUMER_URL = 'https://front-app-pub.perfumist.net/api'
BASE_PERFUMER_ASSET_URL = 'https://perfumist-images.fra1.cdn.digitaloceanspaces.com/assets'
AUTH_ID = 'EBfAYDzS6hjizqytkAgx'


# https://perfumist-images.fra1.cdn.digitaloceanspaces.com/assets/brand/mains/files/000/008/199/thumb/12_parfumeurs_logo.png?1483105539


def load(path: str) -> json:
    headers = {"x-perfumist-token": AUTH_ID}

    response = get(f'{BASE_PERFUMER_URL}/{path}', headers=headers)
    return response.json()


def load_asset_stream(path: str) -> Response:
    return get(f'{BASE_PERFUMER_ASSET_URL}/{path}', verify=False, stream=True)
