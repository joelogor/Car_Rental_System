from typing import Optional

from pydantic import BaseModel, EmailStr

class UpdateProfileResponse(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None