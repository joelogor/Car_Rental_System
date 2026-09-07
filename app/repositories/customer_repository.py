from uuid import UUID

from sqlmodel import Session, select

from app.models import Customer

class CustomerRepository:
    def __init__(self,session: Session):
        self._session = session

    def save(self,customer: Customer) -> Customer:
        self._session.add(customer)
        self._session.commit()
        self._session.refresh(customer)
        return customer

    def save_customer(self,customer: Customer) -> Customer:
        self._session.add(customer)
        self._session.commit()
        self._session.refresh(customer)
        return customer

    def find_by_id(self,customer_id: UUID):
        return self._session.get(Customer,customer_id)

    def find_all(self):
        statement = select(Customer)
        return self._session.exec(statement).all()

    def delete_by_id(self,customer_id: UUID) -> bool:
        customer = self.find_by_id(customer_id)

        if customer is not None:
            self._session.delete(customer)
            self._session.commit()
            return True
        return False

    def count (self) -> int:
        customers = self.find_all()
        return len(customers)

    def find_by_username(self,username: str):
        statement = select(Customer).where(Customer.username == username)
        return self._session.exec(statement).one_or_none()

    def find_by_email(self,email: str):
        statement = select(Customer).where(Customer.email == email)
        return self._session.exec(statement).one_or_none()