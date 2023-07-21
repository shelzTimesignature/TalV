from sqlmodel import Session, select
from database import engine
from models import Department
from fastapi import HTTPException, status


def create(name):
    session = Session(engine)
    x = Department(
        name=name
    )
    session.add(x)
    session.commit()
    session.close()


def get():
    session = Session(engine)
    return session.exec(select(Department)).all()


def get_by_id(param):
    session = Session(engine)
    company = session.exec(select(Department).where(Department.id == param)).first()
    if not company:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Department Not Found'
        )
    return company


def remove_by_id(param):
    session = Session(engine)
    x = session.exec(select(Department).where(Department.id == param)).first()
    if not x:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Department Not Found'
        )
    session.delete(x)
    session.commit()
    session.close()
    return f'{x.name} has been deleted'
