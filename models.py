from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class CompanyDepartment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company_id: Optional[int] = Field(default=None, foreign_key='company.id')
    department_id: Optional[int] = Field(default=None, foreign_key='department.id')


class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: str
    registration_date: str
    registration_number: str
    departments: List['Department'] = Relationship(back_populates='departments', link_model=CompanyDepartment)


class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    surname: str
    email: str
    joining_date: str
    retirement_date: str
    company_id: Optional[int] = Field(default=None, foreign_key='company.id')
    company: Optional[Company] = Relationship(back_populates="employees")
    department_id: Optional[int] = Field(default=None, foreign_key='department.id')
    department: Optional[Department] = Relationship(back_populates="employees")
