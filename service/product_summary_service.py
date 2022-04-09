import csv
import json
import os
import time

from model.product_summary import ProductSummary
from perfumer.resource import load_products

PRODUCT_SUMMARIES_FOLDER = './output/product_summaries/'


def get_product_summaries(brand_id: int) -> [ProductSummary]:
    print(f'Scraping product summaries for brand: {brand_id}')
    product_summary_json = load_products(brand_id, 1)
    product_summary_list = parse_product_summary(product_summary_json)

    print(f'Scraping product summaries pagination for brand: {brand_id}')
    product_summary_pagination_json = get_product_summary_pagination(product_summary_json)

    current_page = 2
    while current_page <= product_summary_pagination_json['total_pages']:
        print(f"Scraping current page: {current_page} out of {product_summary_pagination_json['total_pages']}")
        product_summaries = get_product_summary(brand_id, current_page)
        product_summary_list = product_summary_list + product_summaries
        current_page += 1
        time.sleep(3)
    return product_summary_list


def get_product_summary(brand_id: int, page_number: int) -> [ProductSummary]:
    product_summary_json = load_products(brand_id, page_number)
    return parse_product_summary(product_summary_json)


def parse_product_summary(product_summary_json) -> [ProductSummary]:
    product_summary_list = []
    for product_summary_object in product_summary_json['products']:
        product_summary = ProductSummary(product_summary_object['id'],
                                         product_summary_object['name'],
                                         product_summary_object['normal_image_url'],
                                         product_summary_object['thumb_image_url'],
                                         product_summary_object['product_type'],
                                         product_summary_object['bottle_size'],
                                         product_summary_object['year'],
                                         product_summary_object['gender'],
                                         product_summary_object['discontinued'],
                                         95)
        product_summary_list.append(product_summary)
    return product_summary_list


def get_product_summary_pagination(product_summary_json: json) -> json:
    pagination = product_summary_json['meta']['pagination']
    print(f"Pagination: Total pages: {pagination['total_pages']} - Total count: {pagination['total_count']}")
    return pagination


def export_product_summary_list(brand_id: int, product_summaries: [ProductSummary]):
    create_product_summary_directory()
    try:
        with open(f"{PRODUCT_SUMMARIES_FOLDER}/brand_{brand_id}.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for product_summary in product_summaries:
                writer.writerow(
                    [
                        product_summary.id,
                        product_summary.name,
                        product_summary.image_url,
                        product_summary.thumb_image_url,
                        product_summary.product_type,
                        product_summary.bottle_size,
                        product_summary.year,
                        product_summary.gender,
                        product_summary.discontinued,
                        product_summary.brand_id
                    ]
                )
    except BaseException as e:
        print('BaseException:', "product_summary.csv")
    else:
        print('Data has been loaded successfully !')


def create_product_summary_directory():
    directory = os.path.dirname(PRODUCT_SUMMARIES_FOLDER)
    if not os.path.exists(directory):
        os.makedirs(directory)
