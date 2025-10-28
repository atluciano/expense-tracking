from sqlmodel import Session, text, select
from .models import Account

class AccountRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, account: Account) -> Account:
        self.session.add(account)
        self.session.commit()
        self.session.refresh(account)
        return account

    def get_all(self):
        return self.session.exec(select(Account))

    def get_by_id(self, account_id: int) -> Account | None:
        return self.session.get(Account, account_id)

    def delete(self, account_id: int) -> bool:
        result = self.session.exec(
            text("DELETE FROM account WHERE id = :id"),
            {"id": account_id}
        )
        self.session.commit()
        
        return result.rowcount > 0
