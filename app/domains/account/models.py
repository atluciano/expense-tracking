from sqlmodel import SQLModel, Field
from decimal import Decimal

class Account(SQLModel, table=True):
    __tablename__ = "account"
    
    id: int | None = Field(default=None, primary_key=True)
    name: str
    type: str # carteira, corrente, investimentos...
    initial_balance: Decimal = Field(default=Decimal("0.00"))
    balance: Decimal = Field(default=Decimal("0.00"))
