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
def update_expense(db: Session, expense_id: int, expense: ExpenseCreate):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if db_expense:
        db_expense.title = expense.title
        db_expense.amount = expense.amount
        db_expense.category = expense.category
        db.commit()
        db.refresh(db_expense)

    return db_expense


def delete_expense(db: Session, expense_id: int):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if db_expense:
        db.delete(db_expense)
        db.commit()

    return db_expense