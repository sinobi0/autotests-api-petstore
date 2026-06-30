from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.store.store_schema import OrderSchema, CreateOrderRequestSchema
from tools.routs import APIEndpoints


class StoreClient(APIClient):

    def get_inventory_api(self) -> Response:
        """
        Получение объекта с информацией о товарах о животных по статусу
        :return: Объект вида httpx.Response
        """
        return self.get(f"{APIEndpoints.STORE}/inventory")

    def get_order_by_id_api(self, order_id: int) -> Response:
        """
        Получение заказа по его номеру
        :param order_id: Номер заказа с типом int
        :return: Объект вида httpx.Response
        """
        return self.get(f"{APIEndpoints.STORE}/order/{order_id}")

    def create_order_api(self, request: CreateOrderRequestSchema) -> Response:
        """
        Создание заказа по животному
        :param request: Объект с параметрами: order_id, pet_id, quantity,
        ship_date, completed_date
        :return: Объект вида httpx.Response
        """
        return self.post(f"{APIEndpoints.STORE}/order", json=request.model_dump(by_alias=True))

    def delete_order_api(self, order_id: int) -> Response:
        """
        Удаление заказа
        :param order_id: Номер заказа с типом int
        :return: Объект вида httpx.Response
        """
        return self.delete(f"{APIEndpoints.STORE}/order/{order_id}")


def get_store_client() -> StoreClient:
    """
    Функция создаёт экземпляр StoreClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию StoreClient.
    """
    return StoreClient(client=get_public_http_client())
