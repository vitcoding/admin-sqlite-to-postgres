import sqlite3
from contextlib import closing

import psycopg
from psycopg.rows import dict_row

from config import *
from dataclasses_ import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork

# from psycopg import ClientCursor
# from psycopg import connection as _connection
# from dataclasses import astuple, dataclass
# from typing import Generator


def test_transfer(
    sqlite_connection: sqlite3.Connection,
    pg_connection: psycopg.Connection,
    tables: list[str],
):
    """Функция тестирования корректности переноса данных"""

    with closing(sqlite_connection.cursor()) as sqlite_cursor, closing(
        pg_connection.cursor(row_factory=dict_row)
    ) as pg_cursor:

        sqlite_schema = DB_SCHEMA["sqlite"]
        pg_schema = DB_SCHEMA["postgres"]

        for table in tables:
            data_cls = TABLE_DATA[table]

            sqlite_cursor.execute(f"SELECT * FROM {sqlite_schema}{table}")

            while batch := sqlite_cursor.fetchmany(BATCH_SIZE):
                original_table_batch = [data_cls(**dict(row)) for row in batch]
                ids = [row.id for row in original_table_batch]

                pg_cursor.execute(
                    f"SELECT * FROM {pg_schema}{table} WHERE id = ANY(%s)",
                    [ids],
                )
                transferred_table_batch = [
                    data_cls(**row) for row in pg_cursor.fetchall()
                ]

                assert len(original_table_batch) == len(
                    transferred_table_batch
                )
                assert original_table_batch == transferred_table_batch
            logger.debug("Тесты для таблицы '%s' пройдены", table)
