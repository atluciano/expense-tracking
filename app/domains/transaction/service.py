from datetime import datetime
from typing import List
from decimal import Decimal

from .repository import TransactionRepository
from .models import Transaction
from .schemas import TransactionIn

from app.domains.entry.models import Entry as EntryModel


class TransactionService:
    def __init__(self, repo: TransactionRepository):
        self.repo = repo

    def create_transaction(self, transaction_in: TransactionIn) -> Transaction:
        """Create a Transaction and its associated entries atomically.

        If any entry fails validation or DB insertion, the whole operation is rolled back.
        """
        db_transaction = Transaction(
            description=transaction_in.description,
            date=transaction_in.date,
            notes=transaction_in.notes,
        )

        session = self.repo.session

        entries_models: List[EntryModel] = []
        # Use a DB transaction so either all rows are persisted or none are.
        with session.begin():
            session.add(db_transaction)
            # flush to populate db_transaction.id for FK on entries
            session.flush()

            for e in transaction_in.entries:
                # validation: at least one of account_id or category_id must be present
                if (getattr(e, "account_id", None) is None) and (getattr(e, "category_id", None) is None):
                    raise ValueError("Each entry must have at least an account_id or a category_id")

                em = EntryModel(
                    transaction_id=db_transaction.id,
                    account_id=e.account_id,
                    category_id=e.category_id,
                    amount=Decimal(str(e.amount)),
                )
                session.add(em)
                entries_models.append(em)

        # refresh objects after successful commit
        session.refresh(db_transaction)
        for em in entries_models:
            session.refresh(em)

        return db_transaction

    def get_transactions_between(self, from_date: datetime, to_date: datetime) -> List[Transaction]:
        """Return a list of transactions between two datetimes (inclusive).

        Raises ValueError if from_date > to_date.
        """
        if from_date > to_date:
            raise ValueError("from_date must be <= to_date")

        result = self.repo.get_transactions_between(from_date, to_date)
        # repository returns an iterable/result; materialize to list
        return list(result)

    def get_transaction_by_id(self, transaction_id: int) -> Transaction | None:
        return self.repo.get_by_id(transaction_id)

    def delete_transaction(self, transaction_id: int) -> bool:
        """Soft-delete a transaction by id. Returns True if deleted, False if not found."""
        return self.repo.delete(transaction_id)
