from sqlalchemy.orm import Session
from models import Expense
from schemas import ExpenseCreate

def create_expense(db: Session, expense: ExpenseCreate):
    db_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses(db: Session):
    return db.query(Expense).all()