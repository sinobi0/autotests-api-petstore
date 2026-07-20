from enum import Enum
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict, RootModel

from tools.fakers import fake


class OrderStatus(str, Enum):
    """Перечисление для возможных статусов заказа (в Swagger их обычно 3)"""
    PLACED = "placed"
    APPROVED = "approved"
    DELIVERED = "delivered"


class OrderSchema(BaseModel):
    """
    Описание структуры заказа
    """
    model_config = ConfigDict(populate_by_name=True)
    order_id: int = Field(alias="id")
    pet_id: int = Field(alias="petId")
    quantity: int = Field(alias="quantity")
    ship_date: datetime = Field(alias="shipDate")
    complete: bool

class CreateOrderRequestSchema(BaseModel):
    """
    Описание структуры заказа
    """
    model_config = ConfigDict(populate_by_name=True)
    order_id: int = Field(alias="id", default_factory=fake.random_int)
    pet_id: int = Field(alias="petId", default_factory=fake.random_int)
    quantity: int = Field(alias="quantity", default_factory=fake.random_int)
    ship_date: datetime = Field(alias="shipDate", default_factory=fake.random_date)
    complete: bool = Field(default=True)

class CreateOrderResponseSchema(OrderSchema):
    """
    Описание структуры ответа на создание заказа
    """
    model_config = ConfigDict(populate_by_name=True)
    order_id: int = Field(alias="id")
    pet_id: int = Field(alias="petId")
    quantity: int = Field(alias="quantity")
    ship_date: datetime = Field(alias="shipDate")
    complete: bool

class InventoryResponseSchema(RootModel[dict[str, int]]):
    """
    Описание структуры запроса статусов в магазине
    """
    pass
