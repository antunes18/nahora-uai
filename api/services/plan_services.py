from api.repository.plan_repository import PlanRepository
from api.models.plan import Plan


class PlanService:
    def __init__(
        self, plan_repo: PlanRepository
    ):
        self.plan_repo = plan_repo

    def create(self, dto: Plan):
        NotImplementedError()

    def get_all(self):
        NotImplementedError()

    def get_one(self, plan_id: int):
        NotImplementedError()

    def update(self, plan_id: int, update_plan: Plan):
        NotImplementedError()

    def delete(self, plan_id: int):
        NotImplementedError()
