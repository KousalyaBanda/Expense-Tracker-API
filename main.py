from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running successfully"}


@app.post("/expenses")
def create_expense(
        expense: schemas.ExpenseCreate,
        db: Session = Depends(get_db)
):
    return crud.create_expense(db, expense)


@app.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):
    return crud.get_expenses(db)