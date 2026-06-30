from typing import Any
from httpx import Client, URL, QueryParams, Response
from httpx._types import RequestData, RequestFiles
from clients.public_http_builder import get_public_http_client


class APIClient:

    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Функция выполняет get запрос на получение данных и возвращает Response
        :param url: URL ресурса
        :param params: параметры GET запроса (например: ?key=value)
        :return: возвращается объект Response с данными ответа
        """

        return self.client.get(url, params=params)

    def post(
            self,
            url: URL | str,
            json: Any | None,
            data: RequestData | None = None,
            files: RequestFiles | None = None,
    ) -> Response:
        """
        Функция выполняет get запрос создания ресурса и возвращает Response
        :param url: URL ресурса
        :param json: Данные, передаваемые в формате json
        :param data: Данные передаваемые в формате application/x-www-form-urlencoded
        :param files: Файлы для загрузки на сервер
        :return: возвращается объект Response с данными ответа
        """

        return self.client.post(url, json=json, data=data, files=files)

    def put(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Функция выполняет put запрос на полное обновление ресурса и возвращает Response
        :param url: URL ресурса
        :param json: Данные, передаваемые в формате json
        :return: возвращается объект Response с данными ответа
        """
        return self.client.put(url, json=json)

    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Функция выполняет patch запрос на частичное обновление ресурса и возвращает Response
        :param url: URL ресурса
        :param json: Данные, передаваемые в формате json
        :return: возвращается объект Response с данными ответа
        """
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str):
        """
        Функция выполняет delete запрос на удаление ресурса и возвращает Response
        :param url: URL ресурса
        :param json: Данные, передаваемые в формате json
        :return: возвращается объект Response с данными ответа
        """
        return self.client.delete(url)
