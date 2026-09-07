from pydantic import BaseModel


class CreateStaffResponse(BaseModel):
    message: str