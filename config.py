import logging
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

BATCH_SIZE = 700

logging.basicConfig(
    # level=logging.INFO,
    # level=logging.DEBUG,
    level=logging.ERROR,
    format=(
        "#%(levelname)-8s [%(asctime)s] - %(filename)s:"
        "%(lineno)d - %(name)s - %(message)s"
    ),
)


# format = (
#     "#%(levelname)-8s [%(asctime)s] - %(filename)s:"
#     "%(lineno)d - %(name)s - %(message)s"
# )

# formatter = logging.Formatter(fmt=format)

logger = logging.getLogger(__name__)

# stderr_handler = logging.StreamHandler()
# stderr_handler.setFormatter(formatter)
# logger.addHandler(stderr_handler)
