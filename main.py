import sqlite3
from contextlib import closing
from time import perf_counter

import psycopg
from psycopg import ClientCursor
from psycopg.rows import dict_row

from config import *
from get_data import SQLiteLoader
from load_data import PostgresSaver
from tests.check_consistency.test import *

# from dataclasses import astuple, dataclass
# from dataclasses_ import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork
# from psycopg import connection as _connection
# from typing import Generator


def load_from_sqlite(
    sqllite_connection: sqlite3.Connection, pg_connection: psycopg.Connection
):
    """Основной метод загрузки данных из SQLite в Postgres"""
    postgres_saver = PostgresSaver(pg_connection)
    sqlite_loader = SQLiteLoader(sqllite_connection)

    data = sqlite_loader.load_data()
    postgres_saver.save_all_data(data)


if __name__ == "__main__":

    with closing(sqlite3.connect("db.sqlite")) as sqlite_connection, closing(
        psycopg.connect(
            **dsl, row_factory=dict_row, cursor_factory=ClientCursor
        )
    ) as pg_connection:
        start_time = perf_counter()
        load_from_sqlite(sqlite_connection, pg_connection)

        test_transfer(sqlite_connection, pg_connection)
        end_time = perf_counter()
        print(f"\nВремя выполнения: {end_time - start_time}")

    print("🎉 Данные успешно перенесены !!!")
