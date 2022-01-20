from pydantic import BaseModel
from typing import Optional


class ProductCreate(BaseModel):
    name: str
    price: int
    quantity: int


class ProductUpdate(BaseModel):
    name: Optional[str]
    price: Optional[int]
    quantity: Optional[int]


class Product(BaseModel):
    id: int
    name: str
    price: int
    quantity: int

    class Config:
        orm_mode = True
