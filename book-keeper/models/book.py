from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default = None, primary_key=True)
    title: str
    author: str
    description: str
    price: float
    is_sold: bool = Field(default=False)
    #One book can have one user
    user_id: int = Field(foreign_key="user.id")
    owner: Optional["User"] = Relationship(back_populates="books")

#Request body for create book
class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    price: float
    owner_id: int

#Response body for create book
class BookCreateResponse(BaseModel):
    id: int
    title: str
    author: str
    desciption: str
    price: float
    is_sold: bool
    owner_id: int


#Avoid circular import error
from models.user import User
Book.model_rebuild()
