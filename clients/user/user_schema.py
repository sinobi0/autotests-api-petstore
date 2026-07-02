from pydantic import BaseModel, Field, ConfigDict, RootModel

from tools.fakers import fake


class UserSchema(BaseModel):
    """
    Описание структуры пользователя
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: int = Field(alias="id")
    user_name: str = Field(alias="username")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    user_email: str = Field(alias="email")
    user_password: str = Field(alias="password")
    user_phone: str = Field(alias="phone")
    user_status: int = Field(alias="userStatus")


class LoginUserSchema(BaseModel):
    """
    Описание структуры логина
    """
    model_config = ConfigDict(populate_by_name=True)
    user_name: str = Field(alias="username")
    user_password: str = Field(alias="password")


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса создания пользователя
    """
    model_config = ConfigDict(populate_by_name=True)
    user_name: str = Field(alias="username", default_factory=fake.random_name)
    user_password: str = Field(alias="password", default_factory=fake.random_password)


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя
    """
    model_config = ConfigDict(populate_by_name=True)
    code: int
    type: str
    message: str

class CreateUserListApi(RootModel[list[UserSchema]]):
    """
    Описание структуры запроса на создание пользователей
    """
    pass
