# import zoneinfo
from dataclasses import dataclass, field
from datetime import date, datetime  # , tzinfo
from uuid import UUID

from dateutil.parser import parse

# from dateutil.tz import tzutc


# @dataclass
# class ValidateMixin:
#     def __post_init__(self):
#         for key in self.__dict__:
#             value = self.__getattribute__(key)
#             match key:
#                 case "id", "film_work_id", "genre_id", "person_id":
#                     if isinstance(value, str):
#                         value = UUID(value)
#                 case "creation_date":
#                     if isinstance(value, str):
#                         value = parse(value)
#                 case "created_at":
#                     key = "created"
#                     if isinstance(value, str):
#                         value = parse(value)
#                 case "updated_at":
#                     key = "modified"
#                     if isinstance(value, str):
#                         value = parse(value)
#                 case _:
#                     key = key
#                     value = value


@dataclass
class Genre:
    id: UUID
    name: str
    description: str
    created: datetime
    modified: datetime


@dataclass
class Person:
    id: UUID
    full_name: str
    created: datetime
    modified: datetime


@dataclass
class Filmwork:
    id: UUID
    title: str
    description: str
    creation_date: date
    file_path: str
    rating: float
    type: str
    created: datetime
    modified: datetime


@dataclass
class GenreFilmwork:
    id: UUID
    film_work_id: UUID
    genre_id: UUID
    created: datetime


@dataclass
class PersonFilmwork:
    id: UUID
    film_work_id: UUID
    person_id: UUID
    role: str
    created: datetime


if __name__ == "__main__":
    person = PersonFilmwork(
        id="73d0f092-06ed-48d5-bb02-8da8933fbfe2",
        film_work_id="83af8d01-580a-462e-8c96-2171385935cc",
        person_id="97568425-6959-4b86-b81d-d3198eabfdac",
        role="writer",
        created="2021-06-16 20:14:09.93471+00",
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
        created="2021-6-16 20:14:09.269541+00",
        modified="2021-6-16 20:14:09.269557+00",
    )

    print(person)
    print()
    # print(person.__dict__)

    print(filmwork)
    print()

    # print(a := datetime(2021, 6, 16, 20, 14, 9, 927616, tzinfo=tzutc()))
    # print(
    #     b := datetime(
    #         2021,
    #         6,
    #         16,
    #         20,
    #         14,
    #         9,
    #         927616,
    #         tzinfo=zoneinfo.ZoneInfo(key="Etc/UTC"),
    #     )
    # )
    # print(a == b)
    # print()
    # print(person.__dict__)
