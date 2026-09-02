from app.database import Base, engine
from app.models.car import Car

Base.metadata.create_all(engine)

print(Base.metadata.tables.keys())
print("Tables created successfully!")