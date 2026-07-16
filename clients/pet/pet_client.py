from httpx import Response
from tools.routs import APIEndpoints
from clients.api_client import APIClient
from clients.pet.pet_schema import GetPetByStatusRequestSchema, AddPetRequestSchema, \
    UpdatePetRequestSchema, UpdatePetInStoreRequestSchema, UploadImagePetRequestSchema
from clients.public_http_builder import get_public_http_client


class PetClient(APIClient):
    """
    Клиент для работы с /v2/pet
    """

    def get_pet_by_status_api(self, query: GetPetByStatusRequestSchema) -> Response:
        """
        Получение pets по status
        :param query: словарь со status
        :return: Ответ в виде объекта httpx.Response
        """
        return self.get(f"{APIEndpoints.PET}/findByStatus", params=query.model_dump(by_alias=True))

    def get_pet_by_id_api(self, pet_id: int) -> Response:
        """
        Получение pet по id
        :param pet_id: Идентификатор pet_id
        :return: Ответ в виде объекта httpx.Response
        """

        return self.get(f"{APIEndpoints.PET}/{pet_id}")

    def add_new_pet_api(self, request: AddPetRequestSchema):
        """
        Добавление нового pet в store
        :param request: Словарь с данными id, category, name,
        photo_urls, tags, status
        :return: Ответ в виде объекта httpx.Response
        """
        return self.post(APIEndpoints.PET, json=request.model_dump(by_alias=True))

    def upload_image_pet_by_id_api(self, pet_id: int, request: UploadImagePetRequestSchema) -> Response:
        """
        Добавление нового файла нового pet в store
        :param request: Словарь с данными pet_id, additional_metadata, file
        :param pet_id: Идентификатор pet_id
        :return: Ответ в виде объекта httpx.Response
        """
        return self.post(
            f"{APIEndpoints.PET}/{pet_id}/uploadImage",
            data=request.model_dump(by_alias=True, exclude={"file"}),
            files={"file": request.file.read_bytes()},
            json=None
        )

    def update_pet_api(self, request: UpdatePetRequestSchema) -> Response:
        """
        Обновление существующего pet
        :param request: Словарь с данными id, category, name,
        photo_urls, tags, status
        :return: Ответ в виде объекта httpx.Response
        """
        return self.put(APIEndpoints.PET, json=request.model_dump(by_alias=True))

    def update_pet_in_store_api(self, request: UpdatePetInStoreRequestSchema, pet_id: int) -> Response:
        """
        Обновление формы pet в магазине
        :param request: Словарь с данными pet_id, new_name, new_status
        :param pet_id: id животного в магазине
        :return: Ответ в виде объекта httpx.Response
        """
        return self.post(f"{APIEndpoints.PET}/{pet_id}", data=request.model_dump(by_alias=True), json=None)

    def delete_pet_api(self, pet_id: int) -> Response:
        """
        Удаление pet
        :param pet_id: Идентификатор pet
        :return: Ответ в виде объекта httpx.Response
        """

        return self.delete(f"{APIEndpoints.PET}/{pet_id}")


def get_pet_client() -> PetClient:
    """
    Функция создаёт экземпляр PetClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PetClient.
    """
    return PetClient(client=get_public_http_client())
