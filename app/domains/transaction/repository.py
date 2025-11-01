from sqlmodel import Session, select, delete, update
from .models import Transaction
from datetime import datetime, timezone
from typing import List

class TransactionRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, transaction: Transaction) -> Transaction:
        self.session.add(transaction)
        self.session.commit()
        self.session.refresh(transaction)
        return transaction

    def get_transactions_between(self, from_date: datetime, to_date: datetime) -> List[Transaction]:
        stmt = (
            select(Transaction)
            .where(Transaction.date >= from_date)
            .where(Transaction.date <= to_date)
            .where(Transaction.deleted_at.is_(None))
        )
        result = self.session.exec(stmt)
        return result

    def get_by_id(self, transaction_id: int) -> Transaction:
        #return self.session.get(Transaction, transaction_id)
        stmt = select(Transaction).where(Transaction.id == transaction_id, Transaction.deleted_at.is_(None))
        return self.session.exec(stmt).first()
    
    def delete(self, transaction_id: int) -> bool:
        stmt = select(Transaction).where(Transaction.id == transaction_id)
        transaction = self.session.exec(stmt).first()
        if not transaction:
            return False
    
        transaction.deleted_at = datetime.now(timezone.utc)
        self.session.commit()
        return True
