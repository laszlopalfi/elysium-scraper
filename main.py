from perfumer.resource import load_notes, load_brands, load_products
from model.note import Note
from model.brand import Brand
from model.product_summary import ProductSummary

import json
import csv

# notes_json = load_notes()
# notes_list = []
#
# for note_object in notes_json['notes']:
#     note = Note(note_object['id'], note_object['name'], note_object['normal_image_url'], note_object['thumb_image_url'])
#     notes_list.append(note)
#
# print(len(notes_list))
#
# brands_json = load_brands()
# brands_list = []
#
# for brand_object in brands_json['brands']:
#     brand = Brand(brand_object['id'], brand_object['name'], brand_object['normal_image_url'],
#                   brand_object['thumb_image_url'])
#     brands_list.append(brand)
#
# print(len(brands_list))

product_summary_json = load_products(95, "1")
product_summary_list = []

print(product_summary_json)

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

print(len(product_summary_list))

try:
    with open("output/product_summary.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for product_summary in product_summary_list:
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
#
# try:
#     with open("output/notes.csv", 'w', newline='') as f:
#         writer = csv.writer(f)
#         for note in notes_list:
#             writer.writerow([note.id, note.name, note.image_url, note.thumb_image_url])
# except BaseException as e:
#     print('BaseException:', "notes.csv")
# else:
#     print('Data has been loaded successfully !')
#
#     try:
#         with open("output/brands.csv", 'w', newline='') as f:
#             writer = csv.writer(f)
#             for brand in brands_list:
#                 writer.writerow([brand.id, brand.name, brand.image_url, brand.thumb_image_url])
#     except BaseException as e:
#         print('BaseException:', "brands.csv")
#     else:
#         print('Data has been loaded successfully !')

# import json
# from brand import Brand
# import requests
# import json
#
# response = requests.get("https://front-app-pub.perfumist.net/api/brands/", verify=False)
# response_json = response.json()
#
# brand_list = []
# for brand in response_json['brands']:
#     brand_list.append([brand['id'], brand['name']])
#
# print(brand_list);
# # b1 = Brand(1, "brand_1", "", "")
# # b2 = Brand(2, "brand2", "", "")
# # b3 = Brand(3, "brand3", "", "")
# #
# # list = [b1, b2, b3]
# #
# # json_string = json.dumps([ob.__dict__ for ob in list])
# #
# # print(json_string)
