from pydantic import BaseModel, ConfigDict, Field, FilePath
from unicodedata import category

from tools.fakers import fake


class CategorySchema(BaseModel):
    """
    Описание структуры категории
    """
    model_config = ConfigDict(populate_by_name=True)
    category_id: int = Field(alias="id")
    category_name: str = Field(alias="name")


class TagSchema(BaseModel):
    """
    Описание структуры тега
    """
    model_config = ConfigDict(populate_by_name=True)
    tag_id: int = Field(alias="id")
    tag_name: str = Field(alias="name")


class PetSchema(BaseModel):
    """
    Описание структуры сущности животного
    """
    model_config = ConfigDict(populate_by_name=True)

    pet_id: int = Field(alias="id")
    category: CategorySchema
    pet_name: str = Field(alias="name")
    photo_urls: list = Field(alias="photoUrls")
    tags: list[TagSchema]
    pet_status: str = Field(alias="status")


class GetPetByStatusSchema(BaseModel):
    """
    Описание структуры статуса сущности животного
    """
    model_config = ConfigDict(populate_by_name=True)
    status: str


class AddPetRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание сущности животного
    """
    model_config = ConfigDict(populate_by_name=True)
    pet_id: int = Field(alias="id", default_factory=fake.random_int)
    category: CategorySchema = Field(default_factory=lambda: CategorySchema(
        category_id=fake.random_int,
        category_name=fake.random_word
    ))
    pet_name: str = Field(alias="name", default_factory=fake.random_name)
    photo_urls: list = Field(alias="photoUrls", default_factory=fake.random_photo)
    tags: list[TagSchema] = Field(default_factory=lambda: [TagSchema(
        tag_id=fake.random_int,
        tag_name=fake.random_word
    )])
    pet_status: str = Field(alias="status", default="available")


class UploadNewPetRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление сущности животного
    """
    model_config = ConfigDict(populate_by_name=True)

    pet_id: int = Field(alias="petId", default_factory=fake.random_int)
    category: CategorySchema = Field(default_factory=lambda: CategorySchema(
        category_id=fake.random_int,
        category_name=fake.random_word
    ))
    pet_name: str = Field(alias="name", default_factory=fake.random_name)
    additional_metadata: str = Field(
        alias="additionalMetadata",
        default_factory=fake.random_word
    )
    pet_status: str = Field(alias="status", default="available")
    file: FilePath


class UpdatePetRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление сущности животного
    """
    model_config = ConfigDict(populate_by_name=True)
    pet_id: int = Field(alias="id", default_factory=fake.random_int)
    category: CategorySchema = Field(default_factory=lambda: CategorySchema(
        category_id=fake.random_int,
        category_name=fake.random_word
    ))
    pet_name: str = Field(alias="name", default_factory=fake.random_name)
    photo_urls: list = Field(alias="photoUrls", default_factory=fake.random_photo)
    tags: list[TagSchema] = Field(default_factory=lambda: [TagSchema(
        tag_id=fake.random_int,
        tag_name=fake.random_word
    )])
    pet_status: str = Field(alias="status", default="available")


class UpdatePetInStoreRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление сущности животного в магазине
    """
    model_config = ConfigDict(populate_by_name=True)
    pet_id: int = Field(alias="id", default_factory=fake.random_int)
    new_name: str = Field(alias="name", default_factory=fake.random_name)
    new_status: str = Field(alias="status", default="available")
