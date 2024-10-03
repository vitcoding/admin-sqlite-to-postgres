import sqlite3
from contextlib import closing
from typing import Generator

from config import *
from dataclasses_ import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork


class SQLiteLoader:
    def __init__(
        self,
        sqlite_connection: sqlite3.Connection,
        schema: str = DB_SCHEMA["sqlite"],
        table_data: dict[
            str, Filmwork | Genre | Person | GenreFilmwork | PersonFilmwork
        ] = TABLE_DATA,
        batch_size: int = BATCH_SIZE,
    ) -> None:
        self.sqlite_connection = sqlite_connection
        self.schema = schema
        self.table_data = table_data
        self.batch_size = batch_size

    def load_data(
        self,
        table: str,
    ) -> Generator[tuple[str, list[sqlite3.Row]], None, None]:
        """Метод получения данных из SQLite"""

        self.sqlite_connection.row_factory = sqlite3.Row
        with closing(self.sqlite_connection.cursor()) as sqlite_cursor:
            data_cls = self.table_data[table]
            logger.debug("Запущено получение данных из таблицы '%s'", table)
            sqlite_cursor.execute(
                query := f"SELECT * FROM {self.schema}{table}"
            )
            logger.debug("Сформирован SQL запрос:\n'%s'", query)
            while batch := sqlite_cursor.fetchmany(self.batch_size):
                yield [data_cls(**row) for row in batch]
