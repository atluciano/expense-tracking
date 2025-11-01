from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from app.core.db import get_session
from .schemas import CategoryOut, CategoryIn
from .repository import CategoryRepository
from .service import CategoryService

router = APIRouter()

@router.get("/")
def read_categories(session: Session = Depends(get_session)) -> List[CategoryOut]:
    repo = CategoryRepository(session)
    service = CategoryService(repo)
    return service.get_all_categories()

@router.post("/")
def create_category(category: CategoryIn, session: Session = Depends(get_session)):
    repo = CategoryRepository(session)
    service = CategoryService(repo)
    return service.create_category(category)
