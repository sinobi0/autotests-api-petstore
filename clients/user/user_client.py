from httpx import Response

from clients.api_client import APIClient
from clients.user.user_schema import LoginUserSchema, UserSchema, CreateUserListApi


class UserClient(APIClient):

    def get_user_by_name_api(self, user_name: str):
        """
        Получение пользователя по username
        :param user_name: Имя пользователя
        :return: Объект вида httpx.Response
        """
        return self.get(f"/v2/user/{user_name}")

    def login_user_api(self, query: LoginUserSchema):
        """
        Запрос логина пользователя в систему
        :param query: Объект с данными: username, password
        :return: Объект вида httpx.Response
        """
        return self.get("/v2/user/login/", params=query.model_dump(by_alias=True))

    def logout_user_api(self):
        """
        Запрос для выхода пользователя из системы
        :return: Объект вида httpx.Response
        """
        return self.get("/v2/user/logout/")

    def create_user_api(self, request: UserSchema):
        """
        Запрос на создание пользователя
        :param request: Объект с данными: user_id, user_name, first_name, last_name,
        user_email, user_password, user_phone, user_status
        :return: Объект вида httpx.Response
        """
        return self.post("/v2/user", json=request.model_dump(by_alias=True))

    def create_user_list_api(self, request: CreateUserListApi):
        """
        Запрос создания пользователя из переданного списка
        :param request: Список с объектами с данными: user_id, user_name, first_name, last_name,
        user_email, user_password, user_phone, user_status
        :return: Объект вида httpx.Response
        """
        return self.post("/v2/user/createWithList", json=request.model_dump(by_alias=True))

    def create_user_array_api(self, request: CreateUserListApi):
        """
        Запрос создания пользователя из переданного списка
        :param request: Список с объектами с данными: user_id, user_name, first_name, last_name,
        user_email, user_password, user_phone, user_status
        :return: Объект вида httpx.Response
        """
        return self.post("/v2/user/createWithList", json=request.model_dump(by_alias=True))

    def change_user_by_name_api(self, user_name: str, request: UserSchema):
        """
        Запрос изменения пользователя
        :param user_name: Имя пользователя
        :param request: Объект с данными: user_id, user_name, first_name, last_name,
        user_email, user_password, user_phone, user_status
        :return: Объект вида httpx.Response
        """
        return self.put(f"/v2/user/{user_name}", json=request.model_dump(by_alias=True))

    def delete_user_by_name_api(self, user_name: str):
        """
        Запрос удаления пользователя
        :param user_name: Имя пользователя
        :return: Объект вида httpx.Response
        """
        return self.delete(f"/v2/user/{user_name}")
