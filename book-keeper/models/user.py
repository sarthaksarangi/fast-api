from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(index=True, unique=True)
    college:str

    #One user can have many books
    books: list["Book"] = Relationship(back_populates="user")

#Request body for create user
class UserCreate(BaseModel):
    name: str
    email: str
    college: str

#Response body for create user
class UserCreateResponse(BaseModel):
    id: int
    name: str
    email: str
    college: str

#Avoid circular import error
from models.book import Book
User.model_rebuild()