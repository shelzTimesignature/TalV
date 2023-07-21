from sqlmodel import Session, select
from database import engine
from models import Employee
from fastapi import HTTPException, status


def create(name, surname, email, joining_date, retirement_date, company_id, department_id):
    session = Session(engine)
    x = Employee(
        name=name,
        surname=surname,
        email=email,
        joining_date=joining_date,
        retirement_date=retirement_date,
        company_id=company_id,
        department_id=department_id,
    )
    session.add(x)
    session.commit()
    session.close()


def get():
    session = Session(engine)
    return session.exec(select(Employee)).all()


def get_by_id(param):
    session = Session(engine)
    company = session.exec(select(Employee).where(Employee.id == param)).first()
    if not company:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee Not Found'
        )
    return company


def remove_by_id(param):
    session = Session(engine)
    x = session.exec(select(Employee).where(Employee.id == param)).first()
    if not x:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Employee Not Found'
        )
    session.delete(x)
    session.commit()
    session.close()
    return f'{x.name} {x.surname} has been deleted'
