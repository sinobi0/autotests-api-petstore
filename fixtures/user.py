import pytest
from pydantic import BaseModel

from clients.user.user_client import get_user_client, UserClient


class User(BaseModel):
    request: str
    response: str

@pytest.fixture
def user_client() -> UserClient:
    return get_user_client()