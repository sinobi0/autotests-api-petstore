from pydantic import BaseModel, Field, ConfigDict, RootModel

class UserSchema(BaseModel):
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
    model_config = ConfigDict(populate_by_name=True)
    user_name: str = Field(alias="username")
    user_password: str = Field(alias="password")

class CreateUserListApi(RootModel[list[UserSchema]]):
    pass