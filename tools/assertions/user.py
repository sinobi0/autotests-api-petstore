from pydantic import BaseModel

from clients.user.user_schema import CreateUserResponseSchema, CreateUserListResponseSchema, UserSchema, \
    CreateUserRequestSchema
from tools.assertions.base import assert_response


def assert_user_response(
        response: CreateUserResponseSchema,
        expected_code: int = 200,
        expected_type: str = "unknown",
        expected_message: str | None = None
):
    """
    Проверяет корректность ответа на запрос создания пользователя
    :param response: Исходный запрос создания пользователя
    :param expected_code: Ожидаемый код
    :param expected_type: Ожидаемый тип
    :param expected_message: Ожидаемое сообщение
    :raises AssertionError: в случае несоответствия данных
    """
    assert_response(response.code, expected_code, "code")
    assert_response(response.type, expected_type, "type")

    assert response.message, "Поле message пустое, ожидалось числовое значение/ID"
    if expected_message is not None:
        assert_response(response.message, expected_message, "response.message")


def assert_get_user_response(actual: BaseModel, expected: BaseModel):
    """
    Проверяет, что ответ на запрос получения пользователя корректен
    :param actual: Исходный ответ на запрос получения пользователя
    :param expected: Ожидаемые данные UserSchema
    :raises AssertionError: В случае не совпадения хотя бы одного из полей
    """
    assert_response(actual.user_id, expected.user_id, "user_id")
    assert_response(actual.user_name, expected.user_name, "user_name")
    assert_response(actual.first_name, expected.first_name, "first_name")
    assert_response(actual.last_name, expected.last_name, "last_name")
    assert_response(actual.user_email, expected.user_email, "user_email")
    assert_response(actual.user_password, expected.user_password, "user_password")
    assert_response(actual.user_phone, expected.user_phone, "user_phone")
    assert_response(actual.user_status, expected.user_status, "user_status")
