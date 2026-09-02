from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = "mysql+pymysql://root:Ekpery+10@localhost/car_rental_service"

class Base(DeclarativeBase):
    pass

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()



# if __name__ == "__main__":
#     from app.models.car import Car
#
#     print(Base.metadata.tables.keys())
#
#     Base.metadata.create_all(engine)
#
#     print("Tables created successfully!")
