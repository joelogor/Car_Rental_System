from app.models.enums.role import Role
from app.models.user import User


class Admin(User):
    __role : Role = Role.ADMIN