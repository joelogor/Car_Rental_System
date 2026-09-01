from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.models.enums.role import Role

class RegisterUserResponse(BaseModel):
    user_id : Optional[UUID] = None
    username : str
    email : EmailStr
    role : Role
    message : Optional[str]
