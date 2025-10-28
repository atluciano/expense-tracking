from typing import Union
from fastapi import FastAPI
from app.core.db import init_db

from app.domains.accounts.router import router as accounts_router

def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(accounts_router, prefix="/accounts", tags=["Accounts"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
