import pytest

from clients.pet.pet_client import PetClient, get_pet_client


@pytest.fixture
def pet_client() -> PetClient:
    return get_pet_client()
