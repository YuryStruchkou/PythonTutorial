import sqlite3
from sqlite3 import Cursor, Connection

from userCategoryMapper import ResultingDataset


def save_dataset_to_db(database: str, dataset: ResultingDataset):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    _create_db(cursor)
    _insert_rows_to_db(connection, cursor, dataset)
    print(cursor.execute('SELECT * FROM users').fetchall())


def _create_db(cursor: Cursor):
    cursor.execute('DROP TABLE IF EXISTS users')
    cursor.execute('CREATE TABLE IF NOT EXISTS users( \
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        first_name TEXT,\
        last_name TEXT,\
        birth_date TEXT,\
        height INTEGER,\
        country TEXT,\
        categories TEXT,\
        categories_times INTEGER)')


def _insert_rows_to_db(connection: Connection, cursor: Cursor, dataset: ResultingDataset):
    attributes = [
        (
            row.firstName,
            row.lastName,
            row.birthDate,
            row.height,
            row.country,
            ';'.join(row.categories),
            row.categoriesTimes
        ) for row in dataset
    ]
    cursor.executemany(
        'INSERT INTO users( \
        first_name, last_name, birth_date, height, country, categories, categories_times) \
        VALUES(?, ?, ?, ?, ?, ?, ?)', attributes)
    connection.commit()
