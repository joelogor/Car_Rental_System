from pydantic import BaseModel

class LogoutUserResponse(BaseModel):
    username: str
    message: str