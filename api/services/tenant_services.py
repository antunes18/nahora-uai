from api.repository.tenant_repository import TenantRepository
from api.models.tenant import Tenant


class TenantService:
    def __init__(
        self, tenant_repo: TenantRepository
    ):
        self.tenant_repo = tenant_repo

    def create(self, dto: Tenant):
        NotImplementedError()

    def get_all(self):
        NotImplementedError()

    def get_one(self, tenant_id: int):
        NotImplementedError()

    def update(self, tenant_id: int, update_tenant: Tenant):
        NotImplementedError()

    def delete(self, tenant_id: int):
        NotImplementedError()
