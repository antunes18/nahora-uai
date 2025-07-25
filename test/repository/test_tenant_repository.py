from typing import List

from api.models.tenant import Tenant
from api.models.dto.tenant_dto import TenantCreateDTO, TenantUpdateDTO

from api.repository.tenant_repository import TenantRepository

from test.dependencies import (
    real_tenant_repo
)

from test.mocks.tenant import (
    mock_tenant,
    mock_tenant_update,
    mock_tenant_list,
)


class TestTenantRepository:
    def test_create_tenant(self, real_tenant_repo: TenantRepository, mock_tenant: Tenant) -> TenantRepository:
        data = real_tenant_repo.create_tenant(mock_tenant)

        assert data is not None
        assert data.name == mock_tenant.name
        assert data.subdomain == mock_tenant.subdomain
        assert data.primary_color == mock_tenant.primary_color

    def test_get_all(self, real_tenant_repo: TenantRepository, mock_tenant_list) -> List[Tenant]:

        real_tenant_repo.session.add_all(mock_tenant_list)
        real_tenant_repo.session.commit()

        data = real_tenant_repo.get_all(skip=0, limit=100)

        assert data is not None
        assert len(data) == len(mock_tenant_list)

    def test_update_user(
        self,
        real_tenant_repo: TenantRepository,
        mock_tenant: Tenant,
        mock_tenant_update: TenantUpdateDTO
    ):
        mock_tenant.id = 1
        real_tenant_repo.session.add(mock_tenant)
        real_tenant_repo.session.commit()

        original: Tenant = real_tenant_repo.session.get(Tenant, mock_tenant.id)

        original.name = mock_tenant_update.name
        original.subdomain = mock_tenant_update.subdomain
        original.logo_url = mock_tenant_update.logo_url
        original.primary_color = mock_tenant_update.primary_color

        data = real_tenant_repo.update(original)

        assert data is not None

        assert data.name == mock_tenant_update.name
        assert data.subdomain == mock_tenant_update.subdomain
        assert data.logo_url == mock_tenant_update.logo_url
        assert data.primary_color == mock_tenant_update.primary_color

    def test_delete_tenant(self, real_tenant_repo: TenantRepository, mock_tenant: Tenant):
        real_tenant_repo.session.add(mock_tenant)
        real_tenant_repo.session.commit()

        data = real_tenant_repo.delete(mock_tenant)

        assert data is None
