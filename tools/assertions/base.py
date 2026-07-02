from typing import Any


def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус код соответствует ожидаемому
    :param actual: Фактический статус код
    :param expected: Ожидаемый статус код
    :raises AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected: {expected}, Actual: {actual}'
    )

def assert_response(actual: Any, expected: Any, name: str):

    assert actual == expected, (
        f'Incorrect value {name} . '
        f'Expected value: {expected}, Actual value: {actual}'
    )