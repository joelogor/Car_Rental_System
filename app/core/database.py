import uuid
from sqlmodel import SQLModel, create_engine, Session, select
from pwdlib import PasswordHash
from app.models import __init__, User
from app.models.enums.role import Role

DATABASE_URL : str = 'sqlite:///database.db'

connect_args : dict = {'check_same_thread' : False}

pwd_context = PasswordHash.recommended()

engine = create_engine(
    DATABASE_URL,connect_args=connect_args,
    echo=True)

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

    session = Session(engine)
    seed_admin(session)
    session.close()

def get_session():
    with Session(engine) as session:
        yield session

def seed_admin(session : Session):
    statement = select(User).where(User.role == Role.ADMIN)
    existing_admin = session.exec(statement).first()

    if existing_admin:
        return

    hashed_password = pwd_context.hash("SuperAdmin2026!")
    admin = User(
        id=uuid.uuid4(),
        full_name="SuperAdmin",
        username="system_admin",
        email="admin@rentalsystem.com",
        password=hashed_password,
        role=Role.ADMIN,
        is_logged_in=True,
    )
    session.add(admin)
    session.commit()
