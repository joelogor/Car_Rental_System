from pydantic import BaseModel, Field, EmailStr
from app.models.enums.role import Role

class RegisterUserRequest(BaseModel):
    username : str = Field(...,min_length=1,max_length=20)
    email : EmailStr = Field(...,min_length=9,max_length=30)
    password : str = Field(...,min_length=8,max_length=20)
    full_name : str = Field(...,min_length=1,max_length=20)
    role : Role = Field(...,min_length=1,max_length=20)
