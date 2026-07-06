import pytest
from pydantic import BaseModel

from clients.user.user_client import get_user_client, UserClient
from clients.user.user_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema


@pytest.fixture
def user_client() -> UserClient:
    return get_user_client()


@pytest.fixture
def function_create_user(user_client: UserClient):
    request = CreateUserRequestSchema()
    response = user_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    return UserFixture(
        request=request,
        response=response_data
    )
