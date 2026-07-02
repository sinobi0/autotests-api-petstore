from clients.user.user_schema import CreateUserResponseSchema
from tools.assertions.base import assert_response


def assert_create_user_response(
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
