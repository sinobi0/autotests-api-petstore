from http import HTTPStatus

import pytest

from clients.user.user_client import UserClient
from clients.user.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, CreateUserListSchema
from tools.assertions.base import assert_status_code
from tools.assertions.user import assert_create_user_response
from tools.assertions.validate_schema import validate_json_schema

@pytest.mark.regression
@pytest.mark.user
class TestUser:

    def test_create_user(self, user_client: UserClient):
        create_user_req = CreateUserRequestSchema()
        response = user_client.create_user_api(create_user_req)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)

        assert_create_user_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_create_list_users(self, user_client: UserClient):

        create_users_req = CreateUserListSchema()
        response = user_client.create_user_list_api(create_users_req)
        print(response.url)
        assert_status_code(response.status_code, HTTPStatus.OK)
