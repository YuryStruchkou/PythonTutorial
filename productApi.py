import requests
from product import Product


def get_products() -> list[Product]:
    url = 'https://dummyjson.com/products?limit=0'
    products = requests.get(url).json()
    return [Product(x['id'], x['title'], x['category']) for x in products['products']]
