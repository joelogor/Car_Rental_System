from sqlalchemy import StaticPool
from sqlmodel import SQLModel, create_engine, Session
from app.models.user import User
from app.models.car import Car
from app.models.rental import Rental

DATABASE_URL : str = 'sqlite:///database.db'

connect_args : dict = {'check_same_thread' : False}

engine = create_engine(
    DATABASE_URL,connect_args=connect_args,
    echo=True)
#     poolclass=StaticPool
# )

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session