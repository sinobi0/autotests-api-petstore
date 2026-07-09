from http import HTTPStatus

import pytest

from clients.user.user_client import UserClient
from clients.user.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, CreateUserListRequestSchema, \
    CreateUserListResponseSchema, UpdateUserResponseSchema, GetUserResponseSchema, UpdateUserRequestSchema, \
    DeleteUserResponseSchema
from fixtures.user import UserFixture, user_client
from tools.assertions.base import assert_status_code
from tools.assertions.user import assert_user_response, assert_get_user_response
from tools.assertions.validate_schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.user
class TestUser:

    def test_create_user(self, user_client: UserClient):
        create_user_req = CreateUserRequestSchema()

        create_user_response = user_client.create_user_api(create_user_req)
        create_user_response_data = CreateUserResponseSchema.model_validate_json(create_user_response.text)

        assert_status_code(create_user_response.status_code, HTTPStatus.OK)
        validate_json_schema(create_user_response.json(), create_user_response_data.model_json_schema())
        assert_user_response(create_user_response_data)

        get_user_response = user_client.get_user_by_name_api(create_user_req.user_name)
        get_user_response_data = GetUserResponseSchema.model_validate_json(get_user_response.text)

        assert_status_code(get_user_response.status_code, HTTPStatus.OK)
        assert_get_user_response(get_user_response_data, create_user_req)

    @pytest.mark.parametrize("api_method_name", [
        "create_user_list_api",
        "create_user_array_api"
    ])
    def test_create_multiple_users(self, user_client: UserClient, api_method_name: str):
        create_users_req = CreateUserListRequestSchema()

        api_method = getattr(user_client, api_method_name)
        response = api_method(create_users_req)
        response_data = CreateUserListResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_user_response(response_data)

        for users_data in create_users_req.root:
            get_user_response = user_client.get_user_by_name_api(users_data.user_name)
            get_user_response_data = GetUserResponseSchema.model_validate_json(get_user_response.text)

            assert_status_code(get_user_response.status_code, HTTPStatus.OK)
            assert_get_user_response(get_user_response_data, users_data)

    def test_get_user_by_username(
            self,
            user_client: UserClient,
            function_create_user: UserFixture
    ):
        response = user_client.get_user_by_name_api(function_create_user.request.user_name)
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_get_user_response(response_data, function_create_user.request)

    def test_update_user_data(
            self,
            user_client: UserClient,
            function_create_user: UserFixture
    ):
        request_update_user = UpdateUserRequestSchema()

        response_update_user = user_client.update_user_by_name_api(function_create_user.request.user_name,
                                                                   request_update_user)
        response_user_data = UpdateUserResponseSchema.model_validate_json(response_update_user.text)

        assert_status_code(response_update_user.status_code, HTTPStatus.OK)
        validate_json_schema(response_update_user.json(), response_user_data.model_json_schema())
        assert_user_response(response_user_data)

        response_get_user = user_client.get_user_by_name_api(function_create_user.request.user_name)
        response_get_user_data = GetUserResponseSchema.model_validate_json(response_get_user.text)

        assert_status_code(response_get_user.status_code, HTTPStatus.OK)
        assert_get_user_response(response_get_user_data, function_create_user.request)

    def test_delete_user_by_username(
            self,
            user_client: UserClient,
            function_create_user: UserFixture
    ):
        response = user_client.delete_user_by_name_api(function_create_user.request.user_name)
        response_data = DeleteUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_user_response(response_data)

        get_user_response = user_client.get_user_by_name_api(function_create_user.request.user_name)

        assert_status_code(get_user_response.status_code, HTTPStatus.NOT_FOUND)
