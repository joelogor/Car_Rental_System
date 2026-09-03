from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.core.database import create_db_and_tables

from app.routes.auth_router import auth_router
from app.routes.car_router import car_router
from app.routes.rental_router import rental_router


@asynccontextmanager
async def create_tables(app : FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(title="Car Rental System API",lifespan=create_tables)

app.include_router(auth_router)
app.include_router(car_router)
app.include_router(rental_router)