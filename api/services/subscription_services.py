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
            # TODO: Implementar Exception
            raise NotImplementedError("EXCEPTION TENANT NOT EXIST")

        if not self.plan_repo.get_one(dto.plan_id):
            # TODO: Implementar Exception
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
        old_subscription: Subscription = self.subscription_repo.get_one(
            subscription_id=subscription_id)

        if not old_subscription:
            # TODO: Implementar Exception
            raise NotImplementedError("EXCEPTION ENTITY NOT FOUND")

        try:
            old_subscription.status = update_subscription.status
            old_subscription.start_date = update_subscription.start_date
            old_subscription.end_date = update_subscription.end_date
            old_subscription.tenant_id = update_subscription.tenant_id
            old_subscription.plan_id = update_subscription.plan_id

            self.subscription_repo.update(old_subscription)

        except Exception:
            # TODO: Implementar Exception
            raise NotImplementedError("EXCEPTION ENTITY NOT PROCESS")

    def delete(self, subscription_id: int) -> None:
        subscription: Subscription = self.subscription_repo.get_one(
            subscription_id)

        if not subscription:
            # TODO: Implementar Exception
            raise NotImplementedError("EXCEPTION TO ENTITY NOT FIND")

        return self.subscription_repo.delete(subscription=subscription)
