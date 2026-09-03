from uuid import UUID

from sqlmodel import Session, select

from app.models.user import User


class UserRepository:
    def __init__(self,session: Session):
        self._session = session

    def save(self,user: User) -> User:
        self._session.add(user)
        self._session.commit()
        self._session.refresh(user)
        return user

    def find_by_id(self,user_id: UUID):
        return self._session.get(User,user_id)

    def find_all(self):
        statement = select(User)
        return self._session.exec(statement).all()

    def delete_by_id(self,user_id: UUID) -> bool:
        user = self.find_by_id(user_id)

        if user is not None:
            self._session.delete(user)
            self._session.commit()
            return True
        return False

    def count (self) -> int:
        users = self.find_all()
        return len(users)

    def find_by_username(self,username: str):
        statement = select(User).where(User.username == username)
        return self._session.exec(statement).one_or_none()

    def find_by_email(self,email: str):
        statement = select(User).where(User.email == email)
        return self._session.exec(statement).one_or_none()