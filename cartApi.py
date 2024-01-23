import requests
from cart import Cart
from cartItem import CartItem


def get_carts() -> list[Cart]:
    url = 'https://dummyjson.com/carts?limit=0'
    carts = requests.get(url).json()
    return [Cart(x['id'], _create_cart_items(x['products']), x['userId']) for x in carts['carts']]


def _create_cart_items(products: list[dict[str, object]]) -> list[CartItem]:
    return [CartItem(x['id'], x['quantity']) for x in products]
