from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from domains.entry.models import Entry

class Transaction(SQLModel, table=True):
    __tablename__ = "transaction"

    id: int | None = Field(default=None, primary_key=True)
    description: str
    date: datetime
    notes: str
    entries: List["Entry"] = Relationship(back_populates="transaction")

    # default_factory must be a callable; use a lambda to call datetime.now with timezone
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: datetime | None = None
