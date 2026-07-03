from http import HTTPStatus

from clients.user.user_client import UserClient
from clients.user.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema
from tools.assertions.base import assert_status_code
from tools.assertions.user import assert_create_user_response
from tools.assertions.validate_schema import validate_json_schema


class TestUser:

    def test_create_user(self, user_client: UserClient):
        create_user_req = CreateUserRequestSchema()
        response = user_client.create_user_api(create_user_req)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)

        assert_create_user_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())