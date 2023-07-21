from fastapi import APIRouter
from repository import department
from models import Department

router = APIRouter(
    tags=['Department'],
    prefix='/departments'
)


@router.get('/')
def get():
    return department.get()


@router.post('/')
def add(request: Department):
    return department.create(
        name=request.name
    )


@router.get('/{param}')
def get_by_id(param):
    return department.get_by_id(param)


@router.delete('/{param}')
def delete(param):
    return department.remove_by_id(param)
