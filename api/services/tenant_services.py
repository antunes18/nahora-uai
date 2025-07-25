from typing import List

from api.exceptions.generics import EntityAlreadyExists, EntityNotFound, InvalidData, FieldAlreadyUsed

from api.repository.tenant_repository import TenantRepository
from api.models.tenant import Tenant
from api.models.dto.tenant_dto import TenantCreateDTO, TenantResponseDTO, TenantUpdateDTO
from api.models.dto.user_dto import UserResponseDTO


class TenantService:
    def __init__(
        self, tenant_repo: TenantRepository
    ) -> None:
        self.tenant_repo = tenant_repo

    def create(self, tenant_create_dto: TenantCreateDTO) -> Tenant:
        if self.tenant_repo.get_by_name(tenant_create_dto.name):
            raise FieldAlreadyUsed("Nome de Tenant")

        if self.tenant_repo.get_by_subdomain(tenant_create_dto.subdomain):
            raise InvalidData("Subdominio de Tenant")

        tenant = Tenant(
            name=tenant_create_dto.name,
            subdomain=tenant_create_dto.subdomain,
            logo_url=tenant_create_dto.logo_url,
            primary_color=tenant_create_dto.primary_color,

        )
        return self.tenant_repo.create_tenant(tenant)

    def get_all(self, skip: int, limit: int) -> List[Tenant]:
        return self.tenant_repo.get_all(skip, limit)

    def get_one(self, tenant_id: int) -> Tenant:
        return self.tenant_repo.get_one(tenant_id)

    def get_all_users(self, tenant_id: int) -> List[UserResponseDTO]:
        return self.tenant_repo.get_one(tenant_id).users

    def update(self, tenant_id: int, update_tenant: TenantUpdateDTO) -> None:
        old_tenant: Tenant = self.get_one(tenant_id)

        if not old_tenant:
            raise EntityNotFound("Tenant")

        try:
            old_tenant.name = update_tenant.name
            old_tenant.subdomain = update_tenant.subdomain
            old_tenant.logo_url = update_tenant.logo_url
            old_tenant.primary_color = update_tenant.primary_color

            return self.tenant_repo.update(update_tenant=old_tenant)
        except Exception:
            raise InvalidData("Dados da Tenant")

    def delete(self, tenant_id: int) -> None:
        tenant: Tenant = self.tenant_repo.get_one(tenant_id)

        if not tenant:
            raise EntityNotFound("Tenant")

        return self.tenant_repo.delete(tenant)
