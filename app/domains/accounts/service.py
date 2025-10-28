from .repository import AccountRepository
from .models import Account
from .schemas import AccountIn
from decimal import Decimal

class AccountService:
    def __init__(self, repo: AccountRepository):
        self.repo = repo
    
    def create_account(self, account_in: AccountIn) -> Account:
        db_account = Account(
            name = account_in.name,
            type = account_in.type,
            initial_balance=Decimal(str(account_in.initial_balance))
        )
        return self.repo.create(db_account)

    def get_all_accounts(self):
        return self.repo.get_all()
