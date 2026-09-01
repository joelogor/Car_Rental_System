from pydantic import BaseModel

from app.models.enums.role import Role


class LoginUserResponse(BaseModel):
    username: str
    logged_in: bool
    role : Role