from fastapi import FastAPI

from app.routers.car_router import router as car_router

app = FastAPI()

app.include_router(car_router)



