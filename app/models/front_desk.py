from app.models.enums.role import Role
from app.models.user import User


class FrontDesk(User):
    __role : Role = Role.FRONT_DESK