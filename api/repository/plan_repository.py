from sqlalchemy.orm import Session
from api.models.plan import Plan
from typing import List


class PlanRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, plan: Plan) -> Plan:
        self.session.add(plan)
        self.session.commit()
        self.session.refresh(plan)

        return plan

    def get_all(self, skip: int, limit: int) -> List[Plan]:
        return self.session.query(Plan).offset(skip).limit(limit).all()

    def get_one(self, plan_id: int) -> Plan:
        return self.session.query(Plan).filter(Plan.id == plan_id).first()

    def get_name(self, plan_name: int) -> Plan:
        return self.session.query(Plan).filter(Plan.name == plan_name).first()

    def update(self, update_plan: Plan) -> None:
        self.session.commit()
        self.session.refresh(update_plan)

    def delete(self, plan: Plan) -> None:
        self.session.delete(plan)
        self.session.commit()
