from typing import List

from api.repository.plan_repository import PlanRepository
from api.models.plan import Plan
from api.models.dto.plan_dto import PlanCreateDTO, PlanResponseDTO, PlanUpdateDTO


class PlanService:
    def __init__(
        self, plan_repo: PlanRepository
    ) -> None:
        self.plan_repo = plan_repo

    def create(self, dto: PlanCreateDTO) -> Plan:

        plan: Plan = Plan(
            name=dto.name,
            price=dto.price,
            user_limit=dto.user_limit,
            scheduling_limit=dto.scheduling_limit
        )

        if self.plan_repo.get_name(plan_name=dto.name):
            # TODO: Implementar Exception
            raise NotImplementedError("Exception to 'Name' Already Taken")

        return self.plan_repo.create(plan=plan)

    def get_all(self, skip: int, limit: int) -> List[Plan]:
        return self.plan_repo.get_all(skip=skip, limit=limit)

    def get_one(self, plan_id: int) -> Plan:
        return self.plan_repo.get_one(plan_id=plan_id)

    def update(self, plan_id: int, update_plan: PlanUpdateDTO) -> None:
        old_plan = self.plan_repo.get_one(plan_id=plan_id)

        if not old_plan:
            # TODO: Implementar Exception
            raise NotImplementedError("EXCEPTION TO ENTITY NOT FOUND")

        try:
            old_plan.name = update_plan.name
            old_plan.price = update_plan.price
            old_plan.user_limit = update_plan.user_limit
            old_plan.scheduling_limit = update_plan.scheduling_limit

            return self.plan_repo.update(update_plan=old_plan)

        except Exception:
            # TODO: Implementar Exception
            raise NotImplementedError("EXCEPTION ENTITY NOT PROCESS")

    def delete(self, plan_id: int) -> None:
        plan = self.plan_repo.get_one(plan_id=plan_id)

        if not plan:
            # TODO: Implementar Exception
            raise NotImplementedError("EXCEPTION TO ENTITY NOT FOUND")

        self.plan_repo.delete(plan)
