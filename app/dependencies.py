from fastapi import Depends
from sqlmodel import Session

from app.core.database import get_session
from app.repositories.user_repository import UserRepository
from app.services.auth_services import AuthServices

def get_user_repository(session : Session = Depends (get_session)) -> UserRepository:
    return UserRepository(session)

def get_auth_service(user_repository : UserRepository = Depends(get_user_repository)):
    return AuthServices(user_repository)