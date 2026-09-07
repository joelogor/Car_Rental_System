from pydantic import BaseModel

from app.models.enums.role import Role

class CreateStaffRequest(BaseModel):
    full_name: str
    username: str
    email: str
    password: str
    role: Role