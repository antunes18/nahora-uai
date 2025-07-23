from api.repository.subscription_repository import SubscriptionRepository
from api.repository.plan_repository import PlanRepository
from api.repository.tenant_repository import TenantRepository

from api.models.plan import Plan
from api.models.subscription import Subscription


class SubscriptionService:
    def __init__(
        self, subscription_repo: SubscriptionRepository,
        tenant_repo: TenantRepository,
        plan_repo: PlanRepository,
    ):
        self.subscription_repo = subscription_repo
        self.tenant_repo = tenant_repo
        self.plan_repo = plan_repo

    def create(self, dto: Subscription):
        NotImplementedError()

    def get_all(self):
        NotImplementedError()

    def get_one(self, subscription_id: int):
        NotImplementedError()

    def update(self, subscription_id: int, update_subscription: Subscription):
        NotImplementedError()

    def delete(self, subscription_id: int):
        NotImplementedError()
