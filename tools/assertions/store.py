from pydantic import BaseModel

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

