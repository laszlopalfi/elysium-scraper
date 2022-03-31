import json
from perfumer.provider import load, load_asset_stream

BRANDS_PATH = 'brands'
PRODUCTS_PATH = 'brands/{brand_id}/products?page={page_number}'
PRODUCT_PATH = 'products/{product_id}'
NOTES_PATH = 'notes'


def load_notes() -> json:
    return load(NOTES_PATH)


def load_brands() -> json:
    return load(BRANDS_PATH)


def load_products(brand_id: int, page_number: int) -> json:
    return load(PRODUCTS_PATH.format(brand_id=brand_id, page_number=page_number))


def load_product(product_id: int) -> json:
    return load(PRODUCT_PATH.format(product_id))


def load_asset(path: str, id: int, type:str):
    response = load_asset_stream(path)
    with open(f'output/assets/{type}/{id}.png', 'wb') as handle:
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
