from enum import Enum
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict, RootModel


class OrderStatus(str, Enum):
    """Перечисление для возможных статусов заказа (в Swagger их обычно 3)"""
    PLACED = "placed"
    APPROVED = "approved"
    DELIVERED = "delivered"


class OrderSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    order_id: int = Field(alias="id")
    pet_id: int = Field(alias="petId")
    quantity: int = Field(alias="quantity")
    ship_date: datetime = Field(alias="shipDate")
    completed_date: bool


class InventoryResponseSchema(RootModel[dict[str, int]]):
    pass
