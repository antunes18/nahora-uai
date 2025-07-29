from typing import List
from datetime import datetime

from api.repository.subscription_repository import SubscriptionRepository
from api.repository.plan_repository import PlanRepository
from api.repository.tenant_repository import TenantRepository

from api.exceptions.generics import EntityAlreadyExists, EntityNotFound, InvalidData

from api.models.subscription import Subscription
from api.models.dto.subscription_dto import SubscriptionCreateDTO, SubscriptionResponseDTO, SubscriptionUpdateDTO
from api.models.enums.subscription_status import SubscriptionStatus


class SubscriptionService:
    def __init__(
        self, subscription_repo: SubscriptionRepository,
        tenant_repo: TenantRepository,
        plan_repo: PlanRepository
    ):
        self.subscription_repo = subscription_repo
        self.tenant_repo = tenant_repo
        self.plan_repo = plan_repo

    def create(self, dto: SubscriptionCreateDTO) -> Subscription:
        if not self.tenant_repo.get_one(dto.tenant_id):
            raise EntityNotFound("Tenant")

        if not self.plan_repo.get_one(dto.plan_id):
            raise EntityNotFound("Plan")

        if dto.status not in SubscriptionStatus:
            raise InvalidData("Tipo de status inválido!")

        self._validate_time(start_date=dto.start_date, end_date=dto.end_date)

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
        subscription: Subscription = self.subscription_repo.get_one(
            subscription_id)

        if not subscription:
            raise EntityNotFound("Subscription")

        return subscription

    def update(self, subscription_id: int, update_subscription: SubscriptionUpdateDTO) -> None:

        if not self.tenant_repo.get_one(tenant_id=update_subscription.tenant_id):
            raise EntityNotFound("Tenant")

        if not self.plan_repo.get_one(plan_id=update_subscription.plan_id):
            raise EntityNotFound("Plan")

        if update_subscription.status not in SubscriptionStatus:
            raise InvalidData("Tipo de status inválido!")

        old_subscription: Subscription = self.subscription_repo.get_one(
            subscription_id=subscription_id)

        if not old_subscription:
            raise EntityNotFound("Subscription")

        update: Subscription = Subscription(
            status=update_subscription.status,
            start_date=update_subscription.start_date,
            end_date=update_subscription.end_date,
            tenant_id=update_subscription.tenant_id,
            plan_id=update_subscription.plan_id
        )

        self._validate_time(start_date=update.start_date,
                            end_date=update.end_date)

        try:
            old_subscription.status = update.status
            old_subscription.start_date = update.start_date
            old_subscription.end_date = update.end_date
            old_subscription.tenant_id = update.tenant_id
            old_subscription.plan_id = update.plan_id

            return self.subscription_repo.update(old_subscription)

        except Exception:
            raise InvalidData("Dados de Subscription")

    def delete(self, subscription_id: int) -> None:
        subscription: Subscription = self.subscription_repo.get_one(
            subscription_id)

        if not subscription:
            raise EntityNotFound("Subscription")

        return self.subscription_repo.delete(subscription=subscription)

    def _validate_time(self, start_date: datetime, end_date: datetime) -> None:

        if end_date.date() <= datetime.now().date():
            raise InvalidData(
                "Não é possivel registrar a DATA DE VENCIMENTO para anterior ou igual à de Hoje! Data"
            )

        if end_date.date() <= start_date.date():
            raise InvalidData(
                "Não é possivel definir a DATA DE VENCIMENTO anterior ou igual a DATA DE INÍCIO! Data"
            )
