from typing import List
from unittest.mock import Mock

from api.models.dto.tenant_dto import TenantResponseDTO, TenantUpdateDTO
from api.models.tenant import Tenant
from api.models.user import User
from api.services.tenant_services import TenantService

from test.factories.base import BaseMVCTestFactory

from test.dependencies import (
    mock_tenant_services,
    mock_tenant_repo
)

from test.mocks.tenant import (
    mock_tenant,
    mock_tenant_create,
    mock_tenant_list,
    mock_tenant_update,
)


class TestTenantServices(BaseMVCTestFactory):

    def test_get_all(self, mock_tenant_list: List[TenantResponseDTO], mock_tenant_services: TenantService, mock_tenant_repo: Mock):
        mock_tenant_repo.get_all.return_value = mock_tenant_list
        response = mock_tenant_services.get_all(skip=0, limit=100)

        assert response is not None
        assert len(response) == len(mock_tenant_list)

    def test_get_one(self, mock_tenant: Tenant, mock_tenant_services: TenantService, mock_tenant_repo: Mock):
        mock_tenant_repo.get_one.return_value = mock_tenant

        response: Tenant = mock_tenant_services.get_one(1)

        assert response is not None
        assert response == mock_tenant

    def test_create(self, mock_tenant: Tenant, mock_tenant_services: TenantService, mock_tenant_repo: Mock):
        mock_tenant_repo.get_by_name.return_value = None
        mock_tenant_repo.get_by_subdomain.return_value = None

        mock_tenant_repo.create.return_value = mock_tenant

        response = mock_tenant_services.create(mock_tenant)

        assert response is not None
        assert response == mock_tenant

    def test_update(self, mock_tenant: Tenant, mock_tenant_update: TenantUpdateDTO,  mock_tenant_services: TenantService, mock_tenant_repo: Mock):
        mock_tenant_repo.get_one.return_value = mock_tenant
        mock_tenant_repo.update.return_value = (
            mock_tenant_update
        )

        response = mock_tenant_services.update(
            mock_tenant.id, mock_tenant_update
        )

        assert response is not None
        assert response == mock_tenant_update

    def test_delete(self, mock_tenant: Tenant, mock_tenant_update: TenantUpdateDTO,  mock_tenant_services: TenantService, mock_tenant_repo: Mock):
        mock_tenant_repo.get_one.return_value = mock_tenant
        mock_tenant_repo.delete.return_value = None

        response = mock_tenant_services.delete(mock_tenant.id)

        assert response is None
