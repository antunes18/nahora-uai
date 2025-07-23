from sqlalchemy import select
from sqlalchemy.orm import Session
from api.models.plan import Plan


class PlanRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, subscription: Plan) -> Plan:
        NotImplementedError("Create Not NotImplemented")

    def get_all(self) -> list(Plan):
        NotImplementedError(
            "GET ALL 'NEED AVALIATION OF SCOPE' not NotImplemented")

    def get_one(self, subscription_id: int) -> Plan:
        NotImplementedError("GET ONE NotImplemented")

    def update(self, subscription_id: int, update_subscription: Plan):
        NotImplementedError(
            "UPDATE 'NEED AVALIATION OF SCOPE' not NotImplemented")

    def delete(self, subscription_id: int):
        NotImplementedError("DELETE NotImplemented")
