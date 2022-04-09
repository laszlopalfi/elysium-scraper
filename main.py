from service.brand_service import get_brands, get_brand_image


def main():
    print(" --- Scraping brands ---")
    brands = get_brands()
    print(f"Scraped {len(brands)} brands")

    for brand in brands:
        get_brand_image(brand)
    # for i in range(100):
    #     product_summaries = get_product_summaries(i)
    #     export_product_summary_list(i, product_summaries)


#
#     try:
#         with open("output/product_summary.csv", 'w', newline='') as f:
#             writer = csv.writer(f)
#             for product_summary in product_summaries:
#                 writer.writerow(
#                     [
#                         product_summary.id,
#                         product_summary.name,
#                         product_summary.image_url,
#                         product_summary.thumb_image_url,
#                         product_summary.product_type,
#                         product_summary.bottle_size,
#                         product_summary.year,
#                         product_summary.gender,
#                         product_summary.discontinued,
#                         product_summary.brand_id
#                     ]
#                 )
#
#     except BaseException as e:
#         print('BaseException:', "product_summary.csv")
#     else:
#         print('Data has been loaded successfully !')


if __name__ == "__main__":
    main()

#
#
# try:
#     with open("output/product_summary.csv", 'w', newline='') as f:
#         writer = csv.writer(f)
#         for product_summary in product_summary_list:
#             writer.writerow(
#                 [
#                     product_summary.id,
#                     product_summary.name,
#                     product_summary.image_url,
#                     product_summary.thumb_image_url,
#                     product_summary.product_type,
#                     product_summary.bottle_size,
#                     product_summary.year,
#                     product_summary.gender,
#                     product_summary.discontinued,
#                     product_summary.brand_id
#                 ]
#             )
#
# except BaseException as e:
#     print('BaseException:', "product_summary.csv")
# else:
#     print('Data has been loaded successfully !')
#
#     # //LOAD asset
#     id = product_summary_list[0].id
#     imageURL = product_summary_list[0].image_url
#     print(imageURL)
#     imageURL_pretty = imageURL[63:]
#     print(imageURL_pretty)
#
#     for product in product_summary_list:
#         id = product.id
#         imageURL = product.image_url
#         imageURL_pretty = imageURL[63:]
#         load_asset(imageURL_pretty, id, "product")
