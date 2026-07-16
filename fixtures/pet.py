import pytest
from pydantic import BaseModel

from clients.pet.pet_client import PetClient, get_pet_client
from clients.pet.pet_schema import AddPetRequestSchema, AddPetResponseSchema


class PetFixture(BaseModel):
    request: AddPetRequestSchema
    response: AddPetResponseSchema


@pytest.fixture
def pet_client() -> PetClient:
    return get_pet_client()


@pytest.fixture
def function_create_pet(pet_client):
    request = AddPetRequestSchema()
    response = pet_client.add_new_pet_api(request)
    response_data = AddPetResponseSchema.model_validate_json(response.text)
    return PetFixture(
        request=request,
        response=response_data
    )
