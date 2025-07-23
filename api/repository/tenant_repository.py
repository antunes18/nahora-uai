from logging import disable
from api.models.enums import roles
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.models.tenant import Tenant


class TenantRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_tenant(self, tenant: Tenant):
        self.session.add(Tenant)
        self.session.commit()
        self.session.refresh()

        return tenant

    def get_all(self, skip: int, limit: int) -> list(Tenant):
        result = self.session.execute(select(Tenant).offset(skip).limit(limit))

        return list(result.scalar().all())

    def get_one(self, tenant_id: int) -> Tenant:
        return self.session.query(Tenant).filter(
            Tenant.id == tenant_id).first()

    def update(self, tenant_id: int, update_tenant: Tenant):
        old_tenant = self.get_one(tenant_id)
        if old_tenant:
            old_tenant.name = update_tenant.name
            old_tenant.subdomain = update_tenant.subdomain
            old_tenant.logo_url = update_tenant.logo_url
            old_tenant.primary_color = update_tenant.primary_color

            self.session.commit()
            self.session.refresh(old_tenant)

        else:
            None

    def delete(self, tenant_id: int):
        tenant = self.get_one(tenant_id)
        if tenant:
            NotImplementedError(
                "Função de Delete de Tenant não foi implementada")
        else:
            None
