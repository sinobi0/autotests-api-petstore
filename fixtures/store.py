import pytest

from clients.store.store_client import StoreClient, get_store_client


@pytest.fixture
def store_client() -> StoreClient:
    return get_store_client()