from http import HTTPStatus

from clients.user.user_client import get_user_client
from clients.user.user_schema import CreateUserRequestSchema


class TestUser:

    def test_create_user(self):
        user_client = get_user_client()
        create_user_req = CreateUserRequestSchema()
        response = user_client.create_user_api(create_user_req)

        assert response.status_code == HTTPStatus.OK
