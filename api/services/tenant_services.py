from api.repository.tenant_repository import TenantRepository
from api.models.tenant import Tenant
from api.models.dto.tenant_dto import TenantCreateDTO, TenantResponseDTO, TenantUpdateDTO


class TenantService:
    def __init__(
        self, tenant_repo: TenantRepository
    ):
        self.tenant_repo = tenant_repo

    def create(self, tenant_create_dto: TenantCreateDTO):
        if self.tenant_repo.get_by_name(tenant_create_dto.name):
            raise NotImplementedError("Error to Tenant Name Already Taken")

        if self.tenant_repo.get_by_subdomain(tenant_create_dto.subdomain):
            raise NotImplementedError("Error to Tenant Already Exist")

        tenant = Tenant(
            name=tenant_create_dto.name,
            subdomain=tenant_create_dto.subdomain,
            logo_url=tenant_create_dto.logo_url,
            primary_color=tenant_create_dto.primary_color,

        )
        return self.tenant_repo.create_tenant(tenant)

    def get_all(self, skip: int, limit: int):
        return self.tenant_repo.get_all(skip, limit)

    def get_one(self, tenant_id: int):
        return self.tenant_repo.get_one(tenant_id)

    def update(self, tenant_id: int, update_tenant: TenantUpdateDTO):
        return self.tenant_repo.update(tenant_id, update_tenant)

    def delete(self, tenant_id: int):
        # FIX: Validar regra para deletar
        # return self.tenant_repo.delete(tenant_id)
        raise NotImplementedError("DELETE not implemented")
