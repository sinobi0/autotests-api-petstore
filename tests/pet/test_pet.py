from http import HTTPStatus

import pytest

from clients.pet.pet_client import PetClient
from clients.pet.pet_schema import GetPetByStatusRequestSchema, GetPetListResponseSchema, PetSchema, \
    AddPetRequestSchema, UpdatePetRequestSchema, UpdatePetInStoreRequestSchema, UpdatePetInStoreResponseSchema
from fixtures.pet import PetFixture
from tools.assertions.base import assert_status_code
from tools.assertions.pet import assert_pet_response, assert_get_pets_by_status_response, assert_pet_response_default, \
    prepare_updated_pet
from tools.assertions.validate_schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.pet
class TestPet:

    def test_get_pet_by_id(
            self,
            pet_client: PetClient,
            create_pet: PetFixture,
    ):
        response = pet_client.get_pet_by_id_api(create_pet.request.pet_id)
        response_data = PetSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_pet_response(response_data, create_pet.request)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_pet_by_status(
            self,
            pet_client: PetClient,
            create_pet: PetFixture
    ):
        request = GetPetByStatusRequestSchema(status=create_pet.request.pet_status)
        response = pet_client.get_pet_by_status_api(request)
        response_data = GetPetListResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_pets_by_status_response(response_data, create_pet.request)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_add_new_pet(self, pet_client: PetClient):

        request_add_pet = AddPetRequestSchema()
        response_add_pet = pet_client.add_new_pet_api(request_add_pet)
        response_add_pet_data = PetSchema.model_validate_json(response_add_pet.text)

        assert_status_code(response_add_pet.status_code, HTTPStatus.OK)
        assert_pet_response(response_add_pet_data, request_add_pet)

        response_get_pet_by_id = pet_client.get_pet_by_id_api(request_add_pet.pet_id)
        response_get_pet_by_id_data = PetSchema.model_validate_json(response_get_pet_by_id.text)
        assert_status_code(response_get_pet_by_id.status_code, HTTPStatus.OK)
        assert_pet_response(response_get_pet_by_id_data, request_add_pet)

    def test_update_pet_in_store(
            self,
            pet_client: PetClient,
            create_pet: PetFixture
    ):
        request_update_pet = UpdatePetInStoreRequestSchema()
        response_update_pet = pet_client.update_pet_in_store_api(request_update_pet, create_pet.request.pet_id)
        response_update_pet_data = UpdatePetInStoreResponseSchema.model_validate_json(response_update_pet.text)

        #1.Полностью копируем объект запроса фикстуры на создание животного
        #2. Обновляем имя старое на новое

        expected_pet = prepare_updated_pet(create_pet.request, request_update_pet)

        assert_status_code(response_update_pet.status_code, HTTPStatus.OK)
        assert_pet_response_default(response_update_pet_data)

        response_get_pet_by_id = pet_client.get_pet_by_id_api(create_pet.request.pet_id)
        response_get_pet_by_id_data = PetSchema.model_validate_json(response_get_pet_by_id.text)

        assert_status_code(response_get_pet_by_id.status_code, HTTPStatus.OK)
        assert_pet_response(response_get_pet_by_id_data, expected_pet)
