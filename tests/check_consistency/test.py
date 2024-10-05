import sqlite3
from contextlib import closing
from typing import Iterable

import psycopg
from psycopg import ClientCursor
from psycopg.rows import dict_row

from config import *
from validate import validate_data

# from time import perf_counter
# from dataclasses_ import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork

# import zoneinfo
# from psycopg import ClientCursor
# from psycopg import connection as _connection
# from dataclasses import astuple, dataclass
# from dateutil.tz import tzutc


def test_transfer(
    sqlite_connection: sqlite3.Connection,
    pg_connection: psycopg.Connection,
    tables: Iterable[str],
):
    """Функция тестирования корректности переноса данных"""

    with closing(sqlite_connection.cursor()) as sqlite_cursor, closing(
        pg_connection.cursor(row_factory=dict_row)
    ) as pg_cursor:
        # sqlite_connection.row_factory = sqlite3.Row
        sqlite_schema = DB_SCHEMA["sqlite"]
        pg_schema = DB_SCHEMA["postgres"]

        for table in tables:
            # for table in ("film_work",):
            data_cls = TABLE_DATA[table]

            while batch := sqlite_cursor.fetchmany(BATCH_SIZE):
                sqlite_cursor.execute(f"SELECT * FROM {sqlite_schema}{table}")
                original_table_batch = [
                    data_cls(**validate_data(row)) for row in batch
                ]
                logger.debug(
                    "original_table_batch: \n%s\n", original_table_batch
                )

                ids = [row.id for row in original_table_batch]
                # logger.debug("ids: \n%s\n", ids)
                pg_cursor.execute(
                    f"SELECT * FROM {pg_schema}{table} "
                    + "WHERE id = ANY(%s)",
                    (ids,),
                )
                transferred_table_batch = [
                    data_cls(**row) for row in pg_cursor.fetchall()
                ]
                logger.debug(
                    "transferred_table_batch: \n%s\n", transferred_table_batch
                )

                assert len(original_table_batch) == len(
                    transferred_table_batch
                )
                assert original_table_batch == transferred_table_batch

            logger.info("Тесты для таблицы '%s' пройдены", table)


if __name__ == "__main__":
    with closing(sqlite3.connect("db.sqlite")) as sqlite_connection, closing(
        psycopg.connect(
            **dsl, row_factory=dict_row, cursor_factory=ClientCursor
        )
    ) as pg_connection:
        # start_time = perf_counter()

        test_transfer(sqlite_connection, pg_connection, TABLES)

        # end_time = perf_counter()

    # execute_time = end_time - start_time
    # logger.info("\nВремя выполнения тестов: %s", execute_time)
