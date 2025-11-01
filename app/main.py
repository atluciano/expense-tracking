from typing import Union
from fastapi import FastAPI
from app.core.db import init_db

from app.domains.account.router import router as account_router
from app.domains.category.router import router as category_router
from app.domains.transaction.router import router as transaction_router

from app.domains.transaction import models as transaction_models
from app.domains.account import models as account_models

def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(account_router, prefix="/accounts", tags=["Accounts"])
app.include_router(category_router, prefix="/categories", tags=["Categories"])
app.include_router(transaction_router, prefix="/transactions", tags=["Transactions"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
