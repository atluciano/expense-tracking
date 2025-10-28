from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from app.core.db import get_session
from .schemas import AccountOut, AccountIn
from .repository import AccountRepository
from .service import AccountService

router = APIRouter()

@router.get("/")
def read_accounts(session: Session = Depends(get_session)) -> List[AccountOut]:
    repo = AccountRepository(session)
    service = AccountService(repo)
    return service.get_all_accounts()

@router.post("/")
def create_account(account: AccountIn, session: Session = Depends(get_session)):
    repo = AccountRepository(session)
    service = AccountService(repo)
    return service.create_account(account)
