from pydantic import BaseModel

class UpdateCarRequest(BaseModel):
    username: str
    plate_number: str