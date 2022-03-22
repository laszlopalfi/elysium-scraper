class ProductSummary:
    def __init__(self, id: int, name: str, image_url: str, thumb_image_url: str, product_type: str, bottle_size: float,
                 year: int, gender: str, discontinued: bool, brand_id: int):
        self.id = id
        self.name = name
        self.image_url = image_url
        self.thumb_image_url = thumb_image_url
        self.product_type = product_type
        self.bottle_size = bottle_size
        self.year = year
        self.gender = gender
        self.discontinued = discontinued
        self.brand_id = brand_id
