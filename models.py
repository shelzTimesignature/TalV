from sqlmodel import SQLModel, Field
from typing import Optional


class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: str
    registration_date: str
    registration_number: str


class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class CompanyDepartment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company_id: Optional[int] = Field(default=None, foreign_key='company.id')
    department_id: Optional[int] = Field(default=None, foreign_key='department.id')


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    surname: str
    email: str
    joining_date: str
    retirement_date: str
    department_id: Optional[int] = Field(default=None, foreign_key='department.id')
