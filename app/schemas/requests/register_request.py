from typing import Optional

from pydantic import BaseModel, Field, EmailStr

class RegisterUserRequest(BaseModel):
    username : str = Field(...,min_length=1,max_length=20)
    email : EmailStr = Field(...,min_length=9,max_length=30)
    password : str = Field(...,min_length=8,max_length=20)
    full_name : str = Field(...,min_length=1,max_length=20)
    phone_number : Optional[str] = Field(None,min_length=9,max_length=20)
    address : Optional[str] = Field(None,min_length=9,max_length=20)
