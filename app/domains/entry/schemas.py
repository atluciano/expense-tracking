from pydantic import BaseModel
from decimal import Decimal
from typing import Optional
from datetime import datetime


class EntryBase(BaseModel):
    account_id: Optional[int] = None
    category_id: Optional[int] = None
    amount: float


class EntryIn(EntryBase):
    pass


class EntryOut(EntryBase):
    id: int
    transaction_id: int
    created_at: datetime
