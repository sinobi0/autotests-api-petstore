from http import HTTPStatus

import pytest

from clients.user.user_client import UserClient
from clients.user.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, CreateUserListRequestSchema, \
    CreateUserListResponseSchema, UserSchema
from fixtures.user import UserFixture, user_client
from tools.assertions.base import assert_status_code
from tools.assertions.user import assert_create_user_response, assert_create_users_response, assert_get_user_response
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
        create_users_req = CreateUserListRequestSchema()
        response = user_client.create_user_list_api(create_users_req)
        response_data = CreateUserListResponseSchema.model_validate_json(response.text)

        assert_create_users_response(response_data)
        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_create_array_users(self, user_client: UserClient):
        create_users_req = CreateUserListRequestSchema()
        response = user_client.create_user_array_api(create_users_req)
        response_data = CreateUserListResponseSchema.model_validate_json(response.text)

        assert_create_users_response(response_data)
        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_user_by_username(
            self,
            user_client: UserClient,
            function_create_user: UserFixture
    ):
        response = user_client.get_user_by_name_api(function_create_user.request.user_name)
        response_data = UserSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_create_user.request)
        validate_json_schema(response.json(), response_data.model_json_schema())
