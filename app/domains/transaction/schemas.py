from pydantic import BaseModel, computed_field
from datetime import datetime
from typing import List

from app.domains.entry.schemas import EntryIn, EntryOut


class TransactionBase(BaseModel):
    description: str
    date: datetime
    notes: str


class TransactionIn(TransactionBase):
    entries: List[EntryIn]


class TransactionOut(TransactionBase):
    id: int
    entries: List[EntryOut]

    @computed_field
    @property
    def amount(self) -> float:
        return sum(e.amount for e in self.entries if e.amount > 0)

    created_at: datetime
    deleted_at: datetime | None
