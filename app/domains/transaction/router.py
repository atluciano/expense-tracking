from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from datetime import datetime

from app.core.db import get_session
from .schemas import TransactionOut
from .schemas import TransactionIn
from .repository import TransactionRepository
from .service import TransactionService

router = APIRouter()


@router.get("/", response_model=List[TransactionOut])
def read_transactions(
    from_date: datetime,
    to_date: datetime,
    session: Session = Depends(get_session),
) -> List[TransactionOut]:
    repo = TransactionRepository(session)
    service = TransactionService(repo)
    return service.get_transactions_between(from_date, to_date)


@router.get("/{transaction_id}", response_model=TransactionOut)
def read_transaction(transaction_id: int, session: Session = Depends(get_session)):
    repo = TransactionRepository(session)
    service = TransactionService(repo)
    transaction = service.get_transaction_by_id(transaction_id)
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    return transaction


@router.post("/", response_model=TransactionOut)
def create_transaction(transaction: TransactionIn, session: Session = Depends(get_session)):
    repo = TransactionRepository(session)
    service = TransactionService(repo)
    try:
        return service.create_transaction(transaction)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, session: Session = Depends(get_session)):
    repo = TransactionRepository(session)
    service = TransactionService(repo)
    deleted = service.delete_transaction(transaction_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    return {"deleted": True}
