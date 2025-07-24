from typing import List

from api.repository.subscription_repository import SubscriptionRepository
from api.repository.plan_repository import PlanRepository
from api.repository.tenant_repository import TenantRepository

from api.models.subscription import Subscription
from api.models.dto.subscription_dto import SubscriptionCreateDTO, SubscriptionResponseDTO, SubscriptionUpdateDTO


class SubscriptionService:
    def __init__(
        self, subscription_repo: SubscriptionRepository,
        tenant_repo: TenantRepository,
        plan_repo: PlanRepository,
    ):
        self.subscription_repo = subscription_repo
        self.tenant_repo = tenant_repo
        self.plan_repo = plan_repo

    def create(self, dto: SubscriptionCreateDTO) -> Subscription:
        if not self.tenant_repo.get_one(dto.tenant_id):
            raise NotImplementedError("EXCEPTION TENANT NOT EXIST")

        if not self.plan_repo.get_one(dto.plan_id):
            raise NotImplementedError("EXCEPTION PLAN NOT EXIST")

        subscription: Subscription = Subscription(
            status=dto.status,
            start_date=dto.start_date,
            end_date=dto.end_date,
            tenant_id=dto.tenant_id,
            plan_id=dto.plan_id
        )

        return self.subscription_repo.create(subscription)

    def get_all(self, skip: int, limit: int) -> List[Subscription]:
        return self.subscription_repo.get_all(skip=skip, limit=limit)

    def get_one(self, subscription_id: int) -> Subscription:
        return self.subscription_repo.get_one(subscription_id=subscription_id)

    def update(self, subscription_id: int, update_subscription: Subscription) -> None:
        return self.subscription_repo.update(subscription_id=subscription_id, update_subscription=update_subscription)

    def delete(self, subscription_id: int) -> None:
        return self.subscription_repo.delete(subscription_id=subscription_id)
