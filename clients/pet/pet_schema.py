from pydantic import BaseModel, ConfigDict, Field, FilePath


class CategorySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    category_id: int = Field(alias="id")
    category_name: str = Field(alias="name")


class TagSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tag_id: int = Field(alias="id")
    tag_name: str = Field(alias="name")


class PetSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    pet_id: int = Field(alias="id")
    category: CategorySchema
    pet_name: str = Field(alias="name")
    photo_urls: list = Field(alias="photoUrls")
    tags: list[TagSchema]
    pet_status: str = Field(alias="status")


class GetPetByStatusSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    status: str


class CreatePetRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    pet_id: int = Field(alias="id")
    category: CategorySchema
    pet_name: str = Field(alias="name")
    photo_urls: list = Field(alias="photoUrls")
    tags: list[TagSchema]
    pet_status: str = Field(alias="status")


class UploadNewPetRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    pet_id: int = Field(alias="petId")
    category: CategorySchema
    pet_name: str = Field(alias="name")
    additional_metadata: str = Field(alias="additionalMetadata")
    file: FilePath


class UpdatePetRequestSchema(BaseModel):
    pet_id: int = Field(alias="petId")
    category: CategorySchema
    pet_name: str = Field(alias="name")
    photo_urls: list = Field(alias="photoUrls")
    tags: list[TagSchema]
    pet_status: str = Field(alias="status")


class UpdatePetInStoreRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    pet_id: int = Field(alias="petId")
    new_name: str = Field(alias="name")
    new_status: str = Field(alias="status")
