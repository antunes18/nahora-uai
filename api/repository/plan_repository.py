from sqlalchemy import select
from sqlalchemy.orm import Session
from api.models.plan import Plan
from typing import List


class PlanRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, plan: Plan) -> Plan:
        self.session.add(plan)
        self.session.commit()
        self.session.refresh(plan)

    def get_all(self, skip: int, limit: int) -> List[Plan]:
        return self.session.query(Plan).offset(skip).limit(limit).all()

    def get_one(self, plan_id: int) -> Plan:
        return self.session.query(Plan).filter(Plan.id == plan_id).first()

    def get_name(self, plan_name: int) -> Plan:
        return self.session.query(Plan).filter(Plan.name == plan_name).first()

    def update(self, plan_id: int, update_plan: Plan):
        old_plan = self.get_one(plan_id)

        if old_plan:
            old_plan.name = update_plan.name
            old_plan.price = update_plan.price
            old_plan.user_limit = update_plan.user_limit
            old_plan.scheduling_limit = update_plan.scheduling_limit

            self.session.commit()
            self.session.refresh(old_plan)

        else:
            None

    def delete(self, plan_id: int):
        raise NotImplementedError("DELETE NotImplemented")
