from http import HTTPStatus

import pytest
from clients.store.store_client import StoreClient
from clients.store.store_schema import OrderSchema, CreateOrderRequestSchema, GetInventoryResponseSchema, \
    DeleteOrderResponseSchema
from fixtures.store import StoreFixture
from tools.assertions.base import assert_status_code
from tools.assertions.store import assert_order_response, assert_delete_pet_response
from tools.assertions.validate_schema import validate_json_schema


@pytest.mark.store
@pytest.mark.regression
class TestStore:

    def test_get_order_by_id(
            self,
            store_client: StoreClient,
            function_create_order: StoreFixture
    ):
        response_get_order = store_client.get_order_by_id_api(function_create_order.request.order_id)
        response_get_order_data = OrderSchema.model_validate_json(response_get_order.text)

        assert_status_code(response_get_order.status_code, HTTPStatus.OK)
        assert_order_response(response_get_order_data, function_create_order.request)
        validate_json_schema(response_get_order.json(), response_get_order_data.model_json_schema())

    def test_place_order(
            self,
            store_client: StoreClient,
    ):
        request_create_order = CreateOrderRequestSchema()
        response_create_order = store_client.create_order_api(request_create_order)
        response_create_order_data = OrderSchema.model_validate_json(response_create_order.text)

        assert_status_code(response_create_order.status_code, HTTPStatus.OK)
        assert_order_response(response_create_order_data, request_create_order)

        response_get_order = store_client.get_order_by_id_api(request_create_order.order_id)
        response_get_order_data = OrderSchema.model_validate_json(response_get_order.text)
        assert_order_response(response_get_order_data, request_create_order)

        validate_json_schema(response_get_order.json(), response_create_order_data.model_json_schema())

    def test_get_store_inventory(
            self,
            store_client: StoreClient,
    ):
        response_get_inventory = store_client.get_inventory_api()
        response_get_inventory_data = GetInventoryResponseSchema.model_validate_json(response_get_inventory.text)

        assert_status_code(response_get_inventory.status_code, HTTPStatus.OK)
        validate_json_schema(response_get_inventory.json(), response_get_inventory_data.model_json_schema())

    def test_delete_order(
            self,
            store_client: StoreClient,
            function_create_order: StoreFixture,
    ):
        response_delete_order = store_client.delete_order_api(function_create_order.request.order_id)
        response_delete_order_data = DeleteOrderResponseSchema.model_validate_json(response_delete_order.text)

        assert_status_code(response_delete_order.status_code, HTTPStatus.OK)
        assert_delete_pet_response(response_delete_order_data)

        response_get_order = store_client.get_order_by_id_api(function_create_order.request.order_id)
        response_get_order_data = DeleteOrderResponseSchema.model_validate_json(response_get_order.text)
        assert_status_code(response_get_order.status_code, HTTPStatus.NOT_FOUND)

        validate_json_schema(response_delete_order.json(), response_delete_order_data.model_json_schema())
