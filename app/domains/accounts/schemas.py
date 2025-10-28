from decimal import Decimal
from pydantic import BaseModel

class AccountBase(BaseModel):
    name: str
    type: str
    initial_balance: float

class AccountIn(AccountBase):
    pass

class AccountOut(AccountBase):
    id: int
    balance: float
