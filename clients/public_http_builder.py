from functools import lru_cache

from httpx import Client
from config import settings

@lru_cache(maxsize=None)  # Кешируем возвращаемое значение
def get_public_http_client() -> Client:
    """
    :return: Функция возвращает готовый базовый httpx client
    """

    return Client(
        base_url=settings.http_client.client_url,
        timeout=settings.http_client.timeout,
    )
