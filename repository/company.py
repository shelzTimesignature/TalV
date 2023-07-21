from sqlmodel import Session, select
from database import engine
from models import Company
from fastapi import HTTPException, status


def create(name, address, registration_date, registration_number):
    session = Session(engine)
    company = Company(
        name=name,
        address=address,
        registration_date=registration_date,
        registration_number=registration_number
    )
    session.add(company)
    session.commit()
    session.close()


def get():
    session = Session(engine)
    companies = select(Company)
    return session.exec(companies).all()


def get_by_id(param):
    session = Session(engine)
    company = session.exec(select(Company).where(Company.id == param)).first()
    if not company:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Company Not Found'
        )
    return company


def remove_by_id(param):
    session = Session(engine)
    company = session.exec(select(Company).where(Company.id == param)).first()
    if not company:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Company Not Found'
        )
    session.delete(company)
    session.commit()
    session.close()
    return f'{company.name} has been deleted'
