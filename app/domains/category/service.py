from .repository import CategoryRepository
from .models import Category
from .schemas import CategoryIn

class CategoryService:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo
    
    def create_category(self, category_in: CategoryIn) -> Category:
        db_category = Category(
            name = category_in.name,
            type = category_in.type
        )
        return self.repo.create(db_category)

    def get_all_categories(self):
        return self.repo.get_all()
