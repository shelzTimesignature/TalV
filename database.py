from sqlmodel import create_engine, SQLModel
engine = create_engine("sqlite:///database.sqlite", echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)
