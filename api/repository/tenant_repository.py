from logging import disable
from api.models.enums import roles
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.models.tenant import Tenant

from typing import List


class TenantRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_tenant(self, tenant: Tenant):
        self.session.add(tenant)
        self.session.commit()
        self.session.refresh(tenant)

        return tenant

    def get_all(self, skip: int, limit: int) -> List[Tenant]:
        return self.session.query(Tenant).offset(skip).limit(limit).all()

    def get_one(self, tenant_id: int) -> Tenant:
        return self.session.query(Tenant).filter(
            Tenant.id == tenant_id).first()

    def get_by_name(self, name: str) -> Tenant:
        return self.session.query(Tenant).filter(Tenant.name == name).first()

    def get_by_subdomain(self, subdomain: str) -> Tenant:
        return self.session.query(Tenant).filter(Tenant.subdomain == subdomain).first()

    def update(self, tenant_id: int, update_tenant: Tenant) -> None:
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

    def delete(self, tenant_id: int) -> None:
        tenant = self.get_one(tenant_id)
        if tenant:
            raise NotImplementedError(
                "Função de Delete de Tenant não foi implementada")
        else:
            None
