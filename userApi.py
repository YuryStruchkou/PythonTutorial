import requests

import coordinateResolver
from user import User


def get_users() -> list[User]:
    url = 'https://dummyjson.com/users?limit=0'
    users = requests.get(url).json()
    return [_create_user(x) for x in users['users']]


def _create_user(user_json: dict[str, any]) -> User:
    user_id, first_name, last_name = user_json['id'], user_json['firstName'], user_json['lastName']
    birth_date, height = user_json['birthDate'], user_json['height']
    latitude, longitude = user_json['address']['coordinates']['lat'], user_json['address']['coordinates']['lng']
    country = coordinateResolver.resolve(latitude, longitude)['address']['country']
    return User(user_id, first_name, last_name, birth_date, height, country)
