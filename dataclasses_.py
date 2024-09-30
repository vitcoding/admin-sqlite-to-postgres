from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import UUID

from dateutil.parser import parse


class PostInitMixin:
    def __post_init__(self):
        for item in self.__dict__:
            if item.endswith("id") and isinstance(self.__dict__[item], str):
                self.__dict__[item] = UUID(self.__dict__[item])
            if item.endswith("at") and isinstance(self.__dict__[item], str):
                self.__dict__[item] = parse(self.__dict__[item])
            if item.endswith("_date") and isinstance(self.__dict__[item], str):
                self.__dict__[item] = parse(self.__dict__[item])


@dataclass
class Genre(PostInitMixin):
    id: UUID
    name: str
    description: str
    created_at: datetime
    updated_at: datetime


@dataclass
class Person(PostInitMixin):
    id: UUID
    full_name: str
    created_at: datetime
    updated_at: datetime


@dataclass
class Filmwork(PostInitMixin):
    id: UUID
    title: str
    description: str
    creation_date: date
    file_path: str
    rating: float
    type: str
    created_at: datetime
    updated_at: datetime


@dataclass
class GenreFilmwork(PostInitMixin):
    id: UUID
    film_work_id: UUID
    genre_id: UUID
    created_at: datetime


@dataclass
class PersonFilmwork(PostInitMixin):
    id: UUID
    film_work_id: UUID
    person_id: UUID
    role: str
    created_at: datetime


if __name__ == "__main__":
    person = PersonFilmwork(
        id="73d0f092-06ed-48d5-bb02-8da8933fbfe2",
        film_work_id="83af8d01-580a-462e-8c96-2171385935cc",
        person_id="97568425-6959-4b86-b81d-d3198eabfdac",
        role="writer",
        created_at="2021-06-16 20:14:09.93471+00",
    )

    filmwork = Filmwork(
        id="fd78a0e5-d4ec-435e-8994-4ccbdfc4e60b",
        title="Lone Star Restoration",
        description='Brent Hull is a man on a mission to "quit building crap and build more beautiful things." Along with his faithful dog Romeo, Brent and his team from Hull Historical are saving America\'s architectural history one project at time.',
        # creation_date=None,
        creation_date="2021-6-16",
        file_path=None,
        type="movie",
        rating=8.7,
        created_at="2021-6-16 20:14:09.269541+00",
        updated_at="2021-6-16 20:14:09.269557+00",
    )

    print(person)
    print()
    # print(person.__dict__)

    print(filmwork)
    print()
    # print(person.__dict__)
