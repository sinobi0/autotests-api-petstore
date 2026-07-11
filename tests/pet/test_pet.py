from http import HTTPStatus

import pytest

from clients.pet.pet_client import PetClient
from clients.pet.pet_schema import GetPetResponseSchema
from fixtures.pet import PetFixture
from tools.assertions.base import assert_status_code
from tools.assertions.pet import assert_pet_response
from tools.assertions.validate_schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.user
class TestPet:

    def test_get_pet_by_id(
            self,
            pet_client: PetClient,
            create_pet: PetFixture,
    ):
        response = pet_client.get_pet_by_id_api(create_pet.request.pet_id)
        response_data = GetPetResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_pet_response(response_data, create_pet.request)
        validate_json_schema(response.json(), response_data.model_json_schema())


