from sqlmodel import Session, select, delete
from .models import Category

class CategoryRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, category: Category) -> Category:
        self.session.add(category)
        self.session.commit()
        self.session.refresh(category)
        return category

    def get_all(self):
        return self.session.exec(select(Category))
    
    def get_by_id(self, category_id: int) -> Category | None:
        return self.session.get(Category, category_id)
    
    def delete(self, category_id: int) -> bool:
        stmt = delete(Category).where(Category.id == category_id)
        result = self.session.exec(stmt)
        self.session.commit()

        return result.rowcount > 0
