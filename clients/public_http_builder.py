from httpx import Client
from config import settings


def get_public_http_client() -> Client:
    """
    :return: Функция возвращает готовый базовый httpx client
    """

    return Client(
        base_url=settings.http_client.client_url,
        timeout=settings.http_client.timeout,
    )
