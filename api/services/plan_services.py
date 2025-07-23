from api.repository.plan_repository import PlanRepository
from api.models.plan import Plan


class PlanService:
    def __init__(
        self, plan_repo: PlanRepository
    ):
        self.plan_repo = plan_repo

    def create(self, dto: Plan):
        raise NotImplementedError("CREATE Not Implemented")

    def get_all(self):
        raise NotImplementedError("GET ALL Not Implemented")

    def get_one(self, plan_id: int):
        raise NotImplementedError("GET ONE Not Implemented")

    def update(self, plan_id: int, update_plan: Plan):
        raise NotImplementedError("UPDATE Not Implemented")

    def delete(self, plan_id: int):
        raise NotImplementedError("DELETE Not Implemented")
