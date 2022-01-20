from pydantic import BaseModel
from typing import Optional


# Create Inventory Schema (Pydantic Model)
class ProductCreate(BaseModel):
    name: str
    price: int
    quantity: int


# Update Inventory Schema (Pydantic Model)
class ProductUpdate(BaseModel):
    id: int
    name: Optional[str]
    price: Optional[int]
    quantity: Optional[int]


# Complete Inventory Schema (Pydantic Model)
class Product(BaseModel):
    id: int
    name: str
    price: int
    quantity: int

    class Config:
        orm_mode = True
