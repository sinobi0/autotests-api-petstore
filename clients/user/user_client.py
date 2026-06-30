from httpx import Response

from clients.public_http_builder import get_public_http_client
from tools.routs import APIEndpoints
from clients.api_client import APIClient
from clients.user.user_schema import LoginUserSchema, CreateUserListApi, CreateUserRequestSchema


class UserClient(APIClient):

    def get_user_by_name_api(self, user_name: str):
        """
        Получение пользователя по username
        :param user_name: Имя пользователя
        :return: Объект вида httpx.Response
        """
        return self.get(f"{APIEndpoints.USER}/{user_name}")

    def login_user_api(self, query: LoginUserSchema):
        """
        Запрос логина пользователя в систему
        :param query: Объект с данными: username, password
        :return: Объект вида httpx.Response
        """
        return self.get(f"{APIEndpoints.USER}/login/", params=query.model_dump(by_alias=True))

    def logout_user_api(self):
        """
        Запрос для выхода пользователя из системы
        :return: Объект вида httpx.Response
        """
        return self.get(f"{APIEndpoints.USER}/logout/")

    def create_user_api(self, request: CreateUserRequestSchema):
        """
        Запрос на создание пользователя
        :param request: Объект с данными: user_id, user_name, first_name, last_name,
        user_email, user_password, user_phone, user_status
        :return: Объект вида httpx.Response
        """
        return self.post(APIEndpoints.USER, json=request.model_dump(by_alias=True))

    def create_user_list_api(self, request: CreateUserListApi):
        """
        Запрос создания пользователя из переданного списка
        :param request: Список с объектами с данными: user_id, user_name, first_name, last_name,
        user_email, user_password, user_phone, user_status
        :return: Объект вида httpx.Response
        """
        return self.post(f"{APIEndpoints.USER}/createWithList", json=request.model_dump(by_alias=True))

    def create_user_array_api(self, request: CreateUserListApi):
        """
        Запрос создания пользователя из переданного списка
        :param request: Список с объектами с данными: user_id, user_name, first_name, last_name,
        user_email, user_password, user_phone, user_status
        :return: Объект вида httpx.Response
        """
        return self.post(f"{APIEndpoints.USER}/createWithList", json=request.model_dump(by_alias=True))

    def change_user_by_name_api(self, user_name: str, request: CreateUserRequestSchema):
        """
        Запрос изменения пользователя
        :param user_name: Имя пользователя
        :param request: Объект с данными: user_id, user_name, first_name, last_name,
        user_email, user_password, user_phone, user_status
        :return: Объект вида httpx.Response
        """
        return self.put(f"{APIEndpoints.USER}/{user_name}", json=request.model_dump(by_alias=True))

    def delete_user_by_name_api(self, user_name: str):
        """
        Запрос удаления пользователя
        :param user_name: Имя пользователя
        :return: Объект вида httpx.Response
        """
        return self.delete(f"{APIEndpoints.USER}/{user_name}")


def get_user_client() -> UserClient:
    """
    Функция создает уже настроенный клиент
    :return: Возвращается готовый к использованию UserClient
    """
    return UserClient(client=get_public_http_client())
