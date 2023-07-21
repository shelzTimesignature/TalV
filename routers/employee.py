from fastapi import APIRouter
from repository import employee
from models import Employee

router = APIRouter(
    tags=['Employee'],
    prefix='/employees'
)


@router.get('/')
def get():
    return employee.get()


@router.post('/')
def add(request: Employee):
    return employee.create(
        name=request.name
    )


@router.get('/{param}')
def get_by_id(param):
    return employee.get_by_id(param)


@router.delete('/{param}')
def delete(param):
    return employee.remove_by_id(param)
