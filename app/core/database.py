from sqlmodel import SQLModel, create_engine, Session
from app.models import __init__

DATABASE_URL : str = 'sqlite:///database.db'

connect_args : dict = {'check_same_thread' : False}

engine = create_engine(
    DATABASE_URL,connect_args=connect_args,
    echo=True)

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session