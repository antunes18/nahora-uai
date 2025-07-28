from fastapi import Depends
from sqlalchemy.orm import Session
from api.core.database import get_db


from api.repository.user_repository import UserRepository
from api.repository.scheduling_repository import SchedulingReposistory
from api.repository.plan_repository import PlanRepository
from api.repository.invoice_repository import InvoiceRepository
from api.repository.subscription_repository import SubscriptionRepository
from api.repository.tenant_repository import TenantRepository

from api.services.auth_services import UserServices
from api.services.scheduling_services import SchedulingService
from api.services.invoice_services import InvoiceService
from api.services.plan_services import PlanService
from api.services.subscription_services import SubscriptionService
from api.services.tenant_services import TenantService


# ==================== Repository =============================
def get_user_repo(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(session=db)


def get_scheduling_repo(db: Session = Depends(get_db)) -> SchedulingReposistory:
    return SchedulingReposistory(session=db)


def get_plan_repo(db: Session = Depends(get_db)) -> PlanRepository:
    return PlanRepository(session=db)


def get_invoice_repo(db: Session = Depends(get_db)) -> InvoiceRepository:
    return InvoiceRepository(session=db)


def get_subscription_repo(db: Session = Depends(get_db)) -> SubscriptionRepository:
    return SubscriptionRepository(session=db)


def get_tenant_repo(db: Session = Depends(get_db)) -> TenantRepository:
    return TenantRepository(session=db)


# ==================== Services ==============================
def get_user_services(
    user_repo: UserRepository = Depends(get_user_repo),
    tenant_repo: TenantRepository = Depends(get_tenant_repo)
) -> UserServices:
    return UserServices(user_repo=user_repo, tenant_repo=tenant_repo)


def get_scheduling_services(
    user_repo: UserRepository = Depends(get_user_repo),
    scheduling_repo: SchedulingReposistory = Depends(get_scheduling_repo),
    tenant_repo: TenantRepository = Depends(get_tenant_repo)
) -> SchedulingService:
    return SchedulingService(scheduling_repo=scheduling_repo, user_repo=user_repo, tenant_repo=tenant_repo)


def get_plan_services(
    plan_repo: PlanRepository = Depends(get_plan_repo),
) -> PlanService:
    return PlanService(plan_repo=plan_repo)


def get_invoice_services(
    invoice_repo: InvoiceRepository = Depends(get_invoice_repo),
    subscription_repo: SubscriptionRepository = Depends(get_subscription_repo)
) -> InvoiceService:
    return InvoiceService(invoice_repo=invoice_repo, subscription_repo=subscription_repo)


def get_subscription_services(
    subscription_repo: SubscriptionRepository = Depends(get_subscription_repo),
    plan_repo: PlanRepository = Depends(get_plan_repo),
    tenant_repo: TenantRepository = Depends(get_tenant_repo)
) -> SubscriptionService:
    return SubscriptionService(subscription_repo=subscription_repo, plan_repo=plan_repo, tenant_repo=tenant_repo)


def get_tenant_services(
    tenant_repo: TenantRepository = Depends(get_tenant_repo),
) -> TenantService:
    return TenantService(tenant_repo=tenant_repo)
