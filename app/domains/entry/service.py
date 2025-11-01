from typing import List
from decimal import Decimal
from .repository import EntryRepository
from .models import Entry
from .schemas import EntryIn


class EntryService:
    def __init__(self, repo: EntryRepository):
        self.repo = repo

    def create_entries_for_transaction(self, transaction_id: int, entries_in: List[EntryIn]) -> List[Entry]:
        created = []
        for e in entries_in:
            db_entry = Entry(
                transaction_id=transaction_id,
                account_id=e.account_id,
                category_id=e.category_id,
                amount=Decimal(str(e.amount)),
            )
            created.append(self.repo.create(db_entry))

        return created
