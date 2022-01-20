from sqlalchemy import Column, Integer, String
from src.database import Base
from dataclasses import dataclass


@dataclass
class Product(Base):
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(256), nullable=False)
    # price is in cents, and can be utilized downstream by dividing by 100
    price: int = Column(Integer, nullable=False)
    quantity: int = Column(Integer, nullable=False)

    __tablename__ = 'Product'
