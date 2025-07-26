import pytest
from sqlalchemy.orm import Session
from unittest.mock import MagicMock

from api.repository.user_repository import UserRepository
from api.repository.scheduling_repository import SchedulingReposistory
from api.repository.invoice_repository import InvoiceRepository
from api.repository.plan_repository import PlanRepository
from api.repository.subscription_repository import SubscriptionRepository
from api.repository.tenant_repository import TenantRepository


from api.services.auth_services import UserServices
from api.services.scheduling_services import SchedulingService
from api.services.invoice_services import InvoiceService
from api.services.plan_services import PlanService
from api.services.subscription_services import SubscriptionService
from api.services.tenant_services import TenantService


# ============= Mock Repository ==================

@pytest.fixture
def mock_user_repo():
    return MagicMock(spec=UserRepository)


@pytest.fixture
def mock_scheduling_repo():
    return MagicMock(spec=SchedulingReposistory)


@pytest.fixture()
def mock_invoice_repo():
    return MagicMock(spec=InvoiceRepository)


@pytest.fixture()
def mock_plan_repo():
    return MagicMock(spec=PlanRepository)


@pytest.fixture()
def mock_subscription_repo():
    return MagicMock(spec=SubscriptionRepository)


@pytest.fixture()
def mock_tenant_repo():
    return MagicMock(spec=TenantRepository)


# =========== Mock Services =====================

@pytest.fixture
def mock_user_service(mock_user_repo: UserRepository, mock_tenant_repo: TenantRepository):
    return UserServices(user_repo=mock_user_repo, tenant_repo=mock_tenant_repo)


@pytest.fixture
def mock_scheduling_services(
    mock_scheduling_repo: SchedulingReposistory,
    mock_user_repo: UserRepository,
    mock_tenant_repo: TenantRepository
):
    return SchedulingService(
        scheduling_repo=mock_scheduling_repo, user_repo=mock_user_repo, tenant_repo=mock_tenant_repo
    )


@pytest.fixture()
def mock_invoice_services(
        mock_invoice_repo: InvoiceRepository,
        mock_subscription_repo: SubscriptionRepository
):
    return InvoiceService(invoice_repo=mock_invoice_repo, subscription_repo=mock_subscription_repo)


@pytest.fixture()
def mock_plan_services(mock_plan_repo: PlanRepository):
    return PlanService(plan_repo=mock_plan_repo)


@pytest.fixture()
def mock_subscription_services(
        mock_subscription_repo: SubscriptionRepository,
        mock_tenant_repo: TenantRepository,
        mock_plan_repo: PlanRepository
):
    return SubscriptionService(
        subscription_repo=mock_subscription_repo,
        tenant_repo=mock_tenant_repo,
        plan_repo=mock_plan_repo
    )


@pytest.fixture()
def mock_tenant_services(mock_tenant_repo):
    return TenantService(tenant_repo=mock_tenant_repo)


# ============= Real Repository ==================

@pytest.fixture
def real_user_repo(db_session_for_test: Session):
    """Fixture que fornece uma instância real do UserRepository com uma sessão de teste."""
    return UserRepository(session=db_session_for_test)


@pytest.fixture
def real_scheduling_repo(db_session_for_test: Session):
    """Fixture que fornece uma instância real do SchedulingRepository com uma sessão de teste."""
    return SchedulingReposistory(session=db_session_for_test)


@pytest.fixture()
def real_invoice_repo(db_session_for_test: Session):
    """Fixture que fornece uma instância real do InvoiceRepository com uma sessão de teste."""
    return InvoiceRepository(session=db_session_for_test)


@pytest.fixture()
def real_plan_repo(db_session_for_test: Session):
    """Fixture que fornece uma instância real do PlanRepository com uma sessão de teste."""
    return PlanRepository(session=db_session_for_test)


@pytest.fixture()
def real_subscription_repo(db_session_for_test: Session):
    """Fixture que fornece uma instância real do SubscriptionRepository com uma sessão de teste."""
    return SubscriptionRepository(session=db_session_for_test)


@pytest.fixture()
def real_tenant_repo(db_session_for_test: Session):
    """Fixture que fornece uma instância real do SubscriptionRepository com uma sessão de teste."""
    return TenantRepository(session=db_session_for_test)


# ============= Real Service ==================

@pytest.fixture(scope="function")
def real_users_services(user_repo: UserRepository, tenant_repo: TenantRepository):
    """Fixture que fornece uma instância do UserService com um repositório real (para testes de integração)."""
    return UserServices(user_repo=user_repo, tenant_repo=tenant_repo)


@pytest.fixture
def real_scheduling_services(
    scheduling_repo: SchedulingReposistory,
    user_repo: UserRepository,
    tenant_repo: TenantRepository
):
    """Fixture que fornece uma instância do SchedulingService com um repositório real (para testes de integração)."""
    return SchedulingService(
        scheduling_repo=scheduling_repo, user_repo=user_repo, tenant_repo=tenant_repo
    )


@pytest.fixture(scope="function")
def real_invoice_services(invoice_repo: InvoiceRepository):
    """Fixture que fornece uma instância do InvoiceService com um repositório real (para testes de integração)."""
    return InvoiceService(invoice_repo=invoice_repo)


@pytest.fixture(scope="function")
def real_plan_services(plan_repo: PlanRepository):
    """Fixture que fornece uma instância do PlanService com um repositório real (para testes de integração)."""
    return PlanService(plan_repo=plan_repo)


@pytest.fixture(scope="function")
def real_subscription_services(subscription_repo: SubscriptionRepository):
    """Fixture que fornece uma instância do SubscriptionService com um repositório real (para testes de integração)."""
    return SubscriptionService(subscription_repo=subscription_repo)


@pytest.fixture(scope="function")
def real_tenant_services(tenant_repo: TenantRepository):
    """Fixture que fornece uma instância do TenantService com um repositório real (para testes de integração)."""
    return SubscriptionService(tenant_repo=tenant_repo)
