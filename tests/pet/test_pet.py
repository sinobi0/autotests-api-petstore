from http import HTTPStatus

import pytest

from clients.pet.pet_client import PetClient
from clients.pet.pet_schema import GetPetByStatusRequestSchema, GetPetListResponseSchema, PetSchema, \
    AddPetRequestSchema, UpdatePetRequestSchema, UpdatePetInStoreRequestSchema, UpdatePetInStoreResponseSchema, \
    UploadImagePetResponseSchema, UploadImagePetRequestSchema, DeletePetResponseSchema
from config import settings
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
            function_create_pet: PetFixture,
    ):
        response = pet_client.get_pet_by_id_api(function_create_pet.request.pet_id)
        response_data = PetSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_pet_response(response_data, function_create_pet.request)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_pet_by_status(
            self,
            pet_client: PetClient,
            function_create_pet: PetFixture
    ):
        request = GetPetByStatusRequestSchema(status=function_create_pet.request.pet_status)
        response = pet_client.get_pet_by_status_api(request)
        response_data = GetPetListResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_pets_by_status_response(response_data, function_create_pet.request)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_add_new_pet(self, pet_client: PetClient):

        request_add_pet = AddPetRequestSchema()
        response_add_pet = pet_client.add_new_pet_api(request_add_pet)
        response_add_pet_data = PetSchema.model_validate_json(response_add_pet.text)

        assert_status_code(response_add_pet.status_code, HTTPStatus.OK)
        assert_pet_response(response_add_pet_data, request_add_pet)
        validate_json_schema(response_add_pet.json(), response_add_pet_data.model_json_schema())

        response_get_pet_by_id = pet_client.get_pet_by_id_api(request_add_pet.pet_id)
        response_get_pet_by_id_data = PetSchema.model_validate_json(response_get_pet_by_id.text)
        assert_status_code(response_get_pet_by_id.status_code, HTTPStatus.OK)
        assert_pet_response(response_get_pet_by_id_data, request_add_pet)

    def test_update_pet_in_store(
            self,
            pet_client: PetClient,
            function_create_pet: PetFixture
    ):
        request_update_pet = UpdatePetInStoreRequestSchema()
        response_update_pet = pet_client.update_pet_in_store_api(request_update_pet, function_create_pet.request.pet_id)
        response_update_pet_data = UpdatePetInStoreResponseSchema.model_validate_json(response_update_pet.text)

        #1.Полностью копируем объект запроса фикстуры на создание животного
        #2. Обновляем имя старое на новое

        expected_pet = prepare_updated_pet(function_create_pet.request, request_update_pet)

        assert_status_code(response_update_pet.status_code, HTTPStatus.OK)
        assert_pet_response_default(response_update_pet_data)
        validate_json_schema(response_update_pet.json(), response_update_pet_data.model_json_schema())

        response_get_pet_by_id = pet_client.get_pet_by_id_api(function_create_pet.request.pet_id)
        response_get_pet_by_id_data = PetSchema.model_validate_json(response_get_pet_by_id.text)

        assert_status_code(response_get_pet_by_id.status_code, HTTPStatus.OK)
        assert_pet_response(response_get_pet_by_id_data, expected_pet)

    def test_upload_pet_image(
            self,
            pet_client: PetClient,
            function_create_pet: PetFixture
    ):
        request_upload_image = UploadImagePetRequestSchema(file=settings.test_data.image_file)
        response_upload_file = pet_client.upload_image_pet_by_id_api(function_create_pet.request.pet_id, request_upload_image)
        response_upload_file_data = UploadImagePetResponseSchema.model_validate_json(response_upload_file.text)

        assert_status_code(response_upload_file.status_code, HTTPStatus.OK)
        assert_pet_response_default(response_upload_file_data)
        validate_json_schema(response_upload_file.json(), response_upload_file_data.model_json_schema())

    def test_delete_pet_from_store(
            self,
            function_create_pet: PetFixture,
            pet_client: PetClient
    ):
        response_delete_pet = pet_client.delete_pet_api(function_create_pet.request.pet_id)
        response_delete_pet_data = DeletePetResponseSchema.model_validate_json(response_delete_pet.text)

        assert_status_code(response_delete_pet.status_code, HTTPStatus.OK)
        assert_pet_response_default(response_delete_pet_data)
        validate_json_schema(response_delete_pet.json(), response_delete_pet_data.model_json_schema())

        response_get_pet = pet_client.get_pet_by_id_api(function_create_pet.request.pet_id)
        assert_status_code(response_get_pet.status_code, HTTPStatus.NOT_FOUND)


