from enum import Enum
from sqlmodel import SQLModel, Field
from typing import Optional

class CategoryType(str, Enum):
    income = "income"
    outcome = "outcome"

class Category(SQLModel, table=True):
    __tablename__ = "category"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    type: CategoryType = Field(nullable=False)
