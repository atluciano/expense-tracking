from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional
from decimal import Decimal
from datetime import datetime, timezone

if TYPE_CHECKING:
    from domains.transaction.models import Transaction

class Entry(SQLModel, table=True):
    __tablename__ = "entry"

    id: Optional[int] = Field(default=None, primary_key=True)
    transaction_id: int = Field(foreign_key="transaction.id")

    account_id: Optional[int] = Field(default=None, foreign_key="account.id")
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")

    transaction: "Transaction" = Relationship(back_populates="entries")

    amount: Decimal

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
