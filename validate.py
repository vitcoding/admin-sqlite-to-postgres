from typing import Any
from uuid import UUID

from dateutil.parser import parse

from config import logger


def validate_data(row: dict[str, Any]) -> dict[str, Any]:
    """функция валидации данных таблиц БД"""

    transformed_row = {}
    for key, value in dict(row).items():
        match key:
            case "id", "film_work_id", "genre_id", "person_id":
                if isinstance(value, str):
                    value = UUID(value)
            case "creation_date":
                if isinstance(value, str):
                    value = parse(value)
            case "created_at":
                key = "created"
                if isinstance(value, str):
                    value = parse(value)
            case "updated_at":
                key = "modified"
                if isinstance(value, str):
                    value = parse(value)
            case _:
                key = key
                value = value

        transformed_row[key] = value
    logger.debug("Валидированные данные:\n'%s'", transformed_row)
    return transformed_row


# Без переименования столбцов можно использовать в __post_init__.
# def validate_data_temp(key: str, value: Any) -> tuple[str, Any]:
#     """функция валидации данных таблиц БД"""

#     match key:
#         case "id", "film_work_id", "genre_id", "person_id":
#             if isinstance(value, str):
#                 value = UUID(value)
#         case "creation_date":
#             if isinstance(value, str):
#                 value = parse(value)
#         case "created_at":
#             key = "created"
#             if isinstance(value, str):
#                 value = parse(value)
#         case "updated_at":
#             key = "modified"
#             if isinstance(value, str):
#                 value = parse(value)
#         case _:
#             key = key
#             value = value

#     return key, value
