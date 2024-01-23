import cartApi
import userApi
import productApi
import userCategoryMapper
from csvWriter import save_dataset_to_csv
from sqliteWriter import save_dataset_to_db


def main():
    users = userApi.get_users()
    products = productApi.get_products()
    carts = cartApi.get_carts()
    resulting_dataset = userCategoryMapper.map_users_to_most_common_categories(users, products, carts)
    print(*resulting_dataset)
    save_dataset_to_csv(resulting_dataset, 'result.csv')
    save_dataset_to_db('testing.db', resulting_dataset)


if __name__ == '__main__':
    main()
