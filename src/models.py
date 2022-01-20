from sqlalchemy import Column, Integer, String
from src.database import Base
from dataclasses import dataclass


# Define Product class inheriting from Base
@dataclass
class Product(Base):
    id: int
    name:  str
    price:  int
    quantity: int
    __tablename__ = 'Product'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    price = Column(Integer)
    quantity = Column(Integer)
