from fastapi import FastAPI
from database import create_db_and_tables
from routers import company, department, employee
app = FastAPI()

app.include_router(company.router)
app.include_router(department.router)
app.include_router(employee.router)


@app.on_event('startup')
def startup():
    create_db_and_tables()


@app.get('/')
def root():
    return {
        "Hello": "World"
    }
