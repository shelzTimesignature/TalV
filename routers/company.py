from fastapi import APIRouter
from repository import company
from models import Company

router = APIRouter(
    tags=['Company'],
    prefix='/company'
)


@router.get('/')
def get():
    return company.get()


@router.post('/')
def add(request: Company):
    return company.create(
        name=request.name,
        address=request.address,
        registration_date=request.registration_date,
        registration_number=request.registration_number
    )


@router.get('/{param}')
def get_by_id(param):
    return company.get_by_id(param)


@router.delete('/{param}')
def delete(param):
    return company.remove_by_id(param)
