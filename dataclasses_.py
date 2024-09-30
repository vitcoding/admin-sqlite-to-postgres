import uuid
from datetime import date, datetime
from dataclasses import dataclass, field


@dataclass
class Genre:
    id: uuid.UUID
    name: str
    description: str
    created: datetime
    modified: datetime


@dataclass
class Person:
    id: uuid.UUID
    full_name: str
    created: datetime
    modified: datetime


@dataclass
class Filmwork:
    id: uuid.UUID
    title: str
    description: str
    creation_date: date
    file_path: str
    type: str
    created_at: datetime
    updated_at: datetime
    rating: float = field(default=0.0)


@dataclass
class GenreFilmwork:
    id: uuid.UUID
    film_work: uuid.UUID
    genre: uuid.UUID
    created: datetime


@dataclass
class PersonFilmwork:
    id: uuid.UUID
    film_work: uuid.UUID
    person: uuid.UUID
    role: str
    created: datetime
