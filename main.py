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


@app.post("/expenses", response_model=schemas.ExpenseResponse)
def create_expense(
        expense: schemas.ExpenseCreate,
        db: Session = Depends(get_db)
):
    return crud.create_expense(db, expense)


@app.get("/expenses",response_model=list[schemas.ExpenseResponse])
def get_expenses(db: Session = Depends(get_db)):
    return crud.get_expenses(db)

@app.put("/expenses/{expense_id}")
def update_expense(
        expense_id: int,
        expense: schemas.ExpenseCreate,
        db: Session = Depends(get_db)
):
    return crud.update_expense(db, expense_id, expense)


@app.delete("/expenses/{expense_id}")
def delete_expense(
        expense_id: int,
        db: Session = Depends(get_db)
):
    return crud.delete_expense(db, expense_id)