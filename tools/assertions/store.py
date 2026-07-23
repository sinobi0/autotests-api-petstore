from pydantic import BaseModel

from clients.store.store_schema import DeleteOrderResponseSchema
from tools.assertions.base import assert_response


def assert_order_response(actual: BaseModel, expected: BaseModel):
    """
    Проверяет, что исходный ответ соответствует ожидаемому
    :param actual: Исходный ответ заказа
    :param expected: Ожидаемый ответ
    :raises:AssertionError: если хотя бы одно поле не совпадает
    """

    assert_response(actual.order_id, expected.order_id, "order_id")
    assert_response(actual.pet_id, expected.pet_id, "pet_id")
    assert_response(actual.quantity, expected.quantity, "quantity")
    assert_response(actual.ship_date, expected.ship_date, "ship_date")
    assert_response(actual.complete, expected.complete, "complete")

def assert_delete_pet_response(
        response: DeleteOrderResponseSchema,
        expected_code: int = 200,
        expected_type: str = "unknown",
        expected_message: str | None = None
):
    """
    Проверяет корректность ответа на запрос создания животного
    :param response: Исходный запрос создания живоотного
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