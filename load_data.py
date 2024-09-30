import sqlite3
from contextlib import closing
from dataclasses import astuple
from typing import Generator

import psycopg
from psycopg.rows import dict_row

from config import *
from dataclasses_ import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork
from tests.check_consistency.test import *

# from psycopg import ClientCursor
# from psycopg import connection as _connection


class PostgresSaver:
    def __init__(
        self,
        pg_connection: psycopg.Connection,
        schema: str = DB_SCHEMA["postgres"],
        table_data: dict[
            str, Filmwork | Genre | Person | GenreFilmwork | PersonFilmwork
        ] = TABLE_DATA,
    ):
        self.pg_connection = pg_connection
        self.schema = schema
        self.table_data = table_data
        self._cache = {"table": None, "args_names": None, "args_values": None}

    def get_cache(self, table: str) -> dict[str, str]:
        """Метод, возвращающий данные по обрабатываемой таблице БД"""
        data_cls = self.table_data[table]
        args_tuple = data_cls.__dict__["__match_args__"]
        _cache_dict = {
            "table": table,
            "args_names": ", ".join(args_tuple),
            "args_values": ", ".join(["%s"] * len(args_tuple)),
        }
        return _cache_dict

    def save_all_data(
        self, data: Generator[tuple[str, list[sqlite3.Row]], None, None]
    ):
        """Метод загрузки данных в Postgres"""
        schema = self.schema
        cnt = 0
        with closing(
            self.pg_connection.cursor(row_factory=dict_row)
        ) as pg_cursor:
            for table, batch in data:
                # print(table)

                if self._cache["table"] != table:
                    self._cache.update(**self.get_cache(table))
                    args_names = self._cache["args_names"]
                    args_values = self._cache["args_values"]
                query = f"INSERT INTO {schema}{table} \
                            ({args_names}) \
                            VALUES ({args_values}) \
                            ON CONFLICT (id) DO NOTHING"
                # print(query)
                batch_as_tuples = [astuple(row) for row in batch]
                try:
                    pg_cursor.executemany(query, batch_as_tuples)
                except Exception as e:
                    print(e)
                    print()
                    # pass

                self.pg_connection.commit()
                cnt += 1

        print()
        print(cnt)
        return None
