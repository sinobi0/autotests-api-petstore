from pydantic import BaseModel

from clients.pet.pet_schema import PetSchema, AddPetResponseSchema, GetPetListResponseSchema, AddPetRequestSchema
from tools.assertions.base import assert_response, assert_length


def assert_pet_response(actual: PetSchema, expected: BaseModel):
    assert_length(actual.tags, expected.tags, "tags")
    assert_length(actual.photo_urls, expected.photo_urls, "photo_urls")

    assert_response(actual.pet_id, expected.pet_id, "pet_id")
    assert_response(actual.category.category_id, expected.category.category_id, "category_id")
    assert_response(actual.category.category_name, expected.category.category_name, "category_name")
    assert_response(actual.pet_name, expected.pet_name, "pet_name")
    assert_response(actual.pet_status, expected.pet_status, "pet_status")

    for index, actual_tag in enumerate(actual.tags):
        expected_tag = expected.tags[index]

        assert_response(actual_tag.tag_id, expected_tag.tag_id, f"tags[{index}].tag_id")
        assert_response(actual_tag.tag_name, expected_tag.tag_name, f"tags[{index}].tag_name")

    for index, actual_url in enumerate(actual.photo_urls):
        expected_url = expected.photo_urls[index]
        assert_response(actual_url, expected_url, "url")

def assert_get_pets_by_status_response(actual: GetPetListResponseSchema, expected: AddPetRequestSchema):

    for actual_pet in actual.root:

        assert_response(actual_pet.pet_status, expected.pet_status, "pet_status")

        if actual_pet.pet_name == expected.pet_name:
            assert_pet_response(actual_pet, expected)