from typing import Any, Sized


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
    """
    Проверяет, что фактический ответ равен ожидаемому
    :param actual: Исходный ответ от API
    :param expected: Ожидаемвй ответ от API
    :param name: Наименование параметра
    :raises:AssertionError: Если хотя бы один параметр некорректен
    """
    assert actual == expected, (
        f'Incorrect value {name} . '
        f'Expected value: {expected}, Actual value: {actual}'
    )

def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины переданных объектов совпадают
    :param actual: Фактический объект
    :param expected: Ожидаемый объект
    :param name: Наименование проверяемого параметра
    :raises: AssertionError: Если длины не совпадают
    """
    assert len(actual) == len(expected), (
        f'Incorrect object length {name} . '
        f'Expected length: {len(expected)}, Actual: {len(actual)}'
    )