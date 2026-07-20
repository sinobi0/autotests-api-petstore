from http import HTTPStatus

import pytest

from clients.store.store_client import StoreClient
from clients.store.store_schema import OrderSchema
from fixtures.store import StoreFixture
from tools.assertions.base import assert_status_code
from tools.assertions.store import assert_order_response
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

