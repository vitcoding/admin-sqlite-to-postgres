import os

from dotenv import load_dotenv

from dataclasses_ import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork

load_dotenv()
dsl = {
    "dbname": os.environ.get("DB_NAME"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
}

TABLES = (
    "film_work",
    "genre",
    "person",
    "genre_film_work",
    "person_film_work",
)

TABLE_DATA = {
    "film_work": Filmwork,
    "genre": Genre,
    "person": Person,
    "genre_film_work": GenreFilmwork,
    "person_film_work": PersonFilmwork,
}

DB_SCHEMA = {
    "postgres": "content.",
    "sqlite": "",
}

BATCH_SIZE = 1_000
