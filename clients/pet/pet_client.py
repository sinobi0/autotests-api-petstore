from httpx import Response

from clients.api_client import APIClient
from clients.pet.pet_schema import GetPetByStatusSchema, AddPetRequestSchema, UploadNewPetRequestSchema, \
    UpdatePetRequestSchema, UpdatePetInStoreRequestSchema


class PetClient(APIClient):
    """
    Клиент для работы с /v2/pet
    """

    def get_pet_by_status_api(self, query: GetPetByStatusSchema) -> Response:
        """
        Получение pets по status
        :param query: словарь со status
        :return: Ответ в виде объекта httpx.Response
        """
        return self.get("/v2/pet", params=query.model_dump(by_alias=True))

    def get_pet_by_id_api(self, pet_id: int) -> Response:
        """
        Получение pet по id
        :param pet_id: Идентификатор pet_id
        :return: Ответ в виде объекта httpx.Response
        """

        return self.get(f"/v2/pet/{pet_id}")

    def add_new_pet_api(self, request: AddPetRequestSchema):
        """
        Добавление нового pet в store
        :param request: Словарь с данными id, category, name,
        photo_urls, tags, status
        :return: Ответ в виде объекта httpx.Response
        """
        return self.post("/v2/pet", json=request.model_dump(by_alias=True))

    def upload_new_pet_by_id_api(self, pet_id: int, request: UploadNewPetRequestSchema) -> Response:
        """
        Добавление нового файла нового pet в store
        :param request: Словарь с данными pet_id, additional_metadata, file
        :param pet_id: Идентификатор pet_id
        :return: Ответ в виде объекта httpx.Response
        """
        return self.post(
            f"/v2/pet/{pet_id}",
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
        return self.put("/v2/pet/", json=request.model_dump(by_alias=True))

    def update_pet_in_store_api(self, request: UpdatePetInStoreRequestSchema) -> Response:
        """
        Обновление формы pet в магазине
        :param request: Словарь с данными pet_id, new_name, new_status
        :return: Ответ в виде объекта httpx.Response
        """
        return self.post("/v2/pet/", data=request.model_dump(by_alias=True), json=None)

    def delete_pet_api(self, pet_id: int) -> Response:
        """
        Удаление pet
        :param pet_id: Идентификатор pet
        :return: Ответ в виде объекта httpx.Response
        """

        return self.delete(f"/v2/pet/{pet_id}")
