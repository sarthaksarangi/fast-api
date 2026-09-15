from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field
from enum import Enum

#OrderStatus(Enum)
class OrderStatus(str, Enum):
    PREPARING = "preparing"
    SHIPPED = "picked_up"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"

#Orders
class Order(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    customer_name: str
    delivery_address: str
    items:str
    status: OrderStatus = Field(default=OrderStatus.PREPARING)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

#Schema for creating a new order
class OrderCreate(SQLModel):
    customer_name: str
    delivery_address: str
    items:str

#Schema for updating order status
class OrderUpdate(SQLModel):
    status: Optional[OrderStatus] = None
    delivery_address: Optional[str] = None


#StatusLog
class StatusLog(SQLModel):
    order_id: int
    old_status: str
    new_status: str
    changed_at: datetime 



