import os
import sqlite3

import psycopg
from psycopg import ClientCursor
from psycopg import connection as _connection
from psycopg.rows import dict_row


class SQLiteLoader:
    def __init__(self, connection):
        self.connection = connection

    def load_movies(self):
        return None


class PostgresSaver:
    def __init__(self, pg_conn):
        self.pg_conn = pg_conn

    def save_all_data(self, data):
        return None


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    postgres_saver = PostgresSaver(pg_conn)
    sqlite_loader = SQLiteLoader(connection)

    data = sqlite_loader.load_movies()
    postgres_saver.save_all_data(data)


if __name__ == "__main__":
    dsl = {
        "dbname": os.environ.get("DB_NAME"),
        "user": os.environ.get("DB_USER"),
        "password": os.environ.get("DB_PASSWORD"),
        "host": "127.0.0.1",
        "port": 5432,
    }
    with sqlite3.connect("db.sqlite") as sqlite_conn, psycopg.connect(
        **dsl, row_factory=dict_row, cursor_factory=ClientCursor
    ) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
