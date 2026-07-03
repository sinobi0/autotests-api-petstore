from typing import Any
from jsonschema import validate, FormatChecker, Draft202012Validator
from referencing.jsonschema import DRAFT202012


def validate_json_schema(json_data: Any, schema: dict):
    """
    Проверяет, соответствует ли JSON-объект (json_data) заданной JSON-схеме (schema)
    :param json_data: JSON-данные, которые надо проверить
    :param schema: Ожидаемая JSON-schema
    :return: jsonschema.exceptions.ValidationError: Если json_data не соответствует schema.
    """

    validate(
        instance=json_data,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )