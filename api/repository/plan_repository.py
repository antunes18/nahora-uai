from sqlalchemy import select
from sqlalchemy.orm import Session
from api.models.plan import Plan


class PlanRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, plan: Plan) -> Plan:
        raise NotImplementedError("Create Not NotImplemented")

    def get_all(self) -> list(Plan):
        raise NotImplementedError(
            "GET ALL 'NEED AVALIATION OF SCOPE' not NotImplemented")

    def get_one(self, plan_id: int) -> Plan:
        raise NotImplementedError("GET ONE NotImplemented")

    def update(self, plan_id: int, update_plan: Plan):
        raise NotImplementedError(
            "UPDATE 'NEED AVALIATION OF SCOPE' not NotImplemented")

    def delete(self, plan_id: int):
        raise NotImplementedError("DELETE NotImplemented")
