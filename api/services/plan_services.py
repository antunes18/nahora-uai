from api.repository.plan_repository import PlanRepository
from api.models.plan import Plan
from api.models.dto.plan_dto import PlanCreateDTO, PlanResponseDTO, PlanUpdateDTO


class PlanService:
    def __init__(
        self, plan_repo: PlanRepository
    ):
        self.plan_repo = plan_repo

    def create(self, dto: PlanCreateDTO) -> Plan:

        plan: Plan = Plan(
            name=dto.name,
            price=dto.price,
            user_limit=dto.user_limit,
            scheduling_limit=dto.scheduling_limit
        )

        if self.plan_repo.get_name(plan_name=dto.name):
            raise NotImplementedError("Exception to 'Name' Already Taken")

        return self.plan_repo.create(plan=plan)

    def get_all(self, skip: int, limit: int):
        return self.plan_repo.get_all(skip=skip, limit=limit)

    def get_one(self, plan_id: int):
        return self.plan_repo.get_one(plan_id=plan_id)

    def update(self, plan_id: int, update_plan: PlanUpdateDTO):
        return self.plan_repo.update(plan_id=plan_id, update_plan=update_plan)

    def delete(self, plan_id: int):
        # TODO: How implement the delete?
        raise NotImplementedError("DELETE Not Implemented")
