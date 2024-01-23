from itertools import groupby, chain
from typing import TypeAlias

from cart import Cart
from cartItem import CartItem
from product import Product
from user import User
from userCategoryData import UserCategoryData

ResultingDataset: TypeAlias = list[UserCategoryData]


def map_users_to_most_common_categories(users: list[User], products: list[Product], carts: list[Cart]):
    sorted_carts = sorted(carts, key=lambda x: x.userId)
    grouped_cart_items = _group_cart_items(sorted_carts)
    categories_by_user = _calculate_categories_by_user(products, grouped_cart_items)
    most_common_categories = {k: _find_all_max_values(v) for k, v in categories_by_user.items()}
    return _create_resulting_dataset(users, most_common_categories)


def _group_cart_items(carts: list[Cart]) -> dict[int, list[CartItem]]:
    grouped_carts = {k: list(g) for k, g in groupby(carts, key=lambda x: x.userId)}
    grouped_cart_items = {}
    for k, v in grouped_carts.items():
        grouped_cart_items[k] = list(chain.from_iterable((x.products for x in v)))
    return grouped_cart_items


def _calculate_categories_by_user(products: list[Product], grouped_cart_items: dict[int, list[CartItem]]) \
        -> dict[int, dict[str, int]]:
    categories_dictionary = {x.id: x.category for x in products}
    categories_by_user = {}
    for k, v in grouped_cart_items.items():
        categories_by_user[k] = {}
        for cart_item in v:
            if categories_dictionary[cart_item.productId] not in categories_by_user[k]:
                categories_by_user[k][categories_dictionary[cart_item.productId]] = 0
            categories_by_user[k][categories_dictionary[cart_item.productId]] += cart_item.quantity
    return categories_by_user


def _find_all_max_values(source: dict[str, int]) -> (int, list[str]):
    if not dict:
        return 0, []
    max_value = max(source.values())
    return max_value, [k for k, v in source.items() if v == max_value]


def _create_resulting_dataset(users: list[User], categories: dict[int, (int, list[str])]) \
        -> ResultingDataset:
    column_names = ['firstName', 'lastName', 'country', 'birthDate', 'height', 'categories', 'categoriesTimes']
    rows = [(
        x.first_name,
        x.last_name,
        x.country,
        x.birth_date,
        x.height,
        categories.get(x.id, (0, []))[1],
        categories.get(x.id, (0, []))[0]
    ) for x in users]
    result_dicts = [{column: value for column, value in zip(column_names, row)} for row in rows]
    return [UserCategoryData(**x) for x in result_dicts]
