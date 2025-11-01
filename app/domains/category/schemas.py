from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str
    type: str

class CategoryIn(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int
