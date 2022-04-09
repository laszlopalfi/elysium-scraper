from model.brand import Brand
from perfumer.resource import load_brands, load_asset


def get_brands() -> [Brand]:
    brands_json = load_brands()
    brands_list = []
    for brand_object in brands_json['brands']:
        brand = Brand(brand_object['id'],
                      brand_object['name'],
                      brand_object['normal_image_url'],
                      brand_object['thumb_image_url'])
        brands_list.append(brand)
    return brands_list


def get_brand_image(brand: Brand):
    load_asset(brand.image_url[63:], brand.id, "brand")
