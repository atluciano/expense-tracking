from sqlmodel import Session, select
from .models import Entry
from typing import List


class EntryRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, entry: Entry) -> Entry:
        self.session.add(entry)
        self.session.commit()
        self.session.refresh(entry)
        return entry

    def get_by_transaction(self, transaction_id: int) -> List[Entry]:
        stmt = select(Entry).where(Entry.transaction_id == transaction_id)
        return list(self.session.exec(stmt))
