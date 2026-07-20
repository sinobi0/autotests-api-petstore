import pytest
from pydantic import BaseModel

from clients.store.store_client import StoreClient, get_store_client
from clients.store.store_schema import CreateOrderRequestSchema, CreateOrderResponseSchema


class StoreFixture(BaseModel):
    request: CreateOrderRequestSchema
    response: CreateOrderResponseSchema


@pytest.fixture
def store_client() -> StoreClient:
    return get_store_client()


@pytest.fixture
def function_create_order(store_client):
    request = CreateOrderRequestSchema()
    response = store_client.create_order_api(request)
    response_data = CreateOrderResponseSchema.model_validate_json(response.text)
    return StoreFixture(
        request=request,
        response=response_data
    )
